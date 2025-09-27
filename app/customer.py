from typing import List, Dict
from app.car import Car
from app.shop import Shop


class Customer:

    def __init__(
            self,
            name: str,
            location: List[float],
            money: float,
            product_cart: Dict[str, int],
            car_data: Dict
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car_data = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"]
        )

    def calculate_trip_cost(self, shop: Shop, full_price: float) -> float:
        distance_to_shop =
