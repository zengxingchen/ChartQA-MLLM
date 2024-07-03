
import matplotlib.pyplot as plt
import squarify

categories = ['Rent', 'Utilities', 'Groceries', 'Transportation', 'Insurance', 'Healthcare', 'Leisure', 'Travel', 'Savings', 'Education', 'Dining', 'Clothing', 'Miscellaneous', 'Books', 'Streaming', 'Gym', 'Gifts', 'Subscriptions', 'Entertainment', 'Pet Care', 'Charity', 'Home Improvement', 'Childcare', 'Electronics', 'Hobbies']
expenditure = [150000, 30000, 100000, 45000, 25000, 50000, 20000, 35000, 75000, 40000, 15000, 10000, 5000, 8000, 12000, 6000, 11000, 7000, 9000, 13000, 14000, 16000, 17000, 18000, 19000]

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500', '#9ACD32', '#483D8B', '#20B2AA', '#FA8072', '#778899', '#8B0000', '#B22222', '#FF8C00', '#FFB6C1', '#7FFF00', '#5F9EA0', '#FF1493', '#A52A2A', '#D2691E', '#00FF7F', '#DC143C', '#6A5ACD']

plt.figure(figsize=(16, 14))

squarify.plot(sizes=expenditure, label=categories, color=colors, alpha=0.8)

plt.title('Monthly Household Expenditure Breakdown', fontsize=24)

plt.axis('off')

plt.show()