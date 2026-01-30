E-Commerce Sales Data Analysis

Description
This project analyzes an E-Commerce sales dataset to identify revenue trends, customer purchasing behavior, and monthly performance using Python and Pandas.

Demo Video

Watch a walkthrough of this project here: [E-Commerce Data Analysis Demo](https://youtu.be/Wxi37wZdL0s)

Dataset
- Source: Kaggle (Free public dataset)
- File: `ecommerce_sales.csv`
- Data includes: order dates, product categories, prices, quantities, and revenue.

Questions Answered
1. Which product category generated the highest total revenue?
2. What is the average order value per month?
3. Which month had the highest number of orders?

Tools Used
- Python
- Pandas
- Matplotlib

Analysis Summary
- Revenue was aggregated by category to determine top-performing products.
- Monthly averages were calculated to analyze purchasing trends.
- Order counts per month identified peak sales periods.

How to Run the Program

1. Ensure you have Python installed (version 3.7 or higher recommended).
2. Install the required libraries by running:
	
	python -m pip install -r requirements.txt
	
3. Place the dataset file as `data/ecommerce_sales.csv` in the project folder.
4. Run the analysis script:
	
	python analysis.py
	
5. The script will print analysis results to the terminal and display a bar chart of the top products by revenue.

Summary of Findings

- The product “DOTCOM POSTAGE” generated the highest total revenue, followed by “REGENCY CAKESTAND 3 TIER” and “WHITE HANGING HEART T-LIGHT HOLDER.”
- The average order value per month ranged from about £15.93 to £20.30, with the highest in September 2011.
- The number of orders peaked in November 2011, likely due to holiday shopping.
- Some products had negative revenue, indicating fees, returns, or adjustments in the data.

Challenges Encountered

- Matching the code to the actual dataset columns (e.g., using 'Description' instead of 'Category').
- Handling missing or negative values in the data.
- Understanding the business meaning of certain rows (e.g., negative revenue for fees or returns).
- Ensuring all dependencies were installed and the script ran without errors.


Work Log & Hours Breakdown

| Day        | Hours | Tasks Completed                                                                 |
|------------|-------|--------------------------------------------------------------------------------|
| Monday     | 2     | Researched datasets, set up project folder, installed Python and libraries      |
| Tuesday    | 2     | Downloaded and inspected dataset, planned analysis questions                    |
| Wednesday  | 4     | Wrote code to load and clean data, checked column names, initial data prep      |
| Thursday   | 2     | Implemented aggregation, sorting, and time-based queries in analysis.py         |
| Friday     | 3     | Created and refined visualizations, tested code, fixed bugs                     |
| Saturday   | 2     | Drafted and polished README.md, summarized findings, final testing and review   |
| Total hrs | 15                                                                                 

This schedule reflects a typical week of focused work, totaling 15 hours. Each day was dedicated to a specific aspect of the project, from setup and data exploration to analysis, visualization, and documentation.

 Visualization
A bar chart was created to visualize total revenue by product category.

Conclusion
The analysis shows clear differences in revenue between product categories and reveals seasonal trends in customer purchasing behavior. These insights can be used to improve inventory planning and marketing strategies.

