from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeUser,
    UpdateUserModel,
)

router = APIRouter()


@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Get users data OK")
    return ResponseModel(users, "Get users data empty")

@router.get("/{id}", response_description="User data By ID OK")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "Get User data OK")
    return ErrorResponseModel("Error", 404, "The user not exist")

@router.post("/", response_description="User data added to the Data Base")
async def add_user_data(user: SchemaDeUser = Body(...)):
    user = jsonable_encoder(user)
    new_user= await add_user(user)
    return ResponseModel(new_user, "User added.")