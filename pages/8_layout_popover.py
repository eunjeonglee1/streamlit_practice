import streamlit as st

st.header('Popover Container')

with st.popover('Open popover'):
    st.write('Hello')
    name = st.text_input("what's your name?")
st.write('Your name : ',name)

popover = st.popover('좋아하는 색상은?',use_container_width=True)
red = popover.checkbox('red',True)
blue = popover.checkbox('blue')

if red:
    st.write(':red[빨강]')
if blue:
    st.write(':blue[파랑]')

with st.popover('popover사용시 주의점'):
    st.write('popover 안에 또 다른 popover 배치 불가')