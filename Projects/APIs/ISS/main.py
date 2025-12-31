#Mini project to let you know when the ISS is over you
import requests
import time
from datetime import datetime
import smtplib

# Your location
MY_LAT = 12.971599
MY_LONG = -0.127758

# Email credentials (App Password)
MY_EMAIL = "Your email address"
MY_PWD = "Your app password"   # App password


def iss_overhead():
    """Return True if ISS is within ±5 degrees of your location."""
    response = requests.get(
        "http://api.open-notify.org/iss-now.json",
        timeout=5
    )
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )


def is_night():
    """Return True if it is currently night at your location."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters,
        timeout=5
    )
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour

    return current_hour >= sunset or current_hour <= sunrise


while True:
    try:
        if iss_overhead():
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PWD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
                )

            print("Email sent! Cooling down...")
            time.sleep(600)  # 10-minute cooldown to avoid spam

        else:
            print("ISS not overhead.")

    except Exception as error:
        print("Error occurred:", error)
