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
groups = list(impacts['Group'])

groups = ['Community Impact Internship Program' if ('Community Impact Internship' in group) or ('CIIP' in group) else group for group in groups]
groups = ['SOURCE' if 'SOURCE' in group else group for group in groups]
groups = ['Baltimore First' if 'Baltimore First' in group else group for group in groups]
groups = ['Centro SOL' if 'Centro SOL' in group else group for group in groups]
groups = ['Community Outreach Program' if 'Community Outreach Program' in group else group for group in groups]
groups = ['France-Merrick Civic Fellows' if 'France-Merrick' in group else group for group in groups]
groups = ['HIV Counseling and Testing Program' if 'HIV Counseling' in group else group for group in groups]
groups = ['Hopkins Community Connection' if 'Hopkins Community Connection' in group else group for group in groups]
groups = ['HopkinsCORPS' if 'HopkinsCORPS' in group else group for group in groups]
groups = ['Tutorial Project' if group[:len('Tutorial Project')] ==  'Tutorial Project' else group for group in groups]


impacts['Zip or Postal Code'] = impacts['Zip or Postal Code'].map(lambda x: str(x)[:5]).replace('nan', np.nan).replace('2120i', 21218).astype(float).astype('Int64')
impacts['Group'] = groups

impacts.to_excel("~/Desktop/test_impacts.xlsx", index=False)