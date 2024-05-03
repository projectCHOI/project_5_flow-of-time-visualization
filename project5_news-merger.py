# news-merger
import os
import pandas as pd

folder_path = '병합 대상 폴더'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

data_frames = [pd.read_csv(os.path.join(folder_path, file)) for file in csv_files]
merged_df = pd.concat(data_frames, ignore_index=True)

merged_df.to_csv('저장 경로/파일이름.csv', index=False)

print('CSV 병합 완료.')
