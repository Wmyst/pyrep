import os
from flask import Flask, render_template, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

## Configuration ##

app = Flask(__name__)
app.config["DEBUG"] = True

db = SQLAlchemy(app)
db.create_all()
db.session.add(Location("Hill House")
db.session.commit()

## Routing ##

@app.route("/")
@app.route("/tours")
def tours():
    return render_template('tours.html')


@app.route("/indtour/<int:value>")
def indtour(value):
    return render_template('indtour.html')

# if __name__ == "__main__":
#     app.run()

