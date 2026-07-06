from scorer import late_risk_label


def test_heavy_order_rule():

    delivery = {
        "distance_km": 25,
        "active_orders": 2,
        "weather": "clear",
        "pickup_hour": 12,
        "item_count": 15
    }

    assert late_risk_label(delivery) == "MEDIUM"
