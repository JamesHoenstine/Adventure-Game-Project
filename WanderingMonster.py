
import random
 
class WanderingMonster:
    
    
    def __init__(self,x,y,monster_type,color,hp,power, money = 0):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = color
        self.hp = hp
        self.power = power
        self.money = money
        
    def random_spawn(self,occupied,forbidden,grid_w,grid_h):
        x = random.randint(0, grid_w - 1)
        y = random.randint(0, grid_h -1)
        return x, y
        
    def from_dict(data):
         return{
             "x": 0,
             "y": 0,
             "monster_type": data["name"],
             "color": "purple",
             "hp": data["hp"],
             "power": data["power"]
             
             }
     
    def to_dict(self):
        return{
        "x": self.x,
        "y": self.y,
       "monster_type": self.monster_type,
        "color": self.color,
        "hp": self.hp,
        "power": self.power
        }
            
   
    def move(self,occupied,forbidden,grid_w,grid_h):
        self.occupied = occupied
        self.forbidden = forbidden
        self.grid_w = grid_w
        self.grid_h = grid_h


state = {
     "monsters":[
         WanderingMonster(x=1, y=1, monster_type="Witch", color="purple", hp=10, power = 5 ,money=10),
         WanderingMonster(x=2, y=1, monster_type="Bat", color="red", hp=10, power = 2 ,money= 4),
         WanderingMonster(x=4, y=1, monster_type="Ghost", color="grey", hp=10, power=3, money=2)
         ]}

monster = WanderingMonster.from_dict({"name": "Witch", "hp": 10,"power": 5})
        
