from flask import Flask, request, jsonify
from flask_cors import CORS
from BlueprintArchitech import Home, Doujin, Listing, Viewer
 
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(Listing.blueprint,url_prefix='/query')
app.register_blueprint(Doujin.blueprint,url_prefix='/scraper')
app.register_blueprint(Viewer.blueprint,url_prefix='/view')
app.register_blueprint(Home.blueprint,url_prefix='/')
if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')