from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")

@app.get("/search")
def search():	
    args = request.args.get("q")
    return redirect(f"https://google.com/search?q={args}")


@app.get("/lucky")
def lucky():
    query = request.args.get("q")
    return redirect(f"https://en.wikipedia.org/wiki/{query}")


if __name__ == "__main__":
    app.run(debug=True)