from pymongo import MongoClient
from datetime import datetime

def test_insert():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    feedback_collection = db["feedback"]

    new_feedback = {
        "feedback_text": "Test feedback",
        "timestamp": datetime.now()
    }

    result = feedback_collection.insert_one(new_feedback)
    print(f"Inserted Feedback ID: {result.inserted_id}")

if __name__ == "__main__":
    test_insert()
