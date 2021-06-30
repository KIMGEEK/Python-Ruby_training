puts("아이디를 입력하세요.")
ID_user = gets.chomp()
puts("패스워드를 입력하세요.")
PWD_user = gets.chomp()

ID_Sinu = "Sinu"
PWD_Sinu = "I came, I saw, I conquered."

ID_Kimgeek = "Kimgeek"
PWD_Kimgeek = "Remarkable"

if ID_user == User_Sinu and PWD_user == PWD_Sinu
  puts("다시 오셔서 기뻐요! "+ID_user+"님.")
elsif ID_user == User_Kimgeek and PWD_user == PWD_Kimgeek
  puts("다시 오셔서 기뻐요! "+ID_user+"님.")
else
  puts("아이디 또는 패스워드가 정확하지 않습니다!")
end
