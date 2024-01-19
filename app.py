import streamlit as st

#import streamlit
#streamlit.title("streamlit 포켓몬 도감")
#streamlit.markdown("**포캣몬**을 하나씩 추가해서 도감을 채워보세요!!")

view=[100,150,30]
st.write("# Youtube view") # '#'을 붙이면 큰 글씨로 
st.write("## Raw")
view
st.write("## Bar Chart")
st.bar_chart(view) #bar_chart 실행

import pandas as pd
sview=pd.Series(view)
sview