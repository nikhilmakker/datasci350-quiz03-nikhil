import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Read the fitness tracker data
with open('fitness_data.txt', 'r') as f:
    lines = f.readlines()

# Skip the header comment and read the data
data_str = ''.join(lines[1:])
from io import StringIO
df = pd.read_csv(StringIO(data_str), sep=r'\s+')

# Convert date column to datetime objects
df['date'] = pd.to_datetime(df['date'])

# Print basic statistics
print("Fitness Tracker Analysis:")
print("=========================")
print(f"Total days analysed: {len(df)}")
print(f"Average daily steps: {df['steps'].mean():,.0f}")
print(f"Total calories burned: {df['calories_burned'].sum():,.0f}")
print(f"Average calories per day: {df['calories_burned'].mean():,.0f}")
peak_idx = df['steps'].idxmax()
peak_date = str(df.at[peak_idx, 'date'])
print(f"Peak activity day: {peak_date} with {df.at[peak_idx, 'steps']:,} steps")
print(f"Average resting heart rate: {df['heart_rate_avg'].mean():.1f} bpm")
print(f"Average sleep duration: {df['sleep_hours'].mean():.1f} hours")

# Create a visualisation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
sns.set_style("whitegrid")

# Plot 1: Daily steps and calories
ax1.plot(df['date'], df['steps'], marker='o', color='steelblue', linewidth=2, label='Steps')
ax1.set_xlabel('Date')
ax1.set_ylabel('Steps', color='steelblue')
ax1.set_title('Daily Steps and Calories Burned', fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='steelblue')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)

ax1b = ax1.twinx()
ax1b.plot(df['date'], df['calories_burned'], marker='s', color='coral', linewidth=2, label='Calories')
ax1b.set_ylabel('Calories Burned', color='coral')
ax1b.tick_params(axis='y', labelcolor='coral')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Plot 2: Heart rate and sleep
ax2.bar(df['date'], df['sleep_hours'], color='mediumpurple', alpha=0.7, label='Sleep (hours)')
ax2.set_xlabel('Date')
ax2.set_ylabel('Sleep (hours)', color='mediumpurple')
ax2.set_title('Sleep Duration and Heart Rate', fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='mediumpurple')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)

ax2b = ax2.twinx()
ax2b.plot(df['date'], df['heart_rate_avg'], marker='D', color='crimson', linewidth=2, label='Heart Rate (bpm)')
ax2b.set_ylabel('Heart Rate (bpm)', color='crimson')
ax2b.tick_params(axis='y', labelcolor='crimson')

lines3, labels3 = ax2.get_legend_handles_labels()
lines4, labels4 = ax2b.get_legend_handles_labels()
ax2.legend(lines3 + lines4, labels3 + labels4, loc='upper left')

plt.tight_layout()
fig.suptitle('30-Day Fitness Tracker Report', fontsize=18, fontweight='bold', y=1.02)

# Save the figure
plt.savefig('fitness_analysis.png', bbox_inches='tight', dpi=300)
print("\nAnalysis complete. Results saved to 'fitness_analysis.png'")
