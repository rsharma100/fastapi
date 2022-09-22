from fastapi import FastAPI
from routers import content, user
import uvicorn
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(content.router)
app.include_router(user.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My First Project",
        version="1.1.0",
        description="This is my first project on FastAPI",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, root_path="/")

# date_time = datetime.utcnow()

# @app.post('/insert', tags=["Content"], dependencies=[Depends(auth_bearer.JWTBearer())])
# def insert_record(request:models.DataInfo):
#     date_time = datetime.utcnow()
#     record_dict = {'file_name' : request.file_name, 'coll_name': request.coll_name, 'date_time': date_time, 'modified_date': None}
#     inset_data = mydb["mydata"].insert_one(record_dict)
#     #print(inset_data)
#     return (f"Record successfully inserted with id : {str(inset_data.inserted_id)}")

# @app.get('/get/{id}', tags=["Content"], dependencies=[Depends(auth_bearer.JWTBearer())])
# def get_record(id):
#     item = mydb["mydata"].find_one(ObjectId(id))
#     #return userEntity(item)
#     if item:
#         return userEntity(item)
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Record not found with id {id}')
#     #print(data)

# @app.get('/getall', tags=["Content"], dependencies=[Depends(auth_bearer.JWTBearer())])
# def getall_record():
#     item = mydb["mydata"].find()
# #    print(item)
#     return usersEntity(item)

# @app.delete('/remove/{id}', tags=["Content"], dependencies=[Depends(auth_bearer.JWTBearer())])
# def delete_record(id):
#     item = mydb["mydata"].find_one_and_delete({"_id":ObjectId(id)})
# #    print(item)
#     if item:
#         return f'Succseefully deleted'
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Record not found with id {id}')

# @app.put('/update/{id}', tags=["Content"], dependencies=[Depends(auth_bearer.JWTBearer())])
# def update_record(id, request: models.DataInfo):
#     date_time = datetime.utcnow()
#     item = mydb["mydata"].find_one({"_id":ObjectId(id)})
# #    print(item)
#     if item:
#         i = {"file_name": request.file_name, "coll_name": request.coll_name, "modified_date": date_time}
#         mydb["mydata"].find_one_and_update({"_id":ObjectId(id)},{"$set":dict(i)})
#         update_item = mydb["mydata"].find_one({"_id":ObjectId(id)})
#         return userEntity(update_item)
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Record not found with id {id}')

# @app.post('/signup', tags=["Signup"])
# def user_signup(req:models.UserInfo):
#     if mydb["myuser"].find_one({"mail": req.mail}):
#         return f"User already registered with email {req.mail}"
#     else:
#         insert_user = mydb["myuser"].insert_one({"name":req.name, "mail":req.mail, "password":req.password})
#         return f"Account created successfully with email {req.mail}"

# @app.get('/login', tags=["Login"])
# def login(Email: str, Password: SecretStr):
#     #user_detail= {"email":request.mail, "password": request.password}
#     my_user = mydb["myuser"].find_one({"mail": Email}, {"_id":0})
#     my_email = my_user["mail"]
#     my_password = SecretStr(my_user["password"])
#     if Email==my_email and Password==my_password:
#         return tokan.encodeJWT(my_email)
#     else:
#         return "Incorrect Email or Password."