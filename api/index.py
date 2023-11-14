import json, urllib.request
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from dotenv import load_dotenv
import os
from api.database import db
from api.model.message import Message, MessageSchema
from api.model.serviceSurvey import serviceDecisionTree
from api.model.productSurvey import productDecisionTree
from api.model.carSurvey import carDecisionTree
from api.messages.controllers import list_all_messages_controller, create_new_message_controller


from . import create_app # from __init__ file


# PostgreSQL Database credentials loaded from the .env file
# DATABASE = os.getenv('DATABASE')
# DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
# DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

load_dotenv()  # loads variables from .env file into environment

# app = Flask(__name__)
# url = os.environ.get("DATABASE_URL")  # gets variables from environment
# connection = psycopg2.connect(url)

# def get_db_connection():
#     conn = psycopg2.connect(host='localhost', database='testdb', user=os.environ['DB_USERNAME'], password=os.environ['DB_PASSWORD'])
#     return conn

'''
conn = get_db_connection()
cur = conn.cursor()
cur.execute('SELECT * FROM books;')
books = cur.fetchall()
cur.close()
conn.close()
'''

app = create_app(os.getenv("CONFIG_MODE"))

# def create_app():    
#     app = Flask(__name__)        
#     app.config.from_mapping(
#         SECRET_KEY = "My_Secret_Key"
#     )     
    
#     app.config.from_object(CoolConfig)    
    
#     # Database related part
#     db.init_app(app)
#     from best_app.models.user import User
#     from best_app.models.car import Car
#     migrate = Migrate(app, db)

#     app.register_blueprint(hello.blueprint)
#     app.register_blueprint(goodbye.blueprint)

#     return app

# counter = float(0)
current_step = ""
messages = []
# Message(float(counter), 'Hi!', True, False, False)

def write_output():
    schema = MessageSchema(many=True)
    messageJSON = schema.dump(messages)
    result = json.dumps(messageJSON, indent=4)
    with open("chatLogs.json", "w+") as file:
        file.write(result)


def get_template(template):
    if template == "service":
        return serviceDecisionTree
    elif template == "product":
        return productDecisionTree
    elif template == "car":
        return carDecisionTree
    else:
        return None


def handle_chatbot_message(message, template):
    # global counter
    global current_step
    next_step = current_step
    if message.getNeedResponse():
        if current_step:
            if "record" in template[current_step]:
                next_step = template[current_step]["next"]
            else:
                if "next" in template[current_step]:
                    if message.getText().lower() in template[current_step]["next"]:
                        next_step = template[current_step]["next"][message.getText().lower()]
                    else:
                        # next_step = current_step
                        additional_text = "I'm sorry, I didn't understand your response. Let's try again. "
                        return Message(1, additional_text + template[current_step]["question"], True, template[current_step]["needResponse"], template[current_step]["needButton"], message.getSurveyType())
                else:
                    current_step = ""
                    print("finished")
                    return ""
        else:
            next_step = "STEP1"
        new_message = Message(1, template[next_step]["question"], True, template[next_step]["needResponse"], template[next_step]["needButton"], message.getSurveyType())
        current_step = next_step
        return new_message
    else:
        return ""
    

def handle_car_chatbot_message(message, template):
    # global counter
    global current_step
    next_step = current_step
    question = ""
    if message.getNeedResponse():
        if current_step:
            if "record" in template[current_step]:
                next_step = template[current_step]["next"]
            else:
                if "next" in template[current_step]:
                    if message.getText().lower() in template[current_step]["next"]:
                        next_step = template[current_step]["next"][message.getText().lower()]
                    else:
                        # next_step = current_step
                        additional_text = "I'm sorry, I didn't understand your response. Let's try again. "
                        return Message(1, additional_text + template[current_step]["question"], True, template[current_step]["needResponse"], template[current_step]["needButton"], message.getSurveyType())
                else:
                    current_step = ""
                    print("finished")
                    return ""
        else:
            question = json.dumps(get_cars())
            next_step = "STEP1"
        if not question:
            question = template[next_step]["question"]
        new_message = Message(1, question, True, template[next_step]["needResponse"], template[next_step]["needButton"], message.getSurveyType())
        current_step = next_step
        return new_message
    else:
        return ""


# GET all the chat messages
@app.route("/api/cars")
def get_cars():
    url = "https://62daf70dd1d97b9e0c49ca5d.mockapi.io/v1/products"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict

# GET all the chat messages
@app.route("/api/messages")
def get_messages():
    # schema = MessageSchema(many=True)
    # result = schema.dump(messages)
    # return jsonify(result)
    return list_all_messages_controller()


# add user message + generate next message
@app.route('/api/messages', methods=['POST'])
def add_message():
    # handle customer message
    # global counter
    result = ""
    message = MessageSchema().load(request.get_json())
    if message.getText():
        result = create_new_message_controller(message)
        # counter = float(counter + 1)
        # message.setID(counter)
        # messages.append(message)
    # send chatbot message
    # counter = float(counter + 1)
    template = get_template(message.getSurveyType())
    if template:
        if message.getSurveyType() == "car":
            newMessage = handle_car_chatbot_message(message, template)
        else:
            newMessage = handle_chatbot_message(message, template)
        if newMessage == "":
            print("no response")
        else:
            result = create_new_message_controller(newMessage)
            # messages.append(newMessage)
    write_output()
    return result, 200

# CRUD operations for messages
from .messages import urls

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5328)
