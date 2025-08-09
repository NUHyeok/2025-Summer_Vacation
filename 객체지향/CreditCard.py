class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        # 여기에 코드를 작성하세요
        self.name = name
        self._passward = password
        self._payment_limit = payment_limit
    
    @property 
    def password(self):
        return "비밀번호는 볼 수 없습니다"
    
    @password.setter
    def password(self, password):
        self._passward = password
    
    @property
    def payment_limit(self):
        return self._payment_limit
    
    @payment_limit.setter
    def payment_limit(self, payment_limit):
        if payment_limit >= CreditCard.MAX_PAYMENT_LIMIT or payment_limit < 0:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
        else:
            self._payment_limit = payment_limit
    
    

card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)