import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import korean_font                  # 한글폰트
import json                         # Json Load

# [1] T5_data.json 파일 내 'risk_return_data'
with open('./T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame( data_json['risk_return_data'])

# [2] 산점도 : 리스크 대비 수익률 , 값에 따른 원형크기 조정 => 버블차트
# s= 원형크기(계산식 있으면 버블차트 표현 가능), alpha = 투명도(겹치는 경우 있기 때문(버블차트에선 권장))
plt.scatter( df['리스크'], df['수익률(%)'],  s = df['수익률(%)']*100, alpha= 0.2 )
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.title('리스크 대비 수익률')
plt.show()

# [3] 산점도 : 자산별 리스크 대비 수익률
# 중복에는 group 사용

categories = df['자산'].unique()      # 중복제거된 자산 리스트
# print( categories )  # ['자산 A', '자산 B', '자산 C', '자산 D', '자산 E']
for i , category in enumerate( categories ):            # enumerate( 리스트 ) : 반복순회자(이터레이터) 으로 인덱스와 요소값을 하나씩 반환
   sub = df[df['자산'] == category ] # 동일한 자산 정보 가져오기 (필터링)
   print( sub )
   plt.scatter( sub['리스크'], sub['수익률(%)'], label = category ) 
plt.legend()
plt.show()