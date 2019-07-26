import requests # import the requests modules so that python can send a standard for making HTTP requests
import os # import the os modules to offer system to use operate system dependent functionality

import shutil # shutil modules offer more operations on files, such as delete or copy


def get_cats(folder, name): # create the function to go to the website and saving the images
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random' # the url of the website
    data = get_data_from_url(url) # obtain the data from the url
    save_image(folder, name, data) # save the images into folder that just created


def get_data_from_url(url): # create the get_data function to obtain the data from the website url
    response = requests.get(url, stream=True)
    return response.raw

def save_image(folder, name, data): # create the save_image function to save the data(images) into the file/ folder
    file_name = os.path.join(folder, name + '.jpg') # new named the images and added .jpg as the type of the images
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)