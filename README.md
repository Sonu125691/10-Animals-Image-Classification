# 🐾 Animal Image Classification (10 Classes)

This is an **Image Classification Deep Learning project** that predicts one of the following 10 animals from an input image:

**Dog, Horse, Elephant, Butterfly, Chicken, Cat, Cow, Sheep, Spider, Squirrel**

The project uses **Transfer Learning with MobileNetV2** and has been implemented as a **Streamlit web application**.

---

## 📌 Preprocessing
- Removed unreadable/corrupted images from dataset
- Resized all images to **224 × 224 × 3**
- Normalized pixel values using `Rescaling(1./255)`
- Batch size used: **32**

## 📌 Data Augmentation
To increase dataset variability and prevent overfitting:
- `RandomFlip("horizontal")`
- `RandomRotation(0.04)`
- `RandomZoom((-0.1, 0.1))`

---

## 🤖 Model Architecture
A **CNN model built on top of MobileNetV2** was used for 10-class animal image classification.

Total parameters: 2,423,754

Trainable parameters: 165,514

Non-trainable parameters: 2,258,240

Model was trained with:
- **EarlyStopping**
- `restore_best_weights = True`

This ensures that the final saved model is the **best-performing version**, not the last epoch.

---

## 📈 Model Performance
- **Train Accuracy:** 97.56%, **Train Loss:** 0.0784 
- **Test Accuracy:** 95.87%, **Test Loss:** 0.1484

The model generalizes well and performs strongly on unseen test images.

---

## 🤖 Model Details
- Architecture: **Convolutional Neural Network (CNN)**
- Framework: **TensorFlow**

---

## ▶️ Run the Project on Your Computer
**To run this project locally, use the following commands in your terminal:**

pip install -r requirements.txt

streamlit run app.py

**These commands will install the required libraries and open the app in your browser (running locally on your computer).**
