import urllib.request
import os
import sys

# Fix Windows terminal encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

plantuml_code = """
@startuml
!theme plain
skinparam backgroundColor transparent
skinparam ArrowColor #444444
skinparam ActivityBorderColor #444444
skinparam ActivityBackgroundColor #EEF4FF
skinparam ActivityDiamondBackgroundColor #FFF5CC
skinparam ActivityDiamondBorderColor #AAAAAA
skinparam SwimlaneBorderColor #AAAAAA
skinparam SwimlaneBackgroundColor #FAFAFA

|Client (Browser)|
start
:Sinh vien nhan "Bat dau thi";
if (JWT hop le?) then (No)
  :Bao loi xac thuc;
  stop
endif
if (Camera duoc cap quyen?) then (No)
  :Yeu cau cap quyen camera;
  stop
endif
fork
  partition "AI Analysis Loop (60 FPS)" {
    repeat
      :Nhan khung hinh tu webcam;
      :Phat hien khuon mat (BlazeFace);
      if (Co khuon mat?) then (No)
        :Ghi nhan "Vang mat";
      else (Yes)
        :Trich xuat 468 diem moc (MediaPipe);
        :Tinh EAR va goc quay dau;
        :Cap nhat Focus Score (Sliding Window);
        :Luu tam vao bo nho (useRef);
      endif
    repeat while (Phien thi dang hoat dong?)
  }
fork again
  partition "Heartbeat Loop (every 5s)" {
    repeat
      :Doi 5 giay;
      :Doc chi so tu bo nho tam;
      :Ky xac thuc HMAC SHA-256;
      :Gui goi tin JSON len Server;

      |Server (Backend)|
      if (Chu ky HMAC hop le?) then (No)
        :Ghi nhan canh bao\ngian lan du lieu;
      else (Yes)
        :Luu ban ghi vao PostgreSQL;
        if (Focus Score thap lien tuc?) then (Yes)
          :Phat sinh thu thach Liveness;

          |Client (Browser)|
          :Hien thi yeu cau cu dong ngau nhien;
          :Dem nguoc 15 giay;
          if (Sinh vien thuc hien dung cu dong?) then (Yes)
            :Gui ket qua thanh cong;
            |Server (Backend)|
            :Ghi nhan Liveness PASSED;
          else (No / Het gio)
            :Gui ket qua that bai;
            |Server (Backend)|
            :Ghi nhan VI PHAM;
            :Thong bao len Dashboard;
          endif
        else (No)
          :Cap nhat trang thai Dashboard;
        endif
      endif
      |Client (Browser)|
    repeat while (Phien thi dang hoat dong?)
  }
end fork
:Sinh vien nhan "Ket thuc phien";
|Server (Backend)|
:Cap nhat trang thai: COMPLETED;
:Tinh toan Focus Score tong ket;
:Luu bao cao cuoi phien;
stop
@enduml
"""

url = "https://kroki.io/plantuml/png"
req = urllib.request.Request(url, data=plantuml_code.encode('utf-8'), headers={
    'Content-Type': 'text/plain',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})

image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
os.makedirs(image_dir, exist_ok=True)
image_path = os.path.join(image_dir, 'activity_diagram.png')

try:
    with urllib.request.urlopen(req) as response:
        with open(image_path, 'wb') as f:
            f.write(response.read())
    print(f"Done: {image_path}")
except Exception as e:
    print("Error:", e, file=sys.stderr)
