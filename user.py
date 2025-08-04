class User:
    
    def say_hello(some_user): # 행동을 정의하는 함수를 인스턴스 메소드 or 메소드
        print(f"안녕하세요! 저는 {some_user.name}입니다!")

user1 = User()
user2 = User() # 클래스로 부터 파생된 객체를 인스턴스라고 부름.



user1.name = "강영훈"
user1.email = "younghoon@codeit.xyz"
user1.passward = "12345"

user2.name = "이윤수"
user2.email = "yoonsoo@codeit.xyz"
user2.passward = "abcde"

User.say_hello(user1)
User.say_hello(user2)

user1.say_hello()



