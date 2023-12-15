# Final Project

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.

## Setting Up the Database

### Prerequisites
- Ensure that MongoDB is installed and running on your local machine.
- Python and `pymongo` should be installed in your Python environment.

### Steps to Set Up the Database

1. **Run the `db_setup.py` Script**:
   Navigate to the `mongodb-database` directory and run the `db_setup.py` script. This script will create two collections (`users` and `feedback`) in the `customer_feedback_db` database and insert some initial data into these collections.

   ```bash
   cd mongodb-database
   python db_setup.py
