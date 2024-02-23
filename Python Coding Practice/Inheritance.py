# 1) Single Inheritance
#parent class
class Father:
    def quality(self):
        print('Inside father class')
        print('father has intelligence and deep thinking power.')
        print('\n')
# child class
class Son(Father):
    def aim(self):
        print('Inside Son class')
        print('Son wants to be Doctor')
        print('\n')

#creating object for son class
s=Son()
s.quality()
s.aim()

# 2) Multi level Inheritance
class Grandfather:
    def gf_quality(self):
        print('Inside Grand father class')
        print('Grand father is honest person')
class Father(Grandfather):
    def quality(self):
        print('Inside father class')
        print('father has intelligence and deep thinking power.')
class Son(Father):
    def aim(self):
        print('Inside Son class')
        print('Son wants to be Doctor')

# creating object for Son class
s1=Son()
s1.gf_quality()
s1.quality()
s1.aim()
#Multiple Inheritance
#parent class-1
print('Multiple Inheritance')
class Father:
    def father_quality(self):
        print('Inside father class')
        print('father has intelligence and deep thinking power.')
    def father_nature(self):
        print('Inside father class')
        print('Father is very strict')
# parent class-2
class Mother:
    def mother_quality(self):
        print('Inside mother class')
        print('mother cooks good.')
    def mother_nature(self):
        print('Inside mother class')
        print('Mother is kind hearted')
#child class
class Son(Father,Mother):
    def son_quality(self):
        print('Inside Son class')
        print('Son is very naughty')

s2=Son()
s2.father_quality()
s2.father_nature()
s2.mother_quality()
s2.mother_nature()
s2.son_quality()

# Heirarchical Inheritance
#parent class
print('Herirarchical Inheritance')
class Father:
    def father_quality(self):
        print('Inside father class')
        print('father has intelligence and deep thinking power.')
#child class-1
class Son1(Father):
    def son1_quality(self):
        print('Inside Son 1 class')
        print('Son is very naughty')

son1=Son1()
son1.father_quality()
son1.son1_quality()

#child class-2
class Son2(Father):
    def son2_quality(self):
        print('Inside Son 2 class')
        print('Son is very disciplined')

son2=Son2()
son2.father_quality()
son2.son2_quality()

# Hybrid Inheritance
print('Hybrid Inheritance')
class Grandfather:
    def gf_quality(self):
        print('inside Grandfather class')
        print('Grandfather was a honest person')

    def gf_nature(self):
        print('inside Grandfather class')
        print('Grandfather is a soft mind person')

    def gf_hobby(self):
        print('inside Grandfather class')
        print('Grandfather s hobby is farming')

class Father(Grandfather):
    def father_quality(self):
        print('inside Father class')
        print('Father has intelligence and deep thinking power!')

    def father_nature(self):
        print('inside Father class')
        print('Father is strict in principle')

class Son1(Father):
    def son1_quality(self):
        print('inside Son1 class')
        print('son1 has deep knowledge about Islamic law')

k1=Son1()
k1.gf_hobby()
k1.father_nature()
k1.son1_quality()

class Son2(Father):
    def son2_quality(self):
        print('inside Son2 class')
        print('son2 want to become software engineer')

k2=Son2()
k2.gf_quality()
k2.father_quality()
k2.son2_quality()
