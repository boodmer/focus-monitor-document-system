import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

IMG_DIR = r"d:\graduation-thesis\document\images"
os.makedirs(IMG_DIR, exist_ok=True)

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')
# Set background color to match dbdiagram's light theme
fig.patch.set_facecolor('#ffffff')

# Hàm vẽ bảng giao diện giống dbdiagram
def draw_table(ax, x, y, title, columns):
    h = 0.5 + len(columns) * 0.45
    w = 4.2
    y_start = y - h
    
    # Draw shadow
    shadow = patches.Rectangle((x+0.05, y_start-0.05), w, h, linewidth=0, facecolor='black', alpha=0.1)
    ax.add_patch(shadow)
    
    # Draw title box (Dark blue)
    rect_title = patches.Rectangle((x, y - 0.5), w, 0.5, linewidth=1, edgecolor='#175b82', facecolor='#175b82')
    ax.add_patch(rect_title)
    ax.text(x + 0.2, y - 0.25, title, ha='left', va='center', weight='bold', color='white', fontsize=12)
    
    # Draw body box (Light gray)
    rect_body = patches.Rectangle((x, y_start), w, h - 0.5, linewidth=1, edgecolor='#d0d4dc', facecolor='#ffffff')
    ax.add_patch(rect_body)
    
    # Draw text
    for i, col in enumerate(columns):
        # Split col name and type
        parts = col.split(' : ')
        col_name = parts[0]
        col_type = parts[1] if len(parts) > 1 else ""
        
        # Determine if it's a key
        is_pk = '(PK)' in col_name
        is_fk = '(FK)' in col_name
        
        if is_pk:
            col_name = col_name.replace('* ', '').replace(' (PK)', '').strip()
            icon = 'PK'
            font_weight = 'bold'
            color = '#333333'
        elif is_fk:
            col_name = col_name.replace('* ', '').replace(' (FK)', '').strip()
            icon = 'FK'
            font_weight = 'normal'
            color = '#0055cc'
        else:
            icon = ''
            font_weight = 'normal'
            color = '#333333'
            
        # Draw PK/FK label
        ax.text(x + 0.15, y - 0.5 - 0.45*i - 0.25, icon, ha='left', va='center', fontsize=10, weight='bold', color=color)
        
        # Draw column name (Căn lề chuẩn xác tại x + 0.6)
        ax.text(x + 0.6, y - 0.5 - 0.45*i - 0.25, col_name, ha='left', va='center', fontsize=11, weight=font_weight, color=color)
        
        # Draw column type aligned right
        ax.text(x + w - 0.2, y - 0.5 - 0.45*i - 0.25, col_type, ha='right', va='center', fontsize=10, color='#888888')
        
    return {
        'top': (x + w/2, y),
        'bottom': (x + w/2, y_start),
        'left': (x, y - h/2),
        'right': (x + w, y - h/2),
        'x': x,
        'y': y,
        'w': w,
        'h': h
    }

# Định nghĩa các bảng
tables = {
    'users': {
        'pos': (0.5, 11), 
        'cols': ['* id (PK) : UUID', 'username : VARCHAR', 'password_hash : VARCHAR', 'role : ENUM']
    },
    'biometric_profiles': {
        'pos': (0.5, 6), 
        'cols': ['* user_id (PK) (FK) : UUID', 'baseline_embedding : VECTOR(256)']
    },
    'sessions': {
        'pos': (6, 11), 
        'cols': ['* id (PK) : UUID', '* user_id (FK) : UUID', 'status : ENUM', 'start_time : TIMESTAMP', 'end_time : TIMESTAMP']
    },
    'heartbeat_logs': {
        'pos': (6, 6), 
        'cols': ['* id (PK) : UUID', '* session_id (FK) : UUID', 'timestamp : TIMESTAMP', 'focus_score : FLOAT', 'blink_rate : INT', 'head_pose : VARCHAR', 'emotion : VARCHAR', 'violations : JSONB']
    },
    'violations': {
        'pos': (11.5, 11), 
        'cols': ['* id (PK) : UUID', '* session_id (FK) : UUID', 'type : VARCHAR', 'severity : ENUM']
    },
    'challenges': {
        'pos': (11.5, 6), 
        'cols': ['* id (PK) : UUID', '* session_id (FK) : UUID', 'issued_at : TIMESTAMP', 'expires_at : TIMESTAMP', 'result : ENUM']
    }
}

