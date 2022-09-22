def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "filename":item["file_name"],
        "collection":item["coll_name"],
        "date and time":item["date_time"],
        "Status":item["status"],
        "By User":item["by_user"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]