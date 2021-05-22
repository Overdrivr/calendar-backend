from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route("/")
def create_meeting():
    token = os.getenv('ZOOM_JWT_TOKEN')

    res = requests.post(
        "https://api.zoom.us/v2/users/remi@cronobo.com/meetings",
        json={
            'topic': 'Meeting',
            'type': 2,
            'start_time': '2021-12-31T00:00:00'
        },
        headers={
            'authorization': 'Bearer {}'.format(token),
        }
    )

    print(res.text)
    assert res.status_code in [200, 201]
    return res.json()
