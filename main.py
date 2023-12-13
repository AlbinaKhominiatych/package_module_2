"""Серіалізація об'єктів класу у JSON:
Створіть клас, який представляє об'єкт з деякими властивостями
(наприклад, користувач з ім'ям та віком).
Серіалізуйте екземпляр цього класу в JSON за
допомогою json.dumps() та переконайтесь, що дані правильно серіалізовані."""
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"

user = User("Alice", 30)
serialized_user = json.dumps(user.__dict__)

print(serialized_user)
load_user = json.loads(serialized_user)
print(load_user)
#user = User(load_user["name"], load_user["age"])
#user = User(**load_user)
user = User(*load_user.values())
print(user)