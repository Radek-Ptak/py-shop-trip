class Car:

    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_for_distance(
            self,
            distance: float,
            fuel_price: float
    ) -> float:

        if self.fuel_consumption <= 0 or fuel_price <= 0 or distance < 0:
            return distance * (self.fuel_consumption / 100) * fuel_price
        else:
            raise ValueError(
                "fuel_consumption, fuel_price must be > 0 "
                "and distance must be >= 0"
            )
