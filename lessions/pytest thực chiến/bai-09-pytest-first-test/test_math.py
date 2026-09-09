# Giải thích dòng 1: Khai báo test function theo prefix test_.
def test_addition():
    # Giải thích dòng 2: Thực hiện hành động và lưu kết quả thực tế.
    actual = 2 + 3
    # Giải thích dòng 3: Khai báo kết quả mong đợi rõ ràng.
    expected = 5
    # Giải thích dòng 4: Cho test pass khi actual bằng expected, ngược lại fail.
    assert actual == expected
# ------------------------------------
# Bài tập thực hành
# Tạo thêm test_subtraction và cố ý cho fail một lần để đọc output.

def test_subtraction():
    actual = 5 - 3
    expected = 3  # Cố ý sai: kết quả đúng là 2.
    assert actual == expected
