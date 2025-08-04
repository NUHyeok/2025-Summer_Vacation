class User:
    
    def say_hello(self): # 행동을 정의하는 함수를 인스턴스 메소드 or 메소드
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
    def login(self, email, passward):
        if self.email == email and self.passward == passward:
            print("로그인 성공, 환영합니다.")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

user1 = User()
user2 = User() # 클래스로 부터 파생된 객체를 인스턴스라고 부름.



user1.name = "강영훈"
user1.email = "younghoon@codeit.xyz"
user1.passward = "12345"

user1.login("younghoon@codeit.xyz", "12345")




