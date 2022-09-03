from flask import Flask, request
import logging
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["POST"])
def main():
    req=request.json
    logging.info(req)

    response = {
        "version": req["version"],
        "session": req["session"],
        "response": {
            "end_session": False
        }
    }

    if req["session"]["new"]:
        response["response"]["text"] = "Привет! Как твои дела? Купи слона!"
    else:
        if req["request"]["original_utterance"]:
            text = "Все говрят "+req["request"]["original_utterance"] + " а ты купи слона!"
            response["response"]["text"] = text

    return json.dumps(response)

app.run(host='0.0.0.0', port=5000)



# def handler(event, context):
#     """
#     Entry-point for Serverless Function.
#     :param event: request payload.
#     :param context: information about current execution context.
#     :return: response to be serialized as JSON.
#     """
#     text = 'Hello! I\'ll repeat anything you say to me.'
#     if 'request' in event and \
#             'original_utterance' in event['request'] \
#             and len(event['request']['original_utterance']) > 0:
#         text = event['request']['original_utterance']
#     return {
#         'version': event['version'],
#         'session': event['session'],
#         'response': {
#             # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
#             'text': text,
#             # Don't finish the session after this response.
#             'end_session': 'false'
#         },
#     }
#

