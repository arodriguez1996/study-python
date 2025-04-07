#Fechas y horas en python

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

#fecha y hora actual
print(datetime.now())

specific_date = datetime(2025, 5, 3)
print(specific_date)


#format
# https://docs.python.org/es/3.9/library/datetime.html#strftime-and-strptime-format-codes
# metodo strftime()
formatted_date = specific_date.strftime("%A /%B/%Y %%")
print(formatted_date)


# Operaciones con fechas 

yesterday = datetime.now() - timedelta(days=1)
minus_half_day = datetime.now() - timedelta(days=0.5)
print(yesterday)
print(minus_half_day)

# obtener componentes individuales de una fecha

now = datetime.now()
month, year = now
print(f" year: {year}, month = {year}")

#diferencia entre 2 fechas

today = datetime.today()
next_week = datetime.today() + timedelta(weeks=1)
difference = next_week - today
print(difference.days)