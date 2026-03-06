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
    book_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
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

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(posters[0])
        st.caption(names[0])
    with col2:
        st.image(posters[1])
        st.caption(names[1])
    with col3:
        st.image(posters[2])
        st.caption(names[2])
    with col4:
        st.image(posters[3])
        st.caption(names[3])
    with col5:
        st.image(posters[4])
        st.caption(names[4])
