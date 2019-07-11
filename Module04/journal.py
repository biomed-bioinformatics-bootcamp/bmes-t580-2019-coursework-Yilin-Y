"""
This is the journal module.
"""
# built up the own journal module for future used

import os
# import the os module to open yhe file and get tge path of the file and so on

def load(name): # function for load the file and get the path of the file
    """
    This method creates and loads a new journal.
    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """

    # todo: populate from file if it exists.
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data




def save(name, journal_data): # saving the name and the file and allow it to add new things into the file
    # base_dir = '~/myworkingfolder'
    # rel_dir = 'data/temp.txt'
    #
    # full_flie = base_dir + '/' + re_dir

    filename = get_full_pathname(name)

    print ('.....saving to: {}'.format(filename))


    # fout = open(filename,'w')
    with open (filename,'w') as fout:

        for entry in journal_data:
            fout.write(entry + '\n')

    # fout.close()


def get_full_pathname(name): # function to get the path name of the file
    filename = os.path.abspath(os.path.join('./journals/' + name + '.jrl'))
    return filename


def add_entry(text,journal_data): # function to adding new words
    journal_data.append(text)
