import pandas as pd
import matplotlib.pyplot as plt

# I am trying different encodings one by one because I had problems with loading the csv file
encodings_to_try = ['utf-8', 'latin1', 'cp1252']

for encoding in encodings_to_try:
    try:
        data = pd.read_csv('Median_Household_Income_2015.csv', encoding=encoding)
        print("File loaded successfully using encoding:", encoding)
        break
    except UnicodeDecodeError:
        print("Failed to load using encoding:", encoding)

# Display the first few rows of the dataset
# print(data.head())

# Geographic Area             City Median Income
# 0              AL       Abanda CDP         11207
# 1              AL   Abbeville city         25615
# 2              AL  Adamsville city         42575
# 3              AL     Addison town         37083
# 4              AL       Akron town         21667

# Summary statistics
# print(data.describe())

# Geographic Area           City Median Income
# count            29322          29322         29271
# unique              51          24249         14592
# top                 PA  Franklin city           (X)
# freq              1762             16          1113
#        Geographic Area           City Median Income
# count            29322          29322         29271
# unique              51          24249         14592
# top                 PA  Franklin city           (X)
# freq              1762             16          1113

# Data Info - 3 columns and 29322 entries
# print(data.info())

# Finding 10 households with the biggest income for 2015

# Clean and convert 'Median Income' column to numeric (remove non-numeric characters and handle missing values)
# data['Median Income'] = pd.to_numeric(data['Median Income'], errors='coerce')
# 
# # Sort the data by 'Median Income' column in descending order and select the top 10 households
# top_10_households = data.sort_values(by='Median Income', ascending=False).head(10)
# 
# # Display the top 10 households
# print(top_10_households)
# 
# # Geographic Area                               City  Median Income
# # 3555               CO                        Crisman CDP       244083.0
# # 17785              NY                  Scarsdale village       242782.0
# # 11024              MD  Chevy Chase Section Three village       242500.0
# # 2521               CA                  Hidden Hills city       241667.0
# # 11025              MD              Chevy Chase View town       238125.0
# # 3529               CO          Cherry Hills Village city       237569.0
# # 24723              TX           Bunker Hill Village city       236250.0
# # 26945              VA                    Great Falls CDP       234091.0
# # 9983               KY                      Glenview city       233036.0
# # 17522              NY                 Muttontown village       230179.0
# 
# # Now I am creating bar chart using Matplotlib
# # Create a horizontal bar chart
# plt.figure(figsize=(10, 6))
# plt.bar(data['City'], data['Median Income'], color='skyblue')
# plt.xlabel('City')
# plt.ylabel('Median Income')
# plt.title('Median Income by City')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.tight_layout()
# plt.show()