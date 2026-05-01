content = open('d:/graduation-thesis/document/content/ch5.txt', encoding='utf-8').read()

old_refs = """CH5_TITLE|TÀI LIỆU THAM KHẢO
[1] Nguyễn Thanh Thủy (2016). Trí tuệ nhân tạo - Phương pháp và ứng dụng. NXB Khoa học và Kỹ thuật, Hà Nội.
[2] Nguyễn Văn Hùng và Nguyễn Quang Hoan (2019). Ứng dụng mạng nơ-ron tích chập trong nhận dạng biểu cảm khuôn mặt người. Tạp chí Khoa học và Công nghệ, Trường Đại học Công nghiệp Hà Nội, số 50, trang 45–52.
[3] Trần Thị Thu Hà và Lê Đình Duy (2020). Phát hiện trạng thái buồn ngủ của lái xe bằng phương pháp phân tích điểm mốc khuôn mặt thời gian thực. Tạp chí Khoa học Kỹ thuật, Học viện Kỹ thuật Quân sự, số 202, trang 30–38.
[4] Phạm Thị Minh Thư và Nguyễn Đức Minh (2021). Giám sát sinh viên trong kỳ thi trực tuyến sử dụng thị giác máy tính và học sâu. Tạp chí Công nghệ thông tin và Truyền thông, số 15, trang 12–21.
[5] Lugaresi, C., Tang, J., Nash, H., McClanahan, C., Uboweja, E., Hays, M., Zhang, F., Chang, C.L., Yong, M.G., Lee, J. và Grundmann, M. (2019). MediaPipe: A Framework for Building Perception Pipelines. arXiv preprint arXiv:1906.08172.
[6] Soukupová, T. và Čech, J. (2016). Real-Time Eye Blink Detection using Facial Landmarks. Trong Kỷ yếu Hội thảo Computer Vision Winter Workshop lần thứ 21, Rimske Toplice, Slovenia, trang 1–8.
[7] Mühler, V. (2020). face-api.js: JavaScript API for Face Detection and Face Recognition in the Browser Implemented on Top of TensorFlow.js Core. GitHub Repository. Truy xuất từ https://github.com/justadudewhohacks/face-api.js
[8] Schroff, F., Kalenichenko, D. và Philbin, J. (2015). FaceNet: A Unified Embedding for Face Recognition and Clustering. Trong Kỷ yếu Hội nghị IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Boston, MA, trang 815–823.
[9] He, K., Zhang, X., Ren, S. và Sun, J. (2016). Deep Residual Learning for Image Recognition. Trong Kỷ yếu Hội nghị IEEE CVPR, Las Vegas, trang 770–778.
[10] Deng, J., Guo, J., Xue, N. và Zafeiriou, S. (2019). ArcFace: Additive Angular Margin Loss for Deep Face Recognition. Trong Kỷ yếu Hội nghị CVPR, Long Beach, trang 4690–4699.
[11] Goodfellow, I., Bengio, Y. và Courville, A. (2016). Deep Learning. MIT Press, Cambridge, MA.
[12] Chollet, F. (2021). Deep Learning with Python, Second Edition. Manning Publications.
[13] Kingma, D.P. và Ba, J. (2014). Adam: A Method for Stochastic Optimization. arXiv preprint arXiv:1412.6980.
[14] Ekman, P. và Friesen, W.V. (1978). Facial Action Coding System: A Technique for the Measurement of Facial Movement. Consulting Psychologists Press, Palo Alto, CA.
[15] Fielding, R.T. (2000). Architectural Styles and the Design of Network-based Software Architectures. Luận án tiến sĩ, University of California, Irvine.
[16] Tihanyi, S. (2022). FastAPI Framework Documentation. Truy xuất từ https://fastapi.tiangolo.com/
[17] React Documentation (2024). React Official Documentation. Truy xuất từ https://react.dev/
[18] PostgreSQL Global Development Group (2024). PostgreSQL 16 Documentation. Truy xuất từ https://www.postgresql.org/docs/16/
[19] pgvector Contributors (2024). pgvector: Open-source Vector Similarity Search for Postgres. GitHub Repository. Truy xuất từ https://github.com/pgvector/pgvector
[20] MDN Web Docs (2024). WebAssembly Concepts. Truy xuất từ https://developer.mozilla.org/en-US/docs/WebAssembly/Concepts
[21] Google Developers (2024). MediaPipe Solutions Guide. Truy xuất từ https://developers.google.com/mediapipe/solutions/guide"""

