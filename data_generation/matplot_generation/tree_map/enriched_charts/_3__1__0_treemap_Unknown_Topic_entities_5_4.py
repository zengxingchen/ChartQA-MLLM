
import matplotlib.pyplot as plt
import squarify

categories = ['Rent', 'Utilities', 'Groceries', 'Transportation', 'Insurance', 'Healthcare', 'Leisure', 'Travel', 'Savings', 'Education', 'Dining', 'Clothing', 'Miscellaneous']
expenditure = [150000, 30000, 100000, 45000, 25000, 50000, 20000, 35000, 75000, 40000, 15000, 10000, 5000]

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500', '#9ACD32', '#483D8B', '#20B2AA', '#FA8072', '#778899']

plt.figure(figsize=(14, 12))

squarify.plot(sizes=expenditure, label=categories, color=colors, alpha=0.8)

plt.title('Monthly Household Expenditure Distribution', fontsize=22)

plt.axis('off')

plt.show()