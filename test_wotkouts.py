from training import *


def test_add_workout():
    log = []

    add_workout(log, "бег", 30)

    assert log == [("бег", 30)]


def test_total_minutes():
    log = []
    add_workout(log, "бег", 30)
    add_workout(log, "плавание", 45)
    assert total_minutes(log) == 75


def test_add_kind():
    kinds_set = set()
    add_kind(kinds_set, "бег")
    add_kind(kinds_set, "бег")
    assert kinds_set == {"бег"}


def test_long_workouts():
    kinds = {"бег": 30, "плавание": 45, "йога": 20}
    long_workouts = [k for k, m in kinds.items() if m > 30]
    assert long_workouts == ["плавание"]
