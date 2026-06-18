from dataclasses import dataclass

from domain.user.entity.user import User


@dataclass
class UpdateUserDto:

    password : str | None
    phone_number : str | None

    def update_entity(self, user_entity: User) -> None: # 기존의 User를 가지고 와서 안의 데이터만 수정하기에 None을 반환한다.

        if self.password is not None:
            user_entity.password = self.password

        if self.phone_number is not None:
            user_entity.phone_number = self.phone_number