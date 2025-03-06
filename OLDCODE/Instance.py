# from Bookingsystem import Bookingsystem
from Station import Station
from Route import Route
from Train import Train
from Schedule import Schedule
from Departure import Departure



def create_instance(control):

    # control = Bookingsystem()

    #### add Station #####
    c1 = Station("สถานีกลางกรุงเทพอภิวัฒน์",)
    c2 = Station("ดอนเมือง",)
    c3 = Station("รังสิต",)
    c4 = Station("อยุธยา",)
    n1 = Station("ลพบุรี",)
    n2 = Station("นครสวรรค์")
    n3 = Station("พิษณุโลก",)
    n4 = Station("ศิลาอาสน์",)
    n5 = Station("เด่นชัย",)
    n6 = Station("นครลำปาง")
    n7 = Station("ขุนตาน",)
    n8 = Station("ลำพูน",)
    n9 = Station("เชียงใหม่",)

    ne1 = Station("สระบุรี",)
    ne2 = Station("ปากช่อง",)
    ne3 = Station("นครราชสีมา",)
    ne4 = Station("ลำปลายมาศ",)
    ne5 = Station("บุรีรัมย์",)
    ne6 = Station("สุรินทร์",)
    ne7 = Station("ศีชรภูมิ",)
    ne8 = Station("อุทุมพรพิสัย",)
    ne9 = Station("ศรัสะเกษ",)
    ne10 = Station("กันทรารมย์",)
    ne11 = Station("อุบลราชธานี",)

    ne12 = Station("ชุมทางแก่งคอย", )
    ne13 = Station("ลำนารายณ์", )
    ne14 = Station("ชุมทางบัวใหญ่", )
    ne15 = Station("เมืองพล", )
    ne16 = Station("บ้านไผ่", )
    ne17 = Station("ขอนแก่น", )
    ne18 = Station("น้ำพอง", )
    ne19 = Station("กุมภวาปี", )
    ne20 = Station("อุดรธานี", )
    ne21 = Station( "หนองคาย", )

    s1 = Station("บางบำหรุ", )
    s2 = Station("ศาลายา", )
    s3 = Station("นครปฐม", )
    s4 = Station("ราชบุรี", )
    s5 = Station("เพชรบุรี", )
    s6 = Station("หัวหิน", )
    s7 = Station("ชุมพร", )
    s8 = Station("สุราษฎร์ธานี", )
    s9 = Station("ชุมทางทุ่งสง", )
    s10 = Station("พัทลุง", )
    s11 = Station("ชุมทางหาดใหญ่", )

    control.add_station(c1, c2, c3, c4, 
                        n1, n2, n3, n4, n5, n6, n7, n8, n9, 
                        ne1, ne2, ne3, ne4, ne5, ne6, ne7, ne8, ne9, ne10, ne11, 
                        ne12, ne13, ne14, ne15, ne16, ne17, ne18, ne19, ne20, ne21,
                        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11
                        )
    
    # add direction trip
    north = [c1, c2, c3, c4, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    northeast_ubon = [c1, c2, c3, c4, ne1, ne2, ne3, ne4, ne5, ne6, ne7, ne8, ne9, ne10, ne11]
    northeast_nongkuy = [c1, c2, c3, c4, n1, ne12, ne13, ne14, ne15, ne16, ne17, ne18, ne19, ne20, ne21]
    south = [c1, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]

    # control.add_trip(north, northeast_ubon, northeast_nongkuy, south)


    # create route

    schedule_train7 = Schedule({north[0].get_station_name : "09.05", 
                            north[1].get_station_name : "09.18",
                            north[2].get_station_name : "09.28",
                            north[3].get_station_name : "09.54",
                            north[4].get_station_name : "10.28",
                            north[5].get_station_name : "11.37",
                            north[6].get_station_name : "13.12",
                            north[7].get_station_name : "14.30",
                            north[8].get_station_name : "15.23",
                            north[9].get_station_name : "17.30",
                            north[10].get_station_name : "18.22",
                            north[11].get_station_name : "19.14",
                            north[12].get_station_name : "19.30"}, "ไป")

    schedule_train8 = Schedule({north[12].get_station_name : "08.50", 
                            north[11].get_station_name : "09.04",
                            north[10].get_station_name : "09.46",
                            north[9].get_station_name : "10.38",
                            north[8].get_station_name : "12.38",
                            north[7].get_station_name : "13.25",
                            north[6].get_station_name : "14.34",
                            north[5].get_station_name : "16.21",
                            north[4].get_station_name : "17.26",
                            north[3].get_station_name : "18.05",
                            north[2].get_station_name : "18.30",
                            north[1].get_station_name : "18.40",
                            north[0].get_station_name : "18.55"}, "กลับ")
    
    # add departure 7 
    route = Route('สถานีกลางกรุงเทพอภิวัฒน์', "เชียงใหม่",)
    train7 = Train(7, "เร็ว",)
    control.add_train(train7)
    departure7 = Departure(route, train7, schedule_train7)
    control.add_departure(departure7)

    # add departure 8 
    back_train8 = Train(8, "ด่วนพิเศษดีเซลราง")
    control.add_train(back_train8)
    departure7 = Departure(route, back_train8, schedule_train8)
    control.add_departure(departure7)
    # control.seach_departure("เชียงใหม่", "นครสวรรค์")
    # control.seach_departure("สถานีกลางกรุงเทพอภิวัฒน์", "นครสวรรค์")
    # a = control.all_station()
    # print(a)

    
# create_instance()