from Route import Route

class Train:
    def __init__(self, train_num, train_type, ):
        self.__train_num = train_num
        self.__train_type = train_type
        self.__carriage_lst = []

    
    @property
    def get_train_num(self):
        return self.__train_num
    
    @property
    def get_train_type(self):
        return self.__train_type
    
    # @property
    # def get_route(self):
    #     return self.__route
    
    
    def add_carriage(self, carriage):
        self.__carriage_lst.append(carriage)

    