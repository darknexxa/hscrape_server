from flask import Blueprint, render_template, abort, jsonify, request, send_file, send_from_directory, make_response
import os
import webbrowser
# from BlueprintArchitech.Library.v2 import lister

blueprint = Blueprint('pdf_viewer', __name__,template_folder='BlueprintArchitech/Viewer')
@blueprint.route('/', methods=['GET'])
def view_pdf():
	hsite = request.args.get('hsite', default = 'all', type = str)
	ctype = request.args.get('ctype', default = 'all', type = str)
	mid = request.args.get('mid', default = 'all', type = str)
	print("Requesting [GET] : "+hsite+"/"+ctype+"/"+mid)
	if mid == 'all':
		return render_template('404.html')
	else:
		return render_template('pdf.html', hsite = hsite, ctype=ctype,mid=mid)