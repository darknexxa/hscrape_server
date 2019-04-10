from flask import Blueprint, render_template, abort, jsonify, request
from BlueprintArchitech.Doujin.func.v1 import hentai_scraper
blueprint = Blueprint('doujin_scrape', __name__,template_folder='BlueprintArchitech/Doujin')
@blueprint.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		
		scrapperclass = hentai_scraper(request.form['mid'], request.form['hsite'],request.form['ctype']) 
		scrapperclass.scraper()
		pdfpath = scrapperclass.pdfmaker()
		respond = {'status' : 200,'msj' : 'POST CALLED', 'pdf' : pdfpath}
		return jsonify(respond)
	else:
		respond = {'status' : 200,'msj' : 'GET CALLED'}
		return jsonify(respond)