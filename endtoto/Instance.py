# from Bookingsystem import Bookingsystem
from Station import Station
from Departure import Departure
from Schedule import Schedule
from Train import Train
from Carriage import Carriage
from Member import Member
from Seat import Seat


def create_instance(control):
    # control = Bookingsystem()

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


    # add schedule north 
    schedule_train07 = Schedule([(north[0].get_station_name, "09.05"), 
                            (north[1].get_station_name, "09.18"),
                            (north[2].get_station_name , "09.28"),
                            (north[3].get_station_name, "09.54"),
                            (north[4].get_station_name , "10.28"),
                            (north[5].get_station_name , "11.37"),
                            (north[6].get_station_name , "13.12"),
                            (north[7].get_station_name , "14.30"),
                            (north[8].get_station_name , "15.23"),
                            (north[9].get_station_name , "17.30"),
                            (north[10].get_station_name , "18.22"),
                            (north[11].get_station_name , "19.14"),
                            (north[12].get_station_name , "19.30")])
    
    schedule_train8 = Schedule([(north[12].get_station_name , "08.50"), 
                            (north[11].get_station_name , "09.04"),
                            (north[10].get_station_name , "09.46"),
                            (north[9].get_station_name , "10.38"),
                            (north[8].get_station_name , "12.38"),
                            (north[7].get_station_name , "13.25"),
                            (north[6].get_station_name , "14.34"),
                            (north[5].get_station_name , "16.21"),
                            (north[4].get_station_name , "17.26"),
                            (north[3].get_station_name , "18.05"),
                            (north[2].get_station_name , "18.30"),
                            (north[1].get_station_name , "18.40"),
                            (north[0].get_station_name , "18.55")])
    

    schedule_train109 = Schedule([(north[0].get_station_name, "14.15"), 
                            (north[1].get_station_name, "14.30"),
                            (north[2].get_station_name , "14.42"),
                            (north[3].get_station_name, "15.17"),
                            (north[4].get_station_name , "16.21"),
                            (north[5].get_station_name , "18.24"),
                            (north[6].get_station_name , "20.35"),
                            (north[7].get_station_name , "22.27"),
                            (north[8].get_station_name , "23.39"),
                            (north[9].get_station_name , "01.54"),
                            (north[10].get_station_name , "02.57"),
                            (north[11].get_station_name , "03.43"),
                            (north[12].get_station_name , "04.05")])
    

    schedule_train102 = Schedule([(north[12].get_station_name , "06.30"), 
                            (north[11].get_station_name , "06.48"),
                            (north[10].get_station_name , "07.35"),
                            (north[9].get_station_name , "08.27"),
                            (north[8].get_station_name , "10.43"),
                            (north[7].get_station_name , "11.37"),
                            (north[6].get_station_name , "13.16"),
                            (north[5].get_station_name , "15.53"),
                            (north[4].get_station_name , "18.05"),
                            (north[3].get_station_name , "19.14"),
                            (north[2].get_station_name , "19.55"),
                            (north[1].get_station_name , "20.08"),
                            (north[0].get_station_name , "20.25")])
    
    schedule_train09 = Schedule([(north[0].get_station_name, "18.40"), 
                            (north[1].get_station_name, "18.55"),
                            (north[2].get_station_name , "19.06"),
                            (north[3].get_station_name, "19.44"),
                            (north[4].get_station_name , "20.41"),
                            (north[5].get_station_name , "22.14"),
                            (north[6].get_station_name , "00.15"),
                            (north[7].get_station_name , "01.44"),
                            (north[8].get_station_name , "02.48"),
                            (north[9].get_station_name , "04.57"),
                            (north[10].get_station_name , "06.01"),
                            (north[11].get_station_name , "06.50"),
                            (north[12].get_station_name , "07.15")])
    
    schedule_train13 = Schedule([(north[0].get_station_name, "20.05"), 
                            (north[1].get_station_name, "20.20"),
                            (north[2].get_station_name , "20.31"),
                            (north[3].get_station_name, "21.06"),
                            (north[4].get_station_name , "21.58"),
                            (north[5].get_station_name , "23.28"),
                            (north[6].get_station_name , "01.47"),
                            (north[7].get_station_name , "03.11"),
                            (north[8].get_station_name , "04.16"),
                            (north[9].get_station_name , "06.30"),
                            (north[10].get_station_name , "07.32"),
                            (north[11].get_station_name , "08.19"),
                            (north[12].get_station_name , "08.40")])
    
    schedule_train51 = Schedule([(north[0].get_station_name, "20.30"), 
                            (north[1].get_station_name, "22.45"),
                            (north[2].get_station_name , "22.58"),
                            (north[3].get_station_name, "23.35"),
                            (north[4].get_station_name , "00.27"),
                            (north[5].get_station_name , "02.21"),
                            (north[6].get_station_name , "04.37"),
                            (north[7].get_station_name , "06.10"),
                            (north[8].get_station_name , "07.17"),
                            (north[9].get_station_name , "09.51"),
                            (north[10].get_station_name , "11.00"),
                            (north[11].get_station_name , "11.48"),
                            (north[12].get_station_name , "12.10")])
    
    # add schedule northes ubon
    schedule_train21 = Schedule([(northeast_ubon[0].get_station_name, "06.10"), 
                            (northeast_ubon[1].get_station_name, "06.25"),
                            (northeast_ubon[2].get_station_name , "06.36"),
                            (northeast_ubon[3].get_station_name, "06.58"),
                            (northeast_ubon[4].get_station_name , "07.33"),
                            (northeast_ubon[5].get_station_name , "08.52"),
                            (northeast_ubon[6].get_station_name , "10.21"),
                            (northeast_ubon[7].get_station_name , "11.13"),
                            (northeast_ubon[8].get_station_name , "11.34"),
                            (northeast_ubon[9].get_station_name , "12.09"),
                            (northeast_ubon[10].get_station_name , "12.32"),
                            (northeast_ubon[11].get_station_name , "13.01"),
                            (northeast_ubon[12].get_station_name , "13.18"),
                            (northeast_ubon[13].get_station_name , "13.38"),
                            (northeast_ubon[14].get_station_name , "14.00"),])
    
    schedule_train135 = Schedule([(northeast_ubon[0].get_station_name, "07.10"), 
                            (northeast_ubon[1].get_station_name, "07.25"),
                            (northeast_ubon[2].get_station_name , "07.38"),
                            (northeast_ubon[3].get_station_name, "08.27"),
                            (northeast_ubon[4].get_station_name , "09.17"),
                            (northeast_ubon[5].get_station_name , "10.52"),
                            (northeast_ubon[6].get_station_name , "12.12"),
                            (northeast_ubon[7].get_station_name , "13.47"),
                            (northeast_ubon[8].get_station_name , "14.19"),
                            (northeast_ubon[9].get_station_name , "15.07"),
                            (northeast_ubon[10].get_station_name , "15.40"),
                            (northeast_ubon[11].get_station_name , "16.34"),
                            (northeast_ubon[12].get_station_name , "17.00"),
                            (northeast_ubon[13].get_station_name , "17.26"),
                            (northeast_ubon[14].get_station_name , "18.00"),])
    

    schedule_train71 = Schedule([(northeast_ubon[0].get_station_name, "10.35"), 
                            (northeast_ubon[1].get_station_name, "10.50"),
                            (northeast_ubon[2].get_station_name , "11.01"),
                            (northeast_ubon[3].get_station_name , "11.30"),
                            (northeast_ubon[4].get_station_name, "12.05"),
                            (northeast_ubon[5].get_station_name , "13.25"),
                            (northeast_ubon[6].get_station_name , "14.27"),
                            (northeast_ubon[7].get_station_name , "15.50"),
                            (northeast_ubon[8].get_station_name , "16.14"),
                            (northeast_ubon[9].get_station_name , "17.08"),
                            (northeast_ubon[10].get_station_name , "17.38"),
                            (northeast_ubon[11].get_station_name , "18.18"),
                            (northeast_ubon[12].get_station_name , "18.40"),
                            (northeast_ubon[13].get_station_name , "19.07"),
                            (northeast_ubon[14].get_station_name , "19.50"),
                            ])
    
    schedule_train139 = Schedule([(northeast_ubon[0].get_station_name, "19.25"), 
                            (northeast_ubon[1].get_station_name, "19.39"),
                            (northeast_ubon[2].get_station_name , "19.51"),
                            (northeast_ubon[3].get_station_name , "20.25"),
                            (northeast_ubon[4].get_station_name, "21.09"),
                            (northeast_ubon[5].get_station_name , "22.46"),
                            (northeast_ubon[6].get_station_name , "00.07"),
                            (northeast_ubon[7].get_station_name , "01.47"),
                            (northeast_ubon[8].get_station_name , "02.22"),
                            (northeast_ubon[9].get_station_name , "03.15"),
                            (northeast_ubon[10].get_station_name , "03.53"),
                            (northeast_ubon[11].get_station_name , "04.44"),
                            (northeast_ubon[12].get_station_name , "05.07"),
                            (northeast_ubon[13].get_station_name , "05.38"),
                            (northeast_ubon[14].get_station_name , "06.15"),
                            ])
    
    schedule_train139 = Schedule([(northeast_ubon[0].get_station_name, "19.25"), 
                            (northeast_ubon[1].get_station_name, "19.39"),
                            (northeast_ubon[2].get_station_name , "19.51"),
                            (northeast_ubon[3].get_station_name , "20.25"),
                            (northeast_ubon[4].get_station_name, "21.09"),
                            (northeast_ubon[5].get_station_name , "22.46"),
                            (northeast_ubon[6].get_station_name , "00.07"),
                            (northeast_ubon[7].get_station_name , "01.47"),
                            (northeast_ubon[8].get_station_name , "02.22"),
                            (northeast_ubon[9].get_station_name , "03.15"),
                            (northeast_ubon[10].get_station_name , "03.53"),
                            (northeast_ubon[11].get_station_name , "04.44"),
                            (northeast_ubon[12].get_station_name , "05.07"),
                            (northeast_ubon[13].get_station_name , "05.38"),
                            (northeast_ubon[14].get_station_name , "06.15"),
                            ])
    

    schedule_train23 = Schedule([(northeast_ubon[0].get_station_name, "21.05"), 
                            (northeast_ubon[1].get_station_name, "21.20"),
                            (northeast_ubon[2].get_station_name , "21.30"),
                            (northeast_ubon[3].get_station_name , "22.01"),
                            (northeast_ubon[4].get_station_name, "22.35"),
                            (northeast_ubon[5].get_station_name , "00.07"),
                            (northeast_ubon[6].get_station_name , "01.36"),
                            (northeast_ubon[7].get_station_name , "03.02"),
                            (northeast_ubon[8].get_station_name , "03.31"),
                            (northeast_ubon[9].get_station_name , "04.13"),
                            (northeast_ubon[10].get_station_name , "04.42"),
                            (northeast_ubon[11].get_station_name , "05.19"),
                            (northeast_ubon[12].get_station_name , "05.38"),
                            (northeast_ubon[13].get_station_name , "06.06"),
                            (northeast_ubon[14].get_station_name , "06.40"),
                            ])
    

    schedule_train141 = Schedule([(northeast_ubon[0].get_station_name, "23.05"), 
                            (northeast_ubon[1].get_station_name, "23.21"),
                            (northeast_ubon[2].get_station_name , "23.35")
                            (northeast_ubon[3].get_station_name , "00.16"),
                            (northeast_ubon[4].get_station_name , "00.58"),
                            (northeast_ubon[5].get_station_name, "02.54"),
                            (northeast_ubon[6].get_station_name , "04.19"),
                            (northeast_ubon[7].get_station_name , "05.53"),
                            (northeast_ubon[8].get_station_name , "06.30"),
                            (northeast_ubon[9].get_station_name , "07.26"),
                            (northeast_ubon[10].get_station_name , "08.05"),
                            (northeast_ubon[11].get_station_name , "08.47"),
                            (northeast_ubon[12].get_station_name , "09.06"),
                            (northeast_ubon[13].get_station_name , "09.38"),
                            (northeast_ubon[14].get_station_name , "10.20"),])
    
