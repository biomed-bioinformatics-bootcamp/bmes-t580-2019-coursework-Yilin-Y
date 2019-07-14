import csv # csv is used to import and export the database
import os

def main():
# call put all functions inorder to obtain the users' criteria to fill out the criteria of the patients
    print_the_header()
    filename = get_filename()
    age_min, age_max = get_age_range()
    small_inf, big_inf = get_inf_length()
    pat_sex = get_pet_sex()
    pat_coin = get_pat_coin()
    pat_ther = get_pat_ther()

    out_filename = filename + '.valid'
    num_pats = 0

    # Open file and start reader
    with open(filename) as handle:
        reader = csv.DictReader(handle)

        # open file base on the out_filename and allow to write the file
        with open(out_filename, mode='w') as out_handle:
            fields = ['PAT_NUM', 'SEX', 'AGE', 'INFECTION_LENGTH', 'ON_THERAPY', 'COINFECTION']
            writer = csv.DictWriter(out_handle, fields)
            writer.writeheader()

# Since the homework requirement ask to record all patients that match the criteria and save them into a new file, ---
#--I use the for and several if loop to find that the patients from inclusion criteria (more easier to output the list)
            # filter out the if the patients is match with the criteria and save them in a new file
            for row in reader:
                # identify and split each item's meaning
                pat_age = int(row['AGE'])
                pat_sex_col = str(row['SEX'])
                pat_therapy = str(row['ON_THERAPY'])
                pat_coinfection = str(row['COINFECTION'])
                inf_length = int(row['INFECTION_LENGTH'])

                # build up the filter for separating out the long logic for clarity
                # age and INFECTION_LENGTH are numbers which also contain within a range
                match_age = (pat_age > age_min) and (pat_age < age_max)
                match_inf_length = (inf_length > small_inf) and (inf_length < big_inf)

                # if the criteria is match, print them out SAVE in a split file
                match_sex = True
                if pat_sex != '0':
                    match_sex = (pat_sex_col == pat_sex)

                match_coin = True
                if pat_coin!= '0':
                    match_coin = (pat_coinfection == pat_coin)


                match_therapy = True
                if pat_ther !='0':
                    match_therapy = (pat_therapy == pat_ther)


                if match_age and match_sex and match_coin and match_therapy and match_inf_length:
                    # count the total number of patients from inclusion criteria
                    num_pats += 1

                    # write the patients that pass filter into the new file
                    writer.writerow(row)

# print the criteria
    print('Based on the following criteria:')
    print(' - Age: [%i, %i]' % (age_min, age_max))
    print(' - Infection Length: [%i, %i]' % (small_inf, big_inf))
    print(' - Gender %s', pat_sex)
    print(' - Coinfection %s', pat_coin)
    print(' - Therapy %s', pat_ther)
    print('There are %i patients from the inclusion criteria' % num_pats)


def print_the_header(): # print the header
    print('---------------------------------')
    print('     Process Demographics     ')
    print('---------------------------------')


# obtain the filename from user so that system can extract those patients' information
def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Please try again.')
            filename = None

    return filename

# asking the user if the patient's age is relative to the study, if yes asking the user to input patients' age for filtering
def get_age_range():
    while True:
        age_input = input("If the patient's age range relative to the study: [Y]es or [N]o: ")
        age_input = age_input.lower().strip()  # changing the uppercase of the input as the lowercase for decrease the error

        # if the patient's age is relative to the study
        if age_input == "y":
            age_min, age_max = None, None

            while age_min is None:
                age_inp = input('What is the youngest age for the study? ')
                try:
                    age_min = int(age_inp)

                # if the user not input a number, asked he/she to re-type the age
                except ValueError:
                    print(age_inp + ' is not a number. Please try again')
                    continue

                if age_min < 18:
                    print('Ethics boards require special permission for youth cohort. Please pick an older age')
                    age_min = None

            while age_max is None:
                age_inp = input('What is the oldest age for the study? ')
                try:
                    age_max = int(age_inp)

                # if the user not input a number, asked he/she to re-type the age
                except ValueError:
                    print(age_inp + ' is not a number. Please try again')
                    continue
            return age_min, age_max
        # if the patient's age is not relative to the study, then break.
        elif age_input == "n":
            age_min = 0 # just randomly guess the min age
            age_max = 100 # just randomly guess the max age
            return age_min, age_max
        else:
            print('Incorrect input. Please try again')
            continue


