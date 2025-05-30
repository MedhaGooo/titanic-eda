import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv('Titanic-Dataset2.csv')

# Basic info
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Plot Age distribution
plt.figure(figsize=(10,6))
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# Plot Survival count by Sex
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Survival Count by Sex')
plt.show()

# Plot Survival rate by Pclass
plt.figure(figsize=(8,5))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.show()

# Interactive pie chart of survival
fig = px.pie(df, names='Survived', title='Survival Proportion')
fig.show()
