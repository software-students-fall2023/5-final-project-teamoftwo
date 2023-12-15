from pymongo import MongoClient

def test_read():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    feedback_collection = db["feedback"]

    for feedback in feedback_collection.find():
        print(feedback)

if __name__ == "__main__":
    test_read()
