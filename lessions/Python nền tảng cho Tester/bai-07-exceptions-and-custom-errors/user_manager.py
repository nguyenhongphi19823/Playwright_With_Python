# Giải thích dòng 1: Tạo loại lỗi riêng kế thừa Exception chuẩn.
class UserNotFoundError(Exception):
    # Giải thích dòng 2: Chưa cần thêm logic riêng cho class lỗi.
    pass
# Giải thích dòng 3: Tạo function tìm user theo email.
def get_user_by_email(users, email):
    # Giải thích dòng 4: Duyệt qua toàn bộ user hiện có.
    for user in users:
        # Giải thích dòng 5: Trả user ngay khi email khớp.
        if user["email"] == email: return user
    # Giải thích dòng 6: Chủ động báo lỗi nếu duyệt xong vẫn không thấy.
    raise UserNotFoundError(email)

# ------------------------------------
# Bài tập thực hành
# Bắt UserNotFoundError và log email đã tìm.

users = [
      {"name": "An", "email": "an@example.com"},
      {"name": "Bình", "email": "binh@example.com"},
  ]

  email_to_find = "tester@example.com"

  try:
      user = get_user_by_email(users, email_to_find)
      print(f"Đã tìm thấy user: {user}")
  except UserNotFoundError:
      print(f"Không tìm thấy user với email: {email_to_find}")

  Nếu muốn log đúng nghĩa bằng module logging:

  import logging

  logging.basicConfig(level=logging.INFO)

  email_to_find = "tester@example.com"

  try:
      user = get_user_by_email(users, email_to_find)
      logging.info("Đã tìm thấy user: %s", user)
  except UserNotFoundError:
      logging.error("Không tìm thấy user với email: %s", email_to_find)
