puts("사용자 계정을 찾아보세요.")
User_id = gets.chomp()

User_Sinu = "Sinu"
User_Kimgeek = "Kimgeek"

if User_id == User_Sinu
  puts("제대로 찾은 거 같네요. Sinu님은 현재 존재하는 사용자입니다!")
elsif User_id == User_Kimgeek
  puts("제대로 찾은 거 같네요. Kimgeek님은 현재 존재하는 사용자입니다!")
else
  puts("아쉽게도 존재하지 않는 사용자네요. 아니라면, 정확히 입력하셨는지 확인해주시겠어요?")
end
