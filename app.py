"""
Flask API Application
"""

from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from, LazyString, LazyJSONEncoder
from cleansing import text_cleansing
from db import (
    create_connection, insert_dictionary_to_db, 
    insert_result_to_db, show_cleansing_result
)
import flask
flask.json.provider.DefaultJSONProvider.sort_keys = False

# Set Up Database
db_connection = create_connection()
insert_dictionary_to_db(db_connection)
db_connection.close()
# initializze flask application
app = Flask(__name__)

#Assign LazyJSONEncoder to app.json_encoder for swagger UI
app.json_encoder = LazyJSONEncoder
# create swagger config & swagger template
Swagger_template ={
    "info":{
        "title": LazyString(lambda: "Text Cleansing API"),
        "version": LazyString(lambda: "1.0.0"),
        "description": LazyString(lambda: "Dokumentasi API untuk membersihkan text")
    },
    "host": LazyString(lambda: request.host)
}
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
# intiliazeSwagger from tempalte & config
swagger = Swagger(app, template=Swagger_template, config=swagger_config)

# homepage
@swag_from('docs/home.yml', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    welcome_msg = {
        "version": "1.0.0",
        "message": "Welcome to Flask API",
        "author": "Adelia Christyanti"
    }
    return jsonify(welcome_msg)

# Show cleansing result
@swag_from('docs/show_cleansing_result.yml', methods=['GET'])
@app.route('/show_cleansing_result', methods=['GET'])
def show_cleansing_result_api():
    db_connection = create_connection()
    cleansing_result = show_cleansing_result(db_connection)
    return jsonify(cleansing_result)

#cleansing text using form
@swag_from('docs/cleansing_form.yml', methods=['POST'])
@app.route('/cleansing_form', methods=['POST'])
def cleansing_form():
    # get text from input user
    raw_text = request.form["raw_text"]
    # cleansing text
    clean_text = text_cleansing(raw_text)
    result_response ={"raw_text": raw_text, "clean_text": clean_text}
    # insert result to database
    db_connection = create_connection()
    insert_result_to_db(db_connection, raw_text, clean_text)
    return jsonify(result_response)

if __name__ == '__main__':
    app.run()