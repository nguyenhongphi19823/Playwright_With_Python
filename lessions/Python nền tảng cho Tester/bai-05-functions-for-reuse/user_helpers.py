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


# Giải thích dòng 1: Tạo function nhận list users và role cần lọc.
def get_emails_by_role(users, role):
    # Giải thích dòng 2: Tạo list mới chỉ lấy trường email của từng user.
    return [user["email"] for user in users
            # Giải thích dòng 3: Chỉ giữ user có role khớp với input.
            if user["role"] == role]
# Giải thích dòng 4: Gọi function và lưu kết quả để dùng tiếp.
tester_emails = get_emails_by_role(users, "tester")



# ------------------------------------
# Bài tập thực hành
# Viết function count_users_by_role trả về số lượng user.

def count_users_by_role(users, role):
    return len([
        user for user in users
        if user["role"] == role

    ])
tester_count = count_users_by_role(users, "tester")







