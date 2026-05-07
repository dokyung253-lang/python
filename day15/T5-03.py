import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import korean_font                  # 한글폰트
import json                         # Json Load

# [1] T5_data.json 파일 내 'patient_status_data'
with open( './T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['patient_status_data'] )


# [2] 막대차트 : 상태별 환자수
plt.bar( df['상태'], df["환자 수"])
plt.title( '상태별 환자 수 비교')
plt.xlabel('상태')
plt.ylabel('환자 수')
plt.show()

# [3] 원형차트 : 전체 대비 각 상태의 환자 비율
# plt.pie( 값  , labels='', autopct='%.nf%%', startangle='시작각도')
plt.pie( df['환자 수'], labels = df['상태'] , autopct='%.2f%%' , startangle= 90 )
plt.title('환자 상태 비율')
plt.show()

