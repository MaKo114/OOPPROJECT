from Train import Train
from Schedule import Schedule
from Route import Route

class Departure:
    def __init__(self, train: Train, schedule: Schedule, route: Route):
        self.__train = train
        self.__schedule = schedule
        self.__route = route

    @property
    def get_schedule(self):
        return self.__schedule
    
    @property
    def get_train(self):
        return self.__train
    
    @property
    def get_route(self):
        return self.__route
    

    def calculate_price(self):
        distance = sum(self.__route.get_distances or [])  # ระยะทางรวม
        # print(f"ระยะทางรวม: {distance} km")

        if distance == 0:
            print("Warning: Distance is zero")
            return []

        base_price_per_km = {
            "เร็ว": 0.5,
            "ด่วนพิเศษ CNR": 1.5,
            "ด่วน": 1.0,
            "ด่วนพิเศษ": 1.1,
            "ด่วนพิเศษดีเซลราง": 1.2
        }
        train_type = self.__train.get_train_type
        base_price = base_price_per_km.get(train_type, 1.0) * distance
        # print(f"Train type: {train_type}, Base price (รวมระยะทาง): {base_price} บาท")

        carriage_prices = []

        for carriage in self.__train.get_carriage:
            seat_multiplier = {
                "นั่ง": 1.0,
                "เตียงบน": 1.2,
                "เตียงล่าง": 1.5
            }
            floor_multiplier = {
                "3": 1.0,
                "2": 1.3,
                "1": 1.8
            }
            aircon_multiplier = 1.5 if carriage.get_room_type == "ปรับอากาศ" else 1.0

            print(f"Processing carriage: {carriage.get_carriage_type}")
            seat_price = seat_multiplier.get(carriage.get_seat, 1.0) * base_price
            floor_price = floor_multiplier.get(carriage.get_floor, 1.0) * seat_price
            final_price = floor_price * aircon_multiplier

            print(f"Seat price: {seat_price}, Floor price: {floor_price}, Final price: {final_price}")

            price_info = {
                "price": round(final_price)
            }
            carriage_prices.append(price_info)

        # print(f"Final carriage prices: {carriage_prices}")
        return carriage_prices
