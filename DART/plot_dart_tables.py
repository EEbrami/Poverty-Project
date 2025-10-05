import pandas as pd
import matplotlib.pyplot as plt

# Load data
median_df = pd.read_csv('dart-table_dhi_median.csv')
pr_df = pd.read_csv('dart-table_dhi_pr.csv')

# List of countries
countries = median_df['countries'].unique()
years = median_df.columns[1:]

# Plot DHI Median over time
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = median_df[median_df['countries'] == country]
    plt.plot(years, country_data.iloc[0, 1:], label=country)
plt.xlabel('Year')
plt.ylabel('DHI Median')
plt.title('DHI Median over Time by Country')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)  # Faded grid
plt.tight_layout()
plt.savefig('dart_median_by_country.png')
plt.show()

# Plot DHI PR over time
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = pr_df[pr_df['countries'] == country]
    plt.plot(years, country_data.iloc[0, 1:], label=country)
plt.xlabel('Year')
plt.ylabel('DHI PR')
plt.title('DHI PR over Time by Country')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)  # Faded grid
plt.tight_layout()
plt.savefig('dart_pr_by_country.png')
plt.show()
