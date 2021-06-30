input_id = input("아이디를 입력하세요\n")
# name_Kimgeek = "Kimgeek"
# name_Milkyway = "Milkyway"
members = ['Kimgeek', 'Milkyway', 'Eunha']
for member in members:
    if member == input_id:
        print('Hello, '+member)
        import sys
        sys.exit()
print("Who are you?")
