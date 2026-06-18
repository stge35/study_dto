"""
CS상담원(주문 받는 사람)

"""
from domain.user.dto.request.create_user_dto import CreateUserDto
from domain.user.dto.response.basic_user_response_dto import BasicUserResponseDto
from domain.user.service.user_service import UserService


class UserController:

    def __init__(self, user_service: UserService):
        self.user_service = user_service


    def signup(self, dto: CreateUserDto) -> BasicUserResponseDto:

        try:
            response : BasicUserResponseDto = self.user_service.register_user(dto)
            return response

        except ValueError as e:
            raise ValueError(f"fail")