import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

def main() :
    st.title('내 앱 대시보드')

    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)

    st.write(df1.shape)

    print(df1.columns[1:])

    lang_list = df1.columns[1:]

    choice_list = st.multiselect('언어를 선택하세요', lang_list)
    print(choice_list)

    if len(choice_list) > 0:

        choice_df = df1[choice_list]

        st.dataframe(choice_df)

        # 스트림릿이 제공하는 라인차트
        st.line_chart(choice_df)

        # 스트림릿이 제공하는 영역차트
        st.area_chart(choice_df)

if __name__ == '__main__':
    main()