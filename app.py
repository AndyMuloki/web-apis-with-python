# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    
    # response = {"usage" : "/dict?=<word>"}
    # return jsonify(response)

    return render_template("index.html")


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get("word")

    response_data = {"words" : []}

    if not word:
        response_data["words"].append({
            "word" : None,
            "status" : "error",
            "data" : "word not found"
        })
    else:
        definitions = match_exact(word)
        if definitions:
            resp_status = "success"
        else:
            definitions = match_like(word)
            if definitions:
                resp_status = "partial"
            else:
                resp_status = "error"
                definitions = []

        response_data["words"].append({
            "word" : word,
            "status" : resp_status,
            "data" : definitions
        })

    response = {"json": response_data}
    return render_template("results.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)
