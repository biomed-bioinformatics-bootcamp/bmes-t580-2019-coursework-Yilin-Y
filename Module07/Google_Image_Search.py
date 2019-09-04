import csv
import google_images_download   #importing the library


# Print Header
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('*********************')
print('                      **********************')
print('            Histology_Image_Search          ')
print('*********************')
print('                      **********************')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# set up the initial condition
search_terms = []
result = google_images_download.googleimagesdownload()

# open the csv file that contains at least 10 different body regions with search terms just create
with open('Histology_Image_SearchTerms.csv', 'r') as filename:
    data = csv.reader(filename)
    search_terms = list(data)

search_terms.pop(0)    # Removes the Header

# searching each term base for the key shows below
for i in search_terms:
    key = {'keywords': i[1], 'limit': '10', 'print_urls': True, 'prefix': i[0]}

    data = result.download(key) # save the result data