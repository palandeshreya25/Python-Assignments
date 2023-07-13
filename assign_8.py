class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c
    
    def display(self):
        print("Values in class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)

class B(A):
    def display(self):
        try:
            print("a:", self.__a)  
        except AttributeError:
            print("Accessing private member 'a' raised an exception.")
        print("b:", self._b)
        print("c:", self.c)

_b=B(10,20,30)
_b.display()