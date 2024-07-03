
import matplotlib.pyplot as plt
import squarify

categories = [
    'Exhibition Fees', 'Workshops', 'Art Supplies', 'Marketing', 'Travel', 'Venue Rental',
    'Website', 'Licenses', 'Miscellaneous', 'Printing', 'Networking', 'Professional Services',
    'Utilities', 'Food & Beverages', 'Legal Fees', 'Sponsorships', 'Insurance', 'Transport'
]
amounts = [
    1200, 800, 500, 400, 600, 1000, 300, 200, 250, 450, 350, 600, 300, 700, 200, 900, 400, 300
]

colors = [
    '#FF7F50', '#6495ED', '#FFD700', '#FF69B4', '#8A2BE2', '#5F9EA0', '#7FFF00', '#DC143C',
    '#7B68EE', '#FFA07A', '#00FA9A', '#D2691E', '#FF4500', '#FF6347', '#32CD32', '#BA55D3',
    '#DAA520', '#6A5ACD'
]

fig, ax = plt.subplots(1, figsize=(20, 10))

squarify.plot(sizes=amounts, label=categories, color=colors, alpha=0.8)

plt.title('Annual Art Exhibition Budget Breakdown', fontsize=18)

plt.axis('off')

plt.show()