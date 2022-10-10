import json


def main(event, context):
    # Verify signature coming from Discord
    verify_signature(event)


    body = event.get('body')
    if body['type'] == 1:
        return {
            'type': 1,
        }

    return {
      "type": 5,
    }
