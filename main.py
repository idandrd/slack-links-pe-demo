import os
import json
import requests

BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']

def handle_event(request):
    request_json = request.get_json()
    if not request_json:
        return 'ok'
    elif 'challenge' in request_json:
        return {'challenge': request_json['challenge']}
    elif 'event' in request_json:
        print('5')
        if request_json['event']['source'] == 'conversations_history' and request_json['event']['links']:
            user = request_json['event']['user']
            links = [x['url'] for x in request_json['event']['links']]
            channel = request_json['event']['channel']
            ts = request_json['event']['message_ts']
            print('link:', links)
            print('channel:', channel)
            print('user:', user)
            unfurl_link(channel, ts, links)
    else:
        return 'ok'

def unfurl_link(channel, ts, links):
    blocks = {
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': "*It looks like you've got a document to sign!*"
                },
                'accessory': {
                    'type': 'button',
                    'action_id': 'orbit',
                    'text': {
                        'type': 'plain_text',
                        'text': 'Open document'
                    },
                    'style': 'primary',
                    'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
                }
            }
        ]
    }
    unfurl_json = {
        'channel': channel,
        'ts': ts,
        'unfurls': {link: blocks for link in links}
    }
    url = 'https://slack.com/api/chat.unfurl'
    payload = json.dumps(unfurl_json)
    headers = {
        'Authorization': f'Bearer {BOT_TOKEN}',
        'Content-Type': 'application/json'
    }
    requests.request('POST', url, headers=headers, data=payload)
