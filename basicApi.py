from flask import Flask, request

app = Flask(__name__)

# Defining routed home
@app.route('/')
def home():
    return "Welcome to the home page"

"""
    Route to send 2 nos through url and add    
    Sample Url http://127.0.0.1:5000/addParam?a=23&b=90
    
    In GET requests the parameters are visible in the Url
"""


@app.route('/addParam', methods=["GET"])
def addParam():
    a = request.args.get("a")
    b = request.args.get("b")

    return str(int(a) + int (b))


"""
    Route to send 2 nos through Postman
    
    In POST requests the parameters are NOT visible in the Url
"""


@app.route('/addParamPost', methods=["POST"])
def addParamPost():
    a = request.form["a"]
    b = request.form["b"]

    return str(int(a) + int(b))


if __name__ == '__main__':
    app.run()