import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "Online Shopping Data.csv"  # Update this path if needed
df = pd.read_csv(file_path)

# Standardize column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_")

# Convert text columns to title case
text_cols = ["Gender", "Online_Shopping_Freq", "Review_Check_Freq", "Attraction_Factor", 
             "Retailer_Choice_Factors", "Preferred_Payment", "Local_vs_Intl_Retailers",
             "Security_Concern_Level", "Promo_Participation", "Price_Sensitivity",
             "Comfortable_Price_Range", "Frequent_Products", "Major_Drawback",
             "Authenticity_Concern"]

for col in text_cols:
    df[col] = df[col].str.title()

# Set visualization style
sns.set_style("whitegrid")

# Gender Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Gender", palette="pastel")
plt.title("Gender Distribution of Online Shoppers")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Shopping Frequency Distribution
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y="Online_Shopping_Freq", order=df["Online_Shopping_Freq"].value_counts().index, palette="muted")
plt.title("Online Shopping Frequency")
plt.xlabel("Count")
plt.ylabel("Shopping Frequency")
plt.show()

# Attraction Factors for Online Shopping
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y="Attraction_Factor", order=df["Attraction_Factor"].value_counts().index, palette="coolwarm")
plt.title("Main Attraction Factors for Online Shopping")
plt.xlabel("Count")
plt.ylabel("Attraction Factor")
plt.show()

# Preferred Payment Methods
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y="Preferred_Payment", order=df["Preferred_Payment"].value_counts().index, palette="Set2")
plt.title("Preferred Payment Methods for Online Shopping")
plt.xlabel("Count")
plt.ylabel("Payment Method")
plt.show()

# Security Concern Levels
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y="Security_Concern_Level", order=df["Security_Concern_Level"].value_counts().index, palette="coolwarm")
plt.title("Level of Concern About Online Payment Security")
plt.xlabel("Count")
plt.ylabel("Security Concern Level")
plt.show()
