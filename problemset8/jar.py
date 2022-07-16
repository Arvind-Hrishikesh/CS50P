class Jar:
    content=0
    def __init__(self,capacity=12):
        if int(capacity)<0:
            raise ValueError
        else:
            self.capacity=capacity

    def __str__(self):
        return "🍪"*self.content

    def deposit(self,n):
        if (self.content+n)<=self.capacity:
            self.content+=n
        else:
            raise ValueError

    def withdraw(self,n):
        if n<=self.content:
            self.content-=n
        else:
            raise ValueError

    def capacity(self):
        return self.capacity

    def size(self):
        return self.content

