from nacl.signing import VerifyKey
import os

PUBLIC_KEY = os.getenv('PUBLIC_KEY')

def verify_signature(event):
    raw_body = json.dumps(event.get('body'), separators=(',', ':'))
    sig = event['headers'].get('x-signature-ed25519')
    ts  = event['headers'].get('x-signature-timestamp')

    message = ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(sig))

