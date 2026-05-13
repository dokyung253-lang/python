import matplotlib.pyplot as plt # 맷플롯립( 시각화 라이브러리 )
import pandas as pd   # 판다스(데이터 표 관리)
import korean_font # 그래프 한글 깨짐 방지
import json  # json파일 load() 용도

# [1] T5_data.json 파일 내 'financial_performance_data'
with open( './T5_data.json', 'r', encoding='utf-8' ) as json_file :
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['financial_performance_data'])

# [2] 플롯박스 : '수익' '비용' '이익'으로 박스플롯 표시
# 플롯박스 : plt.boxplot() : 데이터 최솟값(맨 아래), 최댓값(맨 위), 1사분위(박스 아래), 중앙값(선), 3사분위(박스 위) 시각화
plt.boxplot( [df['수익'], df['비용'], df['이익'] ], tick_labels= ['수익','비용', '이익'] )
plt.ylabel('금액')
plt.title('항목별 금ㄹ액 분포')
plt.show()

# 차트확인 : 비용 데이터에서 800 부근에 이상치(점)가 존재한다.

# [3] 플롯박스 : 분기별 수익 데이터로 박스플롯 표시
# 플롯박스에서 그룹 , df.boxplot( column = ['값'], by='그룹기준')
df.boxplot( column = ['수익'], by='분기') # 분기별 수익
plt.show()

# 차트확인 
# 2분기가 수익 중앙값이 가장 높고, 
# 1분기 박스가 가장 길어서 수익 불안정
# 4분기 박스가 조밀하게 있어서 수익 안정화