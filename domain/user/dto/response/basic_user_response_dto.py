"""
기본 entity 정보 리턴용 주문서
기존의 DB에서가지고 와서 나(BasicUserResponseDto)를 만든다.
"""
from dataclasses import dataclass

from domain.user.entity.user import User

@dataclass
class BasicUserResponseDto:
    name: str
    phone_number: str

    @classmethod
    def from_entity(cls, entity: User) -> "BasicUserResponseDto":

        return cls(
            name = entity.name,
            phone_number = entity.phone_number
        )
