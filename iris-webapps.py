import streamlit as st 
import pandas as pd 
from PIL import Image 
from sklearn import datasets 
from sklearn.naive_bayes import GaussianNB 

st.write("""
# Klasifikasi Bunga Iris
"Metode Naive Bayer Classifier"
"""

)

img = Image.open('iris.png')
st.image(img, use_column_width=False)

st.sidebar.header('Parameter Inputan')

def input_user():
    panjang_sepal=st.sidebar.slider('Panjang Sepal', 4.3,7.9,5.4)
    lebar_sepal=st.sidebar.slider('Lebar Sepal', 2.0,4.4,3.4)
    panjang_petal=st.sidebar.slider('Panjang petal',1.0,6.9,1.3)
    lebar_petal=st.sidebar.slider('Lebar petal',0.1,2.5,0.2)
    data = {'panjang sepal' : panjang_sepal, 
    'lebar sepal ' : lebar_sepal,
    'panjang petal ' : panjang_petal,
    'lebar petal ' : lebar_petal
    }
    fitur = pd.DataFrame(data, index=[0])
    return fitur
df = input_user()

st.subheader('Parameter Input klasifikasi')
st.write(df)

iris=datasets.load_iris()
X=iris.data
Y=iris.target

model=GaussianNB()
model.fit(X,Y)

prediksi=model.predict(df)
prediksi_proba=model.predict_proba(df)

st.subheader('Label kelas dan nomor indeks yang sesuai')
st.write(iris.target_names)

st.subheader('Prediksi (hasil klasifikasi)')
st.write(iris.target_names[prediksi])


st.subheader('Probabilitas hasil prediksi (Klasifikasi)')
st.write(prediksi_proba)
