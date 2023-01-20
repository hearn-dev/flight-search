# Flight Search

Flight Search is a Python automation used to search for affordable flights to specified locations in the next 6 months, and notify the user via SMS if there are any in their specified price range

## Tools

Flight Search uses the [Sheety API](https://sheety.co/) to connect to [Google Sheets](https://www.google.com/sheets/about/) to track specified locations and price ceilings. It uses the [Tequila API](https://tequila.kiwi.com/portal/docs/tequila_api) to search for flights within the specified criteria and [Twilio](https://www.twilio.com/) to send the resulting SMS.

## Basis

This project is based on the Flight Search project from the course [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Angela Yu on Udemy
