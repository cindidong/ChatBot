import json
from flask import Flask, jsonify, request
from model.message import Message, MessageSchema
from model.serviceSurvey import serviceDecisionTree
from model.productSurvey import productDecisionTree

app = Flask(__name__)

counter = float(0)
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
    else:
        return None


def handle_chatbot_message(message, template):
    global counter
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
                        return Message(float(counter), additional_text + template[current_step]["question"], True, template[current_step]["needResponse"], template[current_step]["needButton"], message.getSurveyType())
                else:
                    current_step = ""
                    print("finished")
                    return ""
        else:
            next_step = "STEP1"
        new_message = Message(float(counter), template[next_step]["question"], True, template[next_step]["needResponse"], template[next_step]["needButton"], message.getSurveyType())
        current_step = next_step
        return new_message
    else:
        return ""


# GET all the chat messages
@app.route("/api/messages")
def get_messages():
    schema = MessageSchema(many=True)
    result = schema.dump(messages)
    return jsonify(result)


# add user message + generate next message
@app.route('/api/messages', methods=['POST'])
def add_message():
    # handle customer message
    global counter
    message = MessageSchema().load(request.get_json())
    if message.getText():
        counter = float(counter + 1)
        message.setID(counter)
        messages.append(message)
    # send chatbot message
    counter = float(counter + 1)
    template = get_template(message.getSurveyType())
    if template:
        newMessage = handle_chatbot_message(message, template)
        if newMessage == "":
            print("no response")
        else:
            messages.append(newMessage)
    write_output()
    return "", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5328)
