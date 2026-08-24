# Giải thích dòng 1: Khai báo class đại diện cho bộ quản lý user.
class UserManager:
    # Giải thích dòng 2: Constructor nhận dữ liệu khi object được tạo.
    def __init__(self, users):
        # Giải thích dòng 3: Lưu users vào chính object hiện tại qua self.
        self.users = users
    # Giải thích dòng 4: Tạo instance method trả về số nguyên.
    def count_users(self) -> int:
        # Giải thích dòng 5: Đếm số phần tử trong dữ liệu của object.
        return len(self.users)

# ------------------------------------
# Bài tập thực hành
# Thêm method add_user và kiểm tra count_users tăng lên.

class UserManger:
    def __init__(self, users):
        self.users = users

    def count_users(self) -> int:
        return len(self.users)

    def add_user(self, user) ->None:
        self.users.append(user)

users = [
    {"email": "a@test.com", "role": "admin"},
    {"email": "b@test.com", "role": "tester"}
]
manager = UserManager(users)
print(manager.count_users()) # 2
manager.add_user({"email": "c@test.com", "role": "tester"})
print(manager.count_users()) # 3