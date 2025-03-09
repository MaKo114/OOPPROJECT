from Seat import Seat

class Carriage:
    def __init__(self, carriage_type, floor, room_type, seat, seat_count):
        self.__carriage_type = carriage_type
        self.__floor = floor
        self.__room_type = room_type
        self.__seat = seat
        self.__seat_in_carriage = []

        self.generate_seats(seat_count)
    
    def generate_seats(self, seat_count):
        """สร้างที่นั่งทั้งหมดในตู้โดยสาร"""
        for seat_number in range(1, seat_count + 1):
            self.__seat_in_carriage.append(Seat(seat_number))

    @property
    def get_carriage_type(self):
        return self.__carriage_type
    
    @property
    def get_floor(self):
        return self.__floor
    
    @property
    def get_room_type(self):
        return self.__room_type
    
    @property
    def get_seat(self):
        return self.__seat
    
    @property   
    def get_seat_in_carriage(self):
        return self.__seat_in_carriage

    # เพิ่มฟังก์ชันนี้ในคลาส Carriage
    @property
    def total_seats(self):
        return len(self.__seat_in_carriage)

    def show_seat(self):
        carilist = []
        for i in self.__seat_in_carriage:
            carilist.append(i)
        return carilist



    def add_seat(self, seat):
        self.__seat_lst.append(seat)