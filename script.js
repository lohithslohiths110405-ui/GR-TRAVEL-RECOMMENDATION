
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('../data/routes_dataset.csv')

emission_factors = {
'bike':0.02,
'car':0.12,
'bus':0.05,
'train':0.03,
'flight':0.25
}

def compute_emissions(distance):
    return {mode:distance*factor for mode,factor in emission_factors.items()}

@app.route('/', methods=['GET','POST'])
def index():
    result=None
    if request.method=='POST':
        f = request.form['from']
        t = request.form['to']
        row = df[((df['from']==f)&(df['to']==t)) | ((df['from']==t)&(df['to']==f))]
        if not row.empty:
            distance = int(row.iloc[0]['distance_km'])
            emissions = compute_emissions(distance)
            best = min(emissions,key=emissions.get)
            result = {"distance":distance,"emissions":emissions,"best":best}
    cities = sorted(set(df['from']).union(set(df['to'])))
    return render_template('index.html',cities=cities,result=result)

if __name__ == '__main__':
    app.run(debug=True)
