from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from Bookingsystem import Bookingsystem  # นำเข้าระบบจองของคุณ

# สร้างอินสแตนซ์ของ Bookingsystem
booking_system = Bookingsystem()

# สร้างแอป FastAPI
app = FastAPI()

# โมเดลสำหรับรับข้อมูล
class SearchRequest(BaseModel):
    source: str
    destination: str
    date: str

# Endpoint: แสดงสถานีทั้งหมด
@app.get("/stations")
def get_all_stations():
    stations = [station.get_station_name for station in booking_system.show_all_station()]
    if not stations:
        raise HTTPException(status_code=404, detail="ไม่พบสถานี")
    return {"stations": stations}

# Endpoint: ค้นหาเที่ยวรถไฟ
@app.post("/search")
def search_departures(search: SearchRequest):
    result = booking_system.search_departure(search.source, search.destination, search.date)
    if not result:
        raise HTTPException(status_code=404, detail=f"ไม่พบเที่ยวเดินรถจาก {search.source} ไป {search.destination}")
    return {"departures": result}

# Endpoint: เพิ่มสมาชิกใหม่ (ตัวอย่างการใช้งาน Form Data)
@app.post("/add_member")
def add_member(name: str = Form(...)):
    booking_system.add_member(name)
    return {"message": f"สมาชิก {name} ถูกเพิ่มเรียบร้อยแล้ว"}

# Endpoint: ดูตู้ขบวน
@app.get("/train/{train_num}")
def get_train_details(train_num: str):
    carriage_details = booking_system.show_carriage(train_num)
    if not carriage_details:
        raise HTTPException(status_code=404, detail=f"ไม่พบตู้ขบวนสำหรับรถไฟหมายเลข {train_num}")
    return {"carriages": carriage_details}
