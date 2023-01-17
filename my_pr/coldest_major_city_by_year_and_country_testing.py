import pytest

from coldest_major_city_by_year_and_country import coldest_major_city_by_year_and_country


@pytest.mark.parametrize(
    "year, Country, correct_City",
    [
        (1983, "Russia", "Saint Petersburg"),
        (2003, "Spain", "Madrid"),
        (1960, "Italy", "Rome"),
        (1977, "China", "Harbin"),
    ],
)
def coldest_major_city_by_year_and_country_testing(year, country):
    answer = get_hottest_month_and_city(year, country)
    assert answer["hottest_city"] == correct_City