anchors = {}
for name, data in tables.items():
    anchors[name] = draw_table(ax, data['pos'][0], data['pos'][1], name, data['cols'])

def draw_ortho_line(ax, pt1, pt2, text):
    # Vẽ đường gấp khúc vuông góc
    mid_x = (pt1[0] + pt2[0]) / 2
    
    # Tạo 3 đoạn thẳng
    ax.plot([pt1[0], mid_x], [pt1[1], pt1[1]], color='#888888', lw=1.5)
    ax.plot([mid_x, mid_x], [pt1[1], pt2[1]], color='#888888', lw=1.5)
    ax.plot([mid_x, pt2[0]], [pt2[1], pt2[1]], color='#888888', lw=1.5)
    
    # Vẽ mũi tên ở cuối
    ax.annotate("", xy=pt2, xytext=(pt2[0]-0.1, pt2[1]), arrowprops=dict(arrowstyle="->", color='#888888', lw=1.5))
    
    # Viết text
    ax.text(mid_x, (pt1[1] + pt2[1])/2, text, ha='center', va='center', color='#175b82', fontsize=10, weight='bold', 
            bbox=dict(facecolor='#ffffff', edgecolor='#175b82', boxstyle='round,pad=0.2', alpha=1))

# Vẽ liên kết
# users -> sessions
draw_ortho_line(ax, anchors['users']['right'], anchors['sessions']['left'], "1 : N")

# sessions -> violations
draw_ortho_line(ax, anchors['sessions']['right'], anchors['violations']['left'], "1 : N")

# users -> biometric_profiles (vertical)
pt1 = (anchors['users']['left'][0] + 1, anchors['users']['bottom'][1])
pt2 = (anchors['biometric_profiles']['left'][0] + 1, anchors['biometric_profiles']['top'][1])
ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='#888888', lw=1.5)
ax.annotate("", xy=pt2, xytext=(pt2[0], pt2[1]+0.1), arrowprops=dict(arrowstyle="->", color='#888888', lw=1.5))
ax.text(pt1[0], (pt1[1] + pt2[1])/2, "1 : 1", ha='center', va='center', color='#175b82', fontsize=10, weight='bold', 
        bbox=dict(facecolor='#ffffff', edgecolor='#175b82', boxstyle='round,pad=0.2', alpha=1))

# sessions -> heartbeat_logs (vertical)
pt1 = (anchors['sessions']['left'][0] + 1, anchors['sessions']['bottom'][1])
pt2 = (anchors['heartbeat_logs']['left'][0] + 1, anchors['heartbeat_logs']['top'][1])
ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='#888888', lw=1.5)
ax.annotate("", xy=pt2, xytext=(pt2[0], pt2[1]+0.1), arrowprops=dict(arrowstyle="->", color='#888888', lw=1.5))
ax.text(pt1[0], (pt1[1] + pt2[1])/2, "1 : N", ha='center', va='center', color='#175b82', fontsize=10, weight='bold', 
        bbox=dict(facecolor='#ffffff', edgecolor='#175b82', boxstyle='round,pad=0.2', alpha=1))

# sessions -> challenges
draw_ortho_line(ax, (anchors['sessions']['right'][0], anchors['sessions']['right'][1]-1), anchors['challenges']['left'], "1 : N")

plt.savefig(os.path.join(IMG_DIR, 'erd_diagram.png'), dpi=300, bbox_inches='tight')
print("Da tao xong hinh erd_diagram.png giao dien chuan!")
