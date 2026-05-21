# 🌊 Tsunami Risk Prediction System

An AI-powered **Tsunami Risk Prediction System** built using **Machine Learning** and **Streamlit** for real-time earthquake threat assessment. This application predicts the likelihood of tsunami occurrence based on earthquake-related parameters and provides a modern disaster monitoring dashboard.

---

## 🚀 Features

✅ Real-time tsunami risk prediction  
✅ Interactive and modern Streamlit dashboard  
✅ Machine Learning-based disaster assessment  
✅ Confidence meter for predictions  
✅ Geological safety override system  
✅ Emergency alert ticker with disaster safety information  
✅ User-friendly earthquake parameter inputs

---

## 🛠️ Tech Stack

- **Python**
- **Machine Learning (SVM Model)**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Streamlit**
- **Joblib**

---

## 📊 Machine Learning Model

This project uses a **Support Vector Machine (SVM)** classifier for tsunami prediction.

### Model Comparison

| Algorithm | Accuracy |
|------------|-----------|
| K-Nearest Neighbors (KNN) | 84.07% |
| Support Vector Machine (SVM) | **85.35%** |
| Tuned SVM (GridSearchCV) | 82.16% |

**Selected Model:** Support Vector Machine (SVM)

Reason:
- Best overall accuracy
- Better balance between precision and recall
- More stable real-world prediction performance

---

## 🌍 Input Parameters

The prediction model analyzes:

- Magnitude
- Earthquake Depth
- Community Determined Intensity (CDI)
- Modified Mercalli Intensity (MMI)
- Number of Stations
- Distance to Nearest Station
- Azimuthal Gap
- Latitude
- Longitude

---

## 📸 Application Preview

Create a folder named:

```text
screenshots
