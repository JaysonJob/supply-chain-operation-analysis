# supply-chain-operation-analysis
This project looks at how a company keeps track of its products and makes sure they get to customers on time.We used a dataset (not from a real business) to practice finding problems and suggesting the rcomendations.

- **Where the data came from:** Mockaroo (an ai platform where it generate datasets so its not real)
- **What we did:** Used Python to read,clean,explore and visualize the data

---

## What's Inside

- **Python (Jupyter Notebook)** - Brings in data,cleans it,explores it and answers business questions
- **Matplotlib & Seaborn** - Makes charts showing stockout risk,urgency,shipping costs and warehouse performance
- **Business Questions** - Answers specific questions like "Which products are about to run out?"
- **Key Insights & Recommendations** - What we learned and what to do about it

## Tech Stack

Python · Pandas · Requests · Matplotlib · Seaborn · Jupyter Notebook

---

## Setup / Installation

### 1. Prerequisites

- Python 3.x
- Jupyter Notebook
- Install required packages: `pip install pandas requests matplotlib seaborn`

### 2. Installation Steps

1. Run `importing the data and saving as csv.py` - Downloads data from GitHub and saves as `operation_data.csv`
2. Run `loading and exploring the dataset.py` - Gives first look at the data (shape, types, missing values)
3. Run `data cleaning and analysis.py` - Cleans data and answers business questions
4. Run `visualization.py` - Makes five charts showing key findings

Each script runs independently.Re-run step 1 to get fresh data.

---

## Quick Summary

|                          |                                                     |
| ------------------------ | --------------------------------------------------- |
| **Data source**          | Mockaroo (AI generated,not real)                    |
| **Rows analyzed**        | 50 SKUs                                             |
| **Warehouses**           | East Coast, West Coast, Central                     |
| **Fulfillment statuses** | On Time, Delayed, Backordered                       |
| **Key fields**           | Stock Level, Reorder Point, Lead Time, Demand Rate, Shipping Cost |

---

## Workflow

load → Clean → Explore → Analyze → Visualize

1. **Import** - Pull data from GitHub and save as CSV
2. **Explore** - Check shape,types,stats,missing values and duplicates
3. **Clean** - Fix text spacing,validate numbers,confirm unique IDs
4. **Analyze** - Answer business questions using Pandas
5. **Visualize** - Create charts using Matplotlib and Seaborn libraries

---

## Business Questions Answered

**Stockout Risk** - Which products are below their reorder point right now? We flagged every SKU where current stock is less than the reorder point to see exactly how many are at risk.

**Most Urgent SKUs** - Which products will run out soonest? We calculated days of stock left (current stock ÷ daily demand) and ranked the top 10 most urgent ones.

**Warehouse Performance** - Which warehouses have the most delays? We compared each warehouse's On Time, Delayed, and Backordered rates to spot underperformers.

**Supplier Reliability** - Which suppliers cause the most problems? We looked at each supplier's fulfillment record to see who's responsible for most delays and backorders.

---

## Visualizations

1. **Histogram** - Stock levels vs reorder points (shows how many are at risk)
2. ![alt text](https://github.com/JaysonJob/supply-chain-operation-analysis/blob/9655485dabae781690311df645d8be1a69433350/screenshots/histogram.png)
3. **Bar Chart** - Top 10 most urgent SKUs by days of stock left
4. ![alt text](https://github.com/JaysonJob/supply-chain-operation-analysis/blob/931664640658feec28ad69f0eccff2cc706b2920/screenshots/bar%20chat.png)
5. **Boxplot** - Shipping costs by warehouse location
6. **Heatmap** - Fulfillment rates by warehouse
7. **Scatterplot** - Lead time vs demand rate (colored by risk status)

---

## Key Insights & Recommendations

**Key Insights:**

1. A significant number of SKUs are already below their reorder point,showing that stockouts aren't rare - they're a regular problem that needs fixing.
2. The most urgent SKUs are driven by high daily demand,not just low stock levels so we need to watch how fast things sell,not just how many we have.
3. Warehouse performance varies a lot - some locations have much higher delay and backorder rates than others and need investigation.
4. Shipping costs differ by warehouse,with some locations showing both higher costs and more variation,suggesting inconsistent practices.
5. Some suppliers cause way more delays and backorders than others,making them a risk to the whole supply chain.

**Recommendations:**

1. **Set up automatic reordering for fast-selling SKUs** - Instead of waiting until stock hits the reorder point,trigger orders earlier for products with very few days of stock left and high daily demand, so we never run out.
2. **Investigate underperforming warehouses** - Look into why certain locations have high delay and backorder rates - it could be staffing, carrier issues, or unexpected demand spikes that need addressing.
3. **Review unreliable suppliers** - Suppliers with consistently high delay and backorder counts put the company at risk, so negotiate better performance or find alternative suppliers.
4. **Fix shipping cost inconsistencies** - Wide cost variation within the same warehouse points to inefficient carrier use or routing that could be streamlined to save money.
5. **Adjust safety stock for long lead time, high demand items** - Products that take long to arrive AND sell fast need extra backup stock beyond normal reorder points to prevent shortages.

---

