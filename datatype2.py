# datatype2.py

# 이름과 나이, 키(소수점 1자리), 결혼여부(기혼 : True, 미혼 : False)

name = '곽기현'

age = 25

height = 178.5

marry = False

print("곽기현 25 178.? False")

# 변수를 통한 포맷팅
print(f"이름은 {name} 나이는 {age} 키는 {height} 결혼여부 {marry}") # 이거 추천 보기 편함

print("이름은 {} 나이는  {} 키는 {} 결혼 여부 {}".format(name,age,height,marry))

print("이름은", name, "나이", age, "키는", height,"결혼여부", marry)