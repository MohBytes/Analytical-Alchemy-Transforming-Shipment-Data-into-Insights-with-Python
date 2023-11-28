# Import the pandas package for data manipulation and matplotlib.pyplot for plotting.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Train.csv')

# Analyzing Delivery Performance by Warehouse Block
# Group the data by 'Warehouse_block' and calculate the mean value of 'Reached.on.Time_Y.N'
# which indicates whether the delivery was on time (0) or not (1).
delivery_performance_by_block = data.groupby('Warehouse_block')['Reached.on.Time_Y.N'].mean().reset_index()

# Analyzing Customer Satisfaction by Warehouse Block
# Calculate the average customer rating for each warehouse block.
customer_satisfaction_by_block = data.groupby('Warehouse_block')['Customer_rating'].mean().reset_index()

# Analyzing Product Distribution Across Warehouse Blocks
# Count the number of products distributed from each warehouse block.
product_distribution_by_block = data['Warehouse_block'].value_counts().reset_index()
product_distribution_by_block.columns = ['Warehouse_block', 'Number_of_Products']

# Data Visualization
plt.figure(figsize=(18, 6))

# Delivery Performance Visualization
plt.subplot(1, 3, 1)
sns.barplot(x='Warehouse_block', y='Reached.on.Time_Y.N', data=delivery_performance_by_block)
plt.title('Delivery Performance by Warehouse Block')
plt.xlabel('Warehouse Block')
plt.ylabel('Average Late Delivery Rate')

# Customer Satisfaction Visualization
plt.subplot(1, 3, 2)
sns.barplot(x='Warehouse_block', y='Customer_rating', data=customer_satisfaction_by_block)
plt.title('Customer Satisfaction by Warehouse Block')
plt.xlabel('Warehouse Block')
plt.ylabel('Average Customer Rating')

# Product Distribution Visualization
plt.subplot(1, 3, 3)
sns.barplot(x='Warehouse_block', y='Number_of_Products', data=product_distribution_by_block)
plt.title('Product Distribution Across Warehouse Blocks')
plt.xlabel('Warehouse Block')
plt.ylabel('Number of Products')

# Show the plots
plt.tight_layout()
plt.show()
