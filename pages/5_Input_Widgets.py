import streamlit as st

st.title('Input Widgets!')
st.header('1. Button elements')
st.subheader('Button')
st.button('초기화', type='primary')
if st.button('안녕'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :raising_hand:')


st.subheader('Link Button')
st.link_button('google', 'https://www.google.com')


st.subheader('Page Link', divider=True)
st.page_link('app.py',label='Home',icon='🏠')
st.page_link('pages/1_Text_elements.py', label='Text elements', icon='📄')
st.page_link('pages/2_Data_elements.py', label='Data elements', icon='📊')
st.page_link('pages/이은정_streamlit_연습문제.py', label='Exercise',disabled=True, icon='❗')
st.page_link('https://docs.streamlit.io/develop/api-reference', label='Streamlit Docs', icon='🌎')


st.subheader('Form Submit_Button',divider=True)

with st.form(key='form1'):
    id = st.text_input('Id')
    pw = st.text_input('Password',type='password')
    submitted = st.form_submit_button('로그인')
    if submitted:
        st.write('id : ',id, 'password : ', pw)


form = st.form(key='form2')
title = form.text_input('제목')
contents = form.text_area('질문입력')
submit = form.form_submit_button('작성')
if submit:
    st.write('제목 :',title)



st. divider()

st.header('2. Selection elements')

st.subheader('Checkbox')

agree = st.checkbox('찬성', value=True, label_visibility='visible')
if agree:
    st.write('Good!')


st.subheader('Toggle')
on = st.toggle('선택')
if on:
    st.write('on')

st.subheader('Radio')
fruit = st.radio(
    label='좋아하는 과일은?',
    options=[':banana:바나나', '딸기','메론','사과','배'],
    captions=['웃어요','달콤해요','시원해요','상큼해요','과즙이많아요'],
    horizontal=True,
    index=2)

if fruit==':banana:바나나':
    st.write('바나나를 선택하셨군요')
else:
    st.write('바나나가 아니네요')


st.subheader('Selectbox')
fruit = st.selectbox('과일을 선택하세요',
             options=['바나나','딸기','사과','메론'],index=None,
             placeholder='과일을 선택하세요!',
             label_visibility='collapsed')

st.write(f'당신이 선택한 과일은 : {fruit}')

st.divider()

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()

st.subheader('Multiselect')
color = st.multiselect('당신이 좋아하는 색은?',
                       options=['red','green','blue','yellow','pink'],
                       default=['green','blue'])
st.write('선택한 색상은 :',color)


st.subheader('Selectsliber')
color2 = st.select_slider('당신이 좋아하는 색상은?',
                 options=['red','green','blue','yellow','pink','violet','indigo','orange'])
st.write('당신이 좋아하는 색상은 : ',color2)

color3 = st.select_slider('당신이 좋아하는 색상은?',
                 options=['red','green','blue','yellow','pink','violet','indigo','orange'],
                 value='blue')
st.write('당신이 좋아하는 색상은 : ',color3)

color_st, color_end = st.select_slider('당신이 좋아하는 색상은?',
                 options=['red','green','blue','yellow','pink','violet','indigo','orange'],
                 value=('blue','pink'))
st.write('당신이 좋아하는 색상은 : ',color_st, color_end)


st.subheader('color picker', divider='rainbow')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.header('3. Numeric Input elements')
st.subheader('Number input', divider='rainbow')
num = st.number_input('숫자입력')
st.write(num)

num2 = st.number_input('숫자입력', value=None,
                       placeholder='숫자를 입력하세요',
                       label_visibility='collapsed')
st.write(f'현재 숫자 : {num2}')

num3 = st.number_input('숫자입력', min_value=-10.0,
                       max_value=10.0, step=0.2,
                       format='%.3f')
st.write(f'현재 숫자 : {num3:.3f}')


st.subheader('slider',divider='rainbow')
age = st.slider('나이',min_value=0,max_value=100,value=20,step=2)
st.write(age)

scores = st.slider('점수',min_value=0.0,max_value=100.0,value=(25.0,50.0))
st.write(scores)

st.header('4. Text input elements')
st.subheader('Text input',divider=True)
id = st.text_input('아이디', value='id')
pw = st.text_input('비밀번호', type='password')
st.write(f'아이디 : {id} \n 비밀번호 : {pw}')

st.subheader('Text area',divider=True)
text = st.text_area('질문을 입력하세요')
st.write(text)
st.write(f'총 문자 길이는 {len(text)}')

st.header('5. Date & Time input elements')
st.subheader('Date input', divider=True)


from datetime import datetime,date,time,timedelta

date = st.date_input('일자 선택', value=date(2024,3,1),
                     min_value=date(2023,1,1),
                     max_value=date(2024,10,31),
                     format='DD-MM-YYYY')
st.write(date)

st.subheader('Time input',divider=True)
time1 = st.time_input('시간 입력', value=time(10,00),step=1200)
st.write(time1)

time2 = st.time_input('시간 입력', value=time(11,00),step=timedelta(minutes=10))
st.write(time2)


