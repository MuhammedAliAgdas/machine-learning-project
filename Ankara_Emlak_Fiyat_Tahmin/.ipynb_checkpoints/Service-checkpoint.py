import streamlit as st
import joblib
import numpy as np

# Modeli yükle
loaded_model = joblib.load("bayesian_ridge_model.sav")

# Streamlit uygulamasını tanımla
st.title("Ankara merkez ilçeleri iş yeri-mağaza fiyat tahmin uygulaması")

isinma = [0,0,0,0,0,0,0,0]
isinma = [int(eleman) for eleman in isinma]
yas = [0,0,0,0,0,0,0,0,0]
yas = [int(eleman) for eleman in yas]
kredi_uygun_mu = 0
st.sidebar.header("Giriş verileri")
m2 = st.number_input("Net metrekare giriniz:",step=1,min_value=1, max_value=1000)
oda = st.number_input("Oda sayısı giriniz:",step=1,min_value=1, max_value=10)
kredi = st.selectbox("Krediye uygunluk:", ["Bilinmiyor","Krediye uygun","Krediye uygun değil"])
if (kredi == "Bilinmiyor"):
    kredi_uygun_mu = 0
if (kredi == "Krediye uygun"):
    kredi_uygun_mu = 1
if (kredi == "Krediye uygun değil"):
    kredi_uygun_mu = 2
kat = st.number_input("Kat sayısı giriniz:",step=1,min_value=1, max_value=50)
isinmaSecim = st.selectbox("Isıtma tipi seçiniz:", ["Doğalgaz sobalı", "Fancoil ünitesi", "Isıtma yok","Klimalı","Kombi doğalgaz","Merkezi payölçer","Merkezi doğalgaz","Sobalı"])
if(isinmaSecim=="Doğalgaz sobalı"):
    for i in range(0,8):
        isinma[i]=0
    isinma[0] = 1
if(isinmaSecim=="Fancoil ünitesi"):
    for i in range(0,8):
        isinma[i]=0
    isinma[1]= 1
if(isinmaSecim=="Isıtma yok"):
    for i in range(0,8):
        isinma[i]=0
    isinma[2] = 1
if(isinmaSecim=="Klimalı"):
    for i in range(0,8):
        isinma[i]=0
    isinma[3]= 1
if(isinmaSecim=="Kombi doğalgaz"):
    for i in range(0,8):
        isinma[i]=0
    isinma[4]= 1
if(isinmaSecim=="Merkezi payölçer"):
    for i in range(0,8):
        isinma[i]=0
    isinma[5]= 1
if(isinmaSecim=="Merkezi doğalgaz"):
    for i in range(0,8):
        isinma[i]=0
    isinma[6] = 1
if(isinmaSecim=="Sobalı"):
    for i in range(0,8):
        isinma[i]=0
    isinma[7] = 1

yasSecim = st.selectbox("Binanın yaşını seçiniz:", ["0 yeni", "1", "11-15","16-20","2","21 ve üzeri","3","4","5-10"])
if(yasSecim=="0 yeni"):
    for i in range(0,9):
        yas[i]=0
    yas[0] = 1
if(yasSecim=="1"):
    for i in range(0,9):
        yas[i]=0
    yas[1]= 1
if(yasSecim=="11-15"):
    for i in range(0,9):
        yas[i]=0
    yas[2]= 1
if(yasSecim=="16-20"):
    for i in range(0,9):
        yas[i]=0
    yas[3]= 1
if(yasSecim=="2"):
    for i in range(0,9):
        yas[i]=0
    yas[4]= 1
if(yasSecim=="21 ve üzeri"):
    for i in range(0,9):
        yas[i]=0
    yas[5]= 1
if(yasSecim=="3"):
    for i in range(0,9):
        yas[i]=0
    yas[6] = 1
if(yasSecim=="4"):
    for i in range(0,9):
        yas[i]=0
    yas[7] = 1
if(yasSecim=="5-10"):
    for i in range(0,9):
        yas[i]=0
    yas[8] = 1
    
if st.button("Tahmin Yap"):
    input_data = np.array([[m2,oda,kredi_uygun_mu,kat,isinma[0],isinma[1],isinma[2],isinma[3],isinma[4],isinma[5],isinma[6],isinma[7],yas[0],yas[1],yas[2],yas[3],yas[4],yas[5],yas[6],yas[7],yas[8]]])
    prediction = loaded_model.predict(input_data)

    st.subheader("Tahmin Sonucu")
    st.write("Model tahmini:", np.int64(prediction[0])," TL")