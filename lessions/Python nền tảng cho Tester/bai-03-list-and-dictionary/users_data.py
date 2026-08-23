# Giải thích dòng 1: Bắt đầu một list chứa nhiều bản ghi user.
users = [
    # Giải thích dòng 2: User thứ nhất là dictionary gồm email và role.
    {"email": "a@test.com", "role": "admin"},
    # Giải thích dòng 3: User thứ hai có cùng cấu trúc để dễ xử lý.
    {"email": "b@test.com", "role": "tester"},
# Giải thích dòng 4: Kết thúc list users.
]
# Giải thích dòng 5: Lấy email của user đầu tiên rồi in ra.
print(users[0]["email"])


# ------------------------------------
# Bài tập thực hành
# Thêm user thứ ba và in role của user đó.

users.append({"email": "c@test.com", "role": "developer"})
print(users[2]["role"])
