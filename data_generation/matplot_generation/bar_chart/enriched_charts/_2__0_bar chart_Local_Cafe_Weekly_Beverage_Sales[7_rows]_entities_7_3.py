
import matplotlib.pyplot as plt

countries = ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Netherlands',
             'Norway', 'Sweden', 'Luxembourg', 'New Zealand', 'Austria',
             'Australia', 'Israel', 'Germany', 'Canada', 'Ireland', 
             'Costa Rica', 'United Kingdom', 'Czech Republic', 'United States', 'Belgium']
happiness_scores = [7.84, 7.62, 7.57, 7.55, 7.46, 7.39, 7.36, 7.32, 7.28, 7.27,
                    7.18, 7.16, 7.15, 7.10, 7.08, 7.07, 7.06, 6.97, 6.95, 6.92]

colors = ['#FF9999', '#FF6666', '#FF3333', '#FF0000', '#CC0000', 
          '#990000', '#660000', '#FFCC99', '#FF9933', '#FFCC33', 
          '#FFCC00', '#CC9900', '#999900', '#666600', '#339933', 
          '#33CC33', '#66FF33', '#99FF66', '#CCFF99', '#FFFF99']

plt.figure(figsize=(10, 12))
plt.barh(countries, happiness_scores, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Happiness Score', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Happiness Scores by Country in 2021', fontsize=16)
plt.xlim(6.5, 8.0)

plt.tight_layout()
plt.show()