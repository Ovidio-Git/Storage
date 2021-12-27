import pandas as pd
dataframe=pd.read_excel('/content/drive/MyDrive/almacen/FrecuenciometroExcel_0.xlsx')
SortFile=dataframe.value_counts(sort=False)
SortFile
SortFile.to_excel('/content/drive/MyDrive/almacen/FrecuenciometroExcel_100.xlsx')
