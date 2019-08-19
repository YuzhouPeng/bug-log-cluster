import pandas as pd
import string
df = pd.read_excel("file.xlsx")
db = df['Column Title']
for row in rows(min_row=1, min_col=1, max_row=6, max_col=3):
    for cell in row:
        translator = str.maketrans('', '', string.punctuation)
        sent_pun = db[0].translate(translator)