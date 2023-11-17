class TriangleChecker:
    
    def __init__(self, line1,line2,line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        
    def is_trangle(self):
        if not isinstance(self.line1, int) or not isinstance(self.line2, int) or not isinstance(self.line3, int):
            return print ('Нужно вводить только числа!')
        elif self.line1 < 0 or self.line2 < 0 or self.line3 < 0:
            return print('С отрицательными числами ничего не выйдет!')
        elif self.line1 + self.line2 <= self.line3 or self.line1 + self.line3 <= self.line2 or self.line3 + self.line2 <= self.line1:
            return print('Жаль, но из этого треугольник не сделать.')
        else:
            return print('Ура, можно построить треугольник!')
            
tc = TriangleChecker(1,2,3)
print(tc.is_trangle())