class dot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x)+"|"+str(self.y)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __add__(self,other):
        addedx = self.x+other.x
        addedy = self.y+other.y
        return str(addedx)+"|"+str(addedy)
    def __sub__(self,other):
        subx = self.x-other.x
        suby = self.y-other.y
        return str(subx)+"|"+str(suby)
    def __mul__(self,other):
        mulx = self.x*other.x
        muly = self.y*other.y
        return str(mulx)+"|"+str(muly)
    
dot1 = dot(2,5)
dot2 = dot(2,5)
print(dot1)
print(dot1==dot2)
print(dot1+dot2)
print(dot1-dot2)
print(dot1*dot2)