import pandas as pd
import openpyxl
userfile = pd.read_csv("~/Downloads/users.csv", low_memory=False)
users = userfile[[
    'User ID', 
    'External ID', 
    'Gender', 
    'Veteran', 
    'Ethnicity', 
    'Are you Hispanic or Latino?', 
    'Participation Length', 
    'Years Participated', 
    'Date Joined Group', 
    'Last Visit', 
    'Major', 
    'Major Code', 
    '2nd Major', 
    '2nd Major Code', 
    'Enrollment Date', 
    'Term Code', 
    'Term Description', 
    'Graduation Date', 
    'Role', 
    #'Title', 
    'College', 
    'Currently Enrolled', 
    'Current Year', 
    'Pronouns (CF) [55990]', 
    'Department (CF) [56653]', 
    'College (Faculty & Staff) (CF) [56817]', 
    'Company (CF) [56821]', 
    'Primary Degree (CF) [56822]', 
    'Secondary Degree (CF) [56823]', 
    'Athlete (CF) [56824]', 
    'First Generation (CF) [56825]'
    ]].copy()
#users['Role'] = ['Post Doc' if (str(Title)[:6].lower().startswith('post d') or str(Title)[:5].lower().startswith('postd')) else Role for Role, Title in zip(users['Role'], users['Title'])]

users.to_excel("~/Desktop/users.xlsx", index=False)
print("done")