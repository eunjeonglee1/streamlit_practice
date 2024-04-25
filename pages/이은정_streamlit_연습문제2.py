import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from konlpy.tag import Okt
from collections import Counter
import json
import folium
from streamlit_folium import st_folium


# 1. iris 데이터셋을 이용
st.header('1. iris 데이터')
iris = sns.load_dataset('iris')
iris_df = pd.DataFrame(iris)

# 1-1) iris 데이터셋을 데이터프레임으로 표시
st.subheader('1.iris 데이터프레임')
st.dataframe(iris_df)

# 1-2)multiselect를 사용하여 품종(species)을 선택하면, 해당 품종의 데이터에 대한 데이터프레임을 표시
st.subheader('2.Multiselect를 이용하여 품종 선택')

# iris_groups = iris_df.groupby(iris_df.species)
# # st.write(iris_groups.groups)


options = st.multiselect('데이터 확인하고 싶은 품종을 고르시오',['setosa','versicolor','virginica'])
st.write(iris_df[iris_df['species'].isin(options)])


# 1-3) 품종을 제외한 4가지 컬럼을 radio요소를 사용하여 선택하면 선택한 컬럼에 대한 히스토그램 그리기(matplotlib)
st.subheader('3.품종을 제외한 4가지 컬럼을 선택하여 히스토그램 그리기')

col1, col2 = st.columns(2)

iris_list = ['sepal_length','sepal_width','petal_length','petal_width']

with col1:
    options2 = st.radio('히스토그램으로 확인하고 싶은 데이터를 선택하시오👇',iris_list)

with col2:
    fig, ax = plt.subplots()
    ax.hist(iris_df[options2])
    st.pyplot(fig)



# 2. kor_news 데이터셋을 이용
st.header('2. kor_news 데이터')
news = pd.read_excel('data/kor_news_240326.xlsx')
news_df = pd.DataFrame(news)

# 2-1) 분류의 대분류기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 barchart표시
st.subheader('1.대분류를 선택하여 주요 키워드 20위에 대한 Barchart 표시')

news_df['대분류'] = news_df.분류.str.split('>').str[0]

news_list = [i for i in news_df['대분류'].unique()]

col3, col4 = st.columns([1,2])

with col3:
    news_options = st.radio('대분류를 선택하시오👇',news_list)
with col4:
    okt = Okt()
    @st.cache_data
    def pick_tag_tokens(gobun_name, tag_name='Noun', word_len=1):
        temp_list = []
        for sentence in news_df.제목[news_df.대분류 == gobun_name]:
            s_list = okt.pos(sentence)
            for word, tag in s_list:
                if tag == tag_name and len(word) >= word_len:
                    temp_list.append(word)
        return temp_list

    @st.cache_data
    def counter(pick):
        verb_cnt = Counter(pick)
        verb_df = pd.DataFrame(pd.Series(verb_cnt), columns=['freq'])
        sorted_verb_df = verb_df.sort_values(by='freq', ascending=False)
        return sorted_verb_df

    pick1 = pick_tag_tokens(news_options, tag_name='Noun', word_len=2)
    df2 = counter(pick1)
    df2 = df2.iloc[:20]
    st.bar_chart(df2)


# 3. 경기도 인구데이터
st.header('3. 경기도 인구데이터')
with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
    geo_gg = json.loads(f.read())

df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')

# 3-1) 연도별 인구수에 대한 지도시각화(2007년, 2015년, 2017년 연도를 탭으로 제시)
st.subheader('1. 연도별 인구수에 대한 시각화')

# 파일명과 확장자명을 분리하는것
# import os
# fname, ext = os.path.splitext(file_path)

@st.cache_data
def drow_map(year):
        map = folium.Map(location=[37.566, 126.9782], zoom_start=8)
        folium.GeoJson(geo_gg).add_to(map)
        folium.Choropleth(geo_data=geo_gg,
                          data=df_gg[year],
                          columns=[df_gg.index, df_gg[year]],
                          key_on='feature.properties.name').add_to(map)
        st_folium(map, width=600, height=400)


tab1,tab2,tab3 =st.tabs(['2007년','2015년','2017년'])

with tab1:
    drow_map(2007)


with tab2:
    drow_map(2015)

with tab3:
    drow_map(2017)