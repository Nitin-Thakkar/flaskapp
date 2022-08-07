import runpy
from flask import Flask, render_template , send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import pymongo

app = Flask(__name__)
 
#databse
#localhost
#client = pymongo.MongoClient('localhost',27017)


#### for CLoud
client = pymongo.MongoClient('mongodb+srv://root:root@cluster0.rrrjcs9.mongodb.net/?retryWrites=true&w=majority')
db = client.user_login_system

#routes 
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static',path)

SWAGGER_URL ="/swagger"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':"My First APP"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
if __name__== "__main__":
    runpy.app()