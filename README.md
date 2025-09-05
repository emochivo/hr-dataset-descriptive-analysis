### I. Introduction
For this small project, I chose a fictional dataset containing employee data of a multinational corporation. The dataset includes 2 million employee records with their information on personal ID, job-related attributes, performance, employment status, and annual salary. The data is available as a CSV file. The dataset has 12 attributes:
- Unnamed: The index column (not useful for analysis).
- Employee_ID: A unique identifier assigned to each employee.
- Full_Name: The employee’s full name.
- Department: The department where the employee works (e.g., IT, Marketing, Sales, etc.)
- Job_Title: The job position of the employee.
- Hire_Date: The date when the employee was hired.
- Location: Where the employee resides, including their city and country.
- Performance_Rating: A numeric scale ranging from 1 to 5, evaluating the employee's work performance. The higher the number, the better the performance.
- Experience_Years: Number of years of experience the employee has.
- Status: Current employment status of a person (e.g., Active, Resigned).
- Work_Mode: An employee’s mode of working, whether it’s on-site, hybrid, or remote.
- Salary_INR: The annual salary of each employee in Indian Rupees.

  
### II. Methods
I chose to analyze the dataset using Python open-source libraries such as Pandas, Seaborn, and Matplotlib, as they provide various tools to create statistical graphics. To analyze the dataset, I need to identify the level of measurement (e.g., nominal variable, ordinal variable, continuous variable) for the variables in my dataset. While I did not analyze all columns in my chosen dataset, it has all levels of measurement from nominal, ordinal to continuous variables. I decided to categorize the variables as follows:
- Nominal variables: Department, Status, Work_Mode
- Ordinal variables: Performance_Rating
- Continuous variables: Experience_Years, Salary_INR
  
Department, Status and Work_Mode are nominal variables because these variables divide employees into different categories, and there is no hierarchy between them. For example, the attribute Status will categorize employees into four values – Active, Resigned, Retired, or Terminated. These four statuses are not lower or higher than each other, and they are used to differentiate rather than evaluate employees. I considered Performance_Rating to be the ordinal variable because there is a numerical hierarchy between different categories. Performance_Rating follows the five-level scale from 1 to 5, with 1 being the lowest in performance and 5 being the highest. Experience_Years and Salary_INR are continuous variables measured at the ratio level, as they have an infinite scale and an absolute zero.


### III. Results

![alt text](/figures/Frequency_Distribution_Nominal_Variables.png) 

*Figure 1. The histograms represent frequency distributions of the nominal variables: Department, Status, Work_Mode.*

From the frequency distribution figures, I can identify the numbers of employees in each department, status category, and work mode. Among 2 million employees, IT has the most employees with nearly 600.000 employees (around 30% of the total employee count). The Sales department follows with approximately 400.000 employees (around 20% of the total employee count). The number of active employees dominates the company with more than 1,250,000 employees, which made up over 62.5% of the total employees. The numbers of on-site employees are slightly larger than people who applied for remote work with approximately 1,250,000 and 750,000 employees, respectively.

![alt text](/figures/CDF_and_Frequency_Distribution_Ordinal_Variable.png) 

*Figure 2. The cumulative distribution function represents the percentile (left) and the histogram represents the frequency distribution (right) of the ordinal variable Performance_Rating.*

I use the cumulative distribution function (CDF) to showcase the percentile of employees’ performance ratings, and a histogram to display its frequency distribution. The cumulative distribution curve explains that the employee with the lowest performance rating made up 20% of the employee count, and nearly 40% of the employee having the performance rating less than or equal to 2. About 60% of the employees have a performance rating of less than or equal to 3, 80% having it of less than or equal to 4, and employees with the highest performance rating contain the remaining 20% of the total employee count. The CDF shows that there are an equal number of employees in each rating category, and it shows in the frequency distribution, where each performance rating recorded around 400,000 employees.

![alt text](/figures/Box_Plots_Continuous_Variables.png) 

*Figure 3. The box plots represent the range and interquartile range of continuous variables Experience_Years (left) and Salary_INR (right).*

In Figure 3, the employees’ years of experience and annual salary are described in box plots, which provide information on value ranges and the interquartile range (IQR) within them. The left boxplot shows that 2 years of experience is the 25th percentile among the experience years range, 5 years of experience is the median, and 8 years of experience is the 75th percentile. The maximum number of years of experience is 15, while the minimum experience year is zero. For the annual salary, while there are some people reaching from 2 to 3 million INR, the median for the annual salary is only around 800,000 INR, and the 75th percentile for annual salary is only slightly over 1 million Rupees.


### IV. Discussion
This exercise, as well as the Fisher & Marshall (2008) study, taught me that the level of measurement of a variable is the most important consideration when selecting acceptable descriptive statistics and visualizations. For nominal variables like Department, simple frequency distributions were the best descriptive measures since they accurately represented the data without imposing an artificial order. For the ordinal variable, Performance_Rating, a cumulative distribution function (CDF) was useful, preserving the data's ranking character and exposing an equal distribution of employees across all ratings.

Continuous variables such as Salary_INR and Experience_Years were summarized clearly and robustly using metrics of central tendency and dispersion such as the median and IQR. The box plot was a good choice for visualization because it accurately depicted the data distribution without being affected by outliers. This emphasized the necessity of picking the appropriate visualization to avoid drawing incorrect conclusions.
