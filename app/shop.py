import datetime
from typing import List, Dict


class Shop:

    def __init__(
            self, name: str,
            location: List[float],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(
            self,
            product_cart: Dict[str, int]
    ) -> float:
        total_product_cost = 0.0

        for product_name, quantity in product_cart.items():

            if product_name in self.products:
                price = self.products[product_name]
                total_product_cost += price * quantity
            else:
                raise ValueError(
                    f"Product {product_name} not available in {self.name}"
                )
        return total_product_cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: Dict[str, int],
            total_product_cost: float
    ) -> None:
        data_now = datetime.datetime.now()
        date_time = data_now.strftime("%m/%d/%Y %H:%M:%S")
        print(f"Date: {date_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")

        for product_name, quantity in product_cart.items():

            if product_name in self.products:
                price = self.products[product_name]
                cost_of_item = price * quantity

                print(
                    f"{quantity} {product_name}s for "
                    f"{round(cost_of_item, 2)} dollars"
                )
        print(f"Total cost is {round(total_product_cost, 2)} dollars")
        print("See you again!")
