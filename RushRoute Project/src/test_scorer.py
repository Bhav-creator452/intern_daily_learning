#Testing the Refactored code 
from scorer import late_risk_label


def test_high_risk():
    assert late_risk_label(
        35,
        10,
        "storm",
        18
    ) == "HIGH"


def test_medium_risk():
    assert late_risk_label(
        25,
        6,
        "clear",
        12
    ) == "MEDIUM"


def test_low_risk():
    assert late_risk_label(
        5,
        2,
        "clear",
        14
    ) == "LOW"