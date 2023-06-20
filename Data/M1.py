import pandas as pd 
import matplotlib.pyplot as plt
df1 = pd.read_excel("../fsn_data_2020_07.XLSX")
df1
grouped = df1.groupby('MRP Controller')

group_dataframes = []
for group_name, group_df in grouped:
    group_dataframes.append(group_df)

sum_values = []
for group_df in group_dataframes:
    sum_values.append((group_df['Cl.Value'].sum())/100000)

result_df = pd.DataFrame({'MRP_Controller': grouped.groups.keys(), 'Cl.Value': sum_values})

print(result_df)
cont=result_df['MRP_Controller']
cl= result_df['Cl.Value']

plt.figure(figsize=(30,15))
plt.pie(cl,labels=cont,autopct="%.1f%%")
plt.show()

grouped = df1.groupby('Material Type')

group_dataframes = []
for group_name, group_df in grouped:
    group_dataframes.append(group_df)

sum_values = []
for group_df in group_dataframes:
    sum_values.append((group_df['Cl.Value'].sum())/100000)

result_df1 = pd.DataFrame({'Material_type': grouped.groups.keys(), 'Cl.Value': sum_values})

print(result_df1)