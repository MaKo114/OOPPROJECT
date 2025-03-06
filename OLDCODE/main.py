from fasthtml.common import *
from Bookingsystem import Bookingsystem

app, rt = fast_app(live=True)

control = Bookingsystem()



@rt("/")
def get():
    station_lst = control.all_station()
    print(control.seach_departure("สถานีกลางกรุงเทพอภิวัฒน์" , "เชียงใหม่"))
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
                                    *[Option(f"{station}", value=f"{station}") for station in station_lst],
                                    name="source",
                                ),
                               
                                ),
                                Td(
                                 Label("สถานีปลายทาง:"),
                                Select(
                                    *[Option(f"{station}", value=f"{station}") for station in station_lst],
                                    name="destination",
                                )
                                ),
                                Td(
                                    Label("วันที่เดินทาง:"),
                                    Input(type="date", name="date"),
                                ),
                            
                            Td(
                                Label("จำนวนผู้โดยสาร:"),
                                Input(type="number", name="passenger"),
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
def source_to_destination(source:str, destination:str):

    result = control.seach_departure(source, destination)
    print(result)
    if not (result):
        return P(f'ไม่พบเที่ยวเดินรถจาก "{source}" ไป "{destination}"', style="text-align: center; color: red;")

    return Table(
        Tr(
            Th("เวลาออก"), 
            Th("เวลาถึง"), 
            Th("ขบวน"), 
            Th("ประเภท")
        ),
        *[
            Tr(
                Td(result[0]), 
                Td(result[1]), 
                Td(result[2]), 
                Td(result[3]),
                Td(Button("เลือก", onclick="alert('ควย')"))
            )
            
        ],
        style="margin: auto; width: 60%; border-collapse: collapse; border: 1px solid black;"
    )

serve()
