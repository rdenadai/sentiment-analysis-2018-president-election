from config import app
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse

import uvicorn


@app.route('/')
async def index(request):
    template = app.get_template('index.html')
    content = template.render(request=request)
    return HTMLResponse(content)


@app.route('/analyze', methods=['POST'])
async def analyze(request):
    return JSONResponse({'message': 'Working fine'})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)