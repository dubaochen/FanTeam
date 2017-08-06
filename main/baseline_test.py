import pickle
import pandas as pd
model = pickle.load(open("LR_model.pkl","rb"))
model = model['LR']

data = pd.read_csv("08_data.csv")
test = data.drop(["time","group"],axis=1)
predict = model.predict(test)
data.insert(0,'tag',predict)
print(data.columns)
print(predict)
data.to_csv("predicted.csv")