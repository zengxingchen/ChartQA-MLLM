
import matplotlib.pyplot as plt

countries = ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Netherlands', 
             'Norway', 'Sweden', 'New Zealand', 'Austria', 'Luxembourg', 
             'Canada', 'Australia', 'United Kingdom', 'Ireland', 'Germany', 
             'Belgium', 'United States', 'Czech Republic', 'United Arab Emirates', 
             'Malta', 'France', 'Mexico', 'Taiwan', 'Uruguay']
average_sleep_hours = [8.2, 8.1, 8.0, 7.9, 7.8, 7.7, 7.6, 7.5, 7.4, 7.3, 
                       7.2, 7.1, 7.0, 6.9, 6.8, 6.7, 6.6, 6.5, 6.4, 6.3, 
                       6.2, 6.1, 6.0, 5.9]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
          '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
          '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(12, 10))
plt.bar(countries, average_sleep_hours, color=colors, width=0.6)
plt.ylabel('Average Sleep Hours')
plt.title('Average Sleep Hours per Night in Various Countries', pad=20)
plt.ylim(5.5, 9)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()