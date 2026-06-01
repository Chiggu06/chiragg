class FlightData:
    def __init__(self,price, origin, destination, outbound_date, return_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.outbound_date = outbound_date
        self.return_date = return_date

def check_cheap_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flights found, try for looking for connecting flights")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    cheapest_price = float("inf")
    cheapest_flight = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < cheapest_price:
            cheapest_price = price
            origin_id = flight["flights"][0]["departure_airport"]["id"]
            destination_id = flight["flights"][-1]["arrival_airport"]["id"]
            destination_date = flight["flights"][-1]["arrival_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(cheapest_price, origin_id, destination_id, destination_date, return_date)
            print(f"Lowest price to {destination_id} is INR {cheapest_price}")
    return cheapest_flight