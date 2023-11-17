class Nikola:
    def __init__(self,name,age):
        self.name = 'Николай' if name == 'Николай' else f'Я не {name}, а Николай'
        self.age = age
        
    def __str__(self):
        return f'{self.name} {self.age}'
        
      
n = Nikola('Маским',23)
print(n)