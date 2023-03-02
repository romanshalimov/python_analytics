#Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным значением курса с помощью сервиса

from libs.exchange import Rate #применим класс Rate для решения задачи

def max_rate():
    currency_list = [(item['Name'], item['Value']) for item in Rate().exchange_rates().values()] #воспользуемся функцией exchange_rates для получения данных с сайта ЦБ
    currency_list.sort(key = lambda currency: currency[1], reverse = True) #отсортируем полученный список
    return(currency_list[0][0]) #выведем первую в списке валюту

print(max_rate())