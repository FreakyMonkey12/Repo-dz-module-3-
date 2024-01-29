from datetime import datetime

def get_days_from_today(date):
    try:

        target_date = datetime.strptime(date, '%Y-%m-%d')

        current_date = datetime.today()

        delta = current_date - target_date

        return delta.days
    except ValueError:

        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."


print(get_days_from_today("2014-01-26"))