new_refs = """CH5_TITLE|TÀI LIỆU THAM KHẢO
[1] Nguyễn Thanh Thủy (2016). Trí tuệ nhân tạo - Phương pháp và ứng dụng. NXB Khoa học và Kỹ thuật, Hà Nội.
[2] Nguyễn Văn Hùng và Nguyễn Quang Hoan (2019). Ứng dụng mạng nơ-ron tích chập trong nhận dạng biểu cảm khuôn mặt người. Tạp chí Khoa học và Công nghệ, Trường Đại học Công nghiệp Hà Nội, số 50, trang 45–52.
[3] Phạm Thị Minh Thư và Nguyễn Đức Minh (2021). Giám sát sinh viên trong kỳ thi trực tuyến sử dụng thị giác máy tính và học sâu. Tạp chí Công nghệ thông tin và Truyền thông, số 15, trang 12–21.
[4] Lugaresi, C., Tang, J., Nash, H. và Grundmann, M. (2019). MediaPipe: A Framework for Building Perception Pipelines. arXiv preprint arXiv:1906.08172.
[5] Soukupová, T. và Čech, J. (2016). Real-Time Eye Blink Detection using Facial Landmarks. Trong Kỷ yếu Hội thảo Computer Vision Winter Workshop lần thứ 21, Rimske Toplice, Slovenia, trang 1–8.
[6] Schroff, F., Kalenichenko, D. và Philbin, J. (2015). FaceNet: A Unified Embedding for Face Recognition and Clustering. Trong Kỷ yếu Hội nghị IEEE CVPR, Boston, MA, trang 815–823.
[7] He, K., Zhang, X., Ren, S. và Sun, J. (2016). Deep Residual Learning for Image Recognition. Trong Kỷ yếu Hội nghị IEEE CVPR, Las Vegas, trang 770–778.
[8] Ekman, P. và Friesen, W.V. (1978). Facial Action Coding System: A Technique for the Measurement of Facial Movement. Consulting Psychologists Press, Palo Alto, CA.
[9] Goodfellow, I., Bengio, Y. và Courville, A. (2016). Deep Learning. MIT Press, Cambridge, MA.
[10] Kingma, D.P. và Ba, J. (2014). Adam: A Method for Stochastic Optimization. arXiv preprint arXiv:1412.6980.
[11] Fielding, R.T. (2000). Architectural Styles and the Design of Network-based Software Architectures. Luận án tiến sĩ, University of California, Irvine.
[12] Tihanyi, S. (2022). FastAPI Framework Documentation. Truy xuất từ https://fastapi.tiangolo.com/
[13] pgvector Contributors (2024). pgvector: Open-source Vector Similarity Search for Postgres. GitHub Repository. Truy xuất từ https://github.com/pgvector/pgvector
[14] Mühler, V. (2020). face-api.js: JavaScript API for Face Detection and Face Recognition in the Browser. GitHub Repository. Truy xuất từ https://github.com/justadudewhohacks/face-api.js
[15] MDN Web Docs (2024). WebAssembly Concepts. Truy xuất từ https://developer.mozilla.org/en-US/docs/WebAssembly/Concepts"""

if old_refs in content:
    content = content.replace(old_refs, new_refs)
    open('d:/graduation-thesis/document/content/ch5.txt', 'w', encoding='utf-8').write(content)
    print("SUCCESS")
else:
    print("NOT FOUND - checking...")
    idx = content.find("CH5_TITLE|TÀI LIỆU")
    print(f"Found at index: {idx}")
    print(repr(content[idx:idx+100]))
