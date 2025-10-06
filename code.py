#index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load dataset
df=pd.read_csv("C:\\Python\\Unemployment in India.csv")
print(df.head())

df[' Date'] = pd.to_datetime(df[' Date'], errors='coerce', dayfirst=True)

# --- Step 3: Drop missing values ---
df = df.dropna()

# --- Step 4: Summary Statistics ---
summary_stats = {
    "Average Unemployment Rate (%)": df[' Estimated Unemployment Rate (%)'].mean(),
    "Highest Unemployment Rate (%)": df[' Estimated Unemployment Rate (%)'].max(),
    "Lowest Unemployment Rate (%)": df[' Estimated Unemployment Rate (%)'].min()
}
print("📌 Summary Statistics:\n", summary_stats)

# --- Step 5: Visualizations ---

# 1. Unemployment trend over time (overall)
plt.figure(figsize=(12,6))
plt.plot(df[' Date'], df[' Estimated Unemployment Rate (%)'], marker='o', linestyle='-', alpha=0.6)
plt.title("Unemployment Rate Over Time (All Regions)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# 2. Average unemployment by state/region
region_avg = df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean().sort_values()
plt.figure(figsize=(12,6))
region_avg.plot(kind='bar', color='skyblue')
plt.title("Average Unemployment Rate by State")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=90)
plt.show()

# 3. Unemployment vs Labour Participation Rate
plt.figure(figsize=(8,6))
plt.scatter(df[' Estimated Labour Participation Rate (%)'], df[' Estimated Unemployment Rate (%)'], alpha=0.6)
plt.title("Unemployment vs Labour Participation Rate")
plt.xlabel("Labour Participation Rate (%)")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# 4. Employment trend over time
plt.figure(figsize=(12,6))
plt.plot(df[' Date'], df[' Estimated Employed'], color='green', alpha=0.7)
plt.title("Estimated Employment Over Time")
plt.xlabel("Date")
plt.ylabel("Estimated Employed")
plt.grid(True)
plt.show()

# 5. Average unemployment by area (Rural/Urban)
area_avg = df.groupby('Area')[' Estimated Unemployment Rate (%)'].mean().sort_values()
plt.figure(figsize=(8,6))
area_avg.plot(kind='bar', color='orange')
plt.title("Average Unemployment Rate by Area")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# 6. State-wise unemployment trends (Top 5 states with most data points)
top_states = df['Region'].value_counts().head(5).index
plt.figure(figsize=(14,7))
for state in top_states:
    state_data = df[df['Region'] == state]
    plt.plot(state_data[' Date'], state_data[' Estimated Unemployment Rate (%)'], label=state)

plt.title("Unemployment Rate Trend (Top 5 States)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend()
plt.grid(True)
plt.show()
