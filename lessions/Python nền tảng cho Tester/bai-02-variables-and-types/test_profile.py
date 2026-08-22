# Giải thích dòng 1: Lưu username và ghi rõ biến có kiểu chuỗi.
username: str = "tester01"
# Giải thích dòng 2: Lưu số lần thử lại dưới dạng số nguyên.
retry_count: int = 2
# Giải thích dòng 3: Lưu trạng thái bật/tắt bằng boolean.
headless: bool = True
# Giải thích dòng 4: Cho biết token có thể là chuỗi hoặc chưa có giá trị.
token: str | None = None