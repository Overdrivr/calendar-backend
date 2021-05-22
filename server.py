from flask import Flask, request
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['POST'])
def create_meeting():
    token = os.getenv('ZOOM_JWT_TOKEN')
    start_date = request.get_json()['startDate']

    print('Creating meeting at {}'.format(start_date))

    res = requests.post(
        "https://api.zoom.us/v2/users/remi@cronobo.com/meetings",
        json={
            'topic': 'Meeting',
            'type': 2,
            'start_time': start_date
        },
        headers={
            'authorization': 'Bearer {}'.format(token),
        }
    )

    print(res.text)
    assert res.status_code in [200, 201]
    return res.json()
