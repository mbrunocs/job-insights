from src.counter import count_ocurrences

PATH = "src/jobs.csv"
TOTAL_USERS = 367


def test_counter():
    pass
    assert count_ocurrences(PATH, "users") == TOTAL_USERS
