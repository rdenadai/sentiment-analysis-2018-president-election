from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles

app = Starlette(debug=False, template_directory='src/site/templates')
app.mount('/static', StaticFiles(directory='src/site/media'), name='static')
