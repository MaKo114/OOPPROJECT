# from fasthtml.common import *
# from Bookingsystem import Bookingsystem
# from Member import Member

# app, rt = fast_app(live=True)
# control = Bookingsystem()

# @rt("/")
# def home():
#     station_lst = control.show_all_station()
#     return (
#         print
#         (
#             Title("ระบบจองตั๋วรถไฟ"),
#             Header(
#                 Table(
#                     Tr(
#                         Nav(
#                             A("เข้าสู่ระบบ", href="/login"),
#                             A("สมัครสมาชิก ", href="/member_register"),
#                             A("ติดต่อเรา ", href="/contact_us"),
#                             style="background-color: white; text-align: center; width: 30%; position: sticky; top: 0;",
#                         )
#                     ),
#                     Tr(
#                         Nav(
#                             A("หน้าแรก", href="/"),
#                             A("ประวัติการซื้อ", href="/purchase_history"),
#                             A("เปลี่ยนแปลงตั๋ว", href="/change_ticket"),
#                             A("ยกเลิกตั๋วโดยสาร", href="/cancel_ticket"),
#                             A("สิทธิพิเศษ", href="/benefit"),
#                             style="background-color: white; text-align: center; width: 60%;",
#                         )
#                     ),
#                 ),
#                 style="background-color: white;",
#             ),
#             Body(
#                 H1("ยินดีต้อนรับสู่เว็บไซต์ของเรา", style="text-align: center"),
#                 Form(
#                     Table(
#                         Tr(
#                             Td(Label("สถานีต้นทาง:"),
#                                Select(
#                                    *[Option(f"{station.get_station_name}", value=f"{station.get_station_name}") for station in station_lst],
#                                    name="source",
#                                )),
#                             Td(Label("สถานีปลายทาง:"),
#                                Select(
#                                    *[Option(f"{station.get_station_name}", value=f"{station.get_station_name}") for station in station_lst],
#                                    name="destination",
#                                )),
#                             Td(Label("วันที่เดินทาง:"),
#                                Input(type="date", name="date")),
#                             Td(Label("จำนวนผู้โดยสาร:"),
#                                Select(
#                                    Option(f'จำนวนผู้โดยสาร 1'),
#                                    Option(f'จำนวนผู้โดยสาร 2'),
#                                    Option(f'จำนวนผู้โดยสาร 3'),
#                                    Option(f'จำนวนผู้โดยสาร 4'),
#                                    type="number", name="passenger")),
#                             Td(Button('ค้นหา', type="submit", value="ค้นหา")),
#                         ),
#                     ), method='post', action='/display-train'
#                 ),
#             ),
#             Footer(
#                 P("KMITL: สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง"),
#                 P("เบอร์โทร 000-000-0000"),
#                 P("อีเมล์ xxxxxxxx@kmitl.ac.th"),
#                 style="background-color: white;",
#             ),
#         ),
#     )

# @rt("/display-train")
# def source_to_destination(source: str, destination: str, date):
#     result = control.search_departure(source, destination, date)
#     if not result:
#         return P(f'ไม่พบเที่ยวเดินรถจาก "{source}" ไป "{destination}"', style="text-align: center; color: red;")
#     return Table(
#         Tr(Th("เวลาออก", style="text-align: center"), Th("เวลาถึง", style="text-align: center"), Th("ขบวน", style="text-align: center"), Th("ประเภท", style="text-align: center"), Th("เลือก", style="text-align: center")),
#         *[
#             Tr(
#                 Td(dep["departure_time"]),
#                 Td(dep["arrival_time"]),
#                 Td(dep["train_num"]),
#                 Td(dep["train_type"]),
#                 Td(Form(
#                     Input(type="hidden", name="train_num", value=dep["train_num"]),
#                     Button("เลือก", type="submit"),
#                     method="get",
#                     action="/display-train/detail",
#                 )),
#             )
#             for dep in result
#         ],
#         style="margin: auto; width: 60%; border-collapse: collapse; border: 1px solid black;"
#     )


