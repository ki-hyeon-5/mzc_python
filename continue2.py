
# 사용자로부터 '-'이 포함한 계좌 번호를 입력 받아 '-'을 삭제한 문자열 출력

account_number = input('계좌번호를 입력하세요 : ')

temp = ' '
for ch in account_number:
    if ch == '-':
        continue
    temp += ch
    
print(temp)

# 테스트용 으로 내용을 변경
