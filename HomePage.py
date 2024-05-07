import streamlit as st
import datetime
import sqlite3
import random

st.set_page_config(page_title="Thirukkural.AI", layout="wide")

def get_kural(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    kural = cursor.execute(f"SELECT * FROM kural WHERE id={id}").fetchall()
    return kural[0]

def kural_for_the_day():
    date_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    dates = cursor.execute("SELECT * FROM day").fetchall()
    empty_ids = []
    for i in range(len(dates)):
        if dates[i][1] == date_now:
            return get_kural(dates[i][0])
        if dates[i][1] == None:
            empty_ids.append(i+1)
    if empty_ids != []:
        choice = random.choice(empty_ids)
        cursor.execute(f"UPDATE day SET date='{date_now}' WHERE id={choice}")
        conn.commit()
        return kural_for_the_day()
    else:
        cursor.execute("DROP TABLE day")
        conn.commit()
        cursor.execute("CREATE TABLE day(id INTEGER, date TEXT)")
        conn.commit()
        for i in range(len(dates)):
            cursor.execute(f"INSERT INTO day(id) VALUES({i+1})")
        conn.commit()
        return kural_for_the_day()


def main():
    with st.sidebar:
        kural_num = st.number_input(label="Explore a குறள் quickly", min_value=1, max_value=1330, step=1)
        if st.button("Explore this kural using the chatbot", key="quick"):
            st.session_state["kural"] = kural_num
            if "messages" in st.session_state.keys():
                del st.session_state.messages
            st.switch_page("pages/2_Explore a Kural.py")


    st.title("Thirukkural.AI")
    st.write("#### A Mistral 7B based chat bot to explore Thirukkural")
    kural = kural_for_the_day()
    kural_today = kural[2].split()
    st.divider()
    with st.container(border=True):
        col1, col2 = st.columns(spec=[0.6,0.4], gap="large")
        col1.subheader("Featured குறள் of the day:")
        col1.write(f"{' '.join(kural_today[:4])}<br>{' '.join(kural_today[4:])}", unsafe_allow_html=True)
        col1.write(f"<b>English Meaning:</b> {kural[3]}", unsafe_allow_html=True)
        col2.metric("குறள்",kural[0])
        col2.write(f"அதிகாரம் <br><h5>{kural[1]}</h5>", unsafe_allow_html=True)
        if col2.button("Explore this kural using the chatbot", key="kural_for_the_day"):
            st.session_state["kural"] = int(kural_for_the_day()[0])
            if "messages" in st.session_state.keys():
                del st.session_state.messages
            st.switch_page("pages/2_Explore a Kural.py")

if __name__ == "__main__":
    main()


hide_st_style = """
        <style>
        #MainMenu {visibility:hidden;}
        #footer {visibility:hidden;}
        #header {visibility:hidden;}
        .stDeployButton {
            visibility: hidden;
        }
        </style>
"""
css='''
[data-testid="stSidebarNav"] {
  min-height: 50vh
}
'''
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)