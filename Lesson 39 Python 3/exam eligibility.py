attendance = int(input("Enter the attendance percentage: ")) 

  
if attendance >= 75:
    print("You are eligible to take the exam.")
else:
    med_cert = input("Do you have medical certificates? (yes/no): ")
    if med_cert == "yes":
        print("You are eligible to take the exam.")
    else:
        print("You are not eligible to take the exam.")