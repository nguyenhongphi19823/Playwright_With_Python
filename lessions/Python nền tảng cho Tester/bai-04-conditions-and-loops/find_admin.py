# Giải thích dòng 1: Duyệt lần lượt từng dictionary trong list users.
for user in users:
    # Giải thích dòng 2: Kiểm tra role hiện tại có phải admin không.
    if user["role"] == "admin":
        # Giải thích dòng 3: Chỉ in email khi điều kiện đúng.
        print(user["email"])
        # Giải thích dòng 4: Dừng vòng lặp sau khi tìm thấy kết quả cần thiết.
        break




