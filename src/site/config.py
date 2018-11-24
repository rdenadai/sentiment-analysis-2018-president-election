from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles

app = Starlette(debug=True, template_directory='templates')
app.mount('/static', StaticFiles(directory='media'), name='static')
