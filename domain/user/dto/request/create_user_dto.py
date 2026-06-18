
"""
주문서(그럼 이건 user라는 인스턴스 생성을 받는건가?
"""
from dataclasses import dataclass

from domain.user.entity.user import User

@dataclass
class CreateUserDto:

    name : str
    password: str
    phone_number: str

    def to_entity(self) -> "User":

        return User(
            name = self.name,
            password = self.password,
            phone_number = self.phone_number
        )
