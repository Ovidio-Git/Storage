import pandas as pd

def run():
  df = pd.read_excel('/content/drive/MyDrive/almacen/EA_DataAlmacen.xlsx', sheet_name=0) # can also index sheet by name or fetch all sheets
  mylist = df['Campos'].tolist() 
  print("--------- Data procesada y spliteada ---------")
  print(mylist)


if __name__=='__main__':
  run()
