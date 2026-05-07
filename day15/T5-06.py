import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import korean_font                  # 한글폰트
import seaborn as sns               # [1. 타이타닉 생존 데이터 분석]
# 캐글 : 데이터셋 공유하는 사이트, 데이터분석/ 머신러닝/ 연구에 자주 사용됨
# 다운로드 > train.csv 불러오기

# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# [3. 자료수집 ] 
# https://www.kaggle.com/competitions/titanic/overview
# train.csv 파일 판다스로 불러오기 (day14 T4-02 참조)

df = pd.read_csv(
    './day15/train.csv',
    header=0,
    encoding='utf-8'
)
print( df.head() )          # 상위 5개 출력하여 데이터 확인
df.info()                   # 속성타입 확인
print( df.isnull().sum() )  # 결측치 확인

# [4. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# .fillna( 특정값 ) : 만일 결측이면 특정값으로 채우기 함수
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.

df['Age'] = df['Age'].fillna( df['Age'].median() )      # 177
df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode()[0] ) # 2
print( df.isnull().sum() )  # 결측치 확인


# [5. 데이터 시각화 및 분석] (countplot T3-05)
# 3-1  sns.countplot을 사용하여 전체 생존자(Survived)와 사망자의 비중을 시각화한다.
# plt.bar : 수치값( 남: 3(x축), 여:5(y축) ) vs sns.countplot : 범주값( 남남남여여여여여 )
# bar차트 사용시 ; 따로 합계를 구해야 함 , sns차트 : 자동 합계 계산
# sns.countplot( data=df, x='열이름')
sns.countplot( data = df , x = 'Survived')
plt.title('생존 여부 분포')
plt.xlabel('생존여부 0:사망, 1:생존')
plt.ylabel('인원 수')
plt.show()

# 5-2 히스트그램 : sns.hisplot을 사용하여 나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
print( df[ df[ 'Survived' ] == 0 ]['Age'] ) # 사망한 사람들의 나이만 추출 / 필터링 : df[ 조건식 ]
print( df[ df[ 'Survived' ] == 1 ]['Age'] ) # 생존한 사람들의 나이만 추출
sns.histplot( df[ df['Survived'] == 0 ]['Age'] , label='사망', color='#ff0000', kde= True)
sns.histplot( df[ df['Survived'] == 1 ]['Age'] , label='생존', color='#0000ff', kde= True)

plt.title('나이별 생존 분포')
plt.xlabel('나이')
plt.ylabel('인원수')
plt.legend()
plt.show()

# 5-3 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# sns.countloj
print(df['Sex'][0] )        # male
sns.countplot( data=df, x = 'Sex', hue='Survived' )     # 성별 수
plt.legend( title = '범례제목', labels = ['사망', '생존'])
plt.show()

# 5-4 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
print( df['Pclass'][0] )
sns.countplot(data=df, x = 'Pclass' )

# 5-5 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
print( df['Embarked'][0] )          # C = Cherbourg, Q = Queenstown , S = Southampton
sns.countplot( data= df, x= 'Embarked' , hue='Survived')        # 승선항구 수
plt.show()