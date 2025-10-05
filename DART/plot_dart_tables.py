import pandas as pd
import matplotlib.pyplot as plt

# Load data
median_df = pd.read_csv("DART/dart-table_dhi_median.csv")
pr_df = pd.read_csv("DART/dart-table_dhi_pr.csv")

# Set up years from column names (exclude 'countries')
years = median_df.columns[1:]

# Plot median values
plt.figure(figsize=(12, 6))
for idx, row in median_df.iterrows():
    plt.plot(years, row[1:], label=row['countries'])
plt.title("DHI Median by Country")
plt.xlabel("Year")
plt.ylabel("Median Value")
plt.legend()
plt.grid(True, which='both', alpha=0.2)  # faded grid
plt.tight_layout()
plt.show()

# Plot pr values
plt.figure(figsize=(12, 6))
for idx, row in pr_df.iterrows():
    plt.plot(years, row[1:], label=row['countries'])
plt.title("DHI PR by Country")
plt.xlabel("Year")
plt.ylabel("PR Value")
plt.legend()
plt.grid(True, which='both', alpha=0.2)  # faded grid
plt.tight_layout()
plt.show()
