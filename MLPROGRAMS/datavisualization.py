import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Create dataset
data = {
    "Age": [18, 20, 22, 24, 26, 28, 30],
    "Marks": [65, 70, 75, 80, 85, 90, 95]
}
# Convert dictionary to DataFrame
df = pd.DataFrame(data)
# Scatter Plot (Matplotlib)
plt.figure(figsize=(5,4))
plt.scatter(df["Age"], df["Marks"], color="blue")
plt.title("Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()
# Histogram (Seaborn)
plt.figure(figsize=(5,4))
sns.histplot(data=df, x="Marks", bins=5, color="green")
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
# Box Plot (Seaborn)
plt.figure(figsize=(5,4))
sns.boxplot(y=df["Marks"], color="orange")
plt.title("Box Plot")
plt.ylabel("Marks")
plt.show()