from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from Bookingsystem import Bookingsystem  # นำเข้าระบบจองของคุณ
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from fastapi import Query


# สร้างอินสแตนซ์ของ Bookingsystem
booking_system = Bookingsystem()

# สร้างแอป FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # หรือระบุเฉพาะโดเมน เช่น ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# โมเดลสำหรับรับข้อมูล
class SearchRequest(BaseModel):
    source: str
    destination: str
    date: str

# Endpoint: แสดงสถานีทั้งหมด
@app.get("/stations")
def get_all_stations():
    stations = [station.get_station_name for station in booking_system.show_all_station()]
    return {"stations": stations}


@app.get("/search")
def search_departures(
    source: str,
    destination: str,
    date: str
):
    try:
        datetime.strptime(date, "%Y-%m-%d")  # ตรวจสอบรูปแบบวันที่
    except ValueError:
        raise HTTPException(status_code=400, detail="รูปแบบวันที่ไม่ถูกต้อง (YYYY-MM-DD)")

    result = booking_system.search_departure(source, destination, date)
    if not result:
        raise HTTPException(status_code=404, detail=f"ไม่พบเที่ยวเดินรถจาก {source} ไป {destination}")
    return {"departures": result}



# Endpoint: เพิ่มสมาชิกใหม่ (ตัวอย่างการใช้งาน Form Data)
@app.post("/add_member")
def add_member(name: str = Form(...)):
    booking_system.add_member(name) 
    return {"message": f"สมาชิก {name} ถูกเพิ่มเรียบร้อยแล้ว"}

# Endpoint: ดูตู้ขบวน
@app.get("/train-details/{train_num}")
def get_train_details(train_num: str):
    carriage_details = booking_system.show_carriage(train_num)
    if not carriage_details:
        raise HTTPException(status_code=404, detail=f"ไม่พบตู้ขบวนสำหรับรถไฟหมายเลข {train_num}")
    return {"carriages": carriage_details}


# Endpoint: แสดงที่นั่งทั้งหมดใน Carriage
@app.get("/seats/{train_num}/{carrige_type}")
def get_seats(train_num: str, carrige_type: str):
    seat_details = booking_system.select_seat_in_carriage(train_num, carrige_type)
    if not seat_details:
        raise HTTPException(status_code=404, detail="ไม่พบข้อมูลที่นั่ง")

    # สร้าง JSON response ที่มี seat_id และสถานะ
    seats = [{"seat_id": seat, "status": seat} for seat in seat_details]
    return {"seats": seats}



@app.post("/reserve/{seat_id}")
def reserve_seat(seat_id: int):
    # ดำเนินการจองที่นั่ง
    reserved = booking_system.reserve_seat(seat_id)  # สมมติคุณมีฟังก์ชันนี้ในระบบจอง
    if reserved:
        return {"message": f"Seat {seat_id} reserved successfully"}
    else:
        raise HTTPException(status_code=400, detail=f"Seat {seat_id} is already booked or not available")

