from bson.objectid import ObjectId


class PydanticObjectId(ObjectId):
    """Pydantic ObjectId type for MongoDB"""

    @classmethod
    def __get_validators__(cls):
        """Pydantic validator for ObjectId"""
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Validate ObjectId"""
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)


def ResponseModel(data, message, headers):
    """Response model for API responses"""
    return {
        "payload": data,
        "code": 200,
        "message": message,
        "headers": headers,
    }


def ErrorResponseModel(error, code, message):
    """Error response model for API responses"""
    return {"error": error, "code": code, "message": message}
