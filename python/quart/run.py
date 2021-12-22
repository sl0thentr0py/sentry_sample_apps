from quart import Quart

import sentry_sdk

sentry_sdk.init(
    traces_sample_rate=1.0,
    send_default_pii=True,
    debug=True
)

app = Quart(__name__)
# app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
async def index():
     return 'Hello World'


@app.route('/error')
async def error():
    raise ValueError('quart neel exception')


if __name__ == "__main__":
    app.run()
