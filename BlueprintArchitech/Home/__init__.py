from flask import Blueprint, render_template, abort, jsonify, request
blueprint = Blueprint('home_view', __name__,template_folder='BlueprintArchitech/Home')
@blueprint.route('/', methods=['GET'])
def index():
	return render_template('home.html')