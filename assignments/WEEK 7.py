class Person:
    def _init_(self, our_first_name  ,our_last_name ,our_age):
        self.first_name =our_first_name
        self.last_name = our_last_name
        self.age =our_age
        print(our_first_name,our_last_name,our_age)
person1=Person ("John","Doe",30)

# print(person1._init_('John','Doe',30))
# print(person1.first_name)
# print(person1.last_name)
# print(person1.age)
