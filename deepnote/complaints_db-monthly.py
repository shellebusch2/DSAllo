# insert api call filtered by the past month

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import math

api_key = os.environ["NOTION_TOKEN"]
database_id = os.environ["NOTION_DBID_COMPLAINTS"]

from IPython.display import display, JSON

headers = {
    "Authorization": f"Bearer {api_key}",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
}

payload = {
    "filter": {
        "timestamp": "created_time",
        "created_time": {
            "past_month": {}
        }
  }
}

# Send post request, put in `response` variable
response = requests.post(
    f"https://api.notion.com/v1/databases/{database_id}/query", json=payload,headers=headers
).json()

print('Initial response: ')
display(JSON(response))

# iteratively load all pages
records = response["results"]
while response["has_more"]:
    response = requests.post(
        f"https://api.notion.com/v1/databases/{database_id}/query",
        json={"start_cursor": response["next_cursor"]},
        headers=headers,
    ).json()
    print("Loading page ...")
    records.extend(response.get("results", []))

print(f"Got {len(records)} entries from Complaints in Notion.")
print("Complaints have these properties", [x for x in records[0]['properties']])

# API call for pages
# response = requests.post(
#     f""
# )


# Create Dataframe
def get_raw_value(item):
    item_type = item['type']

    
    if type(item[item_type]) is list:
        # print('is list')

        if item[item_type][0]['type'] == 'text': # Complaint IDs
            return item[item_type][0]['plain_text']
                
    if type(item[item_type]) is dict:
        # print('is dict')
        if item_type == 'select': # City
            return item[item_type].get('name')
        if item_type == 'formula':
            raw_number = item[item_type].get('number')
            if raw_number == None:
                return ''
            else:
                return int(raw_number)
        if item_type == 'status':
            return item[item_type].get('name')
        if item_type == 'date':
            return item[item_type].get('start')
        
                 
    # print(type(item[item_type]))
    return item[item_type]

all_values = []   
for record in records:
    properties = record['properties']
    all_values.append({
        # 'COLUMN NAME' : get_raw_value(properties[PROPERTY_NAME]),
         'Complaint ID' : get_raw_value(properties['Complaint ID']),
         'City': get_raw_value(properties['City']),
         'State': get_raw_value(properties['State']),
         'Department': get_raw_value(properties['Department']),
        # 'Date Submitted': get_raw_value(properties['Date Submitted']),
        # 'Date Resolved': get_raw_value(properties['Date Resolved']),
         'Health or Safety Concern?': get_raw_value(properties['Health or Safety Concern?']),
         'Days To Resolution': get_raw_value(properties['Days To Resolution']),
         'Status': get_raw_value(properties['Status'])
    })

df_complaints_monthly = pd.DataFrame(all_values)
df_complaints_monthly