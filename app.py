import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="تحليل مباريات كرة القدم", layout="wide")
st.title("تحليل مباريات اليوم وتحليل فرق LaLiga")

# تبويبات
tabs = st.tabs(["مباريات اليوم", "تحليل فرق LaLiga"])

# بيانات تجريبية (ممكن تغيرها لاحقًا)
matches_data = pd.DataFrame({
    "الفريق الأول": ["Real Madrid", "Barcelona", "Atletico Madrid"],
    "الفريق الثاني": ["Valencia", "Sevilla", "Real Betis"],
    "احتمال 1": [0.81, 0.76, 0.64],
    "احتمال تعادل": [0.12, 0.18, 0.25],
    "احتمال 2": [0.07, 0.06, 0.11],
    "التوقع": ["1", "1", "1"]
})

laliga_data = pd.DataFrame({
    "الفريق": ["Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla"],
    "متوسط xG هجومي": [2.1, 2.0, 1.8, 1.5],
    "متوسط xG دفاعي": [0.9, 1.1, 1.2, 1.3],
    "نتائج آخر 5 مباريات": ["4V-0D-1L", "3V-2D-0L", "2V-1D-2L", "2V-2D-1L"]
})

# دالة تلوين النتائج
def highlight_prob(val):
    if val >= 0.80:
        color = '#90EE90'  # أخضر فاتح
    elif val >= 0.30:
        color = '#FFA07A'  # برتقالي
    else:
        color = '#FF7F7F'  # أحمر فاتح
    return f'background-color: {color}'

# تبويب مباريات اليوم
with tabs[0]:
    st.subheader("مباريات اليوم المضمونة (75%-90%)")
    styled_matches = matches_data.style.applymap(highlight_prob, subset=["احتمال 1", "احتمال تعادل", "احتمال 2"])
    st.dataframe(styled_matches, use_container_width=True)

# تبويب تحليل فرق لا ليغا
with tabs[1]:
    st.subheader("تحليل فرق LaLiga")
    st.dataframe(laliga_data.style.highlight_max(color='#ADD8E6', axis=0), use_container_width=True)
