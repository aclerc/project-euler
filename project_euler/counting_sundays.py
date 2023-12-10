def count_sundays_on_first_of_month_one_year(year: int, first_day_of_year: int) -> tuple[int, int]:
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = False
    if year % 400 == 0:
        is_leap_year = True
    if year % 4 == 0 and year % 100 != 0:
        is_leap_year = True
    if is_leap_year:
        days_in_months[1] = 29
    answer = 0
    first_day_of_month = first_day_of_year
    for dim in days_in_months:
        sunday_int = 6
        if first_day_of_month == sunday_int:
            answer += 1
        first_day_of_month = (first_day_of_month + dim) % 7
    return answer, first_day_of_month


def count_sundays_on_first_of_month(first_year: int, last_year: int) -> int:
    # 1 Jan 1900 was a Monday.
    first_allowed_year = 1900
    if first_year < first_allowed_year:
        msg = "first_year must be >= 1900"
        raise ValueError(msg)
    answer = 0
    yr = 1900
    first_day_of_year = 0  # 0 means Monday
    while yr <= last_year:
        answer_, first_day_of_year = count_sundays_on_first_of_month_one_year(yr, first_day_of_year)
        print(f"yr={yr}, answer_={answer_}, first_day_of_year={first_day_of_year}")
        if yr >= first_year:
            answer += answer_
        yr += 1
    return answer


if __name__ == "__main__":
    first_year = 1901
    last_year = 2000
    print(
        f"How many Sundays fell on the first of the month during the twentieth century (1 Jan {first_year} "
        f"to 31 Dec {last_year})?",
    )
    print(f"answer: {count_sundays_on_first_of_month(first_year, last_year)}")
