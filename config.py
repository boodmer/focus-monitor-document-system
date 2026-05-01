# config.py
import os

DOC_DIR = r'd:\graduation-thesis\document'
IMG_DIR = os.path.join(DOC_DIR, 'images')
CONTENT_DIR = os.path.join(DOC_DIR, 'content')
OUT_DIR = os.path.join(DOC_DIR, 'out')

META = {
    'department': 'BỘ CÔNG THƯƠNG',
    'university': 'ĐẠI HỌC CÔNG NGHIỆP HÀ NỘI',
    'degree': 'ĐỒ ÁN TỐT NGHIỆP ĐẠI HỌC',
    'major': 'Công nghệ thông tin',
    'title': 'Hệ thống giám sát mức độ tập trung của người dùng dựa trên phân tích hành vi khuôn mặt và cảm xúc sử dụng trí tuệ nhân tạo',
    'supervisor': '.........................................',
    'student_name': 'Nguyễn Quang Minh',
    'student_id': '2024600002',
    'class_name': '2024DHCNTTLT01',
    'cohort': 'K19_LT',
    'location': 'Hà Nội',
    'year': '2026',
    'duration': 'từ 06/04/2026 đến 08/06/2026.',
    'goal': 'Đề tài nhằm giải quyết bài toán đánh giá mức độ tập trung của người dùng trong quá trình học tập và thi cử trực tuyến thông qua phân tích dữ liệu hình ảnh từ webcam.'
}

CHAPTER_FILES = [
    'abstract.txt',
    'ch1.txt',
    'ch2.txt',
    'ch3.txt',
    'ch4.txt',
    'ch5.txt',
    'appendix.txt'
]

ABBREVIATIONS = [
    ('AI', 'Artificial Intelligence – Trí tuệ nhân tạo'),
    ('API', 'Application Programming Interface – Giao diện lập trình ứng dụng'),
    ('ANN', 'Artificial Neural Network – Mạng nơ-ron nhân tạo'),
    ('CEW', 'Closed Eyes In The Wild – Bộ dữ liệu trạng thái mắt chuẩn'),
    ('CNN', 'Convolutional Neural Network – Mạng nơ-ron tích chập'),
    ('CPU', 'Central Processing Unit – Bộ xử lý trung tâm'),
    ('CSDL', 'Cơ sở dữ liệu'),
    ('EAR', 'Eye Aspect Ratio – Tỷ lệ khía cạnh mắt'),
    ('FPS', 'Frames Per Second – Số khung hình mỗi giây'),
    ('GPU', 'Graphics Processing Unit – Bộ xử lý đồ họa'),
    ('HD', 'High Definition – Độ phân giải cao'),
    ('HMAC', 'Hash-based Message Authentication Code – Mã xác thực thông điệp dựa trên hàm băm'),
    ('HNSW', 'Hierarchical Navigable Small World – Thuật toán tìm kiếm láng giềng gần nhất'),
    ('HTTPS', 'HyperText Transfer Protocol Secure – Giao thức truyền tải siêu văn bản bảo mật'),
    ('JWT', 'JSON Web Token – Mã thông báo xác thực JSON'),
    ('LFW', 'Labeled Faces in the Wild – Bộ dữ liệu khuôn mặt chuẩn'),
    ('LTI', 'Learning Tools Interoperability – Khả năng tương tác của công cụ học tập'),
    ('NMS', 'Non-Maximum Suppression – Thuật toán triệt tiêu vĩ đại phi cực đại'),
    ('ORM', 'Object-Relational Mapping – Ánh xạ đối tượng-quan hệ'),
    ('ReLU', 'Rectified Linear Unit – Hàm kích hoạt tuyến tính chỉnh lưu'),
    ('rPPG', 'Remote Photoplethysmography – Đo quang thể tích từ xa'),
    ('SSD', 'Single Shot Detector – Bộ phát hiện đơn bước'),
    ('SUS', 'System Usability Scale – Thang đo khả năng sử dụng hệ thống'),
    ('UI', 'User Interface – Giao diện người dùng'),
    ('UX', 'User Experience – Trải nghiệm người dùng'),
    ('WASM', 'WebAssembly – Định dạng mã máy chạy trên trình duyệt'),
    ('WebRTC', 'Web Real-Time Communication – Giao thức truyền thông thời gian thực trên web'),
]

