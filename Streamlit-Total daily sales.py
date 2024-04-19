import pandas as pd

# 파일 경로 설정
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\Master daily sales.csv'

# CSV 파일 읽기
data = pd.read_csv(file_path)

# 데이터 확인
print(data.head())
