import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

IMG_DIR = r"d:\graduation-thesis\document\images"
os.makedirs(IMG_DIR, exist_ok=True)

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(0, 12)
ax.set_ylim(0, 11)
ax.axis('off')
fig.patch.set_facecolor('#ffffff') # Pure white background

def draw_box(ax, x, y, w, h, text, shape='rect', bg_color='#ffffff', edge_color='#333333', text_color='#333333'):
    x0 = x - w/2
    y0 = y - h/2
    
    # Draw drop shadow for a premium look
    shadow_offset = 0.08
    if shape == 'rect':
        shadow = patches.Rectangle((x0+shadow_offset, y0-shadow_offset), w, h, linewidth=0, facecolor='black', alpha=0.1, zorder=1)
        patch = patches.Rectangle((x0, y0), w, h, linewidth=1.5, edgecolor=edge_color, facecolor=bg_color, zorder=2)
    elif shape == 'db':
        # Shadow
        shadow = patches.PathPatch(
            plt.matplotlib.path.Path(
                [(x0+shadow_offset, y0+h-shadow_offset), (x0+w+shadow_offset, y0+h-shadow_offset), 
                 (x0+w+shadow_offset, y0-shadow_offset), (x0+shadow_offset, y0-shadow_offset), (x0+shadow_offset, y0+h-shadow_offset)],
                [1, 2, 2, 2, 2]
            ), linewidth=0, facecolor='black', alpha=0.1, zorder=1)
        # Cylinder simplified
        patch = patches.PathPatch(
            plt.matplotlib.path.Path(
                [(x0, y0+h), (x0+w, y0+h), (x0+w, y0), (x0, y0), (x0, y0+h)],
                [1, 2, 2, 2, 2]
            ), linewidth=1.5, edgecolor=edge_color, facecolor=bg_color, zorder=2)
    elif shape == 'diamond':
        shadow = patches.Polygon([[x+shadow_offset, y+h/2-shadow_offset], [x+w/2+shadow_offset, y-shadow_offset], 
                                  [x+shadow_offset, y-h/2-shadow_offset], [x-w/2+shadow_offset, y-shadow_offset]], 
                                linewidth=0, facecolor='black', alpha=0.1, zorder=1)
        patch = patches.Polygon([[x, y+h/2], [x+w/2, y], [x, y-h/2], [x-w/2, y]], 
                                linewidth=1.5, edgecolor=edge_color, facecolor=bg_color, zorder=2)
    elif shape == 'round':
        shadow = patches.FancyBboxPatch((x0+shadow_offset, y0-shadow_offset), w, h, boxstyle="round,pad=0.1", 
                                       linewidth=0, facecolor='black', alpha=0.1, zorder=1)
        patch = patches.FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.1", 
                                       linewidth=1.5, edgecolor=edge_color, facecolor=bg_color, zorder=2)
        
    ax.add_patch(shadow)
    ax.add_patch(patch)
    
    # Handle multi-line text alignment
    ax.text(x, y, text, ha='center', va='center', fontsize=11, weight='bold', color=text_color, zorder=3)
    
    return (x, y+h/2), (x, y-h/2), (x-w/2, y), (x+w/2, y) # top, bottom, left, right

def draw_arrow(ax, pt1, pt2, text=None, text_offset=(0,0)):
    # Draw simple straight arrow
    ax.annotate("", xy=pt2, xytext=pt1, arrowprops=dict(arrowstyle="->", color='#666666', lw=2), zorder=1)
    if text:
        mid_x = (pt1[0] + pt2[0])/2 + text_offset[0]
        mid_y = (pt1[1] + pt2[1])/2 + text_offset[1]
        ax.text(mid_x, mid_y, text, ha='center', va='center', fontsize=10, weight='bold', color='#175b82',
                bbox=dict(facecolor='#ffffff', edgecolor='#175b82', boxstyle='round,pad=0.2', alpha=1), zorder=3)

def draw_ortho_arrow(ax, pt1, pt2, text=None):
    # Draw orthogonal line (down then horizontal then down)
    mid_y = (pt1[1] + pt2[1]) / 2
    ax.plot([pt1[0], pt1[0]], [pt1[1], mid_y], color='#666666', lw=2, zorder=1)
    ax.plot([pt1[0], pt2[0]], [mid_y, mid_y], color='#666666', lw=2, zorder=1)
    ax.annotate("", xy=pt2, xytext=(pt2[0], mid_y), arrowprops=dict(arrowstyle="->", color='#666666', lw=2), zorder=1)
    if text:
        ax.text((pt1[0] + pt2[0])/2, mid_y, text, ha='center', va='center', fontsize=10, weight='bold', color='#175b82',
                bbox=dict(facecolor='#ffffff', edgecolor='#175b82', boxstyle='round,pad=0.2', alpha=1), zorder=3)

# Define Corporate Colors
c_blue_bg = '#e1f0fa'
c_blue_ed = '#175b82'
c_green_bg = '#e8f5e9'
c_green_ed = '#2e7d32'
c_yellow_bg = '#fff9c4'
c_yellow_ed = '#f57f17'
c_red_bg = '#ffebee'
c_red_ed = '#c62828'
c_gray_bg = '#f5f5f5'
c_gray_ed = '#616161'

# Nodes
nodes = {
    'A': {'pos': (3.5, 10), 'size': (3.5, 0.9), 'text': "Khung hình Webcam\n(Tốc độ 60 FPS)", 'shape': 'round', 'bg': c_gray_bg, 'ec': c_gray_ed},
    'B': {'pos': (3.5, 8.5), 'size': (3.5, 0.9), 'text': "Phát hiện khuôn mặt\n(Mô hình BlazeFace)", 'shape': 'rect', 'bg': c_blue_bg, 'ec': c_blue_ed},
    'C': {'pos': (3.5, 7), 'size': (3.5, 0.9), 'text': "Trích xuất đặc trưng\n(Mạng ResNet-34)", 'shape': 'rect', 'bg': c_blue_bg, 'ec': c_blue_ed},
    'D': {'pos': (3.5, 5.5), 'size': (3.5, 0.9), 'text': "[ Vector khuôn mặt ]\nHiện tại (D=256)", 'shape': 'rect', 'bg': c_yellow_bg, 'ec': c_yellow_ed},
    
    'DB': {'pos': (8.5, 8.5), 'size': (3, 1.2), 'text': "Cơ sở dữ liệu\nPostgreSQL\n(Bảo mật cao)", 'shape': 'db', 'bg': c_gray_bg, 'ec': c_gray_ed},
    'E': {'pos': (8.5, 5.5), 'size': (3.5, 0.9), 'text': "[ Vector danh tính ]\nGốc (Baseline)", 'shape': 'rect', 'bg': c_yellow_bg, 'ec': c_yellow_ed},
    
    'F': {'pos': (6, 3.8), 'size': (4.5, 0.9), 'text': "Thuật toán đối chiếu\n(Tính khoảng cách Euclidean)", 'shape': 'rect', 'bg': c_blue_bg, 'ec': c_blue_ed},
    
    'G': {'pos': (6, 2), 'size': (3.5, 1.2), 'text': "Khoảng cách\n< Ngưỡng 0.6?", 'shape': 'diamond', 'bg': c_yellow_bg, 'ec': c_yellow_ed},
    
    'H': {'pos': (3, 0.5), 'size': (3, 0.9), 'text': "Xác thực hợp lệ\n(Đúng người)", 'shape': 'round', 'bg': c_green_bg, 'ec': c_green_ed},
    'I': {'pos': (9, 0.5), 'size': (3, 0.9), 'text': "Cảnh báo vi phạm\n(Sai người)", 'shape': 'round', 'bg': c_red_bg, 'ec': c_red_ed},
}

anchors = {}
for k, v in nodes.items():
    anchors[k] = draw_box(ax, v['pos'][0], v['pos'][1], v['size'][0], v['size'][1], v['text'], v['shape'], v['bg'], v['ec'])

# Edges
draw_arrow(ax, anchors['A'][1], anchors['B'][0])
draw_arrow(ax, anchors['B'][1], anchors['C'][0])
draw_arrow(ax, anchors['C'][1], anchors['D'][0])

draw_arrow(ax, anchors['DB'][1], anchors['E'][0], "Truy xuất")

# D -> F
draw_ortho_arrow(ax, anchors['D'][1], anchors['F'][0])

# E -> F
draw_ortho_arrow(ax, anchors['E'][1], anchors['F'][0])

draw_arrow(ax, anchors['F'][1], anchors['G'][0])

# G -> H (Có)
draw_ortho_arrow(ax, anchors['G'][2], anchors['H'][0], "Đúng")

# G -> I (Không)
draw_ortho_arrow(ax, anchors['G'][3], anchors['I'][0], "Sai")

# Không chèn title vào trong ảnh để Word/LaTeX tự sinh caption ở dưới
plt.savefig(os.path.join(IMG_DIR, 'face_biometric_auth.png'), dpi=300, bbox_inches='tight')
print("Da tao xong So do khoi bang Matplotlib (Giao dien nang cao)!")
