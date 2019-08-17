import pandas as pd

filename = ('/home/pengyuzhou/testfiles/ErrorLog_handled_csv.csv')

output_filename = 'Errorlog_sup.csv'

errorlog_df = pd.read_csv(filename)
df = pd.DataFrame(errorlog_df)
id = []
TID_c = []
tracknum_c = []
description_c = []
for index,row in df.iterrows():
    id.append(row['1'].str.replace(r'[^\w\s]+', '').tolist())
    TID_c.append(row['TID'].str.replace(r'[^\w\s]+', '').tolist())
    tracknum_c.append(row['tracknum'].str.replace(r'[^\w\s]+', '').tolist())
    description_c.append(row['description'].str.replace(r'[^\w\s]+', '').tolist())


frame = pd.DataFrame({'id': id, 'work_year_past1': TID_c,
                      'work_year_past2': tracknum_c, 'work_year_past3': description_c})

frame.to_csv('/home/pengyuzhou/testfiles/'+output_filename)