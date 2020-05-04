from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_mars")

@app.route("/")

def home():

    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", destination_data=mars_data)

@app.route("/scrape")

def scrape():

    mars_data = mission_to_mars.scrape()
 
    mongo.db.collection.update({}, mars_data, upsert=True)

  
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)
