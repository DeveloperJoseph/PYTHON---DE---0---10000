#The class Robot
class Robot():
    list_name = []
    list_age = []
    list_emotion = []
    count_people_happy = 0
    count_people_sad = 0
    count_people_adult = 0
    count_people_noadult = 0

    def __init__(self,name,emotion):
        self.name = name
        self.emotion = emotion
        Robot.list_name.append(name)
        Robot.list_emotion.append(emotion)

    def say_hi(self,gender):
        print("[*] Hello {}, How are you?".format(self.name))

        if gender == "male":
            print("[*] My name's Elphia, I'm at your service.")
        if gender == "woman":
            print("[*] My name's Arturk, I'm at your service.")
        
        if gender!= "male" and gender!="woman":
            print("[*] My name's SRobotPy, I'm at your service.")

    def say_goodbye(self):
        print("[*] Hey {}, See you soon.".format(self.name))
        print("[*] Goodbye.")
    
    def check_emotion(self):
        import random
        list_happy_emotion = ["well","happy","good"]
        if self.emotion in list_happy_emotion:
            list_answer_happy = ["your emotion is very well.","your emotion is really good.",
            "your emotion is too good."]
            answer = random.choice(list_answer_happy)
            print("[*] {} {}.".format(self.name,answer))
            Robot.count_people_happy+=1
        
        list_sad_emotion = ["sad","wrong","bored"]
        if self.emotion in list_sad_emotion:
            list_answer_sad = ["your emotion is very wrong.","you need to relax.",
            "you need to breathe."]
            answer = random.choice(list_answer_sad)
            print("[*] {} {}.".format(self.name,answer))
            Robot.count_people_sad+=1

        elif self.emotion not in list_happy_emotion:
            print("[*] Emotion no exist.")
    
    def check_age(self,age):
        if age > 0 and age <= 17:
            print("[*] {} aren't of legal age. ({} years)".format(self.name,age))
            Robot.list_age.append(age)
            Robot.count_people_noadult+=1
        if age >=18 and age <= 120:
            print("[*] {} are of legal age. ({} years)".format(self.name,age))
            Robot.list_age.append(age)
            Robot.count_people_adult+=1
        
        if age <=0 and age >120:
            print("[*] {} your age isn't valid. Try again.".format(self.name))

    def questions(self):
        print("|||||||||| QUESTIONS |||||||||| (")
        print("[%] You use drugs?")
        q_drugs = str(input("[-]Answer (y/n): "))
        print("[%] Suffer from depression?")
        q_depression = str(input("[-]Answer (y/n): "))

        if q_drugs.__eq__('y') and q_depression.__eq__('y'):
            print("[*] {} your previous test is wrong.".format(self.name))
        if q_drugs.__eq__('n') and q_depression.__eq__('n'):
            print("[*] {} your previous test is good.".format(self.name))
        if q_drugs.__eq__('y') and q_depression.__eq__('n'):
            print("[*] {} you need a treatment.".format(self.name))
        if q_drugs.__eq__('n') and q_depression.__eq__('y'):
            print("[*] {} you need to listen classical musics.".format(self.name))

    def say_hour(self):
        from datetime import datetime
        today = datetime.now()
        print("[*] {} the hour is {}.".format(self.name,today))
    
    @classmethod
    def count_people_happy_or_sad(new_self):
        print("[+] Number of happy people {}.".format(new_self.count_people_happy))
        print("[+] Number of sad people {}.".format(new_self.count_people_sad))

    @classmethod
    def count_people_adult_or_noadult(new_self):
        print("[+] Number of adult people {}.".format(new_self.count_people_adult))
        print("[+] Number of not adult people {}.".format(new_self.count_people_noadult))

    @classmethod
    def list_names(new_self):
        print("[*] Names in list: {}".format(Robot.list_name))
    
    @classmethod
    def list_emotions(new_self):
        print("[*] Emotions in list: {}".format(Robot.list_emotion))

#The class Person            
class Person():
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print("[*] Hello {}, How are you?".format(self.name))
        print("[*] My name's Joseph Whoami, I'm at your service.")
    def say_goodbye(self):
        print("[*] Hey {}, See you soon.".format(self.name))
        print("[*] Goodbye.")

#The class Animals    
class Animals():
    cont_animals = 0
    list_name = []

    def __init__(self,name):
        self.name = name    
        Animals.cont_animals+=1
        Animals.list_name.append(name)

    def died(self):
        print("[*] {} is being destroyed.".format(self.name))
        Animals.cont_animals-=1
        if Animals.cont_animals == 0:
            print("[*] {} was the last one".format(self.name))
        else:
            print("[*] There are still {} live animals.".format(Animals.cont_animals))
            Animals.list_name.remove(self.name)
            
    def say_hi(self):
        print("[*] Waooo,wauuu!!")#dog

    @classmethod
    def how_many(new_self):
        print("[*] We have {} animal/s {}.".format(new_self.cont_animals,new_self.list_name))

r = Robot("Mr. Joseph","good")
r.say_hi('male')
r.say_hour()
r.check_emotion()
r.check_age(17)
#r.questions()

print("\n")
r2 = Robot("Sra. Maria","sad")
r2.say_hi('woman')
r2.say_hour()
r2.check_emotion()
r2.check_age(20)

print("\n")
r3 = Robot("Mr. Smith","wrong")
r3.say_hi('male')
r3.say_hour()
r3.check_emotion()
r3.check_age(35)

print("\n====== Results =======")
r2.count_people_adult_or_noadult()
r2.count_people_happy_or_sad()
r2.list_names()
r2.list_emotions()
r.say_goodbye()
r2.say_goodbye()
r3.say_goodbye()


