import requests
from twilio.rest import Client
import os


# my credentials for https://openweathermap.org/
api_key = os.environ['WEATHER_API']

# my satellite position https://www.latlong.net/
my_lat = 51.507351
my_long = -0.127758

# openweather API endpoint
OMV_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# my credentials for Twilio account https://www.twilio.com/docs
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
twilio_phone = os.environ['TWILIO_PHONE']

# my personal phone number
my_phone = os.environ['MY_PHONE']

# structuring parameters data
my_data = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# making API request to get weather data for my location
response = requests.get(url=OMV_Endpoint, params=my_data)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
code_list = []
will_rain = False

# checking weather codes
for i in range(0, 12):
    code = weather_data["hourly"][i]["weather"][0]["id"]
    if code < 700:
        will_rain = True
        print(code)

# sending SMS if the code number is below 700 which means it will rain
if will_rain:
    #print("Bring Umbrella!!!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring umbrella!!! It will rain in next 12 hours",
        from_=twilio_phone,
        to=my_phone
    )
    print(message.status)




