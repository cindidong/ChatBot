from flask import request

from ..index import app
from .controllers import list_all_messages_controller, create_message_controller, retrieve_message_controller, update_message_controller, delete_message_controller

@app.route("/messages", methods=['GET', 'POST'])
def list_create_accounts():
    if request.method == 'GET': return list_all_messages_controller()
    if request.method == 'POST': return create_message_controller()
    else: return 'Method is Not Allowed'

@app.route("/messages/<message_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_accounts(message_id):
    if request.method == 'GET': return retrieve_message_controller(message_id)
    if request.method == 'PUT': return update_message_controller(message_id)
    if request.method == 'DELETE': return delete_message_controller(message_id)
    else: return 'Method is Not Allowed'