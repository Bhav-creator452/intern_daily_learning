from abc import ABC, abstractmethod

from config import (
    DISTANCE_LIMIT,
    ACTIVE_ORDER_LIMIT,
    HEAVY_ORDER_LIMIT,
    RUSH_HOURS,
)


class RiskRule(ABC):
    """
    Abstract base class for all risk rules.
    Every rule must implement the calculate() method.
    """

    @abstractmethod
    def calculate(self, delivery):
        pass


class DistanceRule(RiskRule):
    """Adds risk points for long-distance deliveries."""

    def calculate(self, delivery):
        if delivery["distance_km"] > DISTANCE_LIMIT:
            points = 2
            return points
        return 0


class ActiveOrdersRule(RiskRule):
    """Adds risk points when many active orders are assigned."""

    def calculate(self, delivery):
        if delivery["driver_active_orders"] > ACTIVE_ORDER_LIMIT:
            points=2
            return points
        return 0


class WeatherRule(RiskRule):
    """Adds risk points for stormy weather."""

    def calculate(self, delivery):
        if delivery["weather"].lower() == "storm":
            points=3
            return points
        return 0


class RushHourRule(RiskRule):
    """Adds risk points during peak pickup hours."""

    def calculate(self, delivery):
        if delivery["pickup_hour"] in RUSH_HOURS:
            points=1
            return points
        return 0


class HeavyOrderRule(RiskRule):
    """Adds risk points for heavy orders."""

    def calculate(self, delivery):
        if delivery["item_count"] >= HEAVY_ORDER_LIMIT:
            points = 2
            return points
        return 0