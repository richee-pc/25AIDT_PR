import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. 페이지 설정 ---
# Streamlit 페이지의 기본 설정을 'wide' 레이아웃으로 지정합니다.
# 이렇게 하면 HTML 콘텐츠가 화면에 더 넓게 표시됩니다.
st.set_page_config(
    page_title="AIDT 거점학교 운영 사례",
    page_icon="🚀",
    layout="wide"
)

# --- 2. HTML 파일 불러오기 ---
# HTML 파일의 정확한 경로를 지정합니다.
# app.py와 같은 레벨에 htmls 폴더가 있다고 가정합니다.
html_file_path = os.path.join('htmls', 'index.html')

try:
    # HTML 파일을 열고 내용을 읽어옵니다.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # --- 3. HTML 콘텐츠 렌더링 ---
    # st.components.v1.html을 사용하여 HTML 콘텐츠를 Streamlit 앱에 삽입합니다.
    # height: HTML 컴포넌트의 높이를 넉넉하게 설정합니다. (필요에 따라 조절)
    # scrolling=True: HTML 콘텐츠가 height보다 길 경우 스크롤바를 활성화합니다.
    components.html(html_content, height=4000, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다.")
    st.info("app.py와 같은 경로에 'htmls' 폴더를 만들고, 그 안에 'index.html' 파일이 있는지 확인해주세요.")
except Exception as e:
    st.error(f"HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
