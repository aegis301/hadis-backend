from typing import Optional
from pydantic import BaseModel, Field
from .default import PydanticObjectId


class NewPatient(BaseModel):
    """New patient model"""

    name: str = Field(...)
    age: int = Field(...)
    main_diagnosis: str = Field(...)
    date_of_birth: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Harry Potter",
                "age": 30,
                "main_diagnosis": "Headache",
                "date_of_birth": "1980-07-31",
            }
        }


class UpdatePatient(BaseModel):
    """Fields to update an existing patient"""

    name: Optional[str]
    age: Optional[int]
    main_diagnosis: Optional[str]
    date_of_birth: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Harry Potter",
                "age": 30,
                "main_diagnosis": "Headache",
                "date_of_birth": "1980-07-31",
            }
        }


class Patient(NewPatient):
    """NewPatient + id field"""

    id: PydanticObjectId = Field(..., alias="_id")
