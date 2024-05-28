from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from adapters.out_port.persistence.nosqldatabase.repositories.user_repository import UserRepository
from core.usecases.user_read_use_case import UserReadUseCase
from core.usecases.user_write_use_case import UserWriteUseCase
from core.domain.login_model import LoginModel

from adapters.out_port.jwt.token_manager import (
    generate_token, validate_token
)

from core.domain.token_model import (
    Token,
    ResponseToken,
    ErrorResponseToken
)

from core.domain.user_model import (
    ErrorResponseModel,
    ResponseModel,
    UserModel,
    UpdateUserModel,
)

router = APIRouter()

user_repository = UserRepository()

user_read_use_case = UserReadUseCase(user_repository)
user_write_use_case = UserWriteUseCase(user_repository)


@router.post('/login')
async def login(user: LoginModel):
    #TODO pasar la logica de negocio al usecase
    if user.username == 'test' and user.password == 'test':
        # Generar un token JWT con los datos del usuario
        data = {'username': user.username, 'password': user.password}
        token = generate_token(data)
        validate_token(token)
        return ResponseToken(token, "token generated and validated")
    else:
        return ErrorResponseToken("ERROR", 404, 'Invalid login')


@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await user_read_use_case.find_all()
    if users:
        return ResponseModel(users, "Get users data OK")
    return ResponseModel(users, "Users data empty")


@router.get("/{id}", response_description="User data By ID OK")
async def get_user(user_id):
    user = await user_read_use_case.find_by_id(user_id)
    if user:
        return ResponseModel(user, "Get User data OK")
    return ErrorResponseModel("Error", 404, "The user not exist")


@router.post("/", response_description="User data added to the Data Base")
async def create_user(user_data: UserModel = Body(...)):
    user = jsonable_encoder(user_data)
    new_user = await user_write_use_case.create_user(user)
    return ResponseModel(new_user, "Successfully registered user.")


@router.put("/{id}")
async def update_user(user_id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await user_write_use_case.update_user(user_id, req)
    if updated_user:
        return ResponseModel(
            "Updated ok - ID: {} ".format(user_id), "User Updated correctly"
        )
    return ErrorResponseModel(
        "ERROR",
        404,
        "Error in Update",
    )


@router.delete("/{id}", response_description="User data deleted")
async def delete_user(user_id: str):
    deleted_user = await user_write_use_case.delete_user(user_id)
    if deleted_user:
        return ResponseModel(
            "User ID: {} deleted".format(user_id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "ERROR", 404, "User with id {0} not exist".format(user_id)
    )
