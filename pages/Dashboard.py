import streamlit as st
from app.db import get_connection
from app.cyber_incidents import get_all_cyber_incidents
import pandas as pd
conn = get_connection()
data =get_all_cyber_incidents(conn)

st.title("Cyber incidents Dashboards")



#check if the user is logged in
if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()
else:
    st.success(f"Welcome {st.session_state['username']}! You are logged in.")


with st.sidebar:
    st.header("Navigation")
    severity_= st.selectbox('severity',data['severity'].unique())

filtered_data = data[data['severity'] == severity_]

data['timestamp'] =  pd.to_datetime(data['timestamp'])
col1, col2 = st.columns(2)

with col1:
    st.header("Data 1st column")
    st.line_chart(filtered_data['status'].value_counts())
    

with col2:
    st.write(f"Data 2nd Column")
    st.line_chart(filtered_data,x='timestamp',y='incident_id')


st.write(filtered_data)

 
  