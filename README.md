Diabetes Prediction using Support Vector Machine (SVM)
This project is focused on building a machine learning model that predicts whether a person is diabetic or not based on various medical features. The dataset used in this project contains medical details such as glucose levels, blood pressure, skin thickness, BMI, insulin levels, and more, to predict diabetes outcome.

Dependencies
numpy: For numerical operations and handling data.

pandas: For loading, analyzing, and manipulating data in tabular form.

scikit-learn: For machine learning models, data preprocessing, and splitting data into training and test sets.

matplotlib: For plotting graphs (if needed).

To install the required libraries, run the following:

bash
Copy
Edit
pip install numpy pandas scikit-learn
Dataset
The dataset used in this project is the Pima Indians Diabetes Database, which contains data on women of Pima Indian heritage and whether they are diabetic or not. The dataset contains the following columns:

Pregnancies: Number of times pregnant.

Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test.

BloodPressure: Diastolic blood pressure (mm Hg).

SkinThickness: Triceps skin fold thickness (mm).

Insulin: 2-Hour serum insulin (mu U/ml).

BMI: Body mass index (weight in kg/(height in m)^2).

DiabetesPedigreeFunction: Diabetes pedigree function (a function that scores the likelihood of diabetes based on family history).

Age: Age (in years).

Outcome: 1 if the person is diabetic, 0 if not.

Project Workflow
Data Collection and Analysis:

The dataset is loaded into a Pandas DataFrame.

Basic statistics of the dataset are analyzed, including the distribution of diabetes outcomes (Outcome column).

Data Preprocessing:

Data is standardized using StandardScaler to scale the features to the same scale.

Train-Test Split:

The data is split into training and testing sets with an 80-20% ratio, maintaining the proportion of diabetes cases using the stratify parameter.

Model Training:

A Support Vector Machine (SVM) classifier with a linear kernel is used to train the model on the training data.

Model Evaluation:

The accuracy of the model is calculated for both training and test datasets to assess performance.

Making Predictions:

A sample input is taken (e.g., a person's medical data) and standardized.

The trained classifier predicts whether the person is diabetic or not.

Results
After training, the model's accuracy on both the training and test datasets is calculated. Based on the trained model, it predicts whether a given set of medical data indicates a diabetic person or not.

Sample Prediction
python
Copy
Edit
input_data = (4, 110, 92, 0, 0, 37.6, 0.191, 30)
The above data corresponds to a person with:

4 pregnancies

Glucose level of 110 mg/dl

Blood pressure of 92 mm Hg

Skin thickness of 0 mm

Insulin level of 0

BMI of 37.6

Diabetes Pedigree Function of 0.191

Age of 30 years

The model predicts if this person is diabetic or not based on the given medical features.

Example Output:
csharp
Copy
Edit
The person is diabetic
Conclusion
This project demonstrates how machine learning, particularly Support Vector Machines, can be used to predict diabetes in individuals based on their medical data. By standardizing the data and splitting it into training and testing sets, the model can generalize well to unseen data, providing accurate predictions.

