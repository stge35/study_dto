"""
본사 관리자 / 정산-출고 관리부
본사 관리자의 명령을 만드는 과정?
"""
from domain.user.dto.request.create_user_dto import CreateUserDto
from domain.user.dto.response.basic_user_response_dto import BasicUserResponseDto
from domain.user.repository.user_interface import UserInterface


class UserService:

    def __init__(self, user_repository: UserInterface):
        self.user_repository = user_repository

    def register_user(self, dto: CreateUserDto) -> BasicUserResponseDto:

        saved_user = self.user_repository.create_user(dto) # CreateUserDto 주문서를 넣어주면 repository 기사가 User 제품을 가져와 save_user 파트에 놓아둘게



        return BasicUserResponseDto.from_entity(saved_user) # saved_user 파트의 제품의 영수증을 제작해줄게