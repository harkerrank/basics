from sys import exit
def offier(): 
 print "If you book 5 ticket then you have 30% discount "
 confirm()

def confirm(): 
 print"How many tickets"
 choice =raw_input(">")
 if choice == 'one':
   print" your ticket is booked"
 
 if  choice == 'four':
    offier()
 if choice == 'five':
   print " Thank you"
  
  
  
def adult():
 print " this is adult movie"
 print " give your Identity"
 Age = raw_input("what is your age \n")
 work = raw_input(" where did you work \n")
 if Age == '18':
    confirm() 
 
def start():
 print " welcome to cutc"
 print" we have 3 movies here"
 print " 1. singham \n 2. 3 idiots \n 3. Lazer team "
 print" which one do you like"
 
 choice = raw_input(">")
 if choice == '1':
  confirm()
 elif choice =='2':
  offier()
 elif choice == '3':
  adult()
 else: 
     print " soory , we have only these 3"
	 
	 
start()	 
	 
	 
 