from abc import ABC, abstractmethod

class Vehicle(ABC):
    # 여기에 코드를 작성하세요
    def __init__(self, speed):
        self._speed = speed
        
    @abstractmethod
    def start(self):
        pass
    
    @property
    @abstractmethod
    def speed(self):
        return self._speed
    
    @speed.setter
    def stop(self):
        self._speed = 0
    
    

print(Vehicle.mro())        
print(dir(Vehicle))