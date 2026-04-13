
import streamlit as st
import pandas as pd
import networkx as nx

st.set_page_config(page_title="Green Route AI",layout="wide")

st.title("🌿 Green Route Travel Recommendation System")

df=pd.read_csv("data/routes_dataset.csv")

cities=sorted(set(df['from']).union(set(df['to'])))

col1,col2=st.columns(2)

with col1:
    source=st.selectbox("Select Source City",cities)

with col2:
    dest=st.selectbox("Select Destination City",cities)

G=nx.Graph()

for _,r in df.iterrows():
    G.add_edge(r['from'],r['to'],weight=r['distance_km'])

if st.button("Find Eco Friendly Route"):
    
    path=nx.dijkstra_path(G,source,dest,weight="weight")
    dist=nx.dijkstra_path_length(G,source,dest,weight="weight")
    
    st.success("Best Route: "+" → ".join(path))
    st.info(f"Total Distance: {dist} km")

st.markdown("---")
st.subheader("Dataset Preview")
st.dataframe(df.head(20))
