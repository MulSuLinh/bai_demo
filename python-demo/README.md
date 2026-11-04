# Python Demo Lab

Ứng dụng Streamlit thực hành Python tương tác, được đặt riêng trong thư mục này để giữ nguyên website Mộc Coffee hiện tại ở thư mục gốc.

## Chạy trên máy tính

Yêu cầu Python 3.10 trở lên.

```bash
cd python-demo
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Cài thư viện và khởi chạy:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Mở địa chỉ được Streamlit hiển thị, thường là http://localhost:8501.

## Deploy lên Internet

1. Đẩy repository lên GitHub.
2. Đăng nhập https://share.streamlit.io/ bằng GitHub.
3. Chọn **Create app**, repository `MulSuLinh/bai_demo`, branch `main`.
4. Đặt **Main file path** là `python-demo/app.py`.
5. Deploy ứng dụng.

Website Mộc Coffee hiện tại ở `index.html` và `quan-ly.html` không bị thay thế. Python Demo Lab là ứng dụng Streamlit riêng, cần chạy/deploy bằng Streamlit Community Cloud; GitHub Pages chỉ phục vụ các trang tĩnh HTML.
