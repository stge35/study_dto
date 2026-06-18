"""
물류창고 출고 가이드라인
주문번호와 상품코드(dto)를 주면 물건을(entity)를 출고한다.
"""
from abc import abstractmethod

from domain.user.dto.request.create_user_dto import CreateUserDto
from domain.user.dto.request.update_user_dto import UpdateUserDto
from domain.user.entity.user import User


class UserInterface:

    # CreateUserDto(주문번호 및 상품코드)를 주면 User(물건)을 출고한다.
    @abstractmethod
    def create_user(self, dto: CreateUserDto)-> User:

        """
        create 요리 레시피 규격
        """
        pass

    @abstractmethod
    def update_user(self, dto: UpdateUserDto) -> None:
        pass

    @abstractmethod
    def find_by_user(self, name: str) -> bool:
        """
        물건의 이름으로 찾는 레시피 규격
        존재 여부만 확인
        """
        pass