from openai import OpenAI
import gspread
from google.oauth2.service_account import Credentials
import json






# initializing the client for openai api
client = OpenAI(api_key='your-open-ai-api-key-here')
# asking the user for the workout detail in natural language
user_prompt = input("Enter today Workout Detail with time you spent (each):   ")


# open ai processing
# leting the client to fulfil the user query (give response as completion)
completion = client.chat.completions.create(
    # model="gpt-4o",
    model="gpt-3.5-turbo-0125",
    store=True,
    messages=[
        {
        "role": "system",
        "content": "Extract the user's workout details and return a structured JSON array without column headers. Each row should follow this format: [date, workout name, time (min), estimated calories burned]. Ensure that each value in the list is a string, the date is included in every row, and remove any placeholder values like '-'. Return the response as a properly formatted JSON array, without extra explanations or text."
        },
        {"role": "user", "content": user_prompt}
    ],
    max_tokens=150,
    temperature=0
)



# extracting the data from the openai api
messagedata = completion.choices[0].message.to_dict()
response = messagedata['content']
row_data = json.loads(response)


# sheet id to authorize + key file
sheet_id = 'your-sheet-id'
key_file_path = r'sheet-api-key-file-path'


# athorizing the credentials and initilizing the sheet
creds = Credentials.from_service_account_file(key_file_path, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
sheet = client.open_by_key(sheet_id).sheet1


# appending the row data created from openai to the sheet
for row in row_data:
    data = sheet.append_row(row)




#  some testing code that you can include in other features
# searching the specific row in the data
    # column_data = sheet.col_values(1)
    # index = column_data.index('Date')
    # print(index)


# getting the last index row in the data and appending data at he specific row
    # last_index = len(sheet.get_all_values())
    # print(last_index)
    # row = ['test','test1','test2','rest3','test4']
    # data = sheet.append_row(row,table_range=f"A{last_index+3}")


