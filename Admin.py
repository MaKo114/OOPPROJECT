from User import User




class Admin(User):
    admin_id = 0
    def __init__(self,name,email,role,phone_number,password):
        super().__init__(name,email,role,phone_number,password)
        Admin.admin_id += 1
        self.__admin_id = Admin.admin_id    