"""
실제 상품 / 고유번호, 제조일자, 원가 등이 적혀있는 회사 자산
"""
from dataclasses import dataclass


@dataclass
class User:

    name: str
    password: str   # password는 해쉬로 만든 후 다시 설정
    phone_number: str = "031-903-7360"

    # 이렇게 함으로써 새로운 인스턴스 생성시점을 만든다.
    @classmethod
    def of(cls,
           name: str,
           password: str,
           phone_number: str
        ) -> "User":

        return cls(
            name = name,
            password = password,
            phone_number = phone_number
        )

