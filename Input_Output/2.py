User_id = input("사용자 계정을 찾아보세요.\n")

User_Sinu = "Sinu"
User_Kimgeek = "Kimgeek"

if User_id == User_Sinu :
    print("제대로 찾은 거 같네요. Sinu님은 현재 존재하는 사용자입니다!")
elif User_id == User_Kimgeek :
    print("제대로 찾은 거 같네요. Kimgeek님은 현재 존재하는 사용자입니다!")
else :
    print("아쉽게도 존재하지 않는 사용자네요. 아니라면, 정확히 입력하셨는지 확인해주시겠어요?")
    pass
