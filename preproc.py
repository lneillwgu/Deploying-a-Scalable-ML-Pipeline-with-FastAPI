# Created this to preprocess the data to remove duplicates discovered
# during data exploration as well as any whitespaces

import pandas as pd
import os

project_path = os.getcwd()
data_path = os.path.join(project_path, "data", "census.csv")
df = pd.read_csv(data_path)

df.drop_duplicates(inplace=True)

df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df.to_csv(data_path, index=False)
