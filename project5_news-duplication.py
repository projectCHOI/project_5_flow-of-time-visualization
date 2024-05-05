# project5_news-duplication
import pandas as pd

df = pd.read_csv('찾을파일.csv')

df_unique = df.drop_duplicates()
df_unique.to_csv('정리한 파일.csv', index=False)
print('동일 내용 제거 완료.')
