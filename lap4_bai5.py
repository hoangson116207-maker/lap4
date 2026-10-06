
# Bài 5: Pipeline Tối ưu Siêu tham số (Hyperparameter Grid Search)
# & Phân tích Dụng độ theo Nguyên lý Dirichlet

# --- Phần 1: Lập trình Grid Search bằng Quay lui ---
def custom_grid_search(param_grid):
    keys = list(param_grid.keys())
    results = []

    def backtrack(index, current_config):
        if index == len(keys):
            results.append(current_config.copy())
            return

        key = keys[index]
        for value in param_grid[key]:
            current_config[key] = value
            backtrack(index + 1, current_config)
            del current_config[key]  # Quay lui

    backtrack(0, {})
    return results


# --- Phần 2: Phân tích Nguyên lý Nhân ---
from functools import reduce
import operator

def count_configurations(param_grid):
    return reduce(operator.mul, [len(v) for v in param_grid.values()], 1)


# --- Phần 3: Đánh giá Dụng độ theo Nguyên lý Dirichlet ---
import math

def dirichlet_analysis(total_models, num_servers):
    max_per_server = math.ceil(total_models / num_servers)
    return max_per_server


# --- Test toàn bộ ---
param_grid = {
    'learning_rate': [0.001, 0.01, 0.1],
    'batch_size': [16, 32, 64],
    'optimizer': ['Adam', 'SGD']
}

configs = custom_grid_search(param_grid)
print("=== KẾT QUẢ GRID SEARCH ===")
print(f"Tổng số cấu hình sinh được: {len(configs)}")
for c in configs[:5]:
    print(c)

print("\n=== PHÂN TÍCH NGUYÊN LÝ NHÂN ===")
print(f"Tổng số cấu hình (theo công thức): {count_configurations(param_grid)}")

print("\n=== PHÂN TÍCH DIRICHLET ===")
N = 105  # số mô hình
k = 10   # số cụm máy chủ
max_load = dirichlet_analysis(N, k)
print(f"Với {N} mô hình và {k} cụm máy chủ → mỗi cụm tối đa chứa {max_load} mô hình.")
