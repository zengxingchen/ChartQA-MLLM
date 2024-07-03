
import matplotlib.pyplot as plt
import squarify

# Data
topics = [
    'Startups', 'Innovation', 'Investments', 'Marketing', 'Leadership',
    'Management', 'Strategy', 'Sales', 'Product Development', 'Human Resources',
    'Customer Service', 'Finance', 'Supply Chain', 'Operations', 'Entrepreneurship'
]
values = [
    4500, 4200, 3900, 3600, 3300,
    3000, 2700, 2400, 2100, 1800,
    1500, 1200, 900, 600, 300
]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1',
    '#A133FF', '#FF3333', '#57FF33', '#5733FF', '#FF5733',
    '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF'
]

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=values, label=topics, color=colors, alpha=0.8)
plt.title('Key Areas in Business & Entrepreneurship by Importance', fontsize=20, pad=30)
plt.axis('off')
plt.show()