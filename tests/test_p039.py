from project_euler.integer_right_triangles import maximum_integer_traingles


def test_p039() -> None:
    ans = 840
    assert maximum_integer_traingles(1000) == ans
