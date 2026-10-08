from flask import Flask, render_template, request
from main import get
import json

app = Flask(__name__)

 

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
 
        sym = request.form.get("sym")

        prompt = f"""
        
        Symptoms: {sym}

        Analyze the symptoms and provide general health information.

        Do NOT claim to make a definitive diagnosis.
        Mention possible conditions that could be associated with these symptoms,
        and provide general precautions and advice about when to seek medical care.

        Return ONLY valid JSON in exactly this format:

        {{
            "potential_illness": [],
            "precautions": []
        }}
        """

        result = get(prompt)
        result = json.loads(result)
        potential_illness = result.get("potential_illness", [])
        precautions = result.get("precautions", [])
    

    

        # Example: Gemini response
        

        # Extract Gemini data
         

        return render_template(
            "health_dashboard.html",
            potential_illness=potential_illness,
            precautions=precautions
        )

     
         

    return render_template("home.html")

@app.route("/health_dashboard")
def dashboard():

    return render_template(
        "health_dashboard.html"
    )
if __name__ == "__main__":
    app.run(debug=False)