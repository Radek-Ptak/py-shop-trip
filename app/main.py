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
        name=config["customers"][0]["name"],
        location=config["customers"][0]["location"],
        money=config["customers"][0]["money"],
        product_cart=config["customers"][0]["product_cart"],
        car_data=config["customers"][0]["car"]
    )
    fuel_price = config["FUEL_PRICE"]

    cheapest_trip = None
    best_shop = None

    for shop in shops:
        trip_cost = (
            customer.calculate_trip_cost(shop, fuel_price))
        product_total = (
            shop.calculate_products_cost(customer.product_cart))
        total_cost = trip_cost + product_total if (
            trip_cost is not None) else None

        if total_cost is not None and customer.money >= total_cost:
            if cheapest_trip is None or total_cost < cheapest_trip:
                cheapest_trip = total_cost
                best_shop = shop

    if best_shop:
        trip_cost = customer.calculate_trip_cost(best_shop, fuel_price)
        product_total = best_shop.calculate_products_cost(
            customer.product_cart
        )
        customer.make_purchase(best_shop, trip_cost, product_total)
    else:
        print(
            f"{customer.name} doesn't have enough money"
            f" to make a purchase in any shop"
        )
