from flask import request, jsonify
import uuid

from api.database import db
from .models import Messages

# ----------------------------------------------- #

# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522

def list_all_messages_controller():
    messages = Messages.query.all()
    response = []
    for message in messages: response.append(message.toDict())
    return jsonify(response)

def create_message_controller():
    body = request.get_json()
    print(body)

    # id = str(uuid.uuid4())
    new_message = Messages(
        id = body['id'],
        text = body['text'],
        isBot = body['isBot'],
        needResponse = body['needResponse'],
        needButton = body['needButton'],
        surveyType = body['surveyType'],
        )
    db.session.add(new_message)
    db.session.commit()

    response = Messages.query.get(id).toDict()
    return jsonify(response)

def retrieve_message_controller(message_id):
    response = Messages.query.get(message_id).toDict()
    return jsonify(response)

def update_message_controller(message_id):
    body = request.get_json()
    message = Messages.query.get(message_id)
    message.text = body['text'],
    message.isBot = body['isBot'],
    message.needResponse = body['needResponse'],
    message.needButton = body['needButton'],
    message.surveyType = body['surveyType'],

    db.session.commit()

    response = Messages.query.get(message_id).toDict()
    return jsonify(response)

def delete_message_controller(message_id):
    Messages.query.filter_by(id=message_id).delete()
    db.session.commit()

    return ('Message with Id "{}" deleted successfully!').format(message_id)