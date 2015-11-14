__author__ = 'Frankie'


from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    content = request.get_json()
    file = request.url_root[7:]
    with open(file[:len(file)-6] + ".txt", "a") as myfile:
            myfile.write(str(content))

app.run(host = '0.0.0.0')