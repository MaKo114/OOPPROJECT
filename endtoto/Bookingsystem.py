from Route import Route
from Station import Station
from Train import Train
from Instance import create_instance



class Bookingsystem:
    def __init__(self):
        self.__member_lst = []
        self.__station_lst = []
        self.__booking_lst = []
        self.__departure_lst = []
        self.__train_lst = []
        create_instance(self)


    def add_member(self, member):
        self.__member_lst.append(member)

    def add_station(self, *stations):
        for station in stations:
            self.__station_lst.append(station)

    def add_booking(self, booking):
        self.__booking_lst.append(booking)

    def add_departure(self, departure):
        self.__departure_lst.append(departure)

    def add_train(self, train):
        self.__train_lst.append(train)

    def all_departure(self):
        return self.__departure_lst
    
    def show_all_station(self):
        return self.__station_lst
    
    def show_all_member(self):
        return self.__member_lst
    

  

    def search_departure(self, source, destination, date):
        match_departure = []
        for departure in self.__departure_lst:

            schedule = departure.get_schedule
            train = departure.get_train
            schedule_train = schedule.get_schedule_train
            source_index = -1
            destination_index = -1

            # ค้นหาดัชนีของสถานีต้นทางและปลายทาง
            for i in range(len(schedule_train)):
                if schedule_train[i][0] == source:
                    source_index = i
                if schedule_train[i][0] == destination:
                    destination_index = i

            # ตรวจสอบว่าพบสถานีต้นทางและปลายทางในตารางเวลา
            if source_index != -1 and destination_index != -1 and source_index < destination_index:
                departure_time = schedule_train[source_index][1]
                arrival_time = schedule_train[destination_index][1]
                train_num = train.get_train_num
                train_type = train.get_train_type

                match_departure.append({
                    "departure_time": departure_time,
                    "arrival_time": arrival_time,
                    "train_num": train_num,
                    "train_type": train_type
                })

        return match_departure

    def show_carriage(self, train_num):
        all_carrige = []
        for departure in self.__departure_lst:
            train = departure.get_train
            carriage = train.get_carrige
            
            if train_num == train.get_train_num:

                for i in carriage:
                    carrige_type = i.get_carrige_type
                    carrige_seat = i.get_seat
                    room_type = i.get_room_type
                    floor = i.get_floor
                    all_carrige.append({
                            "carrige_type": carrige_type,
                            "carrige_seat": carrige_seat,
                            "room_type": room_type,
                            "floor": floor
                        })
            
        return all_carrige


    # def show_carriage(self, train_num):
    #     all_carrige = []
    #     found = False  # ป้องกันการค้นหาซ้ำ

    #     for departure in self.__departure_lst:
    #         train = departure.get_train
    #         carriage = train.get_carrige

    #         if train_num == train.get_train_num:
    #             for i in carriage:
    #                 carrige_type = i.get_carrige_type
    #                 carrige_seat = i.get_seat
    #                 room_type = i.get_room_type
    #                 floor = i.get_floor
    #                 all_carrige.append({
    #                     "carrige_type": carrige_type,
    #                     "carrige_seat": carrige_seat,
    #                     "room_type": room_type,
    #                     "floor": floor
    #                 })

    #             found = True  # เจอขบวนแล้ว
    #             break  # ออกจากลูปเพื่อป้องกันการเพิ่มข้อมูลซ้ำ

    #     return all_carrige

            
