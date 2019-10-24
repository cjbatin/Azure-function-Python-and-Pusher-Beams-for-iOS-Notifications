import logging

import azure.functions as func
from pusher_push_notifications import PushNotifications
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    title = req_body.get('title')
    message = req_body.get('message')
    beams_client = PushNotifications(
                    instance_id='YOUR_INSTANCE_ID',
                    secret_key='YOUR_SECRET_KEY',
                    )
    response = beams_client.publish_to_interests(interests=['hello'],
                                                publish_body={
                                                'apns': {
                                                'aps': {
                                                    'alert': {
                                                        'title': title,
                                                        'body': message
                                                        },
                                                    },
                                                },
                                                },
                                                )
    print(response['publishId'])
    return func.HttpResponse(f"Sent message {title}, {message}") 