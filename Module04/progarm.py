import journal
# from Journal import load, save
# from Journal import *
# import the journal module that we built before



def main(): # the main function
    print_header()
    run_event_loop()


def print_header(): # header
    print('------------------------')
    print('     JOURNAL APP     ')
    print('------------------------')




def run_event_loop():
    print('What do you want to do with your journal?')
# asking the user what they wanna do for the journal, adding new stuff or listing all they did before or finish and exit
    command = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()

    while command != 'x'and command:
        # using the first letter of the options as the command
        command = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        command = command.lower().strip() # changing the uppercase of the Command as the lowercase for decrease the error

        if command == 'l':
            list_entries(journal_data)
        elif command == 'a':
            add_entry(journal_data)
        elif command != 'x' and command:
            # if the command is not as L for listing A for adding X for exist
            print("Sorry, we don't understand. Please retype it '{}'.".format(command))
# when the user finish editing his/her journal, print Done and See You Next Time
    print ('Done!')
    print ('See You Next Time ~')
    journal.save(journal_name,journal_data) #saving the journal data and journal name


def list_entries(data):# as the command from the input is l (list), show all the all entries that user added before
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('o [{}] {}'.format(idx + 1, entry))

# as the user input before is A (adding), ask use again for adding new entry
def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    # data.append(text)
    journal.add_entry(text, data) # adding the new entry into the file, and save them into the list

# print ("__file__ "+ __file__)
# print ("__name__ "+ __name__)

if __name__ == '__main__':
    main()

