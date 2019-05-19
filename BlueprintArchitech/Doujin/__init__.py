from flask import Blueprint, render_template, abort, jsonify, request, send_from_directory
from BlueprintArchitech.Doujin.func.v1 import hentai_scraper
import setting
blueprint = Blueprint('doujin_scrape', __name__,template_folder='BlueprintArchitech/Doujin')
@blueprint.route('/doujin', methods=['POST','GET'])
def doujin():
	if request.method == 'POST':
		print("lol")
		if request.get_json()['hsite'] in setting.hlist:
			scrapperclass = hentai_scraper(request.get_json()['mid'], request.get_json()['hsite'],request.get_json()['ctype']) 
			if scrapperclass.lister['status'] == 200:
				if scrapperclass.pdf['status'] == 200:
					pdfpath = scrapperclass.pdf['file']
				else:
					pdfpath = scrapperclass.pdfmaker()
				# respond = {'status' : 200,'msj' : 'POST CALLED', 'pdf' : pdfpath}
				# return jsonify(respond)
			else:
				scrapperclass.scraper()
				pdfpath = scrapperclass.pdfmaker()
				# respond = {'status' : 200,'msj' : 'POST CALLED', 'pdf' : pdfpath}
				# return jsonify(respond)
			respond = {'status' : 200,'msj' : 'POST CALLED', 'pdf' : pdfpath}
			return jsonify(respond)
		else:
			respond = {'status' : 200,'msj' : 'POST CALLED', 'error' : 'site not available'}
			return jsonify(respond)
	else:
		respond = {'status' : 404,'msj' : 'Method not alloed'}
		return jsonify(respond)