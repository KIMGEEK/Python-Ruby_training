a=input("첫 번째 사람의 이름을 입력하세요\n")
b=input("두 번째 사람의 이름을 입력하세요\n")

aAge=input("첫 번째 사람의 나이를 입력하세요\n")
bAge=input("두 번째 사람의 나이를 입력하세요\n")

if  bAge>aAge:
    age = "연상"
elif bAge==aAge:
    age = "동갑"
else:
    age = "연하"

print(a+"는 "+b+"보다 "+age+"입니다.")
