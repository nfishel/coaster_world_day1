from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import queries as q


app = Flask(__name__)

# configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)

#### Place all of your routes below here
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/country", methods=["POST", "GET"])
def get_country():
  if request.method == "GET":
    results = q.get_all_countries()
    return render_template("country.html", countries_list=results)
  else: # using the post request method
    country = request.form.get("country")
    session["country"] = country
    return redirect("/")
    
  






  
#### Place all of your routes above here

#leave at the bottom of your main.py file
if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)