from flask import Blueprint, render_template, abort, jsonify, request
from BlueprintArchitech.Library.v1 import lister
import setting
blueprint = Blueprint('directory_listing', __name__,template_folder='BlueprintArchitech/Listing')
@blueprint.route('/', methods=['GET'])
def all_manga():
	hsite = request.args.get('hsite', default = 'all', type = str)
	ctype = request.args.get('ctype', default = 'all', type = str)
	mid = request.args.get('mid', default = 'all', type = str)
	print("Requesting [GET] : "+hsite+"/"+ctype+"/"+mid)
	result = lister(hsite,ctype,mid)
	hlists = setting.hlist
	return render_template('list.html', result=result,hsite=hsite,ctype=ctype,mid=mid , hlists = hlists)