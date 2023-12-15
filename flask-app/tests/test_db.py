import pytest
from pymongo import MongoClient
from datetime import datetime

@pytest.fixture(scope="module")
def mongo_client():
    # Set up a separate test database
    client = MongoClient("mongodb://localhost:27017/")
    yield client
    # Clean up: Drop the test database after tests are done
    client.drop_database("test_customer_feedback_db")

def test_insert_and_read_feedback(mongo_client):
    test_db = mongo_client["test_customer_feedback_db"]
    feedback_collection = test_db["feedback"]

    # Insert a test feedback
    test_feedback = {
        "feedback_text": "Test feedback",
        "timestamp": datetime.now()
    }
    insert_result = feedback_collection.insert_one(test_feedback)
    assert insert_result.inserted_id

    # Read the inserted feedback
    read_feedback = feedback_collection.find_one({"_id": insert_result.inserted_id})
    assert read_feedback is not None
    assert read_feedback['feedback_text'] == "Test feedback"

def test_update_feedback(mongo_client):
    test_db = mongo_client["test_customer_feedback_db"]
    feedback_collection = test_db["feedback"]

    # Insert a test feedback
    feedback_collection.insert_one({"feedback_text": "Old feedback", "timestamp": datetime.now()})
    
    # Update the feedback
    updated_feedback = "Updated feedback"
    feedback_collection.update_one({"feedback_text": "Old feedback"}, {"$set": {"feedback_text": updated_feedback}})
    
    # Verify update
    updated_record = feedback_collection.find_one({"feedback_text": updated_feedback})
    assert updated_record
    assert updated_record['feedback_text'] == updated_feedback

def test_delete_feedback(mongo_client):
    test_db = mongo_client["test_customer_feedback_db"]
    feedback_collection = test_db["feedback"]

    # Insert a test feedback
    feedback_id = feedback_collection.insert_one({"feedback_text": "Test feedback", "timestamp": datetime.now()}).inserted_id

    # Delete the feedback
    feedback_collection.delete_one({"_id": feedback_id})
    
    # Verify deletion
    deleted_record = feedback_collection.find_one({"_id": feedback_id})
    assert deleted_record is None
