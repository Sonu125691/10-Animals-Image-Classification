# 🐾 Animal Image Classification (10 Classes)

This is an **Image Classification Deep Learning project** that predicts one of the following 10 animals from an input image:

**Dog, Horse, Elephant, Butterfly, Chicken, Cat, Cow, Sheep, Spider, Squirrel**

The project uses **Transfer Learning with MobileNetV2** and has been implemented as a **Streamlit web application**.

---

## 📌 Preprocessing
- Removed unreadable/corrupted image files from dataset
- Resized all images to **224 × 224 × 3**
- Normalized pixel values for CNN input
- Batch size used: **32**

---

## 📈 Model Performance
- **Train Accuracy:** 97.56%, **Train Loss:** 0.0784 
- **Test Accuracy:** 95.87%, **Test Loss:** 0.1484

The model generalizes well and performs strongly on unseen test images.

---
