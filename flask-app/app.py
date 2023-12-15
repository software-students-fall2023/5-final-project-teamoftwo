from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# MongoDB setup (adjust the URI as needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["customer_feedback_db"]
feedback_collection = db["feedback"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def submit_feedback():
    if request.method == 'POST':
        feedback_text = request.form['feedback']
        feedback_collection.insert_one({
            "feedback_text": feedback_text,
            "timestamp": datetime.now()
        })
        flash('Feedback submitted successfully!')  # Flash a confirmation message
        return redirect(url_for('view_feedback'))
    return render_template('feedback.html')

@app.route('/view-feedback')
def view_feedback():
    feedbacks = list(feedback_collection.find())
    return render_template('view_feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
