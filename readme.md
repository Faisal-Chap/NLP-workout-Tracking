# ISS Overhead Notifier

## Overview
This Python script tracks the International Space Station (ISS) and sends an email notification when it is passing overhead. The script checks the ISS's position and whether it is night or day at the user's location, ensuring better visibility when looking at the sky.

## Features
- Retrieves the current ISS position using the Open Notify API.
- Fetches sunrise and sunset times using the Sunrise-Sunset API.
- Checks if the ISS is within a specified range of your location.
- Determines whether it is night or day for better visibility.
- Sends an email notification when the ISS is overhead.

## Prerequisites
- Python 3.x installed
- An SMTP email account (e.g., Gmail)
- Required Python packages:
  - `requests`
  - `smtplib`
  - `datetime`
  - `time`

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies:
   ```sh
   pip install requests
   ```
3. Edit the script to update:
   - Your latitude and longitude.
   - Your email credentials.
   - The recipient email address.

## Configuration
Modify the following constants in the script:
```python
MY_LAT = 31.996754  # Your latitude
MY_LONG = 71.178692  # Your longitude
my_mail = "your_email@gmail.com"  # Your email
my_pass = "your_email_password"  # Your email password
target_address = "target_email@gmail.com"  # Recipient email
smtp_server = "smtp.gmail.com"  # SMTP server
```

## How It Works
1. The script continuously checks the ISS's position every 60 seconds.
2. If the ISS is within a 5-degree range of your location, the script checks if it is nighttime.
3. If both conditions are met, an email notification is sent with a message indicating the ISS is overhead.
4. The script terminates after sending the email.

## Running the Script
Run the script using:
```sh
python iss_notifier.py
```

## Example Output
```
Not in range, currently at 45.123, -122.456
Not in range, currently at 46.789, -123.654
Mail sent: ISS is overhead!
```

## Notes
- Ensure you enable "Less secure apps" access if using Gmail, or generate an app password.
- The script stops running after sending an email. Restart it for continuous monitoring.
- This script uses free APIs that may have rate limits.

## License
This project is open-source and free to use.

## Author
Faisal Zia


