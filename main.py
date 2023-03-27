from flask import Flask, render_template, request
import database
from dna import DNA, FetchAllDNANames, GetDNAFromId

database.InitializeDatabases()

# alphabet = ["A", "C", "G", "T"]
# genome = "".join(
#     [alphabet[random.randint(0,
#                              len(alphabet) - 1)] for i in range(1000)])

# adn = DNA(genome)
# adn.convertedGen = adn.convertedGen[:250] + "HUGO" + adn.convertedGen[250:]

# print(adn.search("HUG"))
# print(adn.searchHard("HUGO"))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', dnaNames=FetchAllDNANames())


@app.route('/api/v1/genes/<geneId>/search/<content>')
def geneSearchContent(geneId, content):
    content = content.upper()
    dna = GetDNAFromId(geneId)
    if not dna:
        return {
            "code": "NOT_FOUND",
            "params": {
                "geneId": geneId
            }
        }, 404
    else:
        searchResult = dna.searchHard(content) if request.args.get('hard-search') == '1' else dna.search(content)
        if searchResult['finded']:
            return {
                "code": "OK",
                "result": {
                    "occurences": searchResult['occurences']
                }
            }, 200
        else:
            return {
                "code": "NOT_FOUND",
                    "params": {
                        "geneId": geneId,
                        "content": content
                    }
                }, 404
        
@app.route('/api/v1/genes/<geneId>')
def geneSearch(geneId):
    dna = GetDNAFromId(geneId)
    if not dna:
        return {
            "code": "NOT_FOUND",
            "params": {
                "geneId": geneId
            }
        }, 404
    else:
        return {
            "code": "OK",
            "result": {
                "name": dna.geneName,
                "id": dna.geneId,
                "original": dna.originalGen,
                "converted": dna.convertedGen
            }
        }
        
@app.route('/api/v1/genes', methods=["POST"])
def createGene():
    body = request.get_json(force=True)
    print(body)
    if not body or not body['name'] or not body['content']:
        return {
            "code": "INVALID_BODY"
        }, 400
    else:
        dna = DNA(body['content'], None, body['name'])
        if dna.geneName != body['name']:
            return {
                "code": "ALREADY_EXISTS",
            }, 422
        else:
            return {
                "code": "OK",
                "result": {
                    "name": dna.geneName,
                    "id": dna.geneId,
                    "original": dna.originalGen,
                    "converted": dna.convertedGen
                }
            }
        

app.run(host='0.0.0.0', port=81)
