# ��� -> �ߺ��Ǵ� �ڵ��� ������ �ذ�
class Employee:
    """���� Ŭ����"""
    company_name = "�ڵ��� ����"
    raise_percentage = 1.03
    
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
    
    def raise_pay(self):
        """�ñ��� �λ��Ѵ�."""
        self *= self.raise_percentage
    
class Cashier(Employee): # �θ� Ŭ���� : Employee / �ڽ� Ŭ���� : Cashier
    """���� ������ Ŭ����"""
    burger_price = 4000
    
    def __init__(self, name, wage, number_sold = 0):
        # Employee.__init__(self, name, wage)
        super.__init__(name, wage) # self�� �Ѱ��� �ʿ䰡 ����.
        self.number_sold = number_sold
    
    
    def take_order(self, money_received):
        """�ֹ��� ���� �ް� �Ž������� �����Ѵ�."""
        if Cashier.burger_price > money_received:
            print("���� ������� �ʽ��ϴ�.")
            return money_received
        else:
            self.number_sold += 1
            return money_received - Cashier.burger_price
    
    def __str__(self):
        return Cashier.company_name + "���� ���� :" + self.name

class DeliveryMan:
    """��޿� Ŭ����"""
    company_name = "�ڵ��� ����"
    raise_percentage = 1.03
    
    def __init__(self, name, wage, on_standby):
        self.name = name
        self.wage = wage
        self.on_standby = on_standby
    
    def raise_pay(self):
        """�ñ��� �λ��Ѵ�."""
        self.wage *= DeliveryMan.raise_percentage
    
    def deliver_to(self, address):
        """��޿��� ������̸� �־��� �ּҷ� ����� ������ �ƴϸ� ���� �޽����� �߰��Ѵ�."""
        if self.on_standby:
            print(address + "�� ��� �����ϴ�!")
            self.on_standby = False
        else:
            print("�̹� ����Ϸ� �������ϴ�!")
    
    def return_from_delivery(self):
        """��޿��� ���͸� ó���Ѵ�."""
        self.on_standby = True
    
    def __str__(self):
        return DeliveryMan.company_name + "��޿� : " + self.name