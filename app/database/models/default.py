def ResponseModel(data, message, headers):
    return {
        "payload": data,
        "code": 200,
        "message": message,
        "headers": headers,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
