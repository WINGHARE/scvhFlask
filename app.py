from flask import Flask, render_template
import pandas as pd
from sklearn.manifold import TSNE
import json
import plotly
import plotly.express as px
app = Flask(__name__)
@app.route('/')
def notdash():
    df = px.data.iris()
    features = df.loc[:, :'petal_width']
    tsne = TSNE(n_components=2, random_state=0)
    projections = tsne.fit_transform(features)

    fig = px.scatter(
        projections, x=0, y=1,
        color=df.species, labels={'color': 'species'}
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('scatter.html', graphJSON=graphJSON)