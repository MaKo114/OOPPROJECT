

class Carriage:
    def __init__(self, carrige_type, floor, room_type, seat ):
        self.__carringe_type = carrige_type
        self.__floor = floor
        self.__room_type = room_type
        self.__seat = seat


    @property
    def get_carrige_type(self):
        return self.__carringe_type
    
    @property
    def get_floor(self):
        return self.__floor
    
    @property
    def get_room_type(self):
        return self.__room_type
    
    @property
    def get_seat(self):
        return self.__seat
    

    def add_seat(self, seat):
        self.__seat_lst.append(seat)