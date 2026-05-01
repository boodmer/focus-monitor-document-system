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

print("Hoan thanh tao cac hinh anh minh hoa!")
