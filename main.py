##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random
import os

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
# ✓ Done: Updated birthdays.csv with Test entry matching today (12/6)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

# EMAIL CONFIGURATION - Update these with your details
MY_EMAIL = "hafizh.ayatillah@gmail.com"
MY_PASSWORD = "tynvxzmleetzecfl"  # Use app-specific password for Gmail
SMTP_ADDRESS = "smtp.gmail.com"
SMTP_PORT = 587

# Get today's date
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# Read the CSV file
birthdays_df = pd.read_csv("birthdays.csv")

# Create a dictionary with (month, day) as key and person's data as value
birthdays_dict = {}
for index, row in birthdays_df.iterrows():
    birthday_month = row["month"]
    birthday_day = row["day"]
    birthdays_dict[(birthday_month, birthday_day)] = row

# Check if today matches a birthday
if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]
    person_name = birthday_person["name"]
    person_email = birthday_person["email"]
    
    # Pick a random letter template
    letters_dir = "letter_templates"
    letter_files = [f for f in os.listdir(letters_dir) if f.endswith(".txt")]
    random_letter = random.choice(letter_files)
    
    # Read the selected letter
    letter_path = os.path.join(letters_dir, random_letter)
    with open(letter_path, "r") as letter_file:
        letter_content = letter_file.read()
    
    # Replace [NAME] with the person's actual name
    personalized_letter = letter_content.replace("[NAME]", person_name)
    
    # Send the email (uncomment and configure with real email/password)
    try:
        with smtplib.SMTP(SMTP_ADDRESS, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )
        print(f"Birthday email sent to {person_name} ({person_email})!")
    except Exception as e:
        print(f"Error sending email: {e}")
        print(f"Personalized letter for {person_name}:\n{personalized_letter}")
else:
    print("No birthdays today!")



