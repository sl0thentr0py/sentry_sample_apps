from quart import Quart
from sentry_sdk import init
from sentry_sdk.integrations.quart import QuartIntegration

app = Quart(__name__)

init(
    integrations=[QuartIntegration()],
    traces_sample_rate=1.0,
)

@app.route('/health', methods=['GET'])
def health():
    return {'status': 'pass'}

app.run()
