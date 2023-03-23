import os
import requests
import pandas as pd

api_key = os.environ["NOTION_TOKEN"]
database_id = 'd9172cfef383463f8180c6512d99c081'

from IPython.display import display, JSON

headers = {
    "Authorization": f"Bearer {api_key}",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
}

# Send post request, put in `response` variable
response = requests.post(
    f"https://api.notion.com/v1/databases/{database_id}/query", headers=headers
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



# Create Dataframe
def get_raw_value(item):
    item_type = item['type']

    
    if type(item[item_type]) is list:
        # print('is list')

        # if item[item_type][0]['type'] == 'text': # Complaint IDs
        #     return item[item_type][0]['plain_text']
        if item_type == 'relation': # Complaint IDs
            return len(item[item_type])
                
    if type(item[item_type]) is dict:
        # print('is dict')
        if item_type == 'select': # City
            return item[item_type].get('name')
        if item_type == 'text':
            return item[item_type].get('content')
        #if item_type == 'relation':
            #return item[item_type].get('id')
        #if item_type == 'relation':
         #   return item[item_type].get()    

    # print(type(item[item_type]))
    #return item[item_type]

# def get_raw_val_relation(item):
#     item_type = item['type']

#     print(item['id'])

#     # if item[item_type] == 'relation':
#     #     print('relation')
    
#     return



all_values = []   
for record in records:
    properties = record['properties']
    all_values.append({
        # 'COLUMN NAME' : get_raw_value(properties[PROPERTY_NAME]),
        # Market 
        'City': get_raw_value(properties['City']),

        # Complaints
        'Complaints': get_raw_value(properties['Complaints'])
    })

market_df = pd.DataFrame(all_values)
market_df