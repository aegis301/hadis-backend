# from db import Patient
# from mongoengine import connect, disconnect
# from dotenv import load_dotenv
# import os


# load_dotenv()

# MONGO_USER = os.getenv("MONGO_USER")
# MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
# MONGO_HOST = os.getenv("MONGO_HOST")
# MONGO_DB = os.getenv("MONGO_DB")
# MONGO_PORT = os.getenv("MONGO_PORT")

# connect(
#     MONGO_DB,
#     host=MONGO_HOST,
#     port=int(MONGO_PORT),
#     username=MONGO_USER,
#     password=MONGO_PASSWORD,
# )


# harry = Patient(
#     name="Harry Potter", age=30, main_diagnosis="Headache", date_of_birth="1980-07-31"
# )
# hermoine = Patient(
#     name="Hermione Granger",
#     age=25,
#     main_diagnosis="Cat allergy",
#     date_of_birth="1985-09-19",
# )
# harry.save()
# hermoine.save()

# disconnect()
