from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from flask import jsonify

from server.jwt.token_manager import (
    generate_token, validate_token    
)

from server.models.token import (
    User, 
    Token,
    ResponseToken,
    ErrorResponseToken
)

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

#@router.post('/login', response_model=Token)
@router.post('/login')
async def login(user: User):
    if user.username == 'test' and user.password == 'test':
        # Generar un token JWT con los datos del usuario
        data = {'username': user.username, 'password' : user.password}
        token = generate_token(data)
        validate_token(token)
        return ResponseToken(token, "token generated and validated")
    else:
        return ErrorResponseToken("ERROR", 404, 'Invalid login')


@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Get users data OK")
    return ResponseModel(users, "Users data empty")

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


#Version 1 -> app/server/user.py
@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "Updated ok - ID: {} ".format(id), "User Updated correctly"
        )
    return ErrorResponseModel(
        "ERROR",
        404,
        "Error in Update",
    )

# #Version 2 -> app/server/models/user.py
# @router.put("/{id}")
# async def update_user_data(id: str, req: SchemaDeUser.as_optional() = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_user = await update_user(id, req)
#     if updated_user:
#         return ResponseModel(
#             "Updated ok - ID: {} ".format(id),
#             "User Updated correctly",
#         )
#     return ErrorResponseModel(
#         "ERROR",
#         404,
#         "Error in Update",
#     )

@router.delete("/{id}", response_description="User data deleted")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User ID: {} deleted".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "ERROR", 404, "User with id {0} not exist".format(id)
    )


