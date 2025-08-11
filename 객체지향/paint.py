from shapes import Rectangle, Circle, EquilateralTriangle, Shape

class Paint:
    """그림판 클래스"""
    def __init__(self):
        self.shapes = []
    
    def add(self, shape: Shape):
        """
        파라미터 shape 도형을 추가한다.
        
        파라미터 shape은 반드시 추상 클래스 Shape의 인스턴스이여야한다.
        """
        self.shapes.append(shape)
    
    def draw(self, index):
        """파라미터 index에 해당하는 도형을 그린다."""
        if 0 <= index and index < len(self.shapes):
            self.shapes[index].draw()
        else:
            print("인덱스를 확인해주세요.")
    
    def draw_all(self):
        """모든 도형을 그린다."""
        if not self.shapes:
            print("그림판에 도형이 없습니다.")
        
        for shape in self.shapes:
            shape.draw()
    
    def __str__(self):
        """그림판 안 도형들의 정보를 리턴한다."""
        result = "\n그림판에 있는 도형들 : \n"
        
        for i in range(len(self.shapes)):
            result += f"    {i+1}. {self.shapes[i]}\n"
        return result
    
rectangle1 = Rectangle(7,8)
circle = Circle(9)
triangle = EquilateralTriangle(7)

paint = Paint()

paint.add(rectangle1)
paint.add(circle)
paint.add(triangle)

paint.draw(0)
paint.draw(2)
paint.draw(3)

paint.draw_all()