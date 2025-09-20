# SEO Audit & Web Performance Dashboard (Power BI)

This project analyzes SEO crawl data (from Screaming Frog SEO Audit Application) to find **indexability**, **crawl budget waste**, **content quality**, **canonicalization issues** and **internal linking**. And it's built in **Power BI** with one flat table and calculated DAX columns/measures.



## Interactive Report
[View Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiYzE1NjAwN2ItODI0My00ZWIxLTgyMTItYzUzOTg2OTU1N2IxIiwidCI6IjU0ZDcxMmI0LWQxZGEtNDRjOC1hM2IzLTlhMzVmZGI3NTllNCIsImMiOjh9
) 


## Report Pages

### 1. Macro Data
<img width="1906" height="1062" alt="Macro Page" src="https://github.com/user-attachments/assets/1b2c132c-ef7f-490c-92a4-579ffa3bd4d2" />

Macro Data

### 2. Web Performance & Metadata
<img width="1915" height="1076" alt="2nd page" src="https://github.com/user-attachments/assets/6df74db6-eec7-4c72-9dce-8e118437db46" />

Web Performance

### 3. Canonicals & No-Index
<img width="1917" height="1064" alt="3rd page" src="https://github.com/user-attachments/assets/7a291e53-c89e-474d-9148-925f3a446f22" />

Canonicals & No-Index

### 4. Crawl Budget
<img width="1900" height="1071" alt="4th page" src="https://github.com/user-attachments/assets/002fe930-5412-4b04-a232-907b646d3e66" />

Crawl Budget

### 5. Inlink Analysis
<img width="1905" height="1082" alt="5th page" src="https://github.com/user-attachments/assets/83229ea2-a2b3-4f15-8dbd-3468e30aaa32" />

Inlinks



## Features
- Cleaning in Power Query (null/empty rows removed).
- All grouping & clustering done with **DAX calculated columns**.
- Filters: URL Type, Content Type, Thin Content Cluster, Inlinks Cluster, Crawl Depth etc.



## Key Insights
- 78% of URLs indexable and 21% wasted due to redirects, blocked or canonicalised pages.
- Thin content detected where ~1 in 5 pages with ≤300 words and missing or weak metadata.
- Crawl performance shows gaps in some pages which load >2s, affecting SEO and UX.
- Most important pages at shallow depth (≤2), many deep pages (4+) and weakly linked URLs limit visibility indicates site structure imbalance. 


