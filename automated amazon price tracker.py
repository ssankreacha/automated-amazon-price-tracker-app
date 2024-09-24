import requests
import smtplib
from headers import headers
from bs4 import BeautifulSoup

# TODO-TASK: Create automated Amazon price tracker; sending email when item price is less than/at current price.

"""
Task Checklist:

1. Ask the user to input a URL of the item they want (completed)
2. Extract the price of that item (completed)
3. Establish connection with email client (completed)
4. Utilise conditional statements (if else) for when price is less than or at a certain value (completed)
"""

# live website used: https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1

# Ask user for URL (live website), Retrieve website code in text format and integrated headers
URL = input("Please copy and paste the URL of the item you're searching for: ")
response = requests.get(url=URL, headers=headers)
price_info = response.text

# Parse the HTML content, Retrieve Text and Remove Spaces
soup = BeautifulSoup(price_info, "html.parser")
pounds = soup.find_all(name="span", class_="a-price-whole")[0].get_text(strip=True)
pence = soup.find_all(name="span", class_="a-price-fraction")[0].get_text(strip=True)
current_price = float(f"{pounds}{pence}")
target_price = 100.00

# Send email to user, when price is below target,
# Target price can be used as user's budget,
if current_price < target_price:
    sender_email = " "      # Enter your email
    sender_password = " "   # Find your app password, this depends on your email domain
    recipient_email = " "   # Enter recipient email

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg="Subject:Amazon Price Alert!\n\n"f"Hey, the price has lowered below your budget!"
                                f"Click to purchase{URL}")
        connection.close()
