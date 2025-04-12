import streamlit as st
from classify import classify_subject

st.set_page_config(page_title="메일 제목 분류기", page_icon="📧")
st.title("📧 메일 제목 자동 분류기 (with Phi-2)")

subject = st.text_input("메일 제목을 입력하세요:")

if st.button("분류하기") and subject:
    with st.spinner("분류 중..."):
        label = classify_subject(subject)
    st.success(f"📌 예측된 분류: **{label}**")
