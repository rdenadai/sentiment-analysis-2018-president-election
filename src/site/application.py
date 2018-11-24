
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import uvicorn
import numpy as np
from sklearn.externals import joblib

from .config import app
from ..ai.utils import tokenizer


emt_tfidf, emt_lsa, emt_ml = joblib.load('src/ai/models/tfidf_emotions.sav'), \
                             joblib.load('src/ai/models/lsa_emotions.sav'), \
                             joblib.load('src/ai/models/model_emotions.sav')
val_tfidf, val_lsa, val_ml = joblib.load('src/ai/models/tfidf_valence.sav'), \
                             joblib.load('src/ai/models/lsa_valence.sav'), \
                             joblib.load('src/ai/models/model_valence.sav')


@app.route('/')
async def index(request):
    template = app.get_template('index.html')
    content = template.render(request=request)
    return HTMLResponse(content)


@app.route('/analyze', methods=['POST'])
async def analyze(request):
    retorno = { 'status': False, }

    data = await request.form()
    phrase = data['phrase'].strip()
    if len(phrase):
        # TOKENIZE
        tokens = tokenizer(phrase)

        X_tfidf = emt_tfidf.transform([tokens])
        X_svd = emt_lsa.transform(X_tfidf)
        emotion = emt_ml.predict(X_svd)[0]
        emotion_prob = list(np.round(emt_ml.predict_proba(X_svd)[0] * 100, 2))
        emotion_classes = emt_ml.classes_

        # Valence
        X_tfidf = val_tfidf.transform([tokens])
        X_svd = val_lsa.transform(X_tfidf)
        valence = val_ml.predict(X_svd)[0]
        valence_prob = list(np.round(val_ml.predict_proba(X_svd)[0] * 100, 2))
        valence_classes = val_ml.classes_

        emotion_probabilities = {}
        valence_probabilities = {}
        for k, classe in enumerate(emotion_classes):
            emotion_probabilities[classe] = emotion_prob[k]
        for k, classe in enumerate(valence_classes):
            valence_probabilities[classe] = valence_prob[k]

        retorno = {
            'status': True,
            'phrase': phrase,
            'tokens': tokens,
            'emotion': emotion,
            'emotion_proba': emotion_probabilities,
            'valence': valence,
            'valence_proba': valence_probabilities
        }
    return JSONResponse(retorno)


if __name__ == '__main__':
    uvicorn.run(app)
