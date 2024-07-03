
import matplotlib.pyplot as plt

countries = ['USA', 'Germany', 'France', 'Italy', 'UK', 'China', 'Spain', 'Russia', 'Canada', 'Australia', 'Japan', 'India']
number_of_museums = [35000, 6200, 5000, 4800, 2500, 6000, 1500, 7000, 2000, 900, 5800, 500]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8333', '#33FFC7', '#A833FF', '#FF3333', '#33A8FF', '#57FF33', '#A8FF33', '#FF33FF']

plt.figure(figsize=(14, 8))
plt.barh(countries, number_of_museums, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Number of Museums', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Number of Museums in Various Countries', fontsize=16)
plt.xlim(0, 40000)

plt.tight_layout()
plt.show()