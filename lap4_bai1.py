def generate_binary_strings(n):
    """
    Sinh toàn bộ 2^n chuỗi nhị phân độ dài n theo thứ tự từ điển.
    Không dùng đệ quy.
    """
    a = [0] * n  # Bước 1: Khởi tạo cấu hình đầu tiên
    result = []

    while True:  # Bước 2: Vòng lặp vô hạn
        result.append("".join(map(str, a)))  # Bước 3: Lưu cấu hình hiện tại

        # Bước 4: Tìm phần tử đầu tiên từ phải sang trái có giá trị 0
        i = n - 1
        while i >= 0 and a[i] == 1:
            i -= 1

        # Bước 5: Nếu không tìm thấy (toàn bit 1) → thoát
        if i < 0:
            break

        # Bước 6: Đổi a[i] = 1 và gán các phần tử phía sau bằng 0
        a[i] = 1
        for j in range(i + 1, n):
            a[j] = 0

    return result
