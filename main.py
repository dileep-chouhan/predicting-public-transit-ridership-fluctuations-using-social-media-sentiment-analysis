import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
# Set a random seed for reproducibility
np.random.seed(42)
# Generate synthetic data for public transit ridership and social media sentiment
num_days = 365
dates = pd.to_datetime(pd.date_range(start='2023-01-01', periods=num_days))
ridership = 1000 + 200 * np.sin(2 * np.pi * np.arange(num_days) / 30) + 50 * np.random.randn(num_days) # Seasonal trend + noise
sentiment = 0.5 + 0.2 * np.sin(2 * np.pi * np.arange(num_days) / 7) + 0.1 * np.random.randn(num_days) # Weekly trend + noise
# Ensure sentiment stays within [0,1] range
sentiment = np.clip(sentiment, 0, 1)
data = {
    'Date': dates,
    'Ridership': ridership,
    'Sentiment': sentiment
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Feature Engineering ---
# (In a real-world scenario, this would involve more extensive cleaning and preprocessing)
df['DayofWeek'] = df['Date'].dt.dayofweek
df['Month'] = df['Date'].dt.month
# --- 3. Analysis ---
# Calculate correlation between ridership and sentiment
correlation = df['Ridership'].corr(df['Sentiment'])
print(f"Correlation between Ridership and Sentiment: {correlation}")
# Analyze ridership by day of week
avg_ridership_by_day = df.groupby('DayofWeek')['Ridership'].mean()
print("\nAverage Ridership by Day of Week:")
print(avg_ridership_by_day)
#Analyze ridership by month
avg_ridership_by_month = df.groupby('Month')['Ridership'].mean()
print("\nAverage Ridership by Month:")
print(avg_ridership_by_month)
# --- 4. Visualization ---
# Plot ridership and sentiment over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Ridership'], label='Ridership')
plt.plot(df['Date'], df['Sentiment'] * 1000, label='Sentiment (scaled)') # Scale sentiment for better visualization
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Ridership and Sentiment Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('ridership_sentiment_plot.png')
print("Plot saved to ridership_sentiment_plot.png")
#Plot average ridership by day of the week
plt.figure(figsize=(8,6))
sns.barplot(x=avg_ridership_by_day.index, y=avg_ridership_by_day.values)
plt.xlabel("Day of Week (0=Monday, 6=Sunday)")
plt.ylabel("Average Ridership")
plt.title("Average Ridership by Day of Week")
plt.savefig("ridership_by_day.png")
print("Plot saved to ridership_by_day.png")
#Plot average ridership by month
plt.figure(figsize=(10,6))
sns.barplot(x=avg_ridership_by_month.index, y=avg_ridership_by_month.values)
plt.xlabel("Month")
plt.ylabel("Average Ridership")
plt.title("Average Ridership by Month")
plt.savefig("ridership_by_month.png")
print("Plot saved to ridership_by_month.png")