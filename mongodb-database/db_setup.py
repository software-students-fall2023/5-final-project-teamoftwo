from pymongo import MongoClient
from datetime import datetime

def create_collections(db):
    # Creating collections
    db.create_collection("users")
    db.create_collection("feedback")

    print("Collections 'users' and 'feedback' created.")

def insert_initial_data(db):
    # Inserting some initial user data
    users_data = [
        {"user_id": 1, "name": "John Doe", "email": "john@example.com"},
        {"user_id": 2, "name": "Jane Doe", "email": "jane@example.com"}
    ]
    db.users.insert_many(users_data)

    # Inserting some initial feedback data
    feedback_data = [
        {"feedback_id": 1, "user_id": 1, "feedback_text": "Great service!", "timestamp": datetime.now()},
        {"feedback_id": 2, "user_id": 2, "feedback_text": "Very satisfied.", "timestamp": datetime.now()}
    ]
    db.feedback.insert_many(feedback_data)

    print("Initial data inserted into 'users' and 'feedback' collections.")

def main():
    # Connect to the MongoDB local client
    client = MongoClient("mongodb://localhost:27017/")

    # Connect to the database (will create if it doesn't exist)
    db = client["customer_feedback_db"]

    # Create collections and insert initial data
    create_collections(db)
    insert_initial_data(db)

if __name__ == "__main__":
    main()
