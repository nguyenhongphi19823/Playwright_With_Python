
# Code từ Python nền tảng cho Tester\bai-03-list-and-dictionary\users_data.py
# Giải thích dòng 1: Bắt đầu một list chứa nhiều bản ghi user.
users = [
    # Giải thích dòng 2: User thứ nhất là dictionary gồm email và role.
    {"email": "a@test.com", "role": "admin"},
    # Giải thích dòng 3: User thứ hai có cùng cấu trúc để dễ xử lý.
    {"email": "b@test.com", "role": "tester"},
# Giải thích dòng 4: Kết thúc list users.
]
#-------------------------------------------------

# Giải thích dòng 1: Duyệt lần lượt từng dictionary trong list users.
for user in users:
    # Giải thích dòng 2: Kiểm tra role hiện tại có phải admin không.
    if user["role"] == "admin":
        # Giải thích dòng 3: Chỉ in email khi điều kiện đúng.
        print(user["email"])
        # Giải thích dòng 4: Dừng vòng lặp sau khi tìm thấy kết quả cần thiết.
        break


# ------------------------------------
# Bài tập thực hành
# Đổi logic để in tất cả user có role tester.
for user in users:
    if user["role"] == "tester":
        print(user["email"])




