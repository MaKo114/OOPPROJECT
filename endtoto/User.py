

class User:
    def __init__(self, username, password, fname, lname, gender, tel):
        self.__username = username
        self.__password = password
        self.__fname = fname
        self.__lname = lname
        self.__gender = gender
        self.__tel = tel
    
    @property
    def get_username(self):
        return self.__username
    
    @property
    def get_password(self):
        return self.__password
    
    @property
    def get_fname(self):
        return self.__fname
    
    @property
    def get_lname(self):
        return self.__lname
    
    @property
    def get_gender(self):
        return self.__gender
    
    @property
    def get_tel(self):
        return self.__tel