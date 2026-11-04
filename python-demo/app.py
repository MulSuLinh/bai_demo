from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Python Demo Lab", page_icon="🐍", layout="wide")

TOPICS = [
    "Biến & kiểu dữ liệu", "Điều kiện", "Chuỗi", "List & Tuple",
    "Vòng lặp", "Hàm", "Dict & Set", "Files & JSON",
    "Xử lý ngoại lệ", "OOP cơ bản",
]

st.sidebar.title("🐍 Python Demo Lab")
st.sidebar.caption("Góc thực hành Python tương tác")
page = st.sidebar.radio("Điều hướng", ["Trang chủ", "Phòng thực hành", "Lộ trình học", "Giới thiệu"])

def home() -> None:
    st.title("Học Python bằng thực hành")
    st.write("Chào mừng bạn đến với Python Demo Lab — nơi bạn có thể thay đổi dữ liệu và xem kết quả Python ngay trên website.")
    a, b, c = st.columns(3)
    a.metric("Chủ đề", "10")
    b.metric("Ví dụ tương tác", "8")
    c.metric("Ngôn ngữ", "Python")
    st.divider()
    st.subheader("Bắt đầu từ đâu?")
    st.markdown(
        "- **Phòng thực hành:** chọn ví dụ, thay đổi đầu vào và quan sát kết quả.\n"
        "- **Lộ trình học:** xem thứ tự các chủ đề nên học.\n"
        "- **Tự thử:** mỗi ví dụ có đoạn code minh họa để bạn đối chiếu."
    )
    st.info("Chọn **Phòng thực hành** ở thanh bên để bắt đầu.")

def playground() -> None:
    st.title("🧪 Phòng thực hành")
    demo = st.selectbox("Chọn bài demo", [
        "Máy tính", "Xếp loại điểm", "Đếm từ trong văn bản", "Thống kê danh sách",
        "Mô phỏng vòng lặp", "Tra cứu Dict", "Hàm giảm giá", "Tạo JSON",
    ])

    if demo == "Máy tính":
        st.subheader("Demo 1 · Biến, kiểu dữ liệu và phép toán")
        left, right = st.columns(2)
        x = left.number_input("Số thứ nhất", value=12.0)
        y = right.number_input("Số thứ hai", value=3.0)
        op = st.selectbox("Phép toán", ["Cộng", "Trừ", "Nhân", "Chia"])
        if op == "Cộng":
            result, expression = x + y, f"{x} + {y}"
        elif op == "Trừ":
            result, expression = x - y, f"{x} - {y}"
        elif op == "Nhân":
            result, expression = x * y, f"{x} * {y}"
        else:
            result, expression = (None, f"{x} / {y}") if y == 0 else (x / y, f"{x} / {y}")
        st.code(f"result = {expression}", language="python")
        st.metric("Kết quả", "Không xác định (chia cho 0)" if result is None else f"{result:g}")

    elif demo == "Xếp loại điểm":
        st.subheader("Demo 2 · Câu lệnh điều kiện")
        score = st.slider("Điểm của bạn", 0, 100, 78)
        if score >= 90:
            grade = "Xuất sắc"
        elif score >= 80:
            grade = "Giỏi"
        elif score >= 65:
            grade = "Khá"
        elif score >= 50:
            grade = "Trung bình"
        else:
            grade = "Cần cố gắng"
        st.code("if score >= 90:\n    grade = 'Xuất sắc'\nelif score >= 80:\n    grade = 'Giỏi'\nelif score >= 65:\n    grade = 'Khá'\nelse:\n    grade = 'Cần cố gắng'", language="python")
        st.success(f"{score}/100 · {grade}")

    elif demo == "Đếm từ trong văn bản":
        st.subheader("Demo 3 · Xử lý chuỗi")
        sentence = st.text_area("Nhập văn bản", "Python rất thú vị. Học Python bằng cách thực hành!")
        words = re.findall(r"\w+", sentence.lower(), flags=re.UNICODE)
        counts = Counter(words)
        st.code("words = re.findall(r'\\w+', text.lower())\ncounts = Counter(words)", language="python")
        a, b = st.columns(2)
        a.metric("Tổng số từ", len(words))
        b.metric("Số từ khác nhau", len(counts))
        if counts:
            st.bar_chart(dict(counts.most_common(10)))
            st.dataframe([{"Từ": k, "Số lần": v} for k, v in counts.most_common()], use_container_width=True)

    elif demo == "Thống kê danh sách":
        st.subheader("Demo 4 · List và thống kê")
        raw = st.text_input("Nhập các số, phân tách bằng dấu phẩy", "12, 8, 15, 20, 5")
        try:
            values = [float(part.strip()) for part in raw.split(",") if part.strip()]
            if not values:
                raise ValueError
            st.code("numbers = [12, 8, 15, 20, 5]\nmaximum = max(numbers)\naverage = sum(numbers) / len(numbers)", language="python")
            a, b, c = st.columns(3)
            a.metric("Số phần tử", len(values))
            b.metric("Lớn nhất", f"{max(values):g}")
            c.metric("Trung bình", f"{sum(values) / len(values):.2f}")
            st.write("Sau khi sắp xếp:", sorted(values))
        except ValueError:
            st.error("Vui lòng nhập ít nhất một số hợp lệ.")

    elif demo == "Mô phỏng vòng lặp":
        st.subheader("Demo 5 · Vòng lặp for")
        limit = st.slider("Lặp từ 1 đến", 1, 30, 5)
        values = list(range(1, limit + 1))
        st.code(f"for number in range(1, {limit + 1}):\n    print(number)", language="python")
        st.write("Các giá trị:", values)
        st.metric("Tổng", sum(values))
        st.dataframe([{"Lần lặp": i, "Giá trị": n, "Tổng tích lũy": sum(values[:i])} for i, n in enumerate(values, 1)])

    elif demo == "Tra cứu Dict":
        st.subheader("Demo 6 · Dictionary")
        students = {
            "An": {"Python": 8.5, "Git": 7.0},
            "Bình": {"Python": 9.0, "Git": 8.0},
            "Chi": {"Python": 7.5, "Git": 9.5},
        }
        name = st.selectbox("Chọn học viên", list(students))
        st.code("scores = {'An': {'Python': 8.5, 'Git': 7.0}}\npython_score = scores[name]['Python']", language="python")
        st.json(students[name])
        st.metric("Điểm Python", students[name]["Python"])

    elif demo == "Hàm giảm giá":
        st.subheader("Demo 7 · Viết hàm và return")
        price = st.number_input("Giá gốc (VNĐ)", min_value=0, value=200000, step=10000)
        discount = st.slider("Giảm giá (%)", 0, 90, 10)
        def final_price(amount: float, percent: int) -> float:
            return amount * (1 - percent / 100)
        total = final_price(price, discount)
        st.code("def final_price(amount, percent):\n    return amount * (1 - percent / 100)", language="python")
        st.metric("Giá sau giảm", f"{total:,.0f} ₫")

    else:
        st.subheader("Demo 8 · Dict và JSON")
        name = st.text_input("Tên", "Lan")
        age = st.number_input("Tuổi", min_value=1, max_value=120, value=20)
        skills = st.multiselect("Kỹ năng", ["Python", "Git", "SQL", "HTML", "Data"], ["Python", "Git"])
        payload = {"name": name, "age": age, "skills": skills}
        result = json.dumps(payload, ensure_ascii=False, indent=2)
        st.code("json_text = json.dumps(data, ensure_ascii=False, indent=2)", language="python")
        st.json(payload)
        st.download_button("Tải file JSON", result, file_name="student.json", mime="application/json")

