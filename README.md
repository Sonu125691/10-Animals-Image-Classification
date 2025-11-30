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

### Data Augmentation
- `RandomFlip("horizontal")`
- `RandomRotation(0.04)`
- `RandomZoom((-0.1, 0.1))`

These augmentations help the model generalize well on real-world animal images.

---

## 📈 Model Performance
- **Train Accuracy:** 97.56%, **Train Loss:** 0.0784 
- **Test Accuracy:** 95.87%, **Test Loss:** 0.1484

The model generalizes well and performs strongly on unseen test images.

---