# @rt("/display-train/detail")
# def show_train_details(train_num: str):
#     train_details = control.show_carriage(train_num)
#     if not train_details:
#         return P(f"ไม่พบข้อมูลของขบวนที่ {train_num}", style="text-align: center; color: red;")
#     return Table(
#         Tr(Th("ประเภทตู้โดยสาร", style="text-align: center"), Th("จำนวนที่นั่ง", style="text-align: center"), Th("ประเภทห้อง", style="text-align: center"), Th("ชั้น", style="text-align: center"), Th("เลือก", style="text-align: center")),
#         *[
#             Tr(
#                 Td(detail["carrige_type"]),
#                 Td(detail["carrige_seat"]),
#                 Td(detail["room_type"]),
#                 Td(detail["floor"]),
#                 # Td(detail["carrige_type"][-2:]),
#                 Td(Form(
#                     Input(type="hidden", name="carrige_type", value=detail["carrige_type"]),
#                     Input(type="hidden", name="carrige_seat", value=detail["carrige_seat"]),
#                     Input(type="hidden", name="room_type", value=detail["room_type"]),
#                     Input(type="hidden", name="floor", value=detail["floor"]),
#                     Button("เลือก", type="submit"),
#                     method="post",
#                     action="/confirm-booking"
#                 )),
#             )
#             for detail in train_details
#         ],
#         style="margin: auto; width: 60%; border-collapse: collapse; border: 1px solid black;"
#     )




# @rt("/confirm-booking")
# def confirm_booking(carrige_type: str, carrige_seat: str, room_type: str, floor: str):
#     return (
#         (
#             Title("ยืนยันการจอง"),
#             Body(
#                 H1("ยืนยันการจองที่นั่ง", style="text-align: center"),
#                 Table(
#                     Tr(Th("ประเภทตู้โดยสาร", style="text-align: center"), Th("จำนวนที่นั่ง", style="text-align: center"), Th("ประเภทห้อง", style="text-align: center"), Th("ชั้น", style="text-align: center")),
#                     Tr(
#                         Td(carrige_type),
#                         Td(carrige_seat),
#                         Td(room_type),
#                         Td(floor),
#                     ),
#                 ),
#                 Form(
#                     Button('ยืนยันการจอง', type="submit", value="ยืนยันการจอง", style="display: block; margin: auto; padding: 10px 20px;"),
#                     method="post",
#                     action="/booking-success"
#                 ),
#                 A("ย้อนกลับ", href="/", style="display: block; margin: 10px auto; text-align: center;")
#             ),
#             Footer(
#                 P("KMITL: สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง"),
#                 P("เบอร์โทร 000-000-0000"),
#                 P("อีเมล์ xxxxxxxx@kmitl.ac.th"),
#                 style="background-color: white;",
#             ),
#         ),
#     )

# @rt("/booking-success")
# def booking_success():
#     return (
#         (
#             Title("การจองสำเร็จ"),
#             Body(
#                 H1("การจองสำเร็จ", style="text-align: center"),
#                 P("ขอขอบคุณที่ใช้บริการของเรา", style="text-align: center; color: green;"),
#                 A("กลับไปหน้าแรก", href="/", style="display: block; margin: auto; text-align: center;")
#             ),
#             Footer(
#                 P("KMITL: สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง"),
#                 P("เบอร์โทร 000-000-0000"),
#                 P("อีเมล์ xxxxxxxx@kmitl.ac.th"),
#                 style="background-color: white;",
#             ),
#         ),
#     )
# if __name__ == "__main__":
#     serve()



# from fastapi import FastAPI
# from Bookingsystem import Bookingsystem

# app = FastAPI()

# # สร้าง instance ของระบบจองตั๋ว
# control = Bookingsystem()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Train Booking API"}


# @app.get("/search_departure/")
# def search_departure(source: str, destination: str, date: str):
#     result = control.search_departure(source, destination, date)
#     return {"result": result}


from fasthtml.common import *
from Bookingsystem import Bookingsystem
from Member import Member
from Carriage import Carriage

app, rt = fast_app(live=True)

control = Bookingsystem()



