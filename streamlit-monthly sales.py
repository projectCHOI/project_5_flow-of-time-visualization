import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 데이터를 불러오는 함수
@st.cache_data
def load_data():
    path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\16y17y18y19y_Total daily sales.csv'
    return pd.read_csv(path)

# 데이터 불러오기
df = load_data()

# Streamlit에서 데이터프레임 표시
st.write("Daily Sales Data:", df)

# 그래프를 그리는 함수
def plot_sales(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['TIME'], df['SALES'], marker='o', color='green')  # 기본 꺽은선 그래프는 초록색으로 설정

    # 최고점과 최저점 표시
    max_index = df['SALES'].idxmax()
    min_index = df['SALES'].idxmin()
    plt.scatter(df['TIME'][max_index], df['SALES'][max_index], color='red', marker='*')  # 최고점은 빨간색 별표로 표시
    plt.scatter(df['TIME'][min_index], df['SALES'][min_index], color='blue')  # 최저점은 파란색으로 표시

    plt.title('Daily Sales Data')
    plt.xlabel('Time')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.xticks(rotation=45)  # x축 라벨 회전
    plt.tight_layout()
    st.pyplot(plt)

# 그래프 그리기
plot_sales(df)