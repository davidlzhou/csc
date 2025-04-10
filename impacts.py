import pandas as pd
import numpy as np
import openpyxl
impactfile = pd.read_csv("~/Downloads/impacts.csv", low_memory=False)
impacts = impactfile[[
    'Impact ID',
    'Date Created',
    'User ID',
    'External ID',
    'Economic Value',
    'Group ID',
    'Group',
    'Event ID',
    'Event Name',
    'Shared with',
    'Type',
    'Start Date',
    'End Date',
    'Start Time',
    'End Time',
    'Review/Reflection',
    'Mobile Checkin',
    'Category',
    'Subcategory',
    'Hours Served',
    'Dollar Amount',
    'Donated Goods',
    'Other Outcome',
    'Rating',
    'Is Private',
    'Verified',
    'Event Type',
    'Kind',
    'Event Address',
    'Event End Address',
    'City',
    'State',
    'Zip or Postal Code'
    ]].copy()

impacts['Zip or Postal Code'] = impacts['Zip or Postal Code'].map(lambda x: str(x)[:5]).replace('nan', np.nan).replace('2120i', 21218).astype(float).astype('Int64')
print(impacts)
impacts.to_excel("~/Desktop/impacts.xlsx", index=False)
print("done")