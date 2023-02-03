from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from src.app.user.schemas import EmailSchema
from src.app.user.services import UserService
from src.core.schemas import ErrorSchema


router = APIRouter(
    tags=['user'],
)


@router.get(
    '/send_one_time_code',
    status_code=200,
    response_model=EmailSchema,
)
async def send_one_time_code(
    email: str,
    user_services: UserService = Depends(),
):
    result = await user_services.create_save_send_code(email)

    if isinstance(result, ErrorSchema):
        raise HTTPException(
            status_code=result.status_code,
            detail=result.detail,
        )

    return EmailSchema(email=email)
