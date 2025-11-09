# 🧬 Breast Cancer Cell Analysis — Flask ML Deployment

A complete end-to-end **machine learning deployment project** predicting whether a breast tumor is **benign** or **malignant** based on nine microscopic cell characteristics.  
Developed and deployed by **Jeremiah Snipes** for **ANA 680: Machine Learning Deployment** at *National University*.

---

## 📘 Overview

This project demonstrates how a trained machine learning model can be deployed as an interactive web application using **Flask** and **Heroku**.  

The model uses cell-level measurements from the *Breast Cancer Wisconsin Dataset* to predict whether a sample is benign (non-cancerous) or malignant (cancerous).  

Users interact with the web interface by adjusting sliders (1–10) that represent how abnormal the cells appear under a microscope. The app returns an instant prediction.

---

## 🧠 How It Works

1. **Model Training**
   - Data: Breast Cancer Wisconsin (Original) dataset  
   - Model: Logistic Regression (scikit-learn)  
   - Output: `model.pkl`  
   - Script: `train_and_save_model.py`

2. **Web Application**
   - Flask loads the saved model (`model.pkl`)
   - Inputs are entered via an HTML interface with sliders
   - The model returns one of two possible results:
     - **Tumor is likely Benign**
     - **Tumor is likely Malignant**

3. **Deployment**
   - Hosted on **Heroku** using **Gunicorn** as the production WSGI server  
   - `Procfile` defines the web process:web: gunicorn app:app
---
## 🧩 Project Structure

breast_cancer_deploy/
│
├── app.py # Flask web app
├── train_and_save_model.py # Model training script
├── model.pkl # Trained Logistic Regression model
├── breast_cancer_data.csv # Dataset
├── templates/
│ └── index.html # Frontend interface
├── requirements.txt # Dependencies
├── Procfile # Heroku process file
└── .github/workflows/ # (Optional) CI/CD pipeline

yaml
Copy code

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Flask** — micro web framework  
- **scikit-learn** — machine learning  
- **pandas / numpy** — data wrangling  
- **Gunicorn** — production server  
- **Heroku** — deployment platform  

---

## 🌐 Live Application

**Heroku App:**  
🔗 [https://breast-cancer-deploy-js-f16b183e339e.herokuapp.com/](https://breast-cancer-deploy-js-f16b183e339e.herokuapp.com/)  

**GitHub Repository:**  
🔗 [https://github.com/jeremiahsnipes/breast_cancer_deploy](https://github.com/jeremiahsnipes/breast_cancer_deploy)

---

## 🩺 Dataset Description

**Source:** UCI Machine Learning Repository — *Breast Cancer Wisconsin (Original) Dataset*  
**Features:**
1. Clump Thickness  
2. Uniformity of Cell Size  
3. Uniformity of Cell Shape  
4. Marginal Adhesion  
5. Single Epithelial Cell Size  
6. Bare Nuclei  
7. Bland Chromatin  
8. Normal Nucleoli  
9. Mitoses  

Each feature is rated from **1 (normal)** to **10 (very abnormal)** based on microscopic analysis.
