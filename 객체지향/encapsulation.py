# 캡슐화 -> 특정 정보에 대한 외부 접근을 차단하는 것. / 객체의 행동과 속성을 하나로 묶는 것.

class Citizen:
    """주민 클래스"""
    drinking_age = 19
    
    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민번호"""
        self.name = name
        self._age = age
        self._resident_id = resident_id
    
    def authenticate(self, resident_id):
        """본인 인증 메소드"""
        return self._resident_id == resident_id
    
    def can_drink(self):
        return self._age >= Citizen.drinking_age
    
    @property
    def age(self):
        print("나이에 접근합니다.")
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다.")
        else:
            print('나이를 설정합니다.')
            self._age = value

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self._age) + "살 입니다!"
    

citizen = Citizen("최규식", 25, "12345678")

citizen.age = 10
print(citizen.age)
        