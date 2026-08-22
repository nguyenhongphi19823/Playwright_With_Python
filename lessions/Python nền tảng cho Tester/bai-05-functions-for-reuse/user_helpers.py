# Giải thích dòng 1: Tạo function nhận list users và role cần lọc.
def get_emails_by_role(users, role):
    # Giải thích dòng 2: Tạo list mới chỉ lấy trường email của từng user.
    return [user["email"] for user in users
            # Giải thích dòng 3: Chỉ giữ user có role khớp với input.
            if user["role"] == role]
# Giải thích dòng 4: Gọi function và lưu kết quả để dùng tiếp.
tester_emails = get_emails_by_role(users, "tester")



# Bài tập thực hành