# Symbols for Word (uses unicode and subscripts)
SYMBOLS_WORD = [
    # --- Ký hiệu toán học cơ bản ---
    ('x, y', 'Vector đầu vào và đầu ra của mạng nơ-ron'),
    ('xᵢ', 'Phần tử thứ i của vector đầu vào'),
    ('wᵢ', 'Trọng số (weight) của kết nối thứ i trong mạng nơ-ron'),
    ('b', 'Hệ số lệch (bias) trong nơ-ron nhân tạo'),
    ('z', 'Tổng có trọng số trước khi áp dụng hàm kích hoạt: z = Σwᵢxᵢ + b'),
    ('f(z)', 'Hàm kích hoạt phi tuyến áp dụng lên z'),
    ('f(z) = max(0, z)', 'Hàm kích hoạt ReLU (Rectified Linear Unit)'),
    ('σ(z)', 'Hàm kích hoạt Sigmoid: σ(z) = 1/(1+e⁻ᶻ)'),
    ('‖.‖', 'Khoảng cách Euclidean giữa hai điểm trong không gian n chiều'),
    # --- Ký hiệu tối ưu hóa ---
    ('L(ŷ, y)', 'Hàm mất mát (Loss Function) đo sai số giữa dự đoán và thực tế'),
    ('∂L/∂w', 'Đạo hàm riêng của hàm mất mát theo trọng số w (Gradient)'),
    ('η (eta)', 'Tốc độ học (learning rate) trong thuật toán tối ưu Adam'),
    ('m₁, m₂', 'Trung bình động bậc 1 và bậc 2 của gradient trong Adam'),
    # --- Ký hiệu EAR và phát hiện khuôn mặt ---
    ('p₁, p₂, ..., p₆', 'Tọa độ 2D của 6 điểm mốc quanh mắt dùng để tính EAR'),
    ('EAR', 'Eye Aspect Ratio – Tỷ lệ khía cạnh mắt: EAR = (‖p₂-p₆‖+‖p₃-p₅‖) / (2‖p₁-p₄‖)'),
    ('EAR_threshold', 'Ngưỡng phân loại mắt nhắm/mở, giá trị chuẩn = 0.20'),
    ('θ (theta)', 'Góc quay đầu (yaw/pitch/roll) so với trục tọa độ camera'),
    # --- Ký hiệu nhận diện khuôn mặt ---
    ('f(x) ∈ ℝ²⁵⁶', 'Vector nhúng khuôn mặt 256 chiều sinh ra bởi mô hình MobileNet'),
    ('d(f(x), f(y))', 'Khoảng cách Euclidean giữa hai vector nhúng khuôn mặt x và y'),
    ('α (alpha)', 'Ngưỡng margin trong Triplet Loss, phân tách mẫu âm và dương'),
    ('L_triplet', 'Hàm mất mát Triplet Loss cho bài toán nhận diện khuôn mặt'),
    ('L_CE', 'Hàm mất mát Cross-Entropy cho bài toán phân loại cảm xúc'),
    # --- Ký hiệu điểm tập trung ---
    ('S_focus', 'Điểm tập trung tổng hợp tại một thời điểm (0–100)'),
    ('W_ear, W_pose, W_emotion', 'Trọng số đóng góp của EAR, góc đầu và cảm xúc vào S_focus'),
    ('N', 'Kích thước cửa sổ trượt (Sliding Window), đơn vị: số heartbeat'),
    ('Σ_N', 'Tổng tích lũy Moving Sum trong cửa sổ N, độ phức tạp O(1)'),
    # --- Ký hiệu độ phức tạp ---
    ('O(1)', 'Độ phức tạp thời gian hằng số, không phụ thuộc kích thước đầu vào'),
    ('O(n)', 'Độ phức tạp thời gian tuyến tính, tỷ lệ với kích thước đầu vào n'),
]

