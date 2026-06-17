# 🏦 Trợ lý Bank Reconciliation
<img width="200" height="300" alt="image" src="https://github.com/user-attachments/assets/aa5a5019-1f40-42d5-a019-b8e04e4b994a" />

AI Agent chuyên dụng cho việc đối chiếu sao kê ngân hàng và hạch toán kế toán.

## Tính năng
- Đối chiếu tự động sao kê ngân hàng với sổ cái nội bộ.
- Phát hiện các giao dịch chênh lệch/chưa hạch toán.
- Gợi ý định khoản Nợ/Có cho các khoản chi/thu mới.
- Hỗ trợ file CSV, Excel.

## Cấu trúc dự án
- `main.py`: Logic xử lý đối chiếu chính.
- `IDENTITY.md`: Định nghĩa vai trò của Agent.
- `SOUL.md`: Triết lý và nguyên tắc làm việc của Agent.
- `requirements.txt`: Danh sách thư viện Python cần thiết.
- `Dockerfile`: Cấu hình môi trường triển khai.

## Hướng dẫn chạy nhanh
1. Cài đặt dependencies: `pip install -r requirements.txt`
2. Chạy ứng dụng: `python main.py`

## Deployment
Dự án này được thiết kế để chạy trên **GreenNode AgentBase Runtime**.
