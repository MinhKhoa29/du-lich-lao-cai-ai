import streamlit as st
import json
import os

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Du lịch Lào Cai AI",
    page_icon="🌄",
    layout="wide"
)

# =========================
# STYLE CSS
# =========================
st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #1f4e79;
}

.section-title {
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f0f2f6;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🌄 Ứng dụng Giới thiệu Di tích Lào Cai</div>', unsafe_allow_html=True)
st.divider()

# =========================
# LOAD DATA
# =========================
try:
    with open("data.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)
except Exception as e:
    st.error(f"Lỗi đọc file data.json: {e}")
    st.stop()

data = {k.strip(): v for k, v in raw_data.items()}

# =========================
# MAP ẢNH THEO DI TÍCH
# =========================
images = {
    "Den Thuong Lao Cai": "images/den_thuong.jpg",
    "Den Bao Ha": "images/den_bao_ha.jpg",
    "Den Chieng Ken": "images/den_chieng_ken.jpg",
    "Dinh Fansipan": "images/fansipan.jpg"
}

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🧭 Điều hướng")

selected_place = st.sidebar.selectbox(
    "📍 Chọn di tích",
    list(data.keys())
)

feature = st.sidebar.radio(
    "⚙️ Tính năng",
    ["Giới thiệu", "Chatbot AI", "Tạo lịch trình", "Quiz AI"]
)

place_data = data[selected_place]

# =========================
# GIỚI THIỆU
# =========================
if feature == "Giới thiệu":

    st.markdown(f"<h2 style='color:#d63384;'>📍 {selected_place}</h2>", unsafe_allow_html=True)

    # LẤY ẢNH AN TOÀN
    image_path = images.get(selected_place, "images/default.jpg")

    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("⚠ Không tìm thấy ảnh. Hãy kiểm tra thư mục images.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">📖 Mô tả</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card">{place_data.get("mo_ta", "Chưa có dữ liệu.")}</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title">🏛 Lịch sử</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card">{place_data.get("lich_su", "Chưa có dữ liệu.")}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-title">📌 Địa điểm</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card">{place_data.get("dia_diem", "Chưa có dữ liệu.")}</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title">🌟 Giá trị văn hóa</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card">{place_data.get("gia_tri_van_hoa", "Chưa có dữ liệu.")}</div>', unsafe_allow_html=True)

# =========================
# CÁC TÍNH NĂNG KHÁC
# =========================
elif feature == "Chatbot AI":
    st.info("🤖 Chatbot AI sẽ được tích hợp ở phiên bản tiếp theo.")

elif feature == "Tạo lịch trình":
    st.info("🗺 Tính năng tạo lịch trình sẽ được phát triển tiếp.")

elif feature == "Quiz AI":
    st.info("📝 Quiz AI đang được xây dựng.")