# Symbols for LaTeX (uses LaTeX math mode)
SYMBOLS_LATEX = [
    # --- Ký hiệu toán học cơ bản ---
    ('$x, y$', 'Vector đầu vào và đầu ra của mạng nơ-ron'),
    ('$x_i$', 'Phần tử thứ $i$ của vector đầu vào'),
    ('$w_i$', 'Trọng số (weight) của kết nối thứ $i$ trong mạng nơ-ron'),
    ('$b$', 'Hệ số lệch (bias) trong nơ-ron nhân tạo'),
    ('$z = \\sum w_i x_i + b$', 'Tổng có trọng số trước khi áp dụng hàm kích hoạt'),
    ('$f(z) = \\max(0, z)$', 'Hàm kích hoạt ReLU (Rectified Linear Unit)'),
    ('$\\sigma(z) = 1/(1+e^{-z})$', 'Hàm kích hoạt Sigmoid'),
    ('$\\|.\\|$', 'Khoảng cách Euclidean giữa hai điểm trong không gian $n$ chiều'),
    # --- Ký hiệu tối ưu hóa ---
    ('$L(\\hat{y}, y)$', 'Hàm mất mát đo sai số giữa dự đoán và thực tế'),
    ('$\\partial L / \\partial w$', 'Đạo hàm riêng của hàm mất mát theo trọng số $w$'),
    ('$\\eta$', 'Tốc độ học (learning rate) trong thuật toán tối ưu Adam'),
    ('$m_1, m_2$', 'Trung bình động bậc 1 và bậc 2 của gradient trong Adam'),
    # --- Ký hiệu EAR ---
    ('$p_1, p_2, ..., p_6$', 'Tọa độ 2D của 6 điểm mốc quanh mắt dùng để tính EAR'),
    ('$\\text{EAR} = \\frac{\\|p_2-p_6\\|+\\|p_3-p_5\\|}{2\\|p_1-p_4\\|}$', 'Công thức tính Eye Aspect Ratio'),
    ('$\\text{EAR}_{threshold}$', 'Ngưỡng phân loại mắt nhắm/mở, giá trị chuẩn = 0.20'),
    ('$\\theta$', 'Góc quay đầu (yaw/pitch/roll) so với trục tọa độ camera'),
    # --- Ký hiệu nhận diện khuôn mặt ---
    ('$f(x) \\in \\mathbb{R}^{256}$', 'Vector nhúng khuôn mặt 256 chiều'),
    ('$d(f(x), f(y))$', 'Khoảng cách Euclidean giữa hai vector nhúng khuôn mặt'),
    ('$\\alpha$', 'Ngưỡng margin trong Triplet Loss'),
    ('$L_{\\text{triplet}}$', 'Hàm mất mát Triplet Loss cho nhận diện khuôn mặt'),
    ('$L_{\\text{CE}}$', 'Hàm mất mát Cross-Entropy cho phân loại cảm xúc'),
    # --- Ký hiệu điểm tập trung ---
    ('$S_{focus}$', 'Điểm tập trung tổng hợp tại một thời điểm (0–100)'),
    ('$W_{ear}, W_{pose}, W_{emo}$', 'Trọng số đóng góp của EAR, góc đầu và cảm xúc'),
    ('$N$', 'Kích thước cửa sổ trượt (Sliding Window)'),
    ('$O(1), O(n)$', 'Ký hiệu độ phức tạp thuật toán hằng số và tuyến tính'),
]


STYLES = {
    'normal_size': 14,
    'chapter_title_size': 14,
    'heading2_size': 14,
    'heading3_size': 14,
}
