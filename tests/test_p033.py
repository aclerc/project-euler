from project_euler.digit_cancelling_fractions import denominator_of_digit_cancelling_two_digit_fractions


def test_p033() -> None:
    assert denominator_of_digit_cancelling_two_digit_fractions() == 100  # noqa PLR2004
