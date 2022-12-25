import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.hadis

patients_collection = database.get_collection("patient")

# retrieve all patients in the database
async def retrieve_patients():
    patients = []
    async for patient in patients_collection.find():
        patients.append(patient_helper(patient))
    return patients


# Add a new patient into to the database
async def add_patient(patient_data: dict) -> dict:
    patient = await patients_collection.insert_one(patient_data)  # returns an object
    new_patient = await patients_collection.find_one({"_id": patient.inserted_id})


# Retrieve a patient with a matching ID
async def retrieve_patient(id: str) -> dict:
    patient = await patients_collection.find_one({"_id": ObjectId(id)})
    if patient:
        return patient_helper(patient)


# Update a patient with a matching ID
async def update_patient(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    patient = await patients_collection.find_one({"_id": ObjectId(id)})
    if patient:
        updated_patient = patients_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_patient:
            return True
        return False


# Delete a patient from the database
async def delete_patient(id: str):
    try:
        patient = await patients_collection.delete_one({"_id": ObjectId(id)})
        print(f"Successfully deleted patient {patient.id} from database")
        return True
    except:
        print("Failed to delete patient")
        return False


# helpers


def patient_helper(patient) -> dict:
    return {
        "id": str(patient["_id"]),
        "name": patient["name"],
        "age": patient["age"],
        "main_diagnosis": patient["main_diagnosis"],
        "date_of_birth": patient["date_of_birth"],
    }
