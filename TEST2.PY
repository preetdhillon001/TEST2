#delaring dictonary
phoneDirectory={}
i=0#INTRODUCING VARIABLE

print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
while(i!=5):#WHILE LOOP
 print("1.Add a record")
 print("2.Search a record")
 print("3.Update a record")
 print("4.Delete a record")
 print("5.Quit")
 i=int(input("Enter your choice: "))
 if(i==1):#IFELSE CONDTION
   b=input("Enter name: ")
   a=int(input("Enter your 10-digit phone number:"))
   phoneDirectory.update({b:a})#ADDING INFO TO DICTIONARY
   #OUTPUT IF USER CHOOSE 1
   print("Record added \n")
    
 elif(i==2):
   b=input("Enter name to search: ")
   x=0
   for j in phoneDirectory.keys():
    #OUTPUT IF USER CHOOSE 2
     if (j==b):
       print(j,":",phoneDirectory[j])#OUTPUT
       x=1
     else:
       pass
    
   if(x==0):
      print("NOT FOUND \n")

 elif(i==3):
   b=input("Enter name: ")
   a=int(input("Enter new 10-digit phone number:"))
   phoneDirectory.update({b:a})#UPDATING DICTIONARY
   #OUTPUT IF USER CHOOSE 3
   print("Record updated \n") 

 elif(i==4):
   b=input("Enter name:")
  #DELETING ITEM
   phoneDirectory.pop(b)
   #OUTPUT IF USER CHOOSE 4
   print("Record deleted \n") 
 #OUTPUT IF USER CHOOSE 5
print("")   
  


  