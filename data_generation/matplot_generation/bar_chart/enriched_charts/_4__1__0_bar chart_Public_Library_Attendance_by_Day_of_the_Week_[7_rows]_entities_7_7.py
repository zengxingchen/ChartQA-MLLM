
import matplotlib.pyplot as plt

categories = ['Food', 'Transportation', 'Utilities', 'Healthcare', 'Education', 
              'Entertainment', 'Rent', 'Groceries', 'Dining Out', 
              'Insurance', 'Savings', 'Miscellaneous']
expenses = [50.3, 47.8, 45.9, 52.4, 55.3, 58.9, 60.2, 61.6, 57.8, 54.1, 51.5, 48.3]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#33FFA5', '#FF8533', 
          '#8D33FF', '#A833FF', '#FF5733', '#33A5FF', '#FF3385', '#33FF85']

plt.figure(figsize=(10, 8))
bars = plt.barh(categories, expenses, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Monthly Expenses ($)')
plt.title('Monthly Expenses Distribution in 2023')
plt.xlim(40, max(expenses) + 5)
plt.tight_layout()

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()