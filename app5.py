# 웹 대시보드에 이미지파일, 동영상 파일 넣는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    img = Image.open('streamlit_data/image_03.jpg')
    st.image(img)
    st.image(img, use_column_width=True) # 화면에 꽉 차게

    image_url = 'https://shopping-phinf.pstatic.net/main_3243627/32436275374.20221019105445.jpg?type=w300'
    st.image(image_url)

# 동영상
    video_file = open('streamlit_data/secret_of_success.mp4', 'rb')
    st.video(video_file)

if __name__ == '__main__' :
    main()