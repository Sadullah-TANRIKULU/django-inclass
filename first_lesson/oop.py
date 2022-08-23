
# print("----------------------------------------------------------")

# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
        
# test = [122, 'victor', [1 ,2 ,3], (1, 2, 3), {1, 2, 3}, True, lambda x:x]

# print_types(test)

# print("----------------------------------------------------------")

# class Person:
#     name = "victor"
#     age = 32
    
# Person.job = "developer"

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.job)






# print("----------------------------------------------------------")

# class Person:
#     name = "victor"
#     age = 32
    
# person1 = Person()
# person2 = Person()

# person1.location = "Turkey"

# print(person2.age)

# person2.age = 25

# print(person1.age)
# # bir instance da yapılan değişiklik diğerini etkilemez

# print("----------------------------------------------------------")

# class Person:
#     company = "clarusway"
    
    
#     def test(self):
#         print("test")
        
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_details(self):
#         print(self.name, self.age)
        
        
# person1 = Person()
# person2 = Person()
    
# # person1.test()
# # Person.test()

# person1.set_details("barry", 20)
# person1.get_details()
# print(person1.name)    
    
    


# print("----------------------------------------------------------")

# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     @staticmethod
#     def salute():
#         print("Hi there!")


# person1 = Person()
# person2 = Person()

# # person1.test()
# # Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.
# person1.set_details("victor", 30)
# person1.get_details()

# person1.salute()

# --------------------------SPECIAL METHODS-----------------------

# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age, gender="male"):  # instance create ederken automatic çalışır, set_details fonksiyonu ile kendimiz yazarız
#         self.name = name
#         self.age = age
#         self.gender = gender
        
        
#     def get_details(self):
#         print(self.name, self.age, self.gender)
        
        
#     def __str__(self):
#         return f"{self.name} - {self.age}"
          

# person1 = Person("henry", 18)
# # person1.get_details()


# person2 = Person("kadir", 35)
# # person2.get_details()

# print(person1)
# print(person2)

# # print(dir(Person))


print("----------------------------------------------------------")

#------------ENCAPSULATION-------------------
# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000  # _ değiştirme sıkıntı çıkar demektir
#         self.__id = 3666 # kısmen encapsulation var
        
        
#     def __str__(self):
#         return f"{self.name} - {self.age}"
    
    
#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person("henry", 50)
# person1._id = 4000
# print(person1._id)
# # print(person1.__id) # doğrudan ulaşamayız
# print(person1._Person__id) # __id olunca böyle ulaşabiliriz


#---------------ABSTRACTION--------------------------

# array = [2, 3, 4, 4]
# array.sort()
# print(array)  # nasıl sort ettiğini bilmeme gerek yok işte bu abstraction

# class larda iki ayrı class ın ortak özelliklerini bir arada tutmak için kullanılır

#---INHERITANCE-POLYMORPHISM-MULTIPLE INHERITANCE----

# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
        
#     def __str__(self):
#         return f"{self.name} - {self.age}"
    
    
#     def get_details(self):
#         print(self.name, self.age)
        
        
# class Lang:
#     def __init__(self, langs):
#         self.langs = langs
        
        
#     def display_langs(self):
#         print(self.langs)
        
        
        


# class Employee(Person, Lang):
#     def __init__(self, name, age, path, langs):
#         super().__init__(name, age) # parent tan miras aldık
#         self.path = path # yeni ekledik override işlemi
#         Lang.__init__(self, langs)
        
        
#     def get_details(self):
#         # print(self.name, self.age, self.path)
#         super().get_details()
#         print(self.path)

# emp1 = Employee("vic", 32, "FS", ["python", "js"])
# # print(emp1)
# emp1.get_details()
# emp1.display_langs()

# farklı parametrelerle aynı methodu tekraren yazmak  overloading

# overload ve override polymorphism içindedir

# birden fazla class dan inheritance ile miras alabilirim

# -------------INNER CLASS (DJANGO özelinde)--------------------------

# from django.db import models

# class Article(models.Model):
#     name = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)
    
#     class Meta:
#         ordering = ["name"]

# print(Employee.mro())  # kalıtım zincirini görmek için
# print(help(Employee))