# northeast_ubon = [c1, c2, c3, c4, ne1, ne2, ne3, ne4, ne5, ne6, ne7, ne8, ne9, ne10, ne11]


    # add train north
    train7 = Train("7", "ด่วนพิเศษดีเซลราง",)
    train9 = Train("9", "ด่วนพิเศษ CNR",)
    train13 = Train("13", "ด่วนพิเศษ")
    train109 = Train("109", "เร็ว",)
    train51 = Train("51", "ด่วน",)

    # add train northes ubon
    train21 = Train("21", "ด่วนพิเศษดีเซลราง")
    train135 = Train("135", "เร็ว")
    train71 = Train("71", "ด่วน")
    train134 = Train("134", "เร็ว",)
    train23 = Train("23", "ด่วนพิเศษ CNR")

    # add train northes 
    train75 = Train("75", "ด่วน")
    train25 = Train ("25", "ด่วนพิเศษ CNR")
    train133 = Train("133", "เร็ว")
    
    # add train sourth
    train171 = Train("171", "เร็ว")
    train31 = Train("37",  "ด่วนพิเศษ")
    train45 = Train("45", "ด่วนพิเศษ")
    train31 = Train("31", "ด่วนพิเศษ CNR")
    train169 = Train("169", "เร็ว", )

    # back train
    train102 = Train("102", "เร็ว")
    train8 = Train("8", "ด่วนพิเศษดีเซลราง")


    # add carrige 
    carrige7 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง")

    carrige109 = Carriage("บชท.48", "2", "พัดลม", "นั่ง")
    carrige109_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง")
    carrige109_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นั่ง")

    carrige8 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง")

    carrige102 = Carriage("บชท.48", "2", "พัดลม", "นั่ง")
    carrige102_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง")




    # add carrige in train
    train7.add_carriage(carrige7)

    train109.add_carriage(carrige109)
    train109.add_carriage(carrige109_1)
    train109.add_carriage(carrige109_2)

    train8.add_carriage(carrige8)

    train102.add_carriage(carrige102)
    train102.add_carriage(carrige102_1)


    #
    departure07 = Departure(train7, schedule_train07,)
    departure08 = Departure(train8, schedule_train8,)
    departure109 = Departure(train109, schedule_train109,)
    departure102 = Departure(train102, schedule_train102,)

    control.add_departure(departure07)
    control.add_departure(departure08)
    control.add_departure(departure109)
    control.add_departure(departure102)

    # carriage_type = control.show_carriage("7")
    # quntity = int(carriage_type["carriage_type"][-2:])

    # s1 = [Seat(seat_id) for seat_id in range(1, quntity + 1)]


    # mem1 = Member("mako", "manasak", "kingslime", "slatt", "Male", "09999999999")
    

    #(control.search_departure("สถานีกลางกรุงเทพอภิวัฒน์", "เชียงใหม่", "141616"))
    #print(control.search_departure("สถานีกลางกรุงเทพอภิวัฒน์", "ลพบุรี", "141616"))
    # print(control.search_departure("สถานีกลางกรุงเทพอภิวัฒน์", "เชียงใหม่", "141616"))
    #print()
    #print(control.search_departure("เชียงใหม่", "เด่นชัย", "141616"))
    # print(control.show_carriage("7"))
    # print()
    # print(control.show_carriage("8"))
    # print()
    # print(control.show_carriage("109"))
    # print()
    # print(control.show_carriage("102"))


#create_instance()