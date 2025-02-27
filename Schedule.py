

class Schedule :
    def __init__(self, schedule_dict, direction):
        self.__schedule_dict = schedule_dict
        self.__direction = direction

    @property
    def get_time(self):
        return self.__schedule_dict
    
    @property
    def get_direction(self):
        return self.__direction
        
    @property
    def start_station(self):
        # สมมุติว่า dict นี้รักษาลำดับการเพิ่มได้
        return list(self.__time_dict.keys())[0]

    @property
    def end_station(self):
        return list(self.__time_dict.keys())[-1]

    
    def get_time_at(self, station_name):
        return self.__schedule_dict.get(station_name, "ไม่มีข้อมูล")