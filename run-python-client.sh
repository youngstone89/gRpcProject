#!/bin/bash

CLIENT_ID=""
SECRET=""
export MY_TOKEN="`curl -s -u "$CLIENT_ID:$SECRET" \
"https://auth.crt.nuance.com/oauth2/token" \
-d 'grant_type=client_credentials' -d 'scope=asr nlu tts dlg' \
| python -c 'import sys, json; print(json.load(sys.stdin)["access_token"])'`"

echo "TOKEN CHECK:: $MY_TOKEN"

./my-python-client.py asr.api.nuance.com:443 $MY_TOKEN ./test.wav