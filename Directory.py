start=1
import time
class register:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def adding(self):
        namesfile=open("names.txt","r")
        runned_times=0
        correct_leter=0
        name_exist=False
        for times in namesfile:
            runned_times=0
            for i in times:
                the_length=len(self.name)
                if(self.name[runned_times]==i):
                    correct_leter+=1
                if(correct_leter==the_length):
                    name_exist=True
                    correct_leter=0
                runned_times+=1
                if(runned_times==the_length):
                    break
        namesfile.close()
        if(name_exist==False):
            namesfile=open("names.txt","a")
            namesfile.write(f"{self.name}: {self.age}"+"\n")
            print("successfully added!")
            namesfile.close()
        elif(name_exist==True):
            print("A user with the same name already exist!")
    def classlist(self):
        namesfile=open("names.txt","r")
        text=namesfile.readlines()
        for lines in text:
            print(lines)
    def find_person(self):
        finding=input("Please enter the person you are looking for: ")
        namesfile=open("names.txt",'r')
        runned_times=0
        matched_name=[]
        correct_leter=0
        for times in namesfile:
            runned_times=0
            for i in times:
                the_length=len(finding)
                if(finding[runned_times]==i):
                    correct_leter+=1
                if(correct_leter==the_length):
                    matched_name.append(times)
                    correct_leter=0
                runned_times+=1
                if(runned_times==the_length):
                    break
        print(matched_name)
        time.sleep(2)
    # def change_age(self):
    #     finding=input("Please enter the person you are looking for: ")
    #     namesfile=open('names.txt','r')

def add_student():
    name=input("Please enter your name: ")
    age=int(input("Please enter your age: "))
    student1=register(name,age)
    student1.adding()

def display():
    student=register(True,True)
    student.classlist()
def find_student():
    student=register(True,True)
    student.find_person()
def quest():
    print("Please enter the instructions:\n\tAdd a student;\n\tChange the age of the student\n\tCheck the class list\n\tFind a student")
    quest=input("")
    if(quest=='Add a student'):
        add_student()
    elif(quest=="Check the class list"):
        display()
    elif(quest=="Find a student"):
        find_student()
while (start==1):
    quest()