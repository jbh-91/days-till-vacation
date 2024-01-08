import pytest
from datetime import date, timedelta
from flaskr.tools.days_till_vacation import days_till_vacation


class TestDaysTillVacation():
    test_date = date.today() + timedelta(days=64)

    year = test_date.year
    month = test_date.month
    day = test_date.day

    def test_days_delta(self):
        assert days_till_vacation.get_days_delta(self.year, self.month, self.day) == 64

    def test_weeks_delta(self):
        assert days_till_vacation.get_weeks_delta(self.year, self.month, self.day) == 9

    def test_days_and_weeks_left(self):
        assert days_till_vacation.days_and_weeks_left(self.year, self.month, self.day) == "64 days in total or 9 weeks and 1 day left"

    def test_translation(self):
        assert days_till_vacation.days_and_weeks_left(self.year, self.month, self.day, "EN") == "64 days in total or 9 weeks and 1 day left"
        assert days_till_vacation.days_and_weeks_left(self.year, self.month, self.day, "DE") == "64 Tage insgesamt oder 9 Wochen und 1 Tag verbleibend"
