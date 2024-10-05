#answer
#no.1
radius=int(input("Enter the radius:"))
volume=(4/3*3.14*radius**2)
print(f"The volume of radius {radius} is: {volume:.2f}")

#NO2
base=int(input("Enter the value of base:" ))
height=int(input("Enter the value of height:"))
area_of_a_triangle=(1/2*base*height)
print(f"The area of atriangle is:{area_of_a_triangle} ")

#NO.3

def calculateGrades():
   
   mark = int(input("Enter mark scored:\t"))


   if mark >= 90 and mark <100:
      print("Grade A ")
   
   elif  mark >= 80 and mark <= 89:
      print("Grade B")
    
   elif mark >= 70 and mark <= 79:
      print("Grade C")
       
   elif mark >= 60 and mark <= 69:
      print("Grade D")
        
   elif mark  <=50 and mark <= 59:
      print("Grade E")
       
   else:
      print("Fail")
      
calculateGrades()      
       
         

  
#no.4
def saccoTransaction():
   
   accountBalance = 0
   run = 1
   
   while run == 1:
      
      print("\nWelcome to, WITU sacco. ")
      
      #menu
      print('1.Deposit Money')
      print('2. Withdraw Money')
      print('3. check balance')
      
      studentChoice= int(input("Enter your selection(1,2,or 3):"))
      
      if studentChoice == 1:
         
         print(".....Processing a deposit transaction....")
         depositAmount=int(input("Enter amount to be deposited:"))
         if depositAmount< 1000:
            print("\nMinimum deposit is 1000")
            
         else:
            accountBalance += depositAmount
            
            print(f"Dear student, you have deposited {depositAmount:,} and your new balance is {accountBalance:,}")
            
              
         
      elif studentChoice == 2:
         
         print(".....Processing a withdraw transaction....")
         withdrawAmount=int(input("Enter amount to be withdrawn:"))
         
         if accountBalance == 0:
            print("Your balance is 0")
         elif withdrawAmount < 500:
            
            print("Minimum withdraw amount is 500")
         elif withdrawAmount > accountBalance:
            print(f"Withdraw failed, insufficient funds")
            
         else:
            accountBalance -= withdrawAmount
            print(f"Dear student, you have withdrawn {withdrawAmount}, and your account balance is {accountBalance}")         
         
         
      elif studentChoice ==3:
         print(f"Your account balance is {accountBalance:,}")
         
         
         
      else:
         print("You have entered a wrong choice!! please select 1,2, or 3\n")
         
         
         
         
         run = int(input("Enter 1 to continue or any number to exit:"))
         
      if run!=1:
         print("Thanks for using our sacco")
         break 
saccoTransaction()        
