# 3-masala.  Social Media User.
# Klass: User
# Properties (xususiyatlar):
# 	username: str - foydalanuvchining nomi
# 	friends: list[str] â€” foydalanuvchining do'stlar ro'yxati
# Methods:
# 	__init__(self, username: str) -> None
# 	Yangi foydalanuvchi yaratadi va uning do'stlar ro'yxatini bo'sh ro'yxatga o'rnatadi.
# 	add_friend(self, friend: str) -> bool
# 	Do'stlar ro'yxatiga yangi foydalanuvchini qo'shadi.
# 	Agar foydalanuvchi allaqachon ro'yxatda bo'lsa, hech narsa qo'shilmaydi va False qaytaradi.
# 	Aks holda do'st qo'shiladi va True qaytaradi.

# 	remove_friend(self, friend: str) -> bool
# 	Do'stlar ro'yxatidan foydalanuvchini o'chiradi.
# 	Agar do'st mavjud bo'lsa - o'chiriladi va True qaytaradi.
# 	Agar mavjud bo'lmasa - hech narsa qilinmaydi va False qaytaradi.

# 	list_friends(self) -> list[str]
# 	Do'stlar ro'yxatini qaytaradi (bo'sh bo'lsa bo'sh ro'yxat qaytaradi).

# 	is_friend(self, friend: str) -> bool
# 	Berilgan friend nomli foydalanuvchi do'stlar ro'yxatida bormi - shuni tekshiradi va True yoki False qaytaradi.

# 	mutual_friends(self, other_user: 'User') -> list[str]
# 	self va other_user o'rtasidagi umumiy do'stlar ro'yxatini topadi va ro'yxat ko'rinishida qaytaradi.
# Namuna:
# user1 = User("Ali")
# user2 = User("Vali")

# print(user1.add_friend("Sami"))    # True
# print(user1.add_friend("Vali"))    # True
# print(user1.add_friend("Sami"))    # False (allaqachon mavjud)

# print(user2.add_friend("Ali"))     # True
# print(user2.add_friend("Sami"))    # True

# print(user1.list_friends())   # ['Sami', 'Vali']
# print(user2.list_friends())    # ['Ali', 'Sami']

# print(user1.is_friend("Vali"))     # True
# print(user1.is_friend("Botir"))    # False

# print(user1.mutual_friends(user2)) # ['Sami']

# print(user1.remove_friend("Vali")) # True
# print(user1.remove_friend("Botir"))# False
# print(user1.list_friends())        # ['Sami']
import os
os.system("cls")

class User:
    def __init__(self, username):
        self.username = username
        self.friends = []

    def add_friend(self, friend):
        if friend in self.friends:
            return False
        else:
            self.friends.append(friend)
            return True

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            return True
        else:
            return False

    def list_friends(self):
        return self.friends

    def is_friend(self, friend):
        return friend in self.friends

    def mutual_friends(self, other_user):
        common_friends = []
        for friend in self.friends:
            if friend in other_user.friends:
                common_friends.append(friend)
                
        return common_friends

user1 = User("Ali")
user2 = User("Vali")

print(user1.add_friend("Sami"))
print(user1.add_friend("Vali"))
print(user2.add_friend("Ali"))
print(user2.add_friend("Sami"))

print("User1 do'stlari:", user1.list_friends())
print("User2 do'stlari:", user2.list_friends())
print("Umumiy do'stlar:", user1.mutual_friends(user2))
# tayyor