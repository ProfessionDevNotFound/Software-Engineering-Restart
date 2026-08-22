#This python file is to understand and write different kind of functions which can be used in python

#for this file iam going to create apython file which is going to run a python function name firstand from there i will call all the possible function which is out there to do different tasks
#Decleration
from datetime import date
def PrintmyName():
    print(GetName())
def GetName():
    return input("Hi there What is your name ")
def GetDOB():
    return input("What is your Date of birth YYYY/MM/DD ")
def GetOccupation():
    return input("What is your occupation ")

def GetHomeTown():
    return input("What is your HomeTown ")
def currentLoc():
    return input("What is your Curent Location ")

def First():
    option=0
    while (option !=4):
          option=int(input(
            "Hi there! This is the Function Game, where you can call different "
            "functions to perform different tasks.\n"
            "Each function has a different purpose. Pick a number to get started:\n\n"
            "1. Print your name \n"
            "2. Get all your bio details \n"
            "3. Calculate the square of a number \n"
            "4. Exit \n"
            ))
          if(option==1):
            PrintmyName()
          elif(option==2):
            Forum()
          elif(option==3):
            Square()
      
         
def GetCurentLoc(town):
        currentLocation=currentLoc()
        if (not currentLocation):
             return town
        else:
             return currentLocation

def CalculateAge(DOB):
    year,month,dateT=(DOB.split('/'))
    today=date.today()

    Age=(today.year)-int(year)
    if (today.month,today.day)<(int(month),int(dateT)):
        Age-=1
    return Age

def Forum():

    name = GetName()
    Date = GetDOB()
    Occupation = GetOccupation()
    age = CalculateAge(Date)
    Home = GetHomeTown()
    CurrentLoc = GetCurentLoc(Home)

    print("Name:", name)
    print("Date of Birth:", Date)
    print("Occupation:", Occupation)
    print("Age:", age)
    print("Home Town:", Home)
    print("Current Location:", CurrentLoc)

def Square():
    print(int(input("Enter the number you want to find the square"))**2)




if __name__=="__main__":
    First()