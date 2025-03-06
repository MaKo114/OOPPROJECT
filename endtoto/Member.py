from User import User

class Member(User):
    def __init__(self, username, password, fname, lname, gender, tel):
        super().__init__(username, password, fname, lname, gender, tel)
        self.__booking_lst = []


    @property
    def get_booking_lst(self):
        return self.__booking_lst
    
    def add_booking_lst(self, booking_lst):
        self.__booking_lst.append(booking_lst)