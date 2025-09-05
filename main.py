'''
Descriptive Analysis Project
Written by Chi Vo
Date: August 2025
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('HR_Data_MNC_Data Science Lovers.csv')



'''NOMINAL VARIABLES: Department, Status, Work_Mode'''

print('-- NOMINAL VARIABLES --')

# Find the mode of the nominal variables: Department, Status, Work_Mode
print("\nThe mode of 'Department' variable: ", data['Department'].mode()[0])
print("The mode of 'Status' variable: ", data['Status'].mode()[0])
print("The mode of 'Work_Mode' variable: ", data['Work_Mode'].mode()[0])


# Plot the frequency distribution of the nominal variables -- Department, Status, Work_Mode (histograms?)
plt.figure(figsize=(7,7.5))

plt.subplot(3, 1, 1)
hist1 = sns.histplot(data['Department'])
hist1.set(xlabel=None)
hist1.set_ylabel('Employee Count')
hist1.set_title('Frequency Distribution: Department')

plt.subplot(3, 1, 2)
hist2 = sns.histplot(data['Status'], color='orange')
hist2.set(xlabel=None)
hist2.set_ylabel('Employee Count')
hist2.set_title('Frequency Distribution: Status')

plt.subplot(3, 1, 3)
hist3 = sns.histplot(data['Work_Mode'], color='green')
hist3.set(xlabel=None)
hist3.set_ylabel('Employee Count')
hist3.set_title('Frequency Distribution: Work Mode')

plt.tight_layout()
plt.savefig('Frequency_Distribution_Nominal_Variables.png')



'''ORDINAL VARIABLES: Performance_Rating'''

print('\n-- ORDINAL VARIABLES --')

# Find the mode and median of the ordinal variable: Performance_Rating
print("\nThe mode of 'Performance_Rating' variable: ", data['Performance_Rating'].mode()[0])
print("The median of 'Performance_Rating' variable: ", data['Performance_Rating'].median())


#Plot the percentiles of the ordinal variable -- Performance_Rating (CDF?)
#Plot the frequency distribution of the ordinal variable -- Performance_Rating (histogram?)
plt.figure(figsize=(9,5))

plt.subplot(1, 2, 1)
kde = sns.kdeplot(data['Performance_Rating'], color='purple', cumulative=True)
kde.set_ylabel('Cumulative Probability')
kde.set_xlabel('Performance Rating')
kde.set_title('Cumulative Distribution Function: Performance Rating',fontsize=10)

plt.subplot(1, 2, 2)
hist4 = sns.histplot(data['Performance_Rating'])
hist4.set(xlabel=None)
hist4.set_xticks(range(1,6,1))
hist4.set_title('Frequency Distribution: Performance Rating',fontsize=10)

plt.tight_layout()
plt.savefig('CDF_and_Frequency_Distribution_Ordinal_Variable.png')


'''CONTINUOUS VARIABLES: Experience_Years, Salary_INR'''

print('\n-- CONTINUOUS VARIABLES --')

# Find the mean, median, mode of the continuous variables: Experience_Years, Salary_INR (Indian rupees)
print("\nThe mean of 'Experience_Years' variable: ", data['Experience_Years'].mean())
print("The median of 'Experience_Years' variable: ", data['Experience_Years'].median())
print("The mode of 'Experience_Years' variable: ", data['Experience_Years'].mode()[0])
print("\nThe mean of 'Salary_INR' variable: ", data['Salary_INR'].mean())
print("The median of 'Salary_INR' variable: ", data['Salary_INR'].median())
print("The mode of 'Salary_INR' variable: ", data['Salary_INR'].mode()[0])

# Find the standard deviation of the continuous variables: Experience_Years, Salary_INR (Indian rupees)
print("\nThe standard deviation of 'Experience_Years' variable: ", data['Experience_Years'].std())
print("The standard deviation of 'Salary_INR' variable: ", data['Salary_INR'].std())

# Plot the box plots of the continuous variables -- Experience_Years, Salary_INR
plt.figure(figsize=(6,4))
plt.subplot(1, 2, 1)
box1 = sns.boxplot(y=data['Experience_Years'], color='lightblue', flierprops={'marker': 'o'})
box1.set_ylabel('Years of Experience')
box1.set_title('Box Plot: Experience Years', fontsize=10)

plt.subplot(1, 2, 2)
box2 = sns.boxplot(y=data['Salary_INR'], color='lightgreen', flierprops={'marker': 'o', 'markersize': 4, 'markerfacecolor': 'white'})
box2.set_ylabel('Annual Salary (INR)')
box2.set_title('Box Plot: Salary (INR)', fontsize=10)


plt.tight_layout()
plt.savefig('Box_Plots_Continuous_Variables.png')


# Show all plots
# plt.show()