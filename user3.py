class User:
    
    def __init__(self, name, email, passward): # 인스턴스가 생성되는 상황에서 자동으로 호출
        self.name = name
        self.email = email
        self.passward = passward
        
    def say_hello(self): # 행동을 정의하는 함수를 인스턴스 메소드 or 메소드
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
    def login(self, email, passward):
        if self.email == email and self.passward == passward:
            print("로그인 성공, 환영합니다.")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

user1 = User("강영훈", "younghoon@codeit.xyz", "12345")
user2 = User("이윤수", "yoonsoo@codeit.xyz", "abcde") # 클래스로 부터 파생된 객체를 인스턴스라고 부름. 

print(user1.name, user1.email, user1.passward)
print(user2.name, user2.email, user2.passward)



