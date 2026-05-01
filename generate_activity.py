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
skinparam backgroundColor white
skinparam ArrowColor #333333
skinparam ActivityBorderColor #5B8DB8
skinparam ActivityBackgroundColor #EFF6FF
skinparam ActivityDiamondBackgroundColor #FFF9C4
skinparam ActivityDiamondBorderColor #F0AD00
skinparam SwimlaneBorderColor #AAAAAA
skinparam defaultFontName Arial
skinparam defaultFontSize 11

|Client|
start
:Bắt đầu thi;

if (JWT + Camera hợp lệ?) then (Không)
  #FFD6D6:Dừng hệ thống;
  stop
endif

fork
  partition "Luồng AI (60 FPS)" {
    repeat
      :Nhận khung hình;

      if (Có khuôn mặt?) then (Có)

        :Trích xuất landmark;
        :Nhận diện khuôn mặt (identity);
        :Nhận diện cảm xúc;

        :Tính EAR + Head pose;
        :Cập nhật Focus Score;

      else (Không)
        :Ghi nhận vắng mặt;
      endif

    repeat while (Phiên đang chạy?)
  }

fork again

  partition "Heartbeat (5 giây)" {
    repeat
      :Gửi dữ liệu lên Server;

      |Server|
      :Lưu dữ liệu;

      if (Vi phạm vượt ngưỡng?) then (Có)
        :Gửi lệnh Logout;
        |Client|
        #FFD6D6:Force logout;
        stop
      endif

      |Client|

      if (Có yêu cầu Liveness?) then (Có)

        :Hiển thị thử thách;
        :Chờ tối đa 30 giây;

        if (Hoàn thành trong thời gian?) then (Có)
          :Gửi kết quả;
        else (Không)
          #FFD6D6:Logout;
          stop
        endif

      endif

    repeat while (Phiên đang chạy?)
  }

end fork

:Kết thúc phiên;

|Server|
:Lưu báo cáo;
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
