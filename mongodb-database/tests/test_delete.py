from pymongo import MongoClient

def test_delete():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customer_feedback_db"]
    feedback_collection = db["feedback"]

    result = feedback_collection.delete_one({"feedback_text": "Updated test feedback"})
    print(f"Deleted {result.deleted_count} document(s)")

if __name__ == "__main__":
    test_delete()
