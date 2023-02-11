#Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка
#напишите формат указанной даты для перевода в объект datetime:
#The Moscow Times — Wednesday, October 2, 2002
#The Guardian — Friday, 11.10.13
#Daily News — Thursday, 18 August 1977

from datetime import datetime

#The Moscow Times
print('The Moscow Times', datetime.strptime('Wednesday, October 02, 2002', '%A, %B %d, %Y'))

#The Guardian
print('The Guardian', datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y'))

#The Guardian
print('The Guardian', datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y'))