# asking the user if the patient's infection length is relative to the study, if yes asking the user to input patient's infection length (range) for filtering
def get_inf_length():
    while True:
        inf_input = input("If the patient's infection length relative to the study: [Y]es or [N]o: ")
        inf_input = inf_input.lower().strip()  # changing the uppercase of the input as the lowercase for decrease the error

        # if the patient's infection length is relative to the study
        if inf_input == "y":
            small_inf, big_inf = None, None

            while small_inf is None:
                small_inf_inp = input('The smallest or minimum infection length for the patient is: ')
                try:
                    small_inf = int(small_inf_inp)

                # if the user not input a number, asked he/she to re-type the infection length
                except ValueError:
                    print(small_inf_inp + ' is not a number. Please try again.')
                    continue

            while big_inf is None:
                big_inf_inp = input('The biggest or maximum infection length for the patient is')
                try:
                    big_inf = int(big_inf_inp)

                # if the user not input a number, asked he/she to re-type the infection length
                except ValueError:
                    print(big_inf_inp + ' is not a number. Please try again.')
                    continue

            return small_inf,big_inf

        # if the patient's infection length is not relative to the study, then break.
        elif inf_input == "n":
            small_inf = 0 # just randomly guess the infection length
            big_inf = 100 # just randomly guess the infection length
            return small_inf, big_inf
        else:
            print('Incorrect input. Please try again')
            continue

# asking the user if the patient's gender is relative to the study, if yes asking the user to input patients' gender for filtering
def get_pet_sex():
    while True:
        gender_input = input("If the patient's gender relative to the study: [Y]es or [N]o: ")
        gender_input = gender_input.lower().strip()  # changing the uppercase of the input as the lowercase for decrease the error

        # if the patient's gender is relative to the study
        if gender_input == "y":
            pat_sex = None

            while pat_sex is None:
                gender= input('What is the gender for the study? [M]ale or [F]emale:')
                gender = gender.lower().strip()  # changing the uppercase of the gender as the lowercase for decrease the error

                try:
                    gender=str(gender)
                # if the user not input a correct word, asked he / she to re-input the gender
                except ValueError:
                    print(gender + ' cannot be found in the system. Please try again')
                    continue

                if gender=='m':
                    pat_sex='Male'
                if gender=='f':
                    pat_sex='Female'

            return pat_sex
        # if the patient's gender is not relative to the study, then break.
        elif gender_input == "n":
            break
        else:
            print('Incorrect input. Please try again')
            continue

# asking the user if the patient has coinfection will relative to the study, if yes asking the user to input patients' coinfection  for filtering
def get_pat_coin():
    while True:
        coin_input = input("If the patient has coinfection will relative to the study: [Y]es or [N]o: ")
        coin_input = coin_input.lower().strip()  # changing the uppercase of the input as the lowercase for decrease the error

        # if the patient has coinfection is relative to the study
        if coin_input == "y":
            pat_coin = None

            while pat_coin is None:
                coinfection = input('Does the patient has coinfection in this study: [Y]es or [N]o :')
                coinfection = coinfection.lower().strip()  # changing the uppercase of the gender as the lowercase for decrease the error

                try:
                    coinfection = str(coinfection)
                # if the user input a incorrect choice, ask he / she to re-input the coinfection
                except ValueError:
                    print(coinfection + ' cannot identified. Please try again')
                    continue

                if coinfection == 'n':
                    pat_coin = 'No'
                if coinfection == 'y':
                    pat_coin = 'Yes'

            return pat_coin
        # if the patient has coinfection is not relative to the study, then break.
        elif coin_input == "n":
            break
        else:
            print('Incorrect input. Please try again')
            continue

# asking the user if the patient on therapy that relative to the study, if yes asking the user to input if the patient is on therapy for filtering
def get_pat_ther():
    while True:
        ther_input = input("If the patient on therapy will relative to the study: [Y]es or [N]o: ")
        ther_input = ther_input.lower().strip()  # changing the uppercase of the input as the lowercase for decrease the error

        # if the patient on therapy is relative to the study
        if ther_input == "y":
            pat_ther = None

            while pat_ther is None:
                therapy= input('Does the patient has the therapy in this study: [Y]es or [N]o: ')
                therapy = therapy.lower().strip()  # changing the uppercase of the gender as the lowercase for decrease the error

                try:
                    therapy=str(therapy)
                # if the user input a incorrect choice, ask he / she to re-input
                except ValueError:
                    print(therapy+' is not one of the choices. Please type in a credible answer')
                    continue

                if therapy=='n':
                    pat_ther='No'
                if therapy=='y':
                    pat_ther='Yes'
            return pat_ther
        # if the patient on therapy is not relative to the study, then break.
        elif ther_input == "n":
            break
        else:
            print('Incorrect input. Please try again')
            continue


if __name__ == '__main__':
    main()