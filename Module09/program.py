import csv # this modules allow users to read and write in the csv file
import os # import the os modules

try: # import  the statistics modules to provides functions for calculating mathematical statistics of numeric data.
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase # improt the data_types module that I created before


def main(): # write down all main functions
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header(): # print the header
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('***************                   ')
    print('     Real Estate Analysis APP     ')
    print('               *******************')
    print('----------------------------------')


def get_data_file(): # the get_data_file is used to get find the target file base on the file name
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename): # this function used to load and read the data from file
    with open(filename, 'r', encoding='utf-8') as fin:
        # with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):
    #  this function used to find the data line by line to obtain the target price and room base on the requirements

    #  list[Purchase]):

    # if the data was sorted by price:
    # data.sort(key = get_price)

    # most expensive house?
    # high_purchase = data[-1]

    # least expensive house?
    # low_purchase = data[0]

    # average price of the house?
    # average price of 2 bedroom's house?

    # note that the line before: data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # for the lambda, it is a small inline method

    # obtain the highest price of the home, and print it based on the format that is shown below
    high_purchase = data[-1]
    print("The most expensive (highest price) house is ${:,} with {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))
    # obtain the lowest price of the home, and print it based on the format that is shown below
    low_purchase = data[0]
    print("The least expensive (lowest price) house is ${:,} with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    # prices = list()  # []
    # for pur in data:
    #     prices.append(pur.price)

    prices = [
        p.price  # projection or items
        for p in data  # the set to process
    ]
    # obtain the average price of the home, and print it based on the format that is shown below
    ave_price = statistics.mean(prices)    # use statistics method to obtain the average price
    print("The average price of home is ${:,}".format(int(ave_price)))


    # average price of 2 bedroom houses
    # prices = []
    # baths = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    # for two_bedroom's price:

    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        # obtian the numbers of 2-bedrooms house
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test / condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    # use the statistics method to obtain the average price of the 2-bedroom house
    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes)) # obatin the average baths
    ave_sqft = statistics.mean((p.sq__ft for p in homes)) # obtain the average square feet for the home
    # print all information based on the format that shown below
    print("Average price of 2-bedroom home is ${:,}, baths={}, sq ft={:,}"
          .format(int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()