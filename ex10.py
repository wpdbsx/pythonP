class Cat :
    def __init__(self,name,age):  #생성자 
        self.__name= name
        self.__age= age
        print("{0}는 {1} 고양이 입니다".format(self.__name,self.__age))
    def meow(self):     
        print("야옹")
    def __str__(self) : #__str__
        return 'Cat(name='+self.__name+', age=' +str(self.__age) +')'
    def set_age(self,age) :
        if age >0 :
            self.__age = age
    def get_age(self):
        return self.__age       


a=Cat("ma",123)
a.meow()
print(a)