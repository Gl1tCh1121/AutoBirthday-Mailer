import pandas
import smtplib
import random
import datetime as dt

my_email = "babutech1121@gmail.com" 
password = "jkkx cwmp fths afqy"
bd = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()

for i in range(len(bd)):
    if now.month == bd["month"][i] and now.day == bd["day"][i]:
        name = bd["Name"][i]
        email = bd["Email"][i]
        goal = True
    if goal:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
            letter = file.read()
        
        letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, 
                                    to_addrs=email,
                                    msg=f"Subject:Happy Birthday\n\n{letter}"
                                    )
    goal = False

