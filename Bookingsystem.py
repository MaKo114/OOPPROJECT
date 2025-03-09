from Route import Route
from Station import Station
from Train import Train
from Payment import Payment
from Booking import Booking
from Ticket import Ticket
from Member import Member
from Instance import create_instance


class Bookingsystem:
    def __init__(self):
        self.__member_lst = []
        self.__station_lst = []
        self.__booking_lst = []
        self.__departure_lst = []
        self.__train_lst = []
        self.base_price_per_km = 1.0  # ราคาต่อกิโลเมตร
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
    
    def all_train(self):
        return self.__train_lst
    
    def show_all_station(self):
        return self.__station_lst
    
    def show_all_member(self):
        return self.__member_lst
    
    def login(self,email,password):
        for member in self.__member:
            if email == member.get_email and password == member.get_password:
                return member
        return None
    
    def logout(self):
        if self.is_login:
            self.is_login = False
            self.login_account_no = None

    def register(self,name,email,phone_number,password):
        self.add_member(Member(name,email,"member",phone_number,password))
        return 'Register Sucess'
    
    @property
    def get_login_member(self):
        for member in self.__member:
            if self.login_account_no == member.get_member_id:
                return member

    def get_all_seat_in_car(self,car_id):
        car = self.find_carriag_by_id(car_id)
        return car.get_all_seat_number_and_status # [[seat_num,status]]
    
    def ticket_info(self,member_id, booking_id, ticket_id):
        member = self.find_member_by_id(member_id)
        ticket = member.find_ticket_by_id(ticket_id)
        return ticket.return_info()
    
    def get_booking_member(self):
        member = self.get_login_member
        booking_list = member.get_all_booking
        return booking_list
    
    def get_ticket_member(self,booking_id):
        member = self.get_login_member
        booking = member.find_booking_by_id(booking_id)
        ticket_list = booking.get_ticket
        return ticket_list
    
    def cancel_ticket(self,ticket_id):
        member = self.get_login_member

        ticket = member.find_ticket_by_id(ticket_id)
        seat = ticket.get_seat
        seat.release_seat()
        member.remove_ticket(ticket_id)
        member.remove_booking()
        return seat.get_status

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
            train = departure.get_train  # ใช้ property
            route = departure.get_route  # ใช้ property

            # ตรวจสอบว่าหมายเลขขบวนตรงกับที่ต้องการ
            if train_num == train.get_train_num:
                # เรียก calculate_price (ไม่ต้องใช้ start_station และ end_station)
                carriage_prices = departure.calculate_price()

                if not carriage_prices:
                    print("ไม่พบข้อมูลโบกี้")
                    return []

                # เพิ่มข้อมูลใน all_carrige
                for i, carriage in enumerate(train.get_carriage):
                    price_info = carriage_prices[i]  # ราคาที่คำนวณแล้ว
                    carrige_type = carriage.get_carriage_type
                    carrige_seat = carriage.get_seat
                    room_type = carriage.get_room_type
                    floor = carriage.get_floor

                    all_carrige.append({
                        "carrige_type": carrige_type,
                        "carrige_seat": carrige_seat,
                        "room_type": room_type,
                        "floor": floor,
                        "price": price_info['price'],
                        "available": True
                    })

        return all_carrige
    

    def booking_ticket(self,member_id,departure_id,train_num,carriage_id,seat_number_list):
        count = 0
        member = self.find_member_by_id(member_id)
        booked_departure = self.find_departure_by_id(departure_id)
        booked_train = self.find_train_by_train_num(train_num)
        booked_carriage = None
        booked_seat = []
        for car in booked_train.get_carriag:
            if carriage_id == car.get_carriage_id:
                booked_carriage = car
        for seat in booked_carriage.get_seat:
            for seat_num in seat_number_list:
                if seat_num == seat.get_seat_number:
                    seat.reserve_seat()
                    booked_seat.append(seat)
        count+=1
        pay = Payment(count,booked_carriage,booked_seat,member)
        pay.processPayment()
        if pay.checkStatus() == 'sucess':
            booking = Booking(member,booked_departure,pay)
            for seat in booked_seat:
                ticket = Ticket(member,booked_departure,booked_carriage,seat)
                ticket.update_attribute()
                booking.ticket_append(ticket)
            member.add_booking(booking)
        return "Book Ticket Sucess"
    
    def select_seat_in_carriage(self, train_num, carriage_type):
        seeatt = []
        for departure in self.__departure_lst:
            train = departure.get_train
            carriage = train.get_carriage
            for i in carriage:
                if train_num == train.get_train_num and carriage_type == i.get_carriage_type:
                    for j in i.show_seat():
                        seeatt.append(j.get_seat_number)
                    return seeatt


a = Bookingsystem()
# all_seat = [e.get_carrige for e in a.all_train()]

# n = [s.get_seat_in_carriage for s in all_seat]
# print(n)
print(a.select_seat_in_carriage("7","กซข.ป.76"))
