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

|Trình duyệt (Client)|
start
:Sinh viên nhấn "Bắt đầu thi";
if (JWT còn hiệu lực?) then (Không)
  :Báo lỗi xác thực;
  stop
endif
if (Camera được cấp quyền?) then (Không)
  :Yêu cầu cấp quyền camera;
  stop
endif
fork
  partition "Luồng phân tích AI (60 FPS)" {
    repeat
      :Nhận khung hình từ webcam;
      :Phát hiện khuôn mặt (BlazeFace);
      if (Có khuôn mặt?) then (Không)
        :Ghi nhận "Vắng mặt";
      else (Có)
        :Trích xuất 468 điểm mốc (MediaPipe);
        :Tính EAR và góc quay đầu;
        :Cập nhật Focus Score (Sliding Window);
        :Lưu tạm vào bộ nhớ (useRef);
      endif
    repeat while (Phiên thi đang hoạt động?)
  }
fork again
  partition "Luồng đồng bộ Heartbeat (5 giây)" {
    repeat
      :Đợi 5 giây;
      :Đọc chỉ số từ bộ nhớ tạm;
      :Ký xác thực HMAC SHA-256;
      :Gửi gói tin JSON lên Server;

      |Server (Backend)|
      if (Chữ ký HMAC hợp lệ?) then (Không)
        :Ghi nhận cảnh báo\\ngian lận dữ liệu;
      else (Có)
        :Lưu bản ghi vào PostgreSQL;
        if (Focus Score thấp liên tục?) then (Có)
          :Phát sinh thử thách Liveness;

          |Trình duyệt (Client)|
          :Hiển thị yêu cầu cử động ngẫu nhiên;
          :Đếm ngược 15 giây;
          if (Sinh viên thực hiện đúng?) then (Có)
            :Gửi kết quả thành công;
            |Server (Backend)|
            :Ghi nhận: Liveness PASSED;
          else (Không / Hết giờ)
            :Gửi kết quả thất bại;
            |Server (Backend)|
            :Ghi nhận VI PHẠM;
            :Thông báo lên Dashboard;
          endif
        else (Không)
          :Cập nhật trạng thái Dashboard;
        endif
      endif
      |Trình duyệt (Client)|
    repeat while (Phiên thi đang hoạt động?)
  }
end fork
:Sinh viên nhấn "Kết thúc phiên";
|Server (Backend)|
:Cập nhật trạng thái: COMPLETED;
:Tính toán Focus Score tổng kết;
:Lưu báo cáo cuối phiên;
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
