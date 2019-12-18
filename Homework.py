import os
from bottle import Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://790bd29991bd4820ab90c961bc453e5b@sentry.io/1857465",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/success')
def success():
    return

@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")

app.run(host='localhost', port=8080)
