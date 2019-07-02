import datetime # import the datetime into the python

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('     BIRTHDAY APP     ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('Ready?')
print('GO')

# asking the user's name
user_name = input('What is your name? ')
print ('Nice to meet you {}'. format(user_name))


# ask the user to obtain the birthday (include year, month, day)
year= int(input('In which year were you born [YYYY]:')) # asking year
month = int(input('In which month were you born [MM]: ') )# asking month
day = int(input('In which day were you born [DD]: ') )# asking day

birthday =  datetime.date(year,month,day) # get the date of user's birthday

# compute the days between birthday date
orig_today_date = datetime.date.today() # find what date is it today
# get the date (month and day) of today's date and use the birthday year to replace today's year for calculation
today_date = datetime.date(birthday.year,orig_today_date.month,orig_today_date.day)
# obtain the difference between the today's date and birthday date
diff_date=  birthday - today_date

# find how much days ago is the user's birthday
if diff_date.days < 0:
    print('{} You had your birthday in {} days ago'. format(user_name,abs(diff_date.days)))

elif diff_date.days> 0:
# find how much days left to the birthday
    print ('{} Get ready to your birthday? Your birthday is in {} days!!!'.format(user_name,diff_date.days))

# find if today is the user's birthday
else:
    print('{} Happy Birthday!!!'. format(user_name))
