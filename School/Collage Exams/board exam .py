# students information data

students = {

17741: {"name" : "Owais Naeem", "Age" : 17 , "Gender" : "Male" , "Marks" : [56, 53, 72, 67, 54, 74, 54] },
17742: {"name" : "Khizer Nadeem", "Age" : 17 , "Gender" : "Male", "Marks" : [32, 53, 65, 64, 59, 74, 21] },
17743: {"name" : "Ibrahim Paneer", "Age" : 17 , "Gender" : "Male", "Marks" : [23, 53, 52, 61, 59, 72, 21] },
17744: {"name" : "Yameen Yousuf", "Age" : 16 , "Gender" : "Male", "Marks" : [23, 52, 52, 66, 59, 74, 21] },
17745: {"name" : "Mateen Uzair", "Age" : 17 , "Gender" : "Male", "Marks" : [23, 53, 52, 64, 59, 74, 21] },
17746: {"name" : "Sinan Hamza", "Age" : 18 , "Gender" : "Male", "Marks" : [23, 53, 41, 74, 59, 75, 21] },
17747: {"name" : "Mustafa Qureshi", "Age" : 16 , "Gender" : "Male", "Marks" : [22, 53, 52, 64, 59, 74, 21] },
17748: {"name" : "Mahmood Javed", "Age" : 15 , "Gender" : "Male" , "Marks" : [23, 53, 52, 64, 59, 74, 21] } ,
17749: {"name" : "Sanaullah Ali", "Age" : 17 , "Gender" : "Male" , "Marks" : [23, 53, 58, 64, 75, 74, 21] } ,
17750: {"name" : "Abdullah Kareem", "Age" : 16 , "Gender" : "Male" , "Marks" : [75,75, 53, 52, 64, 59, 74, ] }

}

# subjects data

Subjects = ["English", "Maths", "Physics", "Chemistry", "Computer", "P_S_T", "Sindhi"]

# Total marks

Total_marks = 550

# user enter a roll number


Roll_number = int(input("Enter Your Roll No. : "))

# student information and check the role number is roll number in students

if Roll_number in students:
    student = students[Roll_number]

# obtained marks

    Obtained_marks = sum(student["Marks"])
    print("\nINFORMATION : " , Roll_number)

# information of student

    print(f"\nName : {student['name']}")
    print(f"Age : {student['Age']}")
    print(f"Gender : {student['Gender']}")
    print("\n" + "The Result : \n")
    for subjects,marks in zip(Subjects , student["Marks"]):
     print(f"{subjects} : {marks}")


    print(f"\nObtained marks :" , Obtained_marks , "/" , Total_marks)
    Percentage = (Obtained_marks/550 * 100)
    print(f"Percentage : " , Percentage)

else:
    print("Roll number not found.")

    








   

     
    