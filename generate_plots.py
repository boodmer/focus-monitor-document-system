import matplotlib.pyplot as plt
import numpy as np
import os

IMG_DIR = r"d:\graduation-thesis\document\images"
os.makedirs(IMG_DIR, exist_ok=True)

# 1. Đồ thị hàm ReLU
plt.figure(figsize=(6, 4))
z = np.linspace(-5, 5, 100)
f_z = np.maximum(0, z)
plt.plot(z, f_z, 'b-', linewidth=2, label='f(z) = max(0, z)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title('Hàm kích hoạt ReLU (Rectified Linear Unit)', fontsize=14)
plt.xlabel('z', fontsize=12)
plt.ylabel('f(z)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'relu_activation.png'), dpi=300)
plt.close()

# 2. Đồ thị Gradient Descent
plt.figure(figsize=(6, 4))
w = np.linspace(-4, 4, 100)
L = w**2
plt.plot(w, L, 'k-', linewidth=2, label='Hàm mất mát L(w)')
# Arrows
w_points = [3.5, 2.5, 1.5, 0.5]
for i in range(len(w_points)-1):
    w1, w2 = w_points[i], w_points[i+1]
    plt.annotate('', xy=(w2, w2**2), xytext=(w1, w1**2),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8))
plt.scatter(0, 0, color='green', s=100, zorder=5, label='Điểm tối ưu (Minimum)')
plt.title('Quá trình tối ưu hóa Gradient Descent', fontsize=14)
plt.xlabel('Trọng số (Weight w)', fontsize=12)
plt.ylabel('Mất mát (Loss L)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'gradient_descent.png'), dpi=300)
plt.close()

# 3. Minh họa Anchor boxes cơ bản
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
# Draw grid
for x in range(11):
    ax.axvline(x, color='gray', linestyle=':', alpha=0.5)
    ax.axhline(x, color='gray', linestyle=':', alpha=0.5)

# Draw a cell center
cx, cy = 5.5, 5.5
ax.plot(cx, cy, 'ro', markersize=8, label='Tâm ô lưới (Grid cell center)')
# Draw anchor boxes
import matplotlib.patches as patches
anchors = [
    patches.Rectangle((cx-1, cy-1), 2, 2, fill=False, edgecolor='blue', linewidth=2, label='Anchor 1 (Tỷ lệ 1:1)'),
    patches.Rectangle((cx-1.5, cy-0.75), 3, 1.5, fill=False, edgecolor='green', linewidth=2, linestyle='--', label='Anchor 2 (Tỷ lệ 2:1)')
]
for a in anchors:
    ax.add_patch(a)
    
ax.set_title('Minh họa Anchor Boxes trong Single Shot Detector', fontsize=14)
ax.legend(loc='lower left', fontsize=10)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'anchor_boxes.png'), dpi=300)
plt.close()

# 4. Ma trận nhầm lẫn (Confusion Matrix)
import itertools

# Tổng số 300 mẫu (150 Tập trung, 100 Mất tập trung, 50 Buồn ngủ)
cm = np.array([[144,   5,   1],
               [  4,  92,   4],
               [  1,   3,  46]])
classes = ['Tập trung', 'Mất tập trung', 'Buồn ngủ']

plt.figure(figsize=(6, 5))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Ma trận nhầm lẫn phân loại trạng thái', fontsize=14)
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

fmt = 'd'
thresh = cm.max() / 2.
for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, format(cm[i, j], fmt),
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black",
             fontsize=12, fontweight='bold')

plt.ylabel('Thực tế (Ground Truth)', fontsize=12)
plt.xlabel('Dự đoán (Predicted)', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'confusion_matrix_final.png'), dpi=300)
plt.close()

# 5. Biểu đồ diễn biến Focus Score
plt.figure(figsize=(10, 4))
time_steps = np.arange(0, 180) # 3 phút (180 giây)
# Giả lập Focus Score: Tập trung cao -> Giảm (Mất tập trung) -> Phục hồi -> Buồn ngủ
np.random.seed(42)
focus_score = np.ones(180) * 95 # Base
focus_score[:60] += np.random.normal(0, 2, 60) # 0-1 mins: Tập trung
focus_score[60:90] = np.linspace(95, 45, 30) + np.random.normal(0, 5, 30) # 1-1.5 mins: Mất tập trung
focus_score[90:120] = np.linspace(45, 90, 30) + np.random.normal(0, 3, 30) # 1.5-2 mins: Phục hồi
focus_score[120:180] = np.linspace(90, 30, 60) + np.random.normal(0, 4, 60) # 2-3 mins: Buồn ngủ

focus_score = np.clip(focus_score, 0, 100)

plt.plot(time_steps, focus_score, 'b-', linewidth=2, label='Điểm tập trung (Focus Score)')
plt.axhline(60, color='r', linestyle='--', linewidth=1.5, label='Ngưỡng cảnh báo (Threshold = 60)')

plt.fill_between(time_steps, 0, 100, where=(time_steps >= 60) & (time_steps <= 90), color='orange', alpha=0.2, label='Giai đoạn Mất tập trung')
plt.fill_between(time_steps, 0, 100, where=(time_steps >= 120), color='gray', alpha=0.2, label='Giai đoạn Buồn ngủ')

plt.title('Biểu đồ diễn biến mức độ tập trung theo thời gian thực', fontsize=14)
plt.xlabel('Thời gian (giây)', fontsize=12)
plt.ylabel('Điểm số (0-100)', fontsize=12)
plt.ylim(0, 110)
plt.legend(loc='lower left')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'evaluation_chart.png'), dpi=300)
plt.close()

print("Hoan thanh tao cac hinh anh minh hoa va bieu do danh gia!")
