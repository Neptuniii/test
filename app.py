import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

df = pd.read_csv("naphaluancod_2025-07-16.csv", usecols=[
    'governor_id', 'governor_name', 'power', 'units_killed', 'tier_1_kills', 'tier_2_kills', 'tier_3_kills', 'tier_4_kills', 'tier_5_kills', 'gold_spent', 'wood_spent', 'stone_spent', 'mana_spent', 'gems_spent'
])

df = df.rename(columns={
    'governor_id': 'ID',
    'governor_name': 'Name',
    'power': 'Power',
    'units_killed': 'Total kill',
    'tier_1_kills': 'T1 kill',
    'tier_2_kills': 'T2 kill',
    'tier_3_kills': 'T3 kill',
    'tier_4_kills': 'T4 kill',
    'tier_5_kills': 'T5 kill',
    'gold_spent': 'Gold spent',
    'wood_spent': 'Wood spent',
    'stone_spent': 'Stone spent',
    'mana_spent': 'Mana spent',
    'gems_spent': 'Gem spent'
})



st.set_page_config(layout="wide")
st.title("GDW Data ")
st.title("By Neptuniii")

search = st.text_input("Tìm theo ID hoặc Tên:")

if search:
    search_lower = search.lower()
    filtered_df = df[
        df['ID'].astype(str).str.contains(search_lower) |
        df['Name'].str.lower().str.contains(search_lower)
    ]
else:
    filtered_df = df

filtered_df = filtered_df.reset_index(drop=True)
filtered_df.index = filtered_df.index + 1

# Format bằng AgGrid
gb = GridOptionsBuilder.from_dataframe(filtered_df)
columns_to_format = [
    'Power', 'Total kill', 'T1 kill', 'T2 kill', 'T3 kill', 'T4 kill', 'T5 kill',
    'Gold spent', 'Wood spent', 'Stone spent', 'Mana spent', 'Gem spent'
]
for col in columns_to_format:
    gb.configure_column(col, type=["numericColumn", "numberColumnFilter", "customNumericFormat"],
                        precision=0, valueFormatter="x.toLocaleString()")

gridOptions = gb.build()

AgGrid(filtered_df, gridOptions=gridOptions, height=600, fit_columns_on_grid_load=True)




