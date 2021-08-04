from flask import Flask, render_template
import pandas as pd
from sklearn.manifold import TSNE
import json
import plotly
import plotly.express as px
import scanpy as sc
from datetime import datetime
import re
app = Flask(__name__)
@app.route('/')
def notdash():
    adata=sc.read_h5ad("data/gccells.h5ad")
    df = adata.obs
    projections = adata.obsm['X_umap']

    fig = px.scatter(
        projections, x=0, y=1,
        color=df.leiden, labels={'color': 'cluster'}
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('scatter.html', graphJSON=graphJSON)

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content