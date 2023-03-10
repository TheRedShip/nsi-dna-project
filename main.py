from flask import Flask, render_template
from string import ascii_lowercase
import random
import math
import database
from dna import ADN

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


genome = "".join(
    [ascii_lowercase[math.floor(random.randint(0, 25))] for i in range(1000)])

database.InitializeDatabases()
# adn = ADN("TGACGAGTAGAC")

app.run(host='0.0.0.0', port=81)
