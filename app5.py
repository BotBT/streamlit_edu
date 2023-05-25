import streamlit as st
from PIL import Image

def main():
    st.title('앱 대시보드')

    img = Image.open('data/image_03.jpg')

    print(img)

    st.image(img)

    st.image(img, use_column_width=True)

    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')

    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)


if __name__ == '__main__':
    main()

 