import streamlit as st
from keras.models import load_model
# from keras.preprocessing import image
import keras.utils as image
import numpy as np
import keras


page_bg_img = """
<style>
[class="block-container css-18e3th9 egzxvld2"] {
background: url("https://coolbackgrounds.io/images/backgrounds/index/compute-ea4c57a4.png");
height: 100%;
width: 100%;
background-size: cover;
background-repeat: no-repeat;
background-position: center;
background-attachment: fixed;
height: auto;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

def classification(img):
    # model = load_model('my_model.h5')
    model = load_model("model_792023.h5")
    # img_new = image.load_img(img, target_size=(224, 224))
    # x = image.img_to_array(img_new)
    # x = np.expand_dims(x, axis=0)
    # predict_category = np.argmax(model.predict(x))
    
    img = keras.utils.load_img(img, target_size=(224,224))
    x = keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    predict_category = model.predict(images)
    st.write(predict_category[0][0])
    
    if predict_category == 0:
        return True
    else:
        return False
        
col1, col2, col3 = st.columns([.5, 6, .5])
with col2: 
    data = False
    st.write('# Bells Palsy Clasification')
    st.write("")
    st.write(" paralisis fasialis idiopatik, merupakan penyebab tersering dari paralisis fasialis unilateral. Bells’ palsy merupakan kejadian akut, unilateral, paralisis saraf fasial type LMN (perifer), yang secara gradual mengalami perbaikan pada 80-90% kasus. Bell’s palsy akan membuat separuh wajah tampak terkulai. Senyum hanya bisa satu sisi, dan mata di sisi yang terkena menolak untuk menutup. Kondisi ini juga dikenal sebagai kelumpuhan wajah perifer akut yang penyebabnya belum diketahui, dan dapat terjadi pada semua usia.")
    st.write("Keterangan: 0.0 = Bell's Palsy dan 1.0 = Normal Face")
    uploaded_files = st.file_uploader("Choose Image", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        
        with open(uploaded_file.name, 'wb') as f:
            f.write(uploaded_file.getbuffer())
            data = True
    
    if data == True:
        test_model = classification(uploaded_file.name)
        st.image(uploaded_file.name)
        
        if test_model == True:
            st.success("Bells Palsy")
        
        elif test_model == False:
            st.success("Normal Face")
    


