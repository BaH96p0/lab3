class Soda:
    def __init__(self, additive):
        self.additive = additive
    
    def show_my_drink(self):
        return print(f'Газировка и {self.additive}')
    
s = Soda('сахар')
print(s.show_my_drink())