import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.hadis

patients_collection = database.get_collection("patient")

test_patient = "639ef5d39b7aca7c3abec5e9"


def test_delete_patient(id):
    # Delete a patient from the database
    print(database)
    print(patients_collection)
    try:
        patients_collection.delete_one({"_id": ObjectId(id)})
        print("Deleted patient")
        return True
    except:
        print("Failed to delete patient")
        return False


if __name__ == "__main__":
    test_delete_patient(test_patient)
