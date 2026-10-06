def generate_subsets_backtracking(features):
    result = []

    def backtrack(start_index, current_path):
        # Bước 2: Thêm bản sao của current_path vào kết quả
        result.append(current_path[:])

        # Bước 3: Duyệt qua các lựa chọn
        for i in range(start_index, len(features)):
            # Bước 4: Chọn phần tử
            current_path.append(features[i])
            # Bước 5: Gọi đệ quy cho bước tiếp theo
            backtrack(i + 1, current_path)
            # Bước 6: Quay lui (bỏ lựa chọn)
            current_path.pop()

    # Bước 1: Gọi hàm đệ quy ban đầu
    backtrack(0, [])
    return result


# Ví dụ sử dụng
features = ['Age', 'Income', 'Score']
print(generate_subsets_backtracking(features))
