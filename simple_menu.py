ans=True
listOfNames = [""]
while ans:
    print ("""
    =========================
      STUDENT RECORD EDITOR
    =========================  
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    """)
    ans=input("What would you like to do?: ") 
    if ans=="1":
      name = input ("type name:")
      listOfNames.append(name)
      f=open("StudentList.txt", "a+")
      print("\n Student Added") 
    elif ans=="2":
      print("\n Student Deleted") 
    elif ans=="3":
      name = input ("type name:")
      for n in listOfNames:
        if n == name :
          print("\n Student Record Found")
          break;
      if n != name:
        print("\n Student Record Not Found")
    elif ans=="4":
      print("\n Goodbye") 
      break
    elif ans !="":
      print("\n Not Valid Choice Try again") 
