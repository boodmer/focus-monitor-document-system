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
skinparam usecase {
    BackgroundColor LightBlue
    BorderColor Black
}
skinparam actor {
    BackgroundColor White
    BorderColor Black
}

left to right direction

actor "Sinh viên\\n(Người bị giám sát)" as student
actor "Giảng viên /\\nQuản trị viên" as admin

package "Hệ thống giám sát độ tập trung của người dùng" {
  usecase "Login" as UC_Auth
  
  usecase "Identity Registration" as UC_Enroll
  usecase "Session Management" as UC_Session
  usecase "Heartbeat" as UC_Heartbeat
  usecase "Submit Challenge" as UC_SubmitChallenge
  
  usecase "Live Monitoring" as UC_Live
  usecase "Trigger Challenge" as UC_TriggerChallenge
  usecase "Analytics & History" as UC_Analytics
  usecase "System Configuration" as UC_Config
}

student --> UC_Auth
student --> UC_Enroll
student --> UC_Session
UC_Session *-- UC_Heartbeat : <<include>>
UC_Session *-- UC_SubmitChallenge : <<include>>

admin --> UC_Auth
admin --> UC_Live
admin --> UC_TriggerChallenge
admin --> UC_Analytics
admin --> UC_Config
@enduml
"""

# Kroki API
url = "https://kroki.io/plantuml/png"
req = urllib.request.Request(url, data=plantuml_code.encode('utf-8'), headers={
    'Content-Type': 'text/plain',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})

image_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(image_dir, exist_ok=True)
image_path = os.path.join(image_dir, 'usecase_diagram.png')

try:
    with urllib.request.urlopen(req) as response:
        with open(image_path, 'wb') as f:
            f.write(response.read())
    print(f"Done: {image_path}")
except Exception as e:
    print("Error:", e, file=sys.stderr)
