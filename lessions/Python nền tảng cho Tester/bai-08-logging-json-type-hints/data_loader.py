# Giải thích dòng 1: Nạp thư viện chuẩn để đọc và ghi JSON.
import json
# Giải thích dòng 2: Nạp hệ thống logging của Python.
import logging
# Giải thích dòng 3: Tạo logger mang tên module hiện tại.
logger = logging.getLogger(__name__)
# Giải thích dòng 4: Khai báo input là đường dẫn và output là list dictionary.
def load_users(path: str) -> list[dict]:
    # Giải thích dòng 5: Mở file an toàn và tự đóng sau khi đọc.
    with open(path, encoding="utf-8") as file:
        # Giải thích dòng 6: Chuyển nội dung JSON thành object Python.
        data = json.load(file)

    # Kiểm tra dữ liệu JSON phải là list.
    if not isinstance(data, list):
        raise ValueError("Dữ liệu JSON phải là list.")

    return data

# ------------------------------------
# Bài tập thực hành
# Thêm validation: nếu JSON không phải list thì raise ValueError.
