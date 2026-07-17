####clean a dataset with missing values
import pandas as pd
df=pd.DataFrame({"Name":["Ravi","Sita","Rahul","Priya"],"Age":[22,None,25,24],"Salary":[30000,40000,None,56000]})
print("original dataset")
print(df)
##checking missing values
print("/n missing values")
print(df.isnull())
##remove rows with missing vaslues
print("/n drop missing values")
print(df.dropna())
###fill missing values with mean
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("/n after filling missing values")
print(df)
####Apply Label Encoding and One-Hot Encoding
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Dataset
df = pd.DataFrame({"Education": ["School", "Degree", "Masters", "Degree"],
    "Gender": ["Male", "Female", "Male", "Female"],
    "City": ["Chennai", "Mumbai", "Chennai", "Mumbai"]
})
# Label Encoding (Ordinal Data)
le = LabelEncoder()
df["Education"] = le.fit_transform(df["Education"])
# One-Hot Encoding (Nominal Data)
df = pd.get_dummies(df, columns=["Gender", "City"], drop_first=True)
print(df)
