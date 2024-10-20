from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the main form page (New or Existing Nomination)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nomination_type = request.form.get("nomination")
        if nomination_type == "new":
            # Redirect to new nomination form
            return redirect(url_for('new_nomination'))
        elif nomination_type == "existing":
            # Redirect to the sport selection page
            return redirect(url_for('select_sport'))
    return render_template('index.html')

# Route to render the New Nomination form
@app.route("/new-nomination", methods=["GET"])
def new_nomination():
    return render_template('new_nomination.html')

# Route for selecting a sport for existing nominations
@app.route("/select-sport", methods=["GET", "POST"])
def select_sport():
    if request.method == "POST":
        sport = request.form.get("sport")
        if sport == "athletics":
            return redirect(url_for('existing_athlete', sport="Athletics"))
        elif sport == "equestrian":
            return redirect(url_for('existing_athlete', sport="Equestrian"))
        elif sport == "fencing":
            return redirect(url_for('existing_athlete', sport="Fencing"))
        elif sport == "judo":
            return redirect(url_for('existing_athlete', sport="Judo"))
        elif sport == "jujitsu":
            return redirect(url_for('existing_athlete', sport="JuJitsu"))
        elif sport == "karate":
            return redirect(url_for('existing_athlete', sport="Karate"))
        elif sport == "para-athletics":
            return redirect(url_for('existing_athlete', sport="Para Athletics"))
        elif sport == "shooting":
            return redirect(url_for('existing_athlete', sport="Shooting"))
        elif sport == "swimming":
            return redirect(url_for('existing_athlete', sport="Swimming"))
        elif sport == "taekwondo":
            return redirect(url_for('existing_athlete', sport="Taekwondo"))
        elif sport == "weightlifting":
            return redirect(url_for('existing_athlete', sport="Weightlifting"))
        elif sport == "wrestling":
            return redirect(url_for('existing_athlete', sport="Wrestling"))
    return render_template('select_sport.html')

# Route for Existing Athlete Nomination (with prefilling in Airtable)
@app.route("/existing_athlete", methods=["GET"])
def existing_athlete():
    sport = request.args.get('sport', '')
    return render_template('existing_athlete.html', sport=sport)

if __name__ == "__main__":
    app.run(debug=True)
