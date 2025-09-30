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
    print(f"{customer.name} has {customer.money} dollars")
    fuel_price = config["FUEL_PRICE"]

    cheapest_trip = None
    best_shop = None

    for shop in shops:
        trip_cost = (
            customer.calculate_trip_cost(shop, fuel_price))

        if trip_cost is not None:
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost:.2f}")
        total_cost = trip_cost
        if total_cost is not None and customer.money >= total_cost:
            if cheapest_trip is None or total_cost < cheapest_trip:
                cheapest_trip = total_cost
                best_shop = shop

    if best_shop:
        trip_cost = customer.calculate_trip_cost(best_shop, fuel_price)
        customer.make_purchase(best_shop, trip_cost)
    else:
        print(
            f"{customer.name} doesn't have enough money"
            f" to make a purchase in any shop"
        )
shop_trip()