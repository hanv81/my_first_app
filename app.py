import streamlit as st

st.title('Bé tập làm toán')
c1,c2,c3 = st.columns(3)
with c1:
  a = st.number_input('a')
with c2:
  op = st.radio('Phép toán', ('\+', '\-', 'x', ':'), horizontal=True)
with c3:
  b = st.number_input('b')

r = st.number_input('Nhập kết quả')

if st.button('Kiểm tra', use_container_width=True, type='primary'):
  if op == '\+':
    c = a + b
  elif op == '\-':
    c = a - b
  elif op == 'x':
    c = a * b
  else:
    c = a / b
  
  if c == r:
    st.success('Chính xác')
    st.balloons()
  else:
    st.error('Sai')
    st.snow()