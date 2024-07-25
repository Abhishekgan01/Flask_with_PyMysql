from flask import json


class Student:
    def __init__(self, id, email, password,  username ):
        self.id = id
        self.email = email
        self.password = password
        self.username = username

    def __str__(self) -> str:
        return f"({self.id} - {self.email}  - {self.password} - {self.username})"

    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__) 