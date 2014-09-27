class Person:
    def ___inti___(self, **kwargs):
        self.vars = kwargs

    def get_vars(self, k):
        return self.vars.get(k, none)
    def set_vars(self, k, v):
            self.vars[k] = v

    def func1(self):
            print("My name is " + self.vars[k])

class Student(Person):


"""

...tuple
...lists
...sets
... these are typical collections
(1,2,3) -- tuple
(1) -- int
(1,) -- tuple
[1,2,3] -- list (can "mutate")
[1,2,3}
    
