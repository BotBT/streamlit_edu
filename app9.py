import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('내 앱 대시보드')

    df = pd.read_csv('data/iris.csv')

    st.dataframe(df)

    # sepal_length, sepal_width의 관계를 차트로

    fig = plt.figure()
    plt.scatter(data= df, x ='sepal_length', y = 'sepal_length')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal length')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data= df, x= 'sepal_') #회귀
    st.pyplot(fig2)

    correlation = df[['sepal_length', 'sepal_width']].corr()
    st.dataframe(correlation)


    # sepal_length로 히스트그램 그리자.
    # bin의 갯수는 20개로
    fig3 = plt.figure(figsize= (10, 4))

    plt.subplot(1, 2, 1)
    plt.hist(data=df, x='sepal_length', rwidth=0.8)

    plt.subplot(1,2,1)
    plt.hist(data=df, x='sepal_length', rwidth=0.8)

    st.pyplot(fig3)

    # species 컬럼에는 종에 대한 정보가 들어있는데, 각 종뵬로 몇개씩의 데이터가 있는지
    # 차트로 나타내시오.
    st.dataframe(['species'].value_counts())

    fig4 = plt.figure()
    sns.countplot(data=df, x='species')
    st.pyplot(fig4)


    ## 데이터프레임의 차트 그리는 코드도 실행 가능!
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind = 'bar') #plot 함수를 이용하여 차트 영역을 생성
    st.pyplot(fig5)

    # # 데이터프레임 자체 plot 함수는 스트림릿에서 안된다.
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)



if __name__ == '__main__':
    main()