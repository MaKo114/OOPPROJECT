class Schedule :
    def __init__(self, schedule,):
        self.__schedule = schedule
        # self.__direction = direction

    @property
    def get_schedule_train(self):
        return self.__schedule
    
    # @property
    # def get_direction(self):
    #     return self.__direction    
    # 
    # 
# distance_bkk_to_chiangmai = [0, 15, 8, 41, 62 , 113, 143, 99, 46, 108, 41, 46, 22]
# distance_bkk_to_ubon = [0, 15, 8, 41, 42 , 67, 84, 82, 30, 44, 42, 32, 21, 29, 31]
# distance_bkk_to_nongkuy = [0, 15, 8, 41, 54 , 84, 137, 32, 30, 42, 34, 49, 36, 52]
# distance_bkk_to_hadyai = [0, 11, 17, 29, 53 , 49, 63, 256, 166, 122, 89, 83]
# print(sum(distance_bkk_to_chiangmai))
# print(sum(distance_bkk_to_ubon))
# print(sum(distance_bkk_to_nongkuy))
# print(sum(distance_bkk_to_hadyai))
