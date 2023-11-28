# Import the pandas library for data manipulation and the matplotlib library for plotting.
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file named 'Train.csv' into a pandas DataFrame called 'data'.
# This assumes that the CSV file is in the same directory as the script.
data = pd.read_csv('Train.csv')

# Perform an analysis on customer satisfaction levels based on the importance of the product.
# Group the data by the 'Product_importance' category and calculate the mean customer rating for each group.
# Reset the index to convert the resulting series into a DataFrame.
satisfaction_by_importance = data.groupby('Product_importance')['Customer_rating'].mean().reset_index()

# Analyze delivery performance, which is measured by whether products reached on time or not.
# Group the data by 'Product_importance' and calculate the mean value of the 'Reached.on.Time_Y.N' column,
# which indicates delivery performance (1 for late, 0 for on-time).
delivery_by_importance = data.groupby('Product_importance')['Reached.on.Time_Y.N'].mean().reset_index()

# Analyze customer care calls and discounts offered, grouped by the importance of the product.
# Use the aggregate (agg) method to calculate the mean number of customer care calls and the mean discount offered,
# providing a dictionary to specify the operations for each column.
calls_and_discounts_by_importance = data.groupby('Product_importance').agg({
    'Customer_care_calls': 'mean',  # Calculate the average number of customer care calls.
    'Discount_offered': 'mean'  # Calculate the average discount offered.
}).reset_index()

# Begin creating plots to visualize the data. Set the figure size to 10x5 inches for better readability.
plt.figure(figsize=(10, 5))

# Create the first subplot for customer satisfaction.
plt.subplot(1, 3, 1)  # Indicate that this is the first of three subplots (1 row, 3 columns, 1st subplot).
plt.bar(satisfaction_by_importance['Product_importance'], satisfaction_by_importance['Customer_rating'])
plt.title('Customer Satisfaction by Product Importance')  # Title for the plot.
plt.xlabel('Product Importance')  # Label for the x-axis.
plt.ylabel('Average Customer Rating')  # Label for the y-axis.

# Create the second subplot for delivery performance.
plt.subplot(1, 3, 2)  # This is the second subplot.
plt.bar(delivery_by_importance['Product_importance'], delivery_by_importance['Reached.on.Time_Y.N'])
plt.title('Delivery Performance by Product Importance')  # Title for the plot.
plt.xlabel('Product Importance')  # Label for the x-axis.
plt.ylabel('Average On-time Delivery Rate')  # Label for the y-axis.

# Create the third subplot for customer care calls and discounts.
plt.subplot(1, 3, 3)  # This is the third subplot.
# Plot the average number of customer care calls for each product importance category.
plt.bar(calls_and_discounts_by_importance['Product_importance'], calls_and_discounts_by_importance['Customer_care_calls'], label='Customer Care Calls')
# Plot the average discount offered for each product importance category, with partial transparency (alpha).
plt.bar(calls_and_discounts_by_importance['Product_importance'], calls_and_discounts_by_importance['Discount_offered'], label='Discount Offered', alpha=0.5)
plt.title('Calls and Discounts by Product Importance')  # Title for the plot.
plt.xlabel('Product Importance')  # Label for the x-axis.
plt.legend()  # Add a legend to differentiate the bars.

# Adjust the layout to prevent overlapping of subplots.
plt.tight_layout()
# Display the plots on the screen.
plt.show()
