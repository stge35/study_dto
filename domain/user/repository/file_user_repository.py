import json
import os.path
from abc import ABCMeta

from domain.user.dto.request.create_user_dto import CreateUserDto
from domain.user.entity.user import User

"""
지게차 기사 : 주문서(dto)를 받아서 물류창고(DB)에서 물품(entity)를 가져온다
거대 물류창고(Database)
"""
from domain.user.repository.user_interface import UserInterface


class FileUserRepository(UserInterface, metaclass=ABCMeta):

    def __init__(self, file_path: str = "users.json"):

        self.file_path = file_path
        
        if not os.path.exists(self.file_path):
            self._save_file({})

    def create_user(self, dto: CreateUserDto) -> User:

        user = dto.to_entity() # 제품 인스턴스를 만든다.

        users_db = self._read_file() # 전체 제품을 읽어온다.

        users_db[user] = {
            "password" : user.password,
            "phone_number" : user.phone_number
        }

        self._save_file(users_db)

        return user

    def _save_file(self, data: dict) -> None:
        with open(self.file_path, "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)


    def _read_file(self) -> dict:

        with open(self.file_path, "r", encoding = "utf-8") as f:
            return json.load(f)