
import matplotlib.pyplot as plt

# Data
companies = [
    "Apple", "Microsoft", "Amazon", "Google", "Facebook", "Alibaba", "Tencent",
    "Berkshire Hathaway", "Samsung", "Toyota", "Volkswagen", "Sony", "Huawei",
    "IBM", "Intel", "Xiaomi", "Nike", "Disney", "Tesla", "Adobe"
]
revenue = [
    274515, 143015, 386064, 182527, 85965, 109480, 73657, 245510, 211940,
    275288, 275188, 75875, 136700, 73563, 77967, 37850, 37403, 65432, 31536, 12910
]
employees = [
    147000, 181000, 1298000, 135301, 58604, 252084, 85858, 360000, 287439,
    366283, 304174, 111700, 197000, 345900, 110600, 23000, 75400, 223000, 70757, 22630
]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change the width and height of the chart
scatter = ax.scatter(
    revenue,
    employees,
    alpha=0.8,
    c=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF2',
        '#FFA533', '#FF3333', '#85FF33', '#33FF85', '#FF8533', '#3385FF',
        '#FF3385', '#85FF33', '#FF33F2', '#33A6FF', '#FF5733', '#33A6FF',
        '#85A6FF', '#A63385'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Revenue vs Number of Employees in Top Tech Companies', fontsize=14)
ax.set_xlabel('Revenue (in million USD)', fontsize=12)
ax.set_ylabel('Number of Employees', fontsize=12)

# Adding the company names as labels next to each point
for i, company in enumerate(companies):
    ax.annotate(company, (revenue[i], employees[i]), fontsize=8)

plt.show()