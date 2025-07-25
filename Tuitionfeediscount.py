name = input("Enter the student's name: ")
grade = int(input("Enter the grade level (1-12): "))
base_fee = float(input("Enter the base tuition fee: "))
topper = input("Is the student an academic topper? (yes/no): ")

if grade < 1 or grade > 12:
    print("Invalid grade! Grade must be between 1 and 12.")
else:

    discount_percent = 0

    if grade >= 9:
        if topper == "yes":
            discount_percent = 20
        else:
            discount_percent = 10
    elif grade >= 6:
        discount_percent = 5
    else:
        discount_percent = 0


    match grade:
        case 10:
            discount_percent += 3
        case 12:
            discount_percent += 5

   
    discount_amount = base_fee * discount_percent / 100
    final_fee = base_fee - discount_amount

    print("Student Name:", name)
    print("Grade Level:", grade)
    print("Academic Topper:", topper.capitalize())
    print("Base Tuition Fee: ₹", base_fee)
    print("Total Discount: ", discount_percent, "%")
    print("Discount Amount: ₹", round(discount_amount, 2))
    print("Final Fee After Discount: ₹", round(final_fee, 2))