Amazon Price Tracker

This Python program allows you to track the price of an Amazon item and sends you an email when the price drops below a specified value. 
It scrapes the product's price using BeautifulSoup, compares it with your target price, and notifies you via email.

Features:

- Tracks prices of Amazon items
- Sends an email alert when the price drops
- Scheduled to run daily at 9:00 AM (optional via task scheduler, time and scheulde module)

Add Your Information:

- In the Python file, input your email, recipient email, and password.
- Specify the target price to trigger the email notification.
- Run the Program: Enter the URL of the Amazon product you'd like to track when prompted.

Note:
- The email, password and recipient email fields are not included in this version.
- The program can be automated using Python’s schedule module and Task Scheduler (Windows) or cron (macOS/Linux).
- Certain Amazon prices ARE NOT displayed in exact locations, therefore the name and class_ would need to change. 
