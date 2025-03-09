from fasthtml.common import *
from Bookingsystem import Bookingsystem

app, rt = fast_app(live=True)



control = Bookingsystem()

# list โง่ๆ
trains = [
    {"departure": "09:05", "arrival": "19:30", "type": "ด่วนพิเศษดีเซลราง", "train_no": 7},
    {"departure": "14:15", "arrival": "04:05", "type": "เร็ว", "train_no": 109},
]

@rt("/")
def get():
    station_lst = control.show_all_station()
    return (
        Header(


        ),
        (
            Title("ระบบจองตั๋วรถไฟ"),
            Head(
                Table(
                    Tr(
                        Nav(
                            Td(
                                Button(
                                    "หน้าแรก",
                                    href="/",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                            Td(
                                Button(
                                    "ประวัติการซื้อ",
                                    href="/purchase_history",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                            Td(
                                Button(
                                    "เปลี่ยนแปลงตั๋ว",
                                    href="/change_ticket",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                            Td(
                                Button(
                                    "ยกเลิกตั๋วโดยสาร",
                                    href="/cancel_ticket",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                            Td(
                                Button(
                                    "ศูนย์ความช่วยเหลือ",
                                    href="/help",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                            Td(
                                Style="""
                                text-align: center;
                                width: 30%;
                                top: 0;
                            """,
                            ),
                            Td(
                                Button(
                                    "เข้าสู่ระบบ ",
                                    hx_get="/login",
                                    hx_target="body",
                                    hx_swap="beforeend",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                            Td(
                                Button(
                                    "สมัครสมาชิก",
                                    hx_get="/register",
                                    hx_target="body",
                                    hx_swap="beforeend",
                                    Style="""
                                text-align: center;
                                width: 100%;
                                top: 0;
                                color: #c48a0e;
                                background-color: white;
                                border: none;
                            """,
                                ),
                            ),
                        ),
                        Style="""
                        list-style-type: none;
                    margin: 0;
                    padding: 0;
                    overflow: hidden;
                    background-color: white;
                    color: black;
                    position: fixed;
                    top: 0;
                    width: 100%;
                    display: flex;
                    justify-content: space-between; /* Space between the left and right groups */
                    align-items: center;
                        """,
                    ),
                ),
            ),
            Body(
                Form(             
                    Label(
                        "ยินดีต้อนรับสู่เว็บไซต์ของเรา",
                        style="""
                        text-align: center;
                        margin-top: 20%;
                        margin-bottom: 150px;
                        color: #991c20;
                        font-size: 50px;
                        font-weight: bold;
                       """,
                    ),
                    Card(
                        Table(
                            Tr(
                                Td(
                                    A(
                                        "ทั้งหมด",
                                        href="/",
                                        Style="""
                                        color:  black;
                                        font-size: 18px;
                                        """,
                                    ),
                                    Style="""
                                background-color: white;
                                text-align: center;
                                width: 20%;
                                top: 0;

                            """,
                                ),
                                Td(
                                    A(
                                        "สายเหนือ",
                                        href="/",
                                        Style="""
                                        color:  black;
                                        font-size: 18px;
                                        """,
                                    ),
                                    Style="""
                                background-color: white;
                                text-align: center;
                                width: 20%;
                                top: 0;
                            """,
                                ),
                                Td(
                                    A(
                                        "สายตะวันออกเฉียงเหนือ",
                                        href="/",
                                        Style="""
                                        color:  black;
                                        font-size: 18px;
                                        """,
                                    ),
                                    Style="""
                                background-color: white;
                                text-align: center;
                                width: 20%;
                                top: 0;
                            """,
                                ),
                                Td(
                                    A(
                                        "สายตะวันออก",
                                        href="/",
                                        Style="""
                                        color:  black;
                                        font-size: 18px;
                                        """,
                                    ),
                                    Style="""
                                background-color: white;
                                text-align: center;
                                width: 20%;
                                top: 0;                                
                            """,
                                ),
                                Td(
                                    A(
                                        "สายใต้",
                                        href="/",
                                        Style="""
                                        color:  black;
                                        font-size: 18px;
                                        """,
                                    ),
                                    Style="""
                                background-color: white;
                                text-align: center;
                                width: 20%;
                                top: 0;
                            """,
                                ),
                            ),
                            Tr(
                                Td(
                                Label("สถานีต้นทาง:", style="color: #c48a0e;"),
                                Select(
                                    *[
                                        Option(f"{station.get_station_name}", value=f"{station.get_station_name}")
                                        for station in station_lst
                                    ],
                                    name="source",  # ชื่อพารามิเตอร์สำหรับสถานีต้นทาง
                                    Style="""
                                    background-color: white;
                                    border-color: #c48a0e;
                                    font-color: #c48a0e;
                                    """,
                                ),
                            ),
                            Td(
                                Label("สถานีปลายทาง:", style="color: #c48a0e;"),
                                Select(
                                    *[
                                        Option(f"{station.get_station_name}", value=f"{station.get_station_name}")
                                        for station in station_lst
                                    ],
                                    name="destination",  # ชื่อพารามิเตอร์สำหรับสถานีปลายทาง
                                    Style="""
                                    background-color: white;
                                    border-color: #c48a0e;
                                    font-color: #c48a0e;
                                    """,
                                ),
                            ),
                                Td(
                                    Label("วันที่เดินทาง:", style="color: #c48a0e;"),
                                    Input(
                                        type="date",
                                        name="date",
                                        Style="""
                                          background-color: white;
                                          border-color: #c48a0e; /* สีเส้นขอบ */
                                          font-color: #c48a0e;
                                          """,
                                    ),
                                    Style="""
                                background-color: white;
                                border-color: #c48a0e; /* สีเส้นขอบ */
                                border: none; /* ลบกรอบทั้งหมด */
                                border-top: 1.5px solid #000; /* เพิ่มเส้นบน */
                                """,
                                ),
                                Td(
                                    Label("จำนวนผู้โดยสาร:", style="color: #c48a0e;"),
                                    Select(
                                        Option("จำนวนผู้โดยสาร 1", value="1"),
                                        Option("จำนวนผู้โดยสาร 2", value="2"),
                                        Option("จำนวนผู้โดยสาร 3", value="3"),
                                        Option("จำนวนผู้โดยสาร 4", value="4"),
                                        name="passenger",
                                        Style="""
                                        background-color: white;
                                        border-color: #c48a0e; /* สีเส้นขอบ */
                                        font-color: #c48a0e;
                                        """,
                                    ),
                                    Style="""
                                background-color: white;
                                border-color: #c48a0e; /* สีเส้นขอบ */
                                border: none; /* ลบกรอบทั้งหมด */
                                border-top: 1.5px solid #000; /* เพิ่มเส้นบน */
                                """,
                                ),
                                Td(
                                    Input(
                                        type="submit",
                                        value="ค้นหา",
                                        Style="""
                                          margin-top: 15%;
                                          background-color: #c48a0e;
                                          border: none;
                                          """,
                                    ),
                                    Style="""
                                background-color: white;
                                border-color: #c48a0e; /* สีเส้นขอบ */
                                border: none; /* ลบกรอบทั้งหมด */
                                border-top: 1.5px solid #000; /* เพิ่มเส้นบน */
                                """,
                                ),
                            ),
                        ),
                        Style="""
                
                background-color: white;
                text-align: center;
                width: 60%;
                margin: auto;
                padding: 20px;
                border-radius: 10px;

            """,
                    ),
                    method="get",
                    action="/display_train",
                ),
                Style="""
        background-image: url("https://www.dticket.railway.co.th/DTicketPublicWeb/assets/img/bg-head.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    """,
    method="post",  # ใช้ method POST เพื่อส่งข้อมูล
                action="/display-train",  # ส่งข้อมูลไปยัง /display_train
            ),
            Footer(
                P(
                    "KMITL: สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง",
                    Style="""
                    margin-left:5%;
                    """,
                ),
                P(
                    "เบอร์โทร 000-000-0000",
                    Style="""
                    margin-left:5%;
                    """,
                ),
                P(
                    "อีเมล์ xxxxxxxx@kmitl.ac.th",
                    Style="""
                    margin-left:5%;
                    """,
                ),
                style="""
                background-color: white;
                margin-top: 50px;                
            """,
            ),
        ),
    )

@rt("/display_train")
def source_to_destination(source : str, destination : str, date : str):
    departure = control.search_departure(source, destination, date)
    print("123564545",departure)
    # ขั้นตอน
    steps = ["เลือกขบวนโดยสาร", "เลือกตู้โดยสาร", "กรอกข้อมูล", "ชำระเงิน"]
    # กำหนดสถานะ
    current_step = 1  # เปลี่ยนเลขตามสถานะที่ต้องการ
    return Html(
        Title("ระบบจองตั๋วรถไฟ"),
        Head(
            Style(
                """
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 0;
                }
                .navbar {
                    display: flex;
                    justify-content: space-between;  /* ให้แต่ละกลุ่มอยู่ซ้ายและขวา */
                    align-items: center;
                    background-color: white;
                    padding: 15px 50px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    height: 60px;
                }
                .nav-left {
                    display: flex;
                    gap: 20px; /* เว้นระยะห่าง */
                }
                .nav-right {
                    display: flex;
                    gap: 20px;
                    margin-left: auto; /* ดันกลุ่ม Login & Register ไปชิดขวา */
                }
                .navbar a {
                    color: #b08d46;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 16px;
                    transition: color 0.3s ease-in-out;
                }
                .navbar a:hover {
                    color: #8a6d2f;
                }
                .card {
                    background: white;
                    padding: 20px;
                    margin: 15px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .card-info {
                    display: flex;
                    flex-direction: column;
                }
                .card-row {
                    display: grid;
                    grid-template-columns: 1fr 1fr 2fr 1fr auto; /* ปรับขนาดคอลัมน์ */
                    align-items: center;
                    gap: 15px;
                    text-align: left;
                    width: 100%;
                }
                .col {
                    min-width: 100px; /* ป้องกันการบีบตัวอักษร */
                }  
                .card {
                    padding: 15px;
                }
                .btn {
                    background-color: #b08d46;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-decoration: none;
                }
                .header-container {
                    display: flex;
                    align-items: center;
                    margin-left: 20px;
                }
                .header-container h2 {
                    margin-right: 10px;
                }
                .progress {
                    display: flex;
                    justify-content: space-around;
                    padding: 20px;
                    background: white;
                    margin: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                .step {
                    text-align: center;
                    color: gray;
                    padding: 10px 20px;
                    position: relative;
                }
                .step.active {
                    color: #b08d46;
                    font-weight: bold;
                    border-bottom: 3px solid #b08d46;
                }
                .footer { 
                    text-align: center; margin-top: 20px; 
                }
            """
            )
        ),
        Body(Div(
            
        ),
            # Navbar
            Div(
                Div(
                    Div(
                        A("หน้าแรก", href="/"),
                        A("ประวัติการซื้อ", href="/"),
                        A("เปลี่ยนแปลงตั๋ว", href="/"),
                        A("ยกเลิกตั๋วโดยสาร", href="/"),
                        A("ศูนย์ความช่วยเหลือ", href="/"),
                        Class="nav-left",
                    ),
                    Div(
                        A("เข้าสู่ระบบ", href="/login"),
                        A("สมัครสมาชิก", href="/signup"),
                        Class="nav-right",
                    ),
                    Class="navbar",
                ),
            ),
            # Progress Bar
            Div(
                *[
                    Div(step, Class=f"step {'active' if i+1 == current_step else ''}")
                    for i, step in enumerate(steps)
                ],
                Class="progress",
            ),
            # รายการขบวนรถ
            Div(
                Div(
                    H2("เลือกขบวนโดยสาร"),
                    H2(
                        "เที่ยวไป",
                        Style="""
                            color: #c48a0e;                       
                        """,
                    ),
                    Class="header-container",
                ),
                Div(
                    Label("ต้นทาง", " >> ", "ปลายทาง"),
                ),
                *[
                    Div(
                        Div(
                           
                            P(f"เวลาออก: {train['departure_time']}", Class="col"),
                            P(f"เวลาถึง: {train['arrival_time']}", Class="col"),
                            P(f"ประเภท: {train['train_num']}", Class="col"),
                            P(f"ขบวนที่: {train['train_type']}", Class="col"),
                            A("เลือก", href=f"/carriage/{train['train_num']}", Class="btn"),
                            Class="card-row",
                        ),
                        Class="card",
                    )
                    for train in departure

                ],
            ),
            Div(A("ย้อนกลับ", href="/", Class="btn"), Class="footer"),
        ),
    )

@rt("/carriage/{train_num}")
def carriage(train_num: str):
    carriages = control.show_carriage(train_num)
    # ขั้นตอน
    steps = ["เลือกขบวนโดยสาร", "เลือกตู้โดยสาร", "กรอกข้อมูล", "ชำระเงิน"]
    # กำหนดสถานะ
    current_step = 2  # เปลี่ยนเลขตามสถานะที่ต้องการ
  

    return Html(
        Title("เลือกตู้โดยสาร"),
        Head(
            Style(
                """
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 0;
                }

                .navbar {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    background-color: white;
                    padding: 15px 50px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    height: 60px;
                }

                .nav-left {
                    display: flex;
                    gap: 20px;
                }

                .nav-right {
                    display: flex;
                    gap: 20px;
                    margin-left: auto;
                }

                .navbar a {
                    color: #b08d46;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 16px;
                    transition: color 0.3s ease-in-out;
                }

                .navbar a:hover {
                    color: #8a6d2f;
                }

                .container {
                    padding: 20px;
                }

                .progress {
                    display: flex;
                    justify-content: space-around;
                    padding: 20px;
                    background: white;
                    margin: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }

                .step {
                    text-align: center;
                    color: gray;
                    padding: 10px 20px;
                    position: relative;
                }

                .step.active {
                    color: #b08d46;
                    font-weight: bold;
                    border-bottom: 3px solid #b08d46;
                }

                .card {
                    background: white;
                    padding: 20px;
                    margin: 15px auto; /* จัดการ์ดให้อยู่ตรงกลาง */
                    border-radius: 10px;
                    display: flex;
                    justify-content: space-between; /* จัดเรียงข้อมูลและปุ่ม "เลือก" ในแนวนอน */
                    align-items: flex-start; /* จัดเรียงองค์ประกอบด้านบน */
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    width: 60%; /* กำหนดความกว้างของการ์ดเป็น 60% */
                    
                }

                .card.disabled {
                    background: #f0f0f0;
                    color: #777;
                }

                .card-info {
                    display: flex;
                    flex-direction: column; /* จัดเรียงข้อมูลในแนวตั้ง */
                    gap: 10px; /* ระยะห่างระหว่างข้อมูล */
                }

                .btn-group {
                    display: flex;
                    flex-direction: column; /* จัดเรียงปุ่มในแนวตั้ง */
                    gap: 10px; /* ระยะห่างระหว่างปุ่ม */
                    align-items: flex-end; /* จัดปุ่มไปทางขวา */
                    align-items: center;
                }

                .btn {
                    background-color: #b08d46;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-decoration: none;
                    font-size: 14px;
                    min-width: 180px; /* กำหนดความกว้างขั้นต่ำของปุ่ม */
                    text-align: center; /* จัดข้อความให้อยู่กึ่งกลาง */
                    
                   
                    
                }

                .btn.disabled {
                    background: #ccc;
                    cursor: not-allowed;
                }

                .footer {
                    text-align: center;
                    margin-top: 20px;
                }
                
            """
            )
        ),
        Body(
            # Navbar
            Div(
                Div(
                    Div(
                        A("หน้าแรก", href="/"),
                        A("ประวัติการซื้อ", href="/"),
                        A("เปลี่ยนแปลงตั๋ว", href="/"),
                        A("ยกเลิกตั๋วโดยสาร", href="/"),
                        A("ศูนย์ความช่วยเหลือ", href="/"),
                        Class="nav-left",
                    ),
                    Div(
                        A("เข้าสู่ระบบ", href="/login"),
                        A("สมัครสมาชิก", href="/signup"),
                        Class="nav-right",
                    ),
                    Class="navbar",
                ),
            ),
            # Progress Bar
            Div(
                *[
                    Div(step, Class=f"step {'active' if i+1 == current_step else ''}")
                    for i, step in enumerate(steps)
                ],
                Class="progress",
            ),
            # List Carriages
            Div(
                *[
                    Div(
                        Div(
                            P(
                                f"{c['carrige_type']}: รถโบกี้ ชั้น {c['floor']} {c['room_type']} - {c['carrige_seat']}"
                            ),
                            P(f"ราคา: {c.get('price', c.get('price', 0))} บาท"),
                            A(
                                "บันทึกไว้ใน Waiting List",
                                href=f"/waiting/{c['carrige_type']}",
                                Class="btn" if c["available"] else "btn disabled",
                            ),
                            Class="card-info",
                        ),
                        A(
                            "เลือก",
                            href=f"/seat/{train_num}/{c['carrige_type']}",
                            Class="btn" if c["available"] else "btn disabled",
                        ),
                        Class="card disabled" if not c["available"] else "card",
                    )
                    for c in carriages
                ],
                Class="container",
            ),
            # Footer
            Div(A("ย้อนกลับ", href="/", Class="btn"), Class="footer"),
        ),
    )

@rt("/seat/{train_num}/{carrige_type}")
def select_seat(seat_num, carriage_type):
    seat_num = control.select_seat_in_carriage(seat_num, carriage_type)

    return Html(
        Title("เลือกที่นั่ง"),
        Head(
            Style(
                """
                .seat-container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding: 20px;
                }

                .seat-info {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    width: 60%;
                    margin-bottom: 20px;
                }

                .seat-grid {
                    display: grid;
                    grid-template-columns: repeat(10, 1fr); /* 10 คอลัมน์สำหรับที่นั่ง */
                    gap: 10px;
                    width: 60%;
                }

                .seat {
                    background-color: #b08d46;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                }

                .seat.occupied {
                    background-color: #ccc;
                    cursor: not-allowed;
                }

                .seat.selected {
                    background-color: #4CAF50;
                }

                .seat-info p {
                    margin: 5px 0;
                }

                .btn {
                    background-color: #b08d46;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-decoration: none;
                    font-size: 14px;
                    margin-top: 20px;
                }
                """
            )
        ),
        Body(
            # Navbar
            Div(
                Div(
                    Div(
                        A("หน้าแรก", href="/"),
                        A("ประวัติการซื้อ", href="/"),
                        A("เปลี่ยนแปลงตั๋ว", href="/"),
                        A("ยกเลิกตั๋วโดยสาร", href="/"),
                        A("ศูนย์ความช่วยเหลือ", href="/"),
                        Class="nav-left"
                    ),
                    Div(
                        A("เข้าสู่ระบบ", href="/login"),
                        A("สมัครสมาชิก", href="/signup"),
                        Class="nav-right"
                    ),
                    Class="navbar"
                ),
            ),

            # ข้อมูลขบวนรถ
            Div(
                Div(
                    # P(f"เลือกที่นั่ง เที่ยวไป ขบวนที่ {train_info['train_no']} {train_info['train_type']}"),
                    # P(f"{train_info['source']} >> {train_info['destination']}"),
                    # P(f"{train_info['carriage']} : {train_info['carriage_type']} - {train_info['passenger_type']}"),
                    # P(f"วันที่เดินทาง: {train_info['date']} | เวลา: {train_info['departure_time']} - {train_info['arrival_time']}"),
                    # Class="seat-info",
                ),
                Class="seat-container",
            ),

            # ตารางที่นั่ง
            Div(
                *[
                    Div(
                        f"ที่นั่ง {seat['seat_no']}",
                        Class=f"seat {'occupied' if seat['status'] == 'occupied' else 'available'}",
                    )
                    for seat in seat_num["seats"]
                ],
                Class="seat-grid",
            ),

            # ปุ่มยืนยัน
            Div(
                A("ยืนยันการเลือกที่นั่ง", href="/confirm", Class="btn"),
                Class="seat-container",
            ),
        ),
    )

@rt("/login")
def get_login():
    return (
        (
            Div(
                Div(
                    H2("เข้าสู่ระบบ"),
                    Form(
                        Table(
                            Tr(
                                Td(
                                    Label("อีเมล:"), Input(type="email", name="email")
                                ),
                                Td(
                                    Label("รหัสผ่าน:"),
                                    Input(type="password", name="password"),
                                ),               
                            ),    
                        ),
                                Input(type="submit", value="เข้าสู่ระบบ"),
                    ),
                    Button(
                        "Close", onclick="document.getElementById('login').remove()"
                    ),
                    style="""
                        background-color: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px 0 rgba(0,0,0,0.25);
                        min-width: 300px;
                        text-align: center;
                    """,
                ),
                id="login",
                style="""
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.5);  /* โปร่งแสง */
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 1000;
                """,
            ),
        ),
    )


@rt("/register")
def get_register():
    return (
        (
            Div(
                Div(
                    H2("สมัครสมาชิก"),
                    Form(
                        Label(
                            Div(
                                "เพศ  ",
                                Label(
                                    Input(type="radio", name="gender", value="male"),
                                    "ชาย",
                                    Style="display: inline-block; margin-right: 10px;",  # เพิ่มสไตล์ให้ radio อยู่ในบรรทัดเดียวกัน
                                ),
                                Label(
                                    Input(type="radio", name="gender", value="female"),
                                    "หญิง",
                                    Style="display: inline-block; margin-right: 10px;",  # เพิ่มสไตล์ให้ radio อยู่ในบรรทัดเดียวกัน
                                ),
                                Style="margin-bottom: 10px;",  # เพิ่มระยะห่างด้านล่าง
                            ),
                        ),
                        Label(Input(type="text", name="first_name", placeholder="ชื่อ")),
                        Label(
                            Input(type="text", name="last_name", placeholder="นามสกุล")
                        ),
                        Label(
                            Input(
                                type="text", name="id_card", placeholder="เลขบัตรประชาชน"
                            )
                        ),
                        Label(Input(type="email", name="email", placeholder="อีเมล")),
                        Label(
                            Input(
                                type="password", name="password", placeholder="รหัสผ่าน"
                            )
                        ),
                        Label(
                            Input(
                                type="password",
                                name="confirm_password",
                                placeholder="ยืนยันรหัสผ่าน",
                            )
                        ),
                        Input(type="submit", value="สมัครสมาชิก"),
                    ),
                    Button(
                        "ปิด",
                        onclick="document.getElementById('register').remove()",
                    ),
                    style="""
                        background-color: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px 0 rgba(0,0,0,0.25);
                        min-width: 350px;
                        text-align: center;
                    """,
                ),
                id="register",
                style="""
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.5);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 1000;
                """,
            ),
        ),
    )


serve()
