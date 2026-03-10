def tinh_tong(a, b):
    """Hàm tính tổng hai số"""
    return a + b

def tinh_tru(a, b):
    """Hàm tính hiệu hai số"""
    return a - b

# Chạy thử nghiệm
num1 = 15
num2 = 7

print(f"Tổng của {num1} và {num2} là: {tinh_tong(num1, num2)}")
print(f"Hiệu của {num1} và {num2} là: {tinh_tru(num1, num2)}")