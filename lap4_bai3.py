def generate_permutations(n):
    # Khởi tạo hoán vị đầu tiên [1, 2, ..., n]
    a = list(range(1, n + 1))
    result = [a[:]]  # Lưu hoán vị đầu tiên

    while True:
        # Bước 1: Tìm i lớn nhất sao cho a[i] < a[i+1]
        i = n - 2
        while i >= 0 and a[i] > a[i + 1]:
            i -= 1
        if i < 0:
            break  # Đạt cấu hình cuối cùng, dừng thuật toán

        # Bước 2: Tìm k lớn nhất sao cho a[k] > a[i]
        k = n - 1
        while a[k] < a[i]:
            k -= 1

        # Bước 3: Đổi chỗ a[i] và a[k]
        a[i], a[k] = a[k], a[i]

        # Bước 4: Lật ngược đoạn từ a[i+1] đến a[n-1]
        a[i + 1:] = reversed(a[i + 1:])

        # Lưu hoán vị mới
        result.append(a[:])

    return result


# Test case mẫu
n = 3
perms = generate_permutations(n)
print(f"Tổng số hoán vị sinh được: {len(perms)}")
for p in perms:
    print(p)
