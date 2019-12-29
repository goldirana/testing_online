#%%
import pandas as pd
from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
     # url = "https://www.nseindia.com/corporates/datafiles/CA_ALL_FORTHCOMING__F&O_SECURITIES.csv"
    # s = requests.get(url).content
    # df = pd.read_csv("D:/BM_All_Forthcoming_-_F&O_Securities.csv")
    # return df.head()
    return "Hello world"

if __name__ == "main":
    app.run()