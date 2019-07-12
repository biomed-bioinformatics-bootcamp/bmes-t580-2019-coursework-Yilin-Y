import requests
import bs4
import collections

# import the modules

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')
# use the collections modules for the weather report

def main():

    print_the_header()

    code = input('What zip code do you want the weather for (19104)? ')
    # asking the input of the zip code to obtain the target location

    html = get_html_from_web(code)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

    # display for the forecast


def print_the_header(): # print out the header
    print('---------------------------------')
    print('     WEATHER APP     ')
    print('---------------------------------')



def get_html_from_web(zipcode): # load the web link to get the weather
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html): # get the information from the website and add those information into the report

    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text() # obtain the conditions from the soup
    temperature = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()# obtain the temperature from the soup
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc) # geting the loaction
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temperature = cleanup_text(temperature)
    scale = cleanup_text(scale)

    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temperature, scale=scale, loc=loc)
    return report


def find_city_and_state_from_location(loc: str): # using the function to get the city and state from the location
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()