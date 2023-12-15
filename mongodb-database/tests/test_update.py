from pymongo import MongoClient

def test_update():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    feedback_collection = db["feedback"]

    result = feedback_collection.update_one(
        {"feedback_text": "Test feedback"}, 
        {"$set": {"feedback_text": "Updated test feedback"}}
    )

    print(f"Modified {result.modified_count} document(s)")

if __name__ == "__main__":
    test_update()
