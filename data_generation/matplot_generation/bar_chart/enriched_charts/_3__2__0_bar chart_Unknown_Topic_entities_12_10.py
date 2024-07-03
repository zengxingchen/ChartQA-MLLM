
import matplotlib.pyplot as plt

countries = ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Netherlands', 
             'Norway', 'Sweden', 'New Zealand', 'Austria', 'Luxembourg', 
             'Canada', 'Australia', 'United Kingdom', 'Ireland', 'Germany', 
             'Belgium', 'United States', 'Czech Republic', 'United Arab Emirates', 
             'Malta', 'France', 'Mexico', 'Taiwan', 'Uruguay']
happiness_scores = [7.8, 7.6, 7.5, 7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 
                    7.1, 7.1, 7.0, 7.0, 6.9, 6.9, 6.8, 6.8, 6.7, 6.7, 
                    6.6, 6.6, 6.5, 6.5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', 
          '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33', '#FF8C33', '#FF5733', 
          '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', '#F633FF', 
          '#F6FF33', '#33A6FF', '#A6FF33', '#FF8C33', '#FF5733', '#33FF57']

plt.figure(figsize=(14, 8))
plt.barh(countries, happiness_scores, color=colors, height=0.5)
plt.xlabel('Happiness Score')
plt.title('Happiness Scores in Various Countries')
plt.xlim(6, max(happiness_scores) + 1)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()