import streamlit as st
import pandas as pd

# 파일 경로
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\16y17y18y19y_Total daily sales.csv'
data = pd.read_csv(file_path)

# 데이터 확인
st.write(data)
