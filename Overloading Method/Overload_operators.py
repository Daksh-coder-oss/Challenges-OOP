#Write a program to overload the less than (<) and equal to (==) operators. 
# For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively.
#  You can additionally create more objects to try different values.
class Compare:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        if self.x < other.x:
            return "x is less than object y"
        else:
            return "x is not less than y"
    def __eq__(self,other):
        if self.x == other.x:
            return "x is equal to y" 
        else:
            return "x is not equal to y"
obj=Compare(3)
obj1=Compare(4)
print(obj>obj1)
print(obj==obj1)

    
        