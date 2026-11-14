import pandas as pd
data={
    "name":["Prachi","Sneha","Rahul","Tina","Anjali"],
    "roll_no":[123,124,234,236,456,],
    "Fther_name":["shashi","manoj","rajiv","ram","shyam"],
    "phone_number":[7043,8901,345678,9082,123467],
    "admission_date":["12 june ","23 feb","13 march","23 oct","10 sep"]
}
df=pd.DataFrame(data)
print(df)
df.to_excel("prachi_created.xlsx",index=False)