
# HeartFailurePrediction
A machine learning project that predicts the risk of heart failure based on clinical records. Trained using Random Forest and deployed with a Flask web application for real-time predictions. Built as part of a predictive modeling bootcamp.


## Project Structure

HeartFailurePrediction/\
├── model_training.ipynb &emsp;&emsp;      # Jupyter notebook for model training\
├── model.pkl        &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;          # Saved ML model\
├── scaler.pkl   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              # Saved scaler for preprocessing\
├── app.py   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                  # Flask backend\
├── templates/\
│   └── index.html     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        # HTML form with inline CSS


## Model

--> Algorithm: Random Forest Classifier

--> Accuracy: ~85% on test data

--> Target: DEATH_EVENT (1 = death occurred, 0 = no death)
## Features

~ Trained ML model using clinical data

~ Flask app with form inputs for 13 health indicators

~ Clean UI with inline CSS

~ Real-time prediction and display of result
## Dataset

Source: Provided by Bootcamp

Filename: heart_failure_clinical_records_dataset.csv

Contains clinical features like age, platelets, serum sodium, creatinine, diabetes, etc.
## Run Locally

Clone the project

```bash
  git clone https://github.com/mrdeyroy/heart-failure-predictor.git
```

Go to the project directory

```bash
  cd heart-failure-predictor
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Flask App

```bash
  python app.py

```


## requirements.txt
flask==2.3.2\
numpy==1.24.3\
pandas==2.1.0\
scikit-learn==1.3.0\
matplotlib==3.7.1\
seaborn==0.12.2
