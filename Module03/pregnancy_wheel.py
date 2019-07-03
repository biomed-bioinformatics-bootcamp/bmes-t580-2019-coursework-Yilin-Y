import datetime

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('     Due date  APP     ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# asking when is the patient's lmp
print("When were the patient's last normal menstrual period (LMP)? ")
date_str = input('Format: [DD/MM/YYYY]')  # 02/18/2019
parts = date_str.split('/') #split the input date into a list

# if the length of the parts is not 3， means the date is incorrect (either missing year/month/day)
# then, ask to rewrite the date
if len(parts) != 3:
    print('Incorrect date, please rewrite the last normal menstrual period (LMP)')
    date_str = input('Format: [DD/MM/YYYY]')  # '02/18/2019'

parts = date_str.split('/') #split the input date into a list
# In python, the order number start from 0
# extract the year, month and day from
year = int(parts[2]) # split into year
month = int(parts[1]) # split into month
day = int(parts[0]) # split into day

lmp = datetime.date(year, month, day) # recombine the lmp year, month and day and rename it as lmp
# print the last normal menstrual period (lmp)
print(lmp)


orig_today_date = datetime.date.today() # find what date is it today
#It is not need to replace the year into lmp's year because the year do impact the calculation of the gestational age
# today_date = datetime.date(lmp.year, orig_today_date.month, orig_today_date.day)
dt = orig_today_date - lmp # obtain the gestational ages
gestational_week = dt.days/7 # obtain the gestational ages in week

print ('Your estimated gestational age is {} days'.format(dt.days))
print('Your estimated gestational age in week is {}'.format(gestational_week))


lmp_day = lmp

gest_length = datetime.timedelta(days=281) # the average delivery days
gest_std = datetime.timedelta(days=13) # the standard deviation
exp_due_date = lmp_day + gest_length # obtain the expected delivery date
min_due_date = exp_due_date - gest_std # get the earliest delivery date
max_due_date = exp_due_date + gest_std # get the latest delivery date

# print the results which for the expected delivery date,the earliest delivery date and the latest delivery date
print('Your expected delivery date is ', exp_due_date.strftime('%a %b %d %Y'))
print('But it may be as early as', min_due_date.strftime('%m/%d/%Y'))
print('Or as late as', max_due_date.strftime('%m/%d/%Y'))
