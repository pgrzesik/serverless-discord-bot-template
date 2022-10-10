import json


def main(event, context):
    # Verify signature coming from Discord
    verify_signature(event)


    body = event.get('body')
    if body['type'] == 1:
        return {
            'type': 1,
        }

    if body['data'].get('name') == 'dummy':
        return json.dumps({
            'type': 4,
            'data': {
                'content': 'dummy response',
            }
        })

    return {
      "type": 5,
    }
