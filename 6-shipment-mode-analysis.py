# Import the pandas package for data manipulation and matplotlib.pyplot for plotting.
import pandas as pd
import matplotlib.pyplot as plt

# Read data from a CSV file into a pandas DataFrame. This is the initial step in the data analysis process,
# where 'Train.csv' is expected to be in the same directory as the script.
data = pd.read_csv('Train.csv')

# Group the data by 'Mode_of_Shipment' and calculate the average customer rating for each mode.
# The reset_index() method is used to convert the resulting groupby object back into a DataFrame.
satisfaction_by_shipment_mode = data.groupby('Mode_of_Shipment')['Customer_rating'].mean().reset_index()

# Similar to the satisfaction analysis, calculate the average on-time delivery rate (1 for late, 0 for on-time)
# for each shipment mode.
delivery_by_shipment_mode = data.groupby('Mode_of_Shipment')['Reached.on.Time_Y.N'].mean().reset_index()

# For a more comprehensive analysis, aggregate the mean cost of the product and the mean discount offered
# for each mode of shipment. This uses the agg() method to apply different aggregation functions to specific columns.
cost_discount_by_shipment_mode = data.groupby('Mode_of_Shipment').agg({
    'Cost_of_the_Product': 'mean',  # Average cost of the product by shipment mode
    'Discount_offered': 'mean'  # Average discount offered by shipment mode
}).reset_index()

# Set up the matplotlib figure for plotting, specifying the overall size of the figure.
plt.figure(figsize=(14, 7))

# The following sections create individual subplots within the figure for different analyses.

# First subplot: Average Customer Rating by Shipment Mode
plt.subplot(1, 3, 1)  # Indicates that this is the first of three subplots
plt.bar(satisfaction_by_shipment_mode['Mode_of_Shipment'], satisfaction_by_shipment_mode['Customer_rating'])
plt.title('Customer Satisfaction by Shipment Mode')  # Title for this subplot
plt.xlabel('Shipment Mode')  # X-axis label
plt.ylabel('Average Customer Rating')  # Y-axis label

# Second subplot: Average On-time Delivery Rate by Shipment Mode
plt.subplot(1, 3, 2)  # Indicates that this is the second of three subplots
plt.bar(delivery_by_shipment_mode['Mode_of_Shipment'], delivery_by_shipment_mode['Reached.on.Time_Y.N'])
plt.title('Delivery Performance by Shipment Mode')  # Title for this subplot
plt.xlabel('Shipment Mode')  # X-axis label
plt.ylabel('Average On-time Delivery Rate')  # Y-axis label

# Third subplot: Average Cost and Discount by Shipment Mode
plt.subplot(1, 3, 3)  # Indicates that this is the third of three subplots
# Plot the average cost with a label for the legend
plt.bar(cost_discount_by_shipment_mode['Mode_of_Shipment'], cost_discount_by_shipment_mode['Cost_of_the_Product'], label='Average Cost')
# Overlay the average discount with partial transparency (alpha) and a label for the legend
plt.bar(cost_discount_by_shipment_mode['Mode_of_Shipment'], cost_discount_by_shipment_mode['Discount_offered'], label='Average Discount', alpha=0.5)
plt.title('Cost and Discount by Shipment Mode')  # Title for this subplot
plt.xlabel('Shipment Mode')  # X-axis label
plt.legend()  # Display the legend for the plot

# Adjust the layout of the subplots to ensure there is no overlap and everything is clearly visible.
plt.tight_layout()
# Show the complete figure with all subplots.
plt.show()
