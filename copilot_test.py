def calculate(a, b):
    print(f"{a} + {b} = {a + b}")  # 덧셈
    print(f"{a} - {b} = {a - b}")  # 뺄셈
    print(f"{a} × {b} = {a * b}")  # 곱셈
    if b != 0:
        print(f"{a} ÷ {b} = {a / b}")  # 나눗셈
    else:
        print("0으로 나눌 수 없습니다.")

def main():
    # 두 수 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    
    # 계산 결과 출력
    calculate(num1, num2)

if __name__ == "__main__":
    main()