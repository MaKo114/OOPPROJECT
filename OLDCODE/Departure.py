from Train import Train
from Schedule import Schedule
from Route import Route

class Departure:
    def __init__(self, route: Route, train: Train, schedule: Schedule):
        self.__route = route
        self.__train = train
        self.__schedule = schedule
    
    @property
    def get_route(self):
        return self.__route
    
    @property
    def get_train(self):
        return self.__train
    
    @property
    def get_schedule(self):
        return self.__schedule