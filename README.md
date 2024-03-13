# CurrencyTrack
CurrencyTrack is a Django project designed to facilitate currency conversion and exchange rate tracking. 
Leveraging the power of the requests library, this project retrieves currency exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/) and allows users to convert currencies effortlessly.

# Features
+ Currency conversion: Easily convert currencies based on the latest exchange rates.
+ Exchange rate tracking: Stay informed about currency exchange rate fluctuations.
+ User-friendly interface: Intuitive interface for seamless currency operations.

# Usage
+ Install the necessary dependencies by running **'pip install -r requirements.txt'**.
+ Start the Django server by running **'python manage.py runserver'**.
+ Navigate to the web application in your browser.
+ Enter the desired currencies and amounts for conversion.
+ View the converted amount and exchange rate information.

# Dependencies
+ Django
+ requests

# Note
Make sure to obtain an API key from ExchangeRate-API and configure it in the project settings before using the application.
***exchange\views.py***
```python
def exchange(request):
    response = requests.get(
        url='API_TOKEN from ExchangeRate-API').json()
    currency = response.get('conversion_rates')
```

# Preview
![](https://github.com/jaynix01/CurrencyTrack/blob/main/preview.png)
