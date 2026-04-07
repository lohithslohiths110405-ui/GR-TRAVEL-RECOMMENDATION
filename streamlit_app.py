
import streamlit as st
import pandas as pd

df = pd.read_csv('data/routes_dataset.csv')

emission_factors = {
'bike':0.02,
'car':0.12,
'bus':0.05,
'train':0.03,
'flight':0.25
}

st.title("Green Route – Carbon Efficient Travel Recommender")

cities = sorted(set(df['from']).union(set(df['to'])))

c1 = st.selectbox("From", cities)
c2 = st.selectbox("To", cities)

if st.button("Calculate"):
    row = df[((df['from']==c1)&(df['to']==c2)) | ((df['from']==c2)&(df['to']==c1))]
    if not row.empty:
        d = int(row.iloc[0]['distance_km'])
        emissions = {m:d*f for m,f in emission_factors.items()}
        best = min(emissions,key=emissions.get)

        st.write("Distance:", d, "km")
        st.write("### Recommended Mode:", best)

        st.bar_chart(emissions)