@rt("/")
def home():
    station_lst = control.show_all_station()
    # print(control.search_departure("สถานีกลางกรุงเทพอภิวัฒน์" , "เชียงใหม่", "14215"))
    return (
        (
            Title("ระบบจองตั๋วรถไฟ"),
            Header(
                Table(
                    Tr(
                        Nav(
                            A("เข้าสู่ระบบ", href="/login"),
                            A("สมัครสมาชิก ", href="/member_register"),
                            A("ติดต่อเรา ", href="/contact_us"),
                            style="""
                background-color: white
                text-align: center
                width: 30%
                position: sticky
                top: 0
            """,
                        )
                    ),
                    Tr(
                        Nav(
                            A("หน้าแรก", href="/"),
                            A("ประวัติการซื้อ", href="/purchase_history"),
                            A("เปลี่ยนแปลงตั๋ว", href="/change_ticket"),
                            A("ยกเลิกตั๋วโดยสาร", href="/cancel_ticket"),
                            A("สิทธิพิเศษ", href="/benefit"),
                            style="""
                background-color: white
                text-align: center
                width: 60%
            """,
                        )
                    ),
                ),
                style="""
                background-color: white
            """,
            ),
            Body(
                H1(
                    "ยินดีต้อนรับสู่เว็บไซต์ของเรา",
                    style="text-align: center",
                ),
                Form(
                    Table(
                        Tr(
                            Td(
                                Div(
                                    A("ทั้งหมด", href="/"),
                                )
                            ),
                            Td(
                                A("สายเหนือ", href="/"),
                            ),
                            Td(
                                A("สายตะวันออกเฉียงเหนือ", href="/"),
                            ),
                            Td(
                                A("สายตะวันออก", href="/"),
                            ),
                            Td(
                                A("สายใต้", href="/"),
                            ),
                        ),
                         
                        Tr(
                            Td(Label("สถานีต้นทาง:"),
                                Select(
                                    *[Option(f"{station.get_station_name}", value=f"{station.get_station_name}") for station in station_lst],
                                    name="source",
                                ),
                               
                                ),
                                Td(
                                 Label("สถานีปลายทาง:"),
                                Select(
                                    *[Option(f"{station.get_station_name}", value=f"{station.get_station_name}") for station in station_lst],
                                    name="destination",
                                )
                                ),
                                Td(
                                    Label("วันที่เดินทาง:"),
                                    Input(type="date", name="date"),
                                ),
                            
                            Td(
                                Label("จำนวนผู้โดยสาร:"),
                                Select(Option(f'จำนวนผู้โดยสาร 1'),
                                       Option(f'จำนวนผู้โดยสาร 2'),
                                       Option(f'จำนวนผู้โดยสาร 3'),
                                       Option(f'จำนวนผู้โดยสาร 4') ,
                                       type="number", name="passenger",),
                            ),
                            Td(
                                Button('ค้นหา', type="submit", value="ค้นหา" ),
                                
                            ),
                        ),
                    ),  method = 'post',
                        action = '/display-train' 
            ),

            Footer(
                
                P("KMITL: สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง"),
                P("เบอร์โทร 000-000-0000"),
                P("อีเมล์ xxxxxxxx@kmitl.ac.th"),
                style="""
                background-color: white
            """,
            ),
        ),
    
        ),)




@rt("/display-train")
def source_to_destination(source:str, destination:str, date):
    
    result = control.search_departure(source, destination, date)
    print(result)
    if not (result):
        return P(f'ไม่พบเที่ยวเดินรถจาก "{source}" ไป "{destination}"', style="text-align: center; color: red;")

    return Table(
        Tr(Th("เวลาออก",style="text-align: center" ), Th("เวลาถึง", style="text-align: center"), Th("ขบวน", style="text-align: center"), Th("ประเภท", style="text-align: center"), Th("เลือก", style="text-align: center"), ),
        *[
            Tr(
                Td(dep["departure_time"]),
                Td(dep["arrival_time"]),
                Td(dep["train_num"]),
                Td(dep["train_type"]),
                Td(Form(
                        Input(type="hidden", name="train_num", value=dep["train_num"]),
                        Button("เลือก", type="submit"),
                        method="get",
                        action="/display-train/detail", 
                    ))
            )
            for dep in result
        ],
        style="margin: auto; width: 60%; border-collapse: collapse; border: 1px solid black;"
    )



@rt("/display-train/detail")
def show_train_details(train_num: str):
    train_details = control.show_carriage(train_num)
    
    if not train_details:
        return P(f"ไม่พบข้อมูลของขบวนที่ {train_num}", style="text-align: center; color: red;")
    
    return train_details # ถ้าไม่ล็อกอินก่อนจะไม่สามารถไปต่อจากหน้าที่แสดง รายละเอียดการทำงาน
         
# mem1 = Member("mako", "manasak", "kingslime", "slatt", "Male", "09999999999")
# control.add_member(mem1)
# print([i.get_username for i in control.show_all_member()])

serve()
