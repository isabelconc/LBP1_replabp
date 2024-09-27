from flask import Blueprint, render_template
from models.pessoa import pessoa

app2 = Blueprint("exemplo", __name__)

@app2.route("/")
def exibir():
    return render_template('index.html')

