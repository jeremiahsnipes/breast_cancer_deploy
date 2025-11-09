# I’m importing the libraries I need.
# pandas helps me load and clean the data,
# scikit-learn gives me tools to split and build the model,
# and pickle lets me save the finished model for later use.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# The dataset doesn’t come with column names, so I’m adding them manually
# to make everything easier to read and work with.
col_names = [
    'Sample_code_number','Clump_Thickness','Uniformity_of_Cell_Size',
    'Uniformity_of_Cell_Shape','Marginal_Adhesion','Single_Epithelial_Cell_Size',
    'Bare_Nuclei','Bland_Chromatin','Normal_Nucleoli','Mitoses','Class'
]

# I’m loading the data and telling pandas to skip any bad rows.
# In this dataset, missing values are marked as question marks,
# so I’m replacing them with proper null values, dropping the bad rows,
# and converting everything to numbers.
df = pd.read_csv("breast_cancer_data.csv", names=col_names, on_bad_lines='skip')
df = df.replace('?', pd.NA).dropna().apply(pd.to_numeric)

# I’m separating the input features from the label I want to predict.
# “X” holds the tumor measurements, and “y” holds the diagnosis (2 or 4).
X = df.drop(['Sample_code_number', 'Class'], axis=1)
y = df['Class']

# I’m splitting the data into training and testing sets.
# This lets me teach the model with most of the data
# and then check how accurate it is on unseen examples.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# I’m using Logistic Regression here because it’s simple, fast,
# and works great for binary outcomes like benign vs malignant.
# The max_iter=1000 just gives it enough time to finish training.
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# I’m checking how well the model performs on the test data.
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained. Accuracy on test data: {accuracy:.3f}")

# Now I’m saving the trained model so my Flask app can load it later.
# This way I don’t have to retrain the model every time the app starts.
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("💾 Model saved as model.pkl")
