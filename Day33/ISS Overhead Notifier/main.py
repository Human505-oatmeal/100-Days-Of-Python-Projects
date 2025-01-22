import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "REDACTED"  # Add your email here
MY_PASSWORD = "REDACTED"  # Add your password here
MY_LONG = 0  # Add your longitude here
MY_LAT = 0  # Add your latitude here


def is_iss_overhead():
    """returns True or False if the ISS is overhead."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 >= iss_longitude >= MY_LONG+5:
        return True


def is_night():
    """returns True if it's night."""
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now >= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.google.com")  # add your smtp server here
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up!\n\nThe ISS is above you in the sky."
        )
    else:
        pass
