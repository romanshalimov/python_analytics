#Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True
#в методах курсов валют (eur, usd итд) будет возвращать не курс валюты, а изменение по сравнению
#в прошлым значением. Считайте, self.diff будет принимать значение True только при возврате значения курса.
#При отображении всей информации о валюте он не используется.

import requests

class Rate:
    def __init__(self, format='value', diff = False):
        self.format = format
        self.diff = diff
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()
        
        if currency in response:
           if self.diff == False: 
               if self.format == 'full':
                   return response[currency]
            
               if self.format == 'value':
                return response[currency]['Value']
        
                return 'Error'
           else:
                return ((response[currency]['Value'] * 10 ** 6 - response[currency]['Previous'] * 10 ** 6) / 10 ** 6)

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def AZN(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format"""
        return self.make_format('AZN')

print(Rate(diff = True).eur())

