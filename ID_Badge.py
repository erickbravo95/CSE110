print ("\nPlease enter the following information: \n")

first_name = input("First name: ")
last_name = input("Last name: ")
email_add = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")
hair_color = input("Hair color: ")
month_start = input("Starting Month: ")
eyes_color = input("Eyes color: ")
adv_trin = input("Advance trining?(Yes/No) ")

print ("\nThe ID Card is: ")
print ("----------------------------------------")
print (f"{last_name.upper()}, {first_name.capitalize()} \n{job_title.title()} \nID: {id_number} \n \n{email_add.lower()} \n{phone_number}")
print ()
print (f"{'Hair: ' + hair_color.capitalize():<25} Eyes: {eyes_color.capitalize()}")
print (f"{'Month: ' + month_start.capitalize():<25} Trining: {adv_trin.capitalize()}")
print ("----------------------------------------")


