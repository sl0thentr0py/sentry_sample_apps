import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


sentry_sdk.init(
    traces_sample_rate=1.0,
    send_default_pii=True,
    debug=True,
    integrations=[StarletteIntegration()]
)


async def homepage(request):
    return JSONResponse({'hello': 'world'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
