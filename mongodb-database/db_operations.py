from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") # Replace with your MongoDB URI
db = client.customer_feedback # Database name
users = db.users # Users collection
feedback = db.feedback # Feedback collection

# Example: Inserting data
user_data = {"user_id": 1, "name": "John Doe", "email": "john@example.com"}
feedback_data = {"feedback_id": 1, "user_id": 1, "feedback_text": "Great service!", "timestamp": "2021-01-01"}

users.insert_one(user_data)
feedback.insert_one(feedback_data)

# Example: Fetching data
for f in feedback.find():
    print(f)
