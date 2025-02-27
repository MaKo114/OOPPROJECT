from Route import Route
from Station import Station
from Train import Train
from Instance import create_instance



class Bookingsystem:
    def __init__(self):
        self.__member_lst = []
        self.__station_lst = []
        self.__booking_lst = []
        # self.__trip_lst = []
        self.__departure_lst = []
        self.__train_lst = []
        create_instance(self)

    
    
    def add_member(self, member):
        self.__member_lst.append(member)
    
    def add_station(self, *stations):
        for station in stations:
            self.__station_lst.append(station)
    
    def add_booking(self, booking):
        self.__booking_lst.append(booking)

    # def add_trip(self, *directions):
    #     for direction in directions:
    #         self.__trip_lst.append(direction)

    def add_departure(self, departure):
        self.__departure_lst.append(departure)

    def add_train(self, train):
        self.__train_lst.append(train)

    # def seach_departure(self, source, destination):
    #     for departure in self.__departure_lst:
    #         train = departure.get_train
    #         schedule = departure.get_schedule

    #         if source in schedule.get_time and destination in schedule.get_time:
    #             departure_time = schedule.get_time_at(source)
    #             arrival_time = schedule.get_time_at(destination)
    #             print(f'เวลาออก - เวลาถึง {departure_time} - {arrival_time} ประเภท {train.get_train_type} ขบวนที่ {train.get_train_num} ')# ต้องเอารอบรถไฟมาใส่
    #         elif 
    
    def all_station(self):
        station = [(i.get_station_name )for i in self.__station_lst]
        return station

    # def seach_departure(self, source, destination):
    #     results = []  # ลิสต์เก็บผลลัพธ์
    #     found = False  # ตัวแปรช่วยตรวจว่าพบขบวนหรือไม่

    #     for departure in self.__departure_lst:
    #         schedule = departure.get_schedule
    #         stations = list(schedule.get_time.keys())  # ดึงลำดับสถานี
            
    #         if source in stations and destination in stations:
    #             source_index = stations.index(source)
    #             dest_index = stations.index(destination)

    #             if (schedule.get_direction == "ไป" and source_index < dest_index) or \
    #             (schedule.get_direction == "กลับ" and source_index > dest_index):
    #                 departure_time = schedule.get_time_at(source)
    #                 arrival_time = schedule.get_time_at(destination)
    #                 results.append([
    #                     departure_time, 
    #                     arrival_time, 
    #                     departure.get_train.get_train_num, 
    #                     departure.get_train.get_train_type
    #                 ])
    #                 found = True

    #     return results if found else []  # ถ้าไม่พบข้อมูลให้คืนค่าเป็น []

    def seach_departure(self, source, destination):
        found = False
        for departure in self.__departure_lst:
            schedule = departure.get_schedule
            # สมมุติว่า schedule.get_time_dict() คืน OrderedDict หรือ dict ที่มีลำดับ
            stations = list(schedule.get_time.keys())
            # เช็กว่าต้นทางและปลายทางอยู่ในตารางเวลาหรือไม่
            if source in stations and destination in stations:
                source_index = stations.index(source)
                dest_index = stations.index(destination)
                # กำหนดทิศทางจากตารางเวลา
                # ตัวอย่าง: ถ้า schedule.direction == "ไป" หมายความว่าตารางเวลานี้จัดเรียงจากกรุงเทพ -> เชียงใหม่
                # ดังนั้น ถ้าค้นหาด้วยต้นทางเป็นกรุงเทพ หรือสถานีที่อยู่ในฝั่งต้นทางของรอบ "ไป" ก็ให้แสดง
                # และถ้า schedule.direction == "กลับ" ก็ตรงข้าม
                if schedule.get_direction == "ไป" and source_index < dest_index:
                    departure_time = schedule.get_time_at(source)
                    arrival_time = schedule.get_time_at(destination)
                    print(f'เวลาออก - เวลาถึง {departure_time} - {arrival_time} \nขบวน {departure.get_train.get_train_num} ประเภท {departure.get_train.get_train_type}')
                    return [departure_time , arrival_time, departure.get_train.get_train_num, departure.get_train.get_train_type]
                    found = True
                elif schedule.get_direction == "กลับ" and source_index < dest_index:
                    # ในกรณีรอบกลับ ลำดับของสถานีจะกลับกัน
                    departure_time = schedule.get_time_at(source)
                    arrival_time = schedule.get_time_at(destination)
                    print(f'เวลาออก - เวลาถึง {departure_time} - {arrival_time} \nขบวน {departure.get_train.get_train_num} ประเภท {departure.get_train.get_train_type}')
                    return [departure_time, arrival_time, departure.get_train.get_train_num, departure.get_train.get_train_type]
                    found = True
        if not found:
            return False
            # print(f'ไม่พบเที่ยวเดินรถจาก "{source}" ไป "{destination}"')