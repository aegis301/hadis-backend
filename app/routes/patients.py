from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database.patients import (
    add_patient,
    delete_patient,
    fetch_patients,
    fetch_patient,
    update_patient,
)
from app.database.models.patient import (
    NewPatient,
    UpdatePatient,
)

from app.database.models.default import ResponseModel, ErrorResponseModel

router = APIRouter()

headers = {"Access-Control-Allow-Origin": "*"}


@router.post("/", response_description="Patient data added into the database")
async def add_patient_data(patient: NewPatient = Body(...)):
    patient = jsonable_encoder(patient)
    new_patient = await add_patient(patient)
    return ResponseModel(new_patient, "Patient added successfully.", headers)


@router.get("/", response_description="Patients retrieved")
async def get_patients():
    patients = await fetch_patients()
    if patients:
        return ResponseModel(patients, "Patients data retrieved successfully", headers)
    return ResponseModel(patients, "Empty list returned", headers)


@router.get("/{id}", response_description="Patient data retrieved")
async def get_patient_data(id):
    patient = await fetch_patient(id)
    if patient:
        return ResponseModel(patient, "Patient data retrieved successfully", headers)
    return ResponseModel("An error occurred.", 404, "Patient does not exist.")


@router.put("/{id}")
async def update_patient_data(id: str, req: UpdatePatient = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_patient = await update_patient(id, req)
    if updated_patient:
        return ResponseModel(
            f"Patient with ID: {id} updated successful",
            "Patient updated successfully",
            headers,
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the patient data.",
    )


@router.delete("/{id}", response_description="Patient data deleted from the database")
async def delete_patient_data(id: str):
    deleted_patient = await delete_patient(id)
    if deleted_patient:
        return ResponseModel(
            f"Patient with ID: {id} removed", "Patient deleted successfully", headers
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"Patient with id {id} doesn't exist"
    )
