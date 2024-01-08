from datetime import date, timedelta
from json import load
import os.path

# TODO: Catch and rephrase string info for vacation that's already in the past

def get_days_delta(year_of_vacation: int, month_of_vacation: int, day_of_vacation: int) -> int:
    
    today: date = date.today()
    vacation_date: date = date(year_of_vacation, month_of_vacation, day_of_vacation)

    delta: timedelta = vacation_date - today

    return delta.days

def get_weeks_delta(year_of_vacation: int, month_of_vacation: int, day_of_vacation: int) -> int:
    
    days_left: int = get_days_delta(year_of_vacation, month_of_vacation, day_of_vacation)

    return days_left // 7

def days_and_weeks_left(year_of_vacation: int, month_of_vacation: int, day_of_vacation: int,
                        translation: str = "EN") -> str:
    
    days_left: int = get_days_delta(year_of_vacation, month_of_vacation, day_of_vacation)
    single_days_left: int = days_left % 7
    weeks_left: int = get_weeks_delta(year_of_vacation, month_of_vacation, day_of_vacation)

    expression: list = []

    with open(os.path.dirname(__file__) + "/../../static/translations.json") as f:
        translations = load(f)

    translate: function = lambda word: translations[translation][word]

    if days_left > 1:
        expression.append(f"{days_left}")
        expression.append(f" {translate('days')}")
    else:
        expression.append(f"{days_left}")
        expression.append(f" {translate('day')}")

    expression.append(f" {translate('in total')} {translate('or')}")
    
    if weeks_left == 0:
        expression.append(f" {translate('less than')} {translate('a week')}")
    elif weeks_left == 1:
        expression.append(f" {translate('a week')}")
    else:
        expression.append(f" {weeks_left} {translate('weeks')}")

    expression.append(f" {translate('and')}")

    if single_days_left > 1:
        expression.append(f" {single_days_left}")
        expression.append(f" {translate('days')}")
    else:
        expression.append(f" {single_days_left}")
        expression.append(f" {translate('day')}")
    
    expression.append(f" {translate('left')}")

    return "".join(expression)


if __name__ == "__main__":
    print(days_and_weeks_left(2024, 3, 12, "DE"))