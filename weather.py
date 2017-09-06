import requests

def convert_temp(kelvin, req_temp):
    if req_temp == 'f':
        return kelvin * 9/5 - 459.67
    elif req_temp =='c':
        return kelvin - 273.15
    else:
        return '{} kelvin'.format(kelvin)


zip_code = input('Enter a zip code to get the weather for that region: ')
temper = input('Would you like to see the temperature in celsius or Fahrenheit? Enter a c or an f: ')

package = {
    'APPID': "cbb2629d415e3c5702a8407c09ea0951",
    'zip': zip_code
}

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

data = r.json()

print('The weather in {} is {}.'.format(data['name'], data['weather'][0]['description']))
print('The temperature is {} {}.'.format(convert_temp(data['main']['temp'], temper), temper))