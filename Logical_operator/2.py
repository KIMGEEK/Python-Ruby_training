ID_user = input("사용자 계정을 입력하세요.\n")
PWD_user = input("패스워드를 입력하세요.\n")

ID_Sinu = "sinu"
PWD_Sinu = "1234567"

ID_Kimgeek = "Kimgeek"
PWD_Kimgeek = "4242424242"

if ID_user == ID_Sinu and PWD_user == PWD_Sinu :
    print("다시 오신 걸 환영합니다! Sinu님.")
elif ID_user == ID_Kimgeek and PWD_user == PWD_Kimgeek :
    print("다시 오신 걸 환영합니다! Kimgeek님.")
else :
    print("이런! 사용자 계정 또는 패스워드가 올바르지 않습니다!")
    pass
