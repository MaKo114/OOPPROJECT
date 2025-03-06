from Schedule import Schedule
    
class Route:
    def __init__(self, source, destination,):
        self.__source = source
        self.__destination = destination
        # self.__schedule = schedule
        # self.__train = train

    @property
    def get_source(self):
        return self.__source
    
    @property
    def get_destination(self):
        return self.__destination
    
    # @property
    # def get_schedule(self):
    #     return self.__schedule
    
    # @property
    # def get_train(self):
    #     return self.__train
    
