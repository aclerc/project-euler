from project_euler.lattice_paths import count_lattice_routes


def test_p015() -> None:
    grid_side = 20
    ans = 137846528820
    assert count_lattice_routes(grid_side) == ans
