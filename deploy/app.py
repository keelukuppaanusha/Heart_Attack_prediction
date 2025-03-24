from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Hardcoded username and password
VALID_USERNAME = "user"
VALID_PASSWORD = "1234"

# Load pre-trained model (update the path as necessary)
model = joblib.load('model.pkl')

# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the form data
        username = request.form["username"]
        password = request.form["password"]
        
        # Check credentials
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # Redirect to home page on successful login
            return redirect(url_for("home"))
        else:
            # Show error message if credentials are incorrect
            error = "Invalid credentials, please try again."
            return render_template("login.html", error=error)
    
    # If it's a GET request, just show the login page
    return render_template("login.html")

# Route for the home page (after successful login)
@app.route("/home")
def home():
    return render_template("home.html")

# Route for the prediction page
@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        try:
            # Get form data and convert to float
            int_features = [float(x) for x in request.form.values()]
            final_features = [np.array(int_features)]
            
            # Make prediction using the model
            prediction = model.predict(final_features)
            output = prediction[0]
            
            # Determine prediction result
            if output == 1:
                prediction_text = "HEART STROKE WILL OCCUR"
            else:
                prediction_text = "HEART STROKE WILL NOT OCCUR"
            
            return render_template("output.html", prediction_text=prediction_text)
        except Exception as e:
            return render_template("output.html", prediction_text=f"Error: {e}")
    
    # If it's a GET request, show the prediction form
    return render_template("prediction.html")

# Route for the classification report page
@app.route("/classification_report")
def classification_report_page():
    return render_template("classification_report.html")

# Route for the accuracy page
@app.route("/accuracy")
def accuracy_page():
    return render_template("accuracy.html")

# Route for logout
@app.route("/logout")
def logout():
    return redirect(url_for("login"))

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)

