import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
img_diabetes = Image.open("images/f_doctor.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Yao :wave:")
    st.title("A Postdoc at NTNU")
    st.write(
        "I like programming and solving technical problems, my goal for the future is to become a proficient programmer."
        " I like to write neat and efficient code, and to design and develop tools for meaningful applications."
    )
    st.write("[My Github >](https://github.com/yaoj90?tab=repositories)")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Web Apps")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.subheader("Diabetes Predictor")
    with text_column:
        st.subheader("[Let's Play!](https://diabetes-predictor.streamlit.app)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    st.header('<a href="yao.jiang@ntnu.no">Contact me !</a>', unsafe_allow_html=True)


