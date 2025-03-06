

class Station :
    def __init__(self, station_name):
        self.__station_name = station_name

    
    @property
    def get_station_name(self):
        return self.__station_name