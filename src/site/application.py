from config import app
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse

import uvicorn


@app.route('/')
async def homepage(request):
    template = app.get_template('index.html')
    content = template.render(request=request)
    return HTMLResponse(content)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)