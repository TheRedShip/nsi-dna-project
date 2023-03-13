from flask import Flask, render_template
from string import ascii_lowercase
import random
import math
import database
from dna import ADN

database.InitializeDatabases()

alphabet = ["A", "C", "G", "T"]
genome = "".join(
    [alphabet[random.randint(0,
                             len(alphabet) - 1)] for i in range(1000)])

# adn = ADN(genome)
# adn.convertedGen = adn.convertedGen[:250] + "HUGO" + adn.convertedGen[200:]

# print(adn.search("HUG"))
# print(adn.searchHard("HUGO"))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/genes/:geneId/search/:content')
def geneSearch():
    pass


app.run(host='0.0.0.0', port=81)
