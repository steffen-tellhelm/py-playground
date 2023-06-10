#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta
import locale

LAST_DATE = "2022-09-26"
WEEK = timedelta(days=7)
PAYOUT = 0.5


def main():
    locale.setlocale(locale.LC_ALL, "de_DE")
    last_date = datetime.fromisoformat(LAST_DATE)

    pay_day = last_date + WEEK
    amount = PAYOUT

    while pay_day < datetime.now():
        print(f"pay out at {pay_day:%x}: €{PAYOUT:.2f}, sum: €{amount:.2f}")
        pay_day += WEEK
        amount += PAYOUT


if __name__ == "__main__":
    main()
