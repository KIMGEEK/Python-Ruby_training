puts("아이디를 생성하세요.")
ID_user = gets.chomp()

ID_Sinu = "Sinu"
ID_Kimgeek = "Kimgeek"

if not (ID_user == ID_Sinu or ID_user == ID_Kimgeek)
  puts("축하합니다! 사용하실 수 있는 계정입니다!")
else
  puts("안타깝군요! 사용자가 존재하는 계정입니다!")
end
