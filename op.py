class Football:
    def __init__(self, name, favorite_team):
        self.name = name
        self.favorite_team = favorite_team

    def cheer(self):
        return f"{self.name} болеет за {self.favorite_team}!"

class McDonaldsLover(Football):
    def favorite_meal(self):
        return "Я обожаю Биг Мак!"

class Kyrgyzstan(Football):
    def location(self):
        return "Я из Кыргызстана!"

class FanFromKyrgyzstan(McDonaldsLover, Kyrgyzstan):
    def introduce(self):
        return f"{self.cheer()} Я из Кыргызстана и люблю ходить в Макдональдс."


fan = FanFromKyrgyzstan("Атай", "Реал Мадрид")

print(fan.introduce())        
print(fan.favorite_meal())      
print(fan.location())          

