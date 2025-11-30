import numpy as np
from PIL import Image
import tensorflow as tf
import streamlit as st


@st.cache_resource
def load_my_model():
    from tensorflow.keras.models import load_model
    return load_model("best_model.keras")

model = load_my_model()


st.title("Animal Image Detection")

st.write('''Please upload an Animal Image that listed here. This application will
         predict which Animal image is that you uploaded.
         Listed Animals are: Dog, Horse, Elephant, Butterfly, Chicken, Cat, Cow, 
         Sheep, Spider, Squirrel.
         ''')


uploaded_file = st.file_uploader("Upload the Image", type = ["jpg", "jpeg", "png"])

if st.button("Predict"):
    if uploaded_file is not None:

        st.image(uploaded_file, caption = "Uploaded Image")

        image = Image.open(uploaded_file)
        image = image.convert("RGB")
        image = image.resize((224,224))

        image = np.array(image)
        image = np.expand_dims(image, axis = 0)

        predict = model.predict(image)
        predict_class = np.argmax(predict)
        confidence = np.max(predict)

        if confidence < 0.70:
            st.warning('''Confidence of the prediction is low.
                       Please upload a clear image of animal that only listed here''')
            
        else:
            st.success(f"Confidence of the prediction is {confidence*100:.2f}")

            if predict_class == 0:
                st.info("Dog")
            elif predict_class == 1:
                st.info("Horse")
            elif predict_class == 2:
                st.info("Elephant")
            elif predict_class == 3:
                st.info("Butterfly")
            elif predict_class == 4:
                st.info("Chicken")
            elif predict_class == 5:
                st.info("Cat")
            elif predict_class == 6:
                st.info("Cow")
            elif predict_class == 7:
                st.info("Sheep")
            elif predict_class == 8:
                st.info("Spider")
            elif predict_class == 9:
                st.info("Squirrel")

    else:
        st.warning("Please upload animal Image")
