# 뉴스 데이터 kor_news_20240326.xlsx를 이용하여 스트림릿으로 구현하기
import pandas as pd
import streamlit as st
from konlpy.tag import Okt
from collections import Counter


@st.cache_data
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

news = load_data('data/kor_news_240326.xlsx')

# 1. 뉴스데이터를 DataFrame으로 표시하기

st.subheader('1. 뉴스데이터를 DataFrame으로 표시하기')
st.dataframe(news)

# 2. 뉴스데이터의 URL컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한 column configuration 사용

st.subheader('2. 뉴스데이터의 URL컬럼을 실제 뉴스기사 페이지로 이동')
st.dataframe(news,column_config={'URL':st.column_config.LinkColumn()})

# 3. 분류컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기

st.subheader('3. 분류컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기')
df = pd.DataFrame(news)
df['대분류'] = df.분류.str.split('>').str[0]
df_maxbun = df['대분류'].value_counts()
st.bar_chart(df_maxbun)


# 4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기
st.subheader('4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기')

okt = Okt()

def pick_tag_tokens(col_name, gobun_name, tag_name='Noun', word_len=1):
    temp_list=[]
    for sentence in col_name[df.대분류== gobun_name]:
        s_list = okt.pos(sentence)
        # token_pos = [okt.pos(word) for word in sentence] # sentence를 리스트로 만들었을때
        for word, tag in s_list:
            if tag == tag_name and len(word) >= word_len:
                temp_list.append(word)
    return temp_list

def counter(pick):
    verb_cnt = Counter(pick)
    verb_df = pd.DataFrame(pd.Series(verb_cnt), columns=['freq'])
    sorted_verb_df = verb_df.sort_values(by='freq', ascending=False)
    return sorted_verb_df


st.markdown(':red[**경제**]분야의 빈도가 많은 주요 키워드 20위')
pick1 = pick_tag_tokens(df['제목'],'경제',tag_name='Noun', word_len=2)
df2 = counter(pick1)
st.bar_chart(df2.iloc[:20])


st.markdown(':red[**사회**]분야의 빈도가 많은 주요 키워드 20위')
pick2 = pick_tag_tokens(df['제목'],'사회',tag_name='Noun', word_len=2)
df3 = counter(pick2)
df3 = df3.iloc[:20]
st.bar_chart(df3)



