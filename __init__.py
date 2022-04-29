import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template("Home.html")


if __name__ == '__main__':
    app.debug = True
    app.run(port=5657)
