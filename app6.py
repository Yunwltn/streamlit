import streamlit as st

# 유저한테 데이터를 입력받는 방법
def main() :
    # 텍스트를 입력 받는 방법
    name = st.text_input('이름을 입력하세요')
    st.title(name)

    name2 = st.text_input('이름 입력', max_chars=5)
    st.title(name2)

    message = st.text_area('메세지를 입력하세요', height=10)
    st.text(message)

    # 숫자 입력 받는 방법
    year = st.number_input('출생년도를 입력하세요',1900, 2300)
    st.text(year)

    number = st.number_input('실수를 입력하세요', 0.5, 100.0, step=0.3)
    st.text(number)

    # 날짜 입력 받는 방법
    my_date = st.date_input('약속 날짜 입력')
    st.write(my_date)
    st.write(my_date.strftime('%Y년 %m월 %d일'))

    # 시간 입력 받는 방법
    my_time = st.time_input('약속 시간 선택')
    st.write(my_time)
    st.write(my_time.strftime('%H : %M'))

    # 비밀번호 입력 받는 방법
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)

    # 색 입력
    color = st.color_picker('색을 선택하세요')
    st.text(color)

if __name__ == '__main__' :
    main()