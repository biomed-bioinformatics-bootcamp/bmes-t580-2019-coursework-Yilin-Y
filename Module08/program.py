import os # import the os modules to offer system to use operate system dependent functionality
import collections # import the collections modules to offer a specialized container data types

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        #if the folder cannot found, print this sentence below
        print("Sorry, the location can't be searched. Please try again.")
        return

    text = get_search_text_from_user()
    if not text:
        # if the text is empty or there is no text, print the sentence below
        print("Sorry, the text cannot be found. Please try again.")
        return

    matches = search_folders(folder, text) # find the match folder
    match_count = 0
    for m in matches:
        match_count += 1
        # print(m)
        # print('file: ' + m.file)
        # print('line: {}'.format(m.line))
        # print('match: ' + m.text.strip())
        # print()


    print('--------- MATCH -------------')  # give a header as the notice for the match folder
    print("Found {:,} matches.".format(match_count))


def print_header(): #print header
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('*****************                    ')
    print('           FILE SEARCH APP           ')
    print('                   ******************')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def get_folder_from_user(): #create the function for search the folder
    # ask user to select a folder, print the pathway of the folder
    folder = input('Which folder do you want to search?')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user(): # create the function for obtaining the text
    # ask user to choose a text for searching
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_folders(folder, text): #create the function for search the folder that match the require from user
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # matches = search_folders(full_item, text)
            # all_matches.extend(matches)

            # for m in matches:
            #     yield m
            # yield from matches
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m

    # return all_matches


def search_file(filename, search_text): #create the function for search the file and the text
    # matches = []
    # finding the file based on the filename and read it line by line to find the text
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0: # change all text into lower case for searching
                m = SearchResult(line=line_num, file=filename, text=line)
                # matches.append(m)
                yield m

        # return matches


if __name__ == '__main__':
    main()
