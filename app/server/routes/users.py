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


@router.post("/", response_description="User data added to the Data Base")
async def add_user_data(user: SchemaDeUser = Body(...)):
    user = jsonable_encoder(user)
    new_user= await add_user(user)
    return ResponseModel(new_user, "User added.")