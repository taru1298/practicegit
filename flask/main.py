from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to the channel</h1>"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    return f"The person has passed and the score is: {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed and the score is: {score}"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        try:
            # Collect form data
            maths = float(request.form.get('maths', 0))
            science = float(request.form.get('science', 0))
            social = float(request.form.get('social', 0))

            # Calculate average marks
            average_marks = (maths + science + social) / 3

            # Redirect based on the score
            if average_marks >= 50:
                return redirect(url_for('success', score=int(average_marks)))
            else:
                return redirect(url_for('fail', score=int(average_marks)))
        except ValueError:
            return "Invalid input. Please enter valid numbers for all fields."
    
    # Render the form template for GET request
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
