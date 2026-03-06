import streamlit as st
import pandas as pd
import numpy as np
import pickle
dfd=pickle.load(open('dfs.pkl','rb'))
df=pd.DataFrame(dfd)
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(book):
    book_index=df[df['title']==book].index[0]
    distance=similarity[book_index]
    book_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]
    recommended=[]
    recommendposter=[]
    for i in book_list:

        recommended.append(df.iloc[i[0]].title)
        recommendposter.append(df.iloc[i[0]].img)
    return recommended,recommendposter

st.title('Book Recommender System')
option= st.selectbox('Which book do you like?',df['title'].values)

if st.button('recommend'):
    names,posters=recommend(option)

    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10=st.columns(10)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])
    with col6:
        st.image(posters[5])
        st.text(names[5])
    with col7:
        st.image(posters[6])
        st.text(names[6])
    with col8:
        st.image(posters[7])
        st.text(names[7])
    with col9:
        st.image(posters[8])
        st.text(names[8])
    with col10:
        st.image(posters[9])
        st.text(names[9])