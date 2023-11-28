# Importing the required libraries for data processing and visualization.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame from a CSV file named 'Train.csv'.
# The file is expected to be in the same directory as the script or a path needs to be provided.
data = pd.read_csv('Train.csv')

# Perform a correlation analysis between the weight of the items (in grams) and the delivery timeliness.
# The delivery timeliness is a binary variable where 1 indicates a delay and 0 indicates on-time delivery.
# The result is a Pearson correlation coefficient indicating the linear relationship between these two variables.
weight_delivery_correlation = data['Weight_in_gms'].corr(data['Reached.on.Time_Y.N'])
# Print the correlation result to the console with an informative message.
print(f"Correlation between Weight and Delivery Timeliness: {weight_delivery_correlation}")

# Perform a group by analysis to calculate on-time delivery rates by warehouse block.
# The data is grouped by 'Warehouse_block', and the on-time delivery status is counted.
# Normalizing the counts to get a percentage and unstacking the multi-level index for easier plotting.
warehouse_delivery = data.groupby('Warehouse_block')['Reached.on.Time_Y.N'].value_counts(normalize=True).unstack() * 100

# Repeat the group by analysis to calculate on-time delivery rates by mode of shipment.
# Similar to the warehouse block analysis, but grouping by 'Mode_of_Shipment' this time.
shipment_mode_delivery = data.groupby('Mode_of_Shipment')['Reached.on.Time_Y.N'].value_counts(normalize=True).unstack() * 100

# Data visualization section to create bar plots for on-time delivery rates by warehouse block.
# The plot is a stacked bar chart representing the percentage of on-time and late deliveries for each warehouse block.
warehouse_delivery.plot(kind='bar', stacked=True)
# Set the title of the plot for clarity.
plt.title('On-time Delivery Rates by Warehouse Block')
# Label the y-axis as 'Percentage' to indicate what the bar heights represent.
plt.ylabel('Percentage')
# Label the x-axis as 'Warehouse Block' to indicate the categories along the x-axis.
plt.xlabel('Warehouse Block')
# Display the plot. The 'show()' function is necessary to render the plot in some Python environments.
plt.show()

# Create and display a similar bar plot for on-time delivery rates by mode of shipment.
shipment_mode_delivery.plot(kind='bar', stacked=True)
plt.title('On-time Delivery Rates by Mode of Shipment')
plt.ylabel('Percentage')
plt.xlabel('Mode of Shipment')
plt.show()