def curriculum() -> None:
    st.title("📚 Lộ trình học Python")
    st.write("Thứ tự gợi ý cho người mới bắt đầu. Có thể chọn một chủ đề trong Phòng thực hành để luyện tập.")
    for i, topic in enumerate(TOPICS, 1):
        with st.expander(f"Chủ đề {i:02d} · {topic}"):
            st.write({
                1: "Biến, số, chuỗi, boolean và nhập/xuất dữ liệu.",
                2: "if, elif, else và biểu thức logic.",
                3: "Indexing, slicing, f-string và các phương thức chuỗi.",
                4: "List, tuple, slicing và thao tác dữ liệu tuần tự.",
                5: "for, while, range và vòng lặp lồng nhau.",
                6: "Tham số, giá trị trả về, phạm vi biến và tái sử dụng code.",
                7: "Dictionary, set và dữ liệu key-value.",
                8: "Đọc/ghi tệp, CSV và JSON.",
                9: "try, except, else, finally và tạo exception.",
                10: "Class, object, thuộc tính, phương thức và kế thừa.",
            }[i])

def about() -> None:
    st.title("ℹ️ Giới thiệu")
    st.write("Python Demo Lab là ứng dụng học tập nhỏ được xây dựng bằng Streamlit. Các ví dụ chạy trong ứng dụng và hiển thị kết quả ngay sau khi thay đổi đầu vào.")
    st.warning("Đây là website demo phục vụ học tập, không phải môi trường chạy mã Python tùy ý do người dùng nhập.")
    st.markdown("**Công nghệ:** Python · Streamlit")

if page == "Trang chủ":
    home()
elif page == "Phòng thực hành":
    playground()
elif page == "Lộ trình học":
    curriculum()
else:
    about()

st.sidebar.divider()
st.sidebar.caption("Python Demo Lab · Học bằng thực hành")
