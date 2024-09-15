import csv
from View import cow,goat
def cow_database(id,  csv_file='model/cow_database.csv'):
    # เปิดไฟล์ CSV และสร้าง reader
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        # ตรวจสอบแต่ละแถวเพื่อดูว่ามี id ที่ป้อนเข้ามาหรือไม่
        for row in reader:
            if row['Id'] == id:
                return row  # คืนค่าข้อมูลแถวที่พบ

    return None  # คืนค่า None ถ้าไม่พบ id

def validInput(id):
    isvalid = True
    # เช็คว่าข้อมูลที่ใส่เข้ามาเป็นตัวเลข 8 ตัวและเริ่มด้วยเลข 0 หรือไม่
    if not id.isdigit() or len(id) != 8 or id[0] == '0':
        isvalid = False
        print("Invalid Id, Please Enter New Id")
        return

    # เช็คว่ามีข้อมูลในฐานข้อมูลหรือไม่
    record = cow_database(id)
    if not cow_database(id):
        isvalid = False
        print("Id not found. Please Enter New Id")
        return  
    
    # ดูประเภทสัตว์ว่า
    animaltype = animal_type(record)
    
def animal_type(record):
    # ดูประเภทสัตว์จาก Udder
    if 'Udder' in record and record['Udder']:  # เช็คว่ามีข้อมูล 'Udder' หรือไม่
        udder_count = int(record['Udder'])
        if udder_count == 3 or udder_count == 4:
            cow.chek_cow(record) 
        else:
            print("Cow might be incomplete. Cannot milk.")
    else :
        goat.chase_goat(record)