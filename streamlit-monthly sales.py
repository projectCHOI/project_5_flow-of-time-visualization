import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 데이터를 불러오는 함수
@st.cache_data
def load_data():
    path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\monthly sales.csv'
    return pd.read_csv(path)

# 데이터 불러오기
df = load_data()

# Streamlit에서 데이터프레임 표시
st.write("Monthly Sales Data :", df)

# 그래프를 그리는 함수
def plot_sales(df):
    plt.figure(figsize=(10, 5))
    plt.plot(['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7'], df.loc[df.index[0], ['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']], marker='o')
    plt.title('Monthly Sales Data')
    plt.xlabel('selling')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.xticks(rotation=45)  # x축 라벨 회전
    plt.tight_layout()
    st.pyplot(plt)

# 그래프 그리기
plot_sales(df)
