import pandas as pd
import random
import numpy as np

random.seed(42)
np.random.seed(42)

# Campaign Data Generation 
campaign_ids = [f"CAMP_{i}" for i in range(1, 101)]
channels = ["Google", "Social", "Email"]

holiday_periods = [
    (pd.Timestamp("2024-11-25"), pd.Timestamp("2024-12-02")),  # Black Friday week
    (pd.Timestamp("2024-12-20"), pd.Timestamp("2024-12-31"))  # Christmas period
]

def holiday(start_date):
    return any(start_date >= start and start_date <= end for start, end in holiday_periods)

campaign_data = []
for campaign_id in campaign_ids:
    for week in range(1, 11):  # 10 weeks of data per campaign
        channel = random.choice(channels)
        budget = random.randint(5000, 20000)
        spend = round(budget * random.uniform(0.7, 1), 2)
        impressions = random.randint(100000, 1000000)
        if holiday(pd.Timestamp("2024-01-01") + pd.Timedelta(weeks=week - 1)):
            impressions = int(impressions * random.uniform(1.2, 1.5))
        clicks = random.randint(1000, impressions // 10)
        conversions = random.randint(10, clicks // 5)
        start_date = pd.Timestamp("2024-01-01") + pd.Timedelta(weeks=week - 1)
        end_date = start_date + pd.Timedelta(days=6)
        campaign_data.append([campaign_id, channel, budget, spend, impressions, clicks, conversions, start_date, end_date])

campaign_df = pd.DataFrame(campaign_data, columns=["Campaign_ID", "Channel", "Budget", "Spend", "Impressions", "Clicks", "Conversions", "Start_Date", "End_Date"])

anomaly = np.random.choice(campaign_df.index, size=10, replace=False)# Add random anomalies to spend
for index in anomaly:
    campaign_df.loc[index, 'Spend'] *= random.uniform(1.5, 2.0)  # Overspend by 50-100%

# Customer Data Generation 

from faker import Faker
fake = Faker()

european_locations = ["Dublin", "London", "Berlin", "Paris", "Madrid", "Rome", "Amsterdam", "Lisbon"]
business_sizes = ["Small", "Medium", "Large"]
industry_types = ["Fashion", "Electronics", "Home Decor", "Groceries", "Health"]
revenue_ranges = {
    "Small": (50000, 150000),
    "Medium": (150001, 500000),
    "Large": (500001, 1000000)
}

customer_data = []
for _ in range(10000):  # 10,000 rows
    customer_id = fake.uuid4()[:8]  # Unique ID
    company_name = fake.company()
    location = random.choice(european_locations)
    business_size = random.choice(business_sizes)
    industry_type = random.choice(industry_types)
    bounce_rate = round(random.uniform(20, 80), 2)  # Percentage
    time_spent = round(random.uniform(1, 15), 2)  # Minutes
    min_revenue, max_revenue = revenue_ranges[business_size]
    annual_revenue = random.randint(min_revenue, max_revenue)
    website_visits = random.randint(1000, 20000)  # Annual visits
    customer_data.append([
        customer_id, company_name, location, business_size, industry_type, 
        bounce_rate, time_spent, annual_revenue, website_visits
    ])

customer_df = pd.DataFrame(customer_data, columns=[
    "Customer_ID", "Company_Name", "Location", "Business_Size", 
    "Industry_Type", "Bounce_Rate", "Time_Spent", "Annual_Revenue", "Website_Visits"
])



# campaign_file_path = "campaign_data.csv"
# customer_file_path = "customer_data.csv"

campaign_file_path = "D:/Data Projects/Marketing Cam_PowerBI/campaign_data.csv" # Save Datasets to CSV
customer_file_path = "D:/Data Projects/Marketing Cam_PowerBI/customer_data.csv"

campaign_df.to_csv(campaign_file_path, index=False)
customer_df.to_csv(customer_file_path, index=False)

