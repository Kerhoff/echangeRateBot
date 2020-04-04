import requests
from bs4 import BeautifulSoup

class ExchangeRate:

    cbrf_exchagne_rate = "https://cbr.ru/currency_base/daily/"
    usd_to_ruble_google_request = "https://www.google.com/search?sxsrf=ALeKk01PBbXHC21rHvbFbO0mMOE_7-pg7g%3A1585400138372&ei=Skl_Xp-qFoWdkgWQzKdw&q=usd+to+ruble&oq=ruble+rate&gs_lcp=CgZwc3ktYWIQARgAMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHMgQIABBHUABYAGD0OWgAcAJ4AIABAIgBAJIBAJgBAKoBB2d3cy13aXo&sclient=psy-ab"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    last_exchange_rate = 0
    difference = 5   

    def __init__(self):
        self.last_exchange_rate = float(self.get_exchange_rate().replace(",", "."))

    def get_exchange_rate(self):
        response = requests.get(self.usd_to_ruble_google_request, headers = self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        rate_source_on_page = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return rate_source_on_page[0].text

    def check_exchage_rate(self):
        exchange_rate = float(self.get_exchange_rate().replace(",", "."))

        #Нужно записывать последнее значение курса в файл csv для сохранеия, а дальше извлекать предпоследнее значение и сравнивать
        exchange_difference = exchange_rate - self.last_exchange_rate

        print("Курс: 1 доллар = " + str(exchange_rate))
        print("Изменения курса: " + str(exchange_difference))



currency = ExchangeRate()
currency.check_exchage_rate()