def solve_n_queens(n):
    results = []
    cols = set()      # Cột đã có quân hậu
    diag1 = set()     # Đường chéo chính (r - c)
    diag2 = set()     # Đường chéo phụ (r + c)

    def backtrack(row, board):
        # Nếu đã đặt đủ n quân hậu → lưu kết quả
        if row == n:
            results.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Không an toàn, bỏ qua

            # Đặt quân hậu
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # Đệ quy sang hàng tiếp theo
            backtrack(row + 1, board)

            # Quay lui (bỏ lựa chọn)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    # Khởi tạo bàn cờ rỗng
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, empty_board)
    return results


# Test case mẫu
for n in [4, 8]:
    solutions = solve_n_queens(n)
    print(f"Với n = {n}: Tổng số cách xếp là {len(solutions)}")
