from app.utils import load_config
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config = load_config("app/config.json")
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in config["shops"]
    ]
    customer = Customer(
        name=config["customer"]["name"],
        location=config["customer"]["location"],
        money=config["customer"]["money"],
        product_cart=config["customer"]["product_cart"],
        car_data=config["customer"]["car_data"]
    )
    fuel_price = config["fuel_price"]

    cheapest_trip = None
    best_shop = None

    for shop in shops:
        trip_cost = customer.calculate_trip_cost(shop, fuel_price)
        if trip_cost is not None and customer.money >= trip_cost:
            if cheapest_trip is None or trip_cost < cheapest_trip:
                cheapest_trip = trip_cost
                best_shop = shop

    if best_shop:
        product_total = best_shop.calculate_products_cost(
            customer.product_cart
        )
        customer.make_purchase(best_shop, cheapest_trip, product_total)
    else:
        print(
            f"{customer.name} doesn't have enough money"
            f" to make a purchase in any shop"
        )
