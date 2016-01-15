from flask import Flask


## Create the application objecet
app = Flask(__name__)

## Error handling
app.config["DEBUG"] = True

# Dynamic route

@app.route("/")
@app.route("/test")
@app.route("/hello")
@app.route("/test/<search_query>")
def search(search_query):
    return search_query + "and hello to you!"

# Various types of non-string values

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"

# Dynamic route w/ explicit status codes

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name), 200
    else:
        return "Not Founded", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()