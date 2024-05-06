import streamlit as st

with st.sidebar:
        kural_num = st.number_input(label="Explore a குறள் quickly", min_value=1, max_value=1330, step=1)
        if st.button("Explore this kural using the chatbot", key="quick"):
            st.session_state["kural"] = kural_num
            if "messages" in st.session_state.keys():
                del st.session_state.messages
            st.switch_page("pages/2_Explore a Kural.py")

col1, col2 = st.columns(2, gap="large")
with col1:
     st.subheader("About Thirukkural")
     st.write("""
    The Thirukkural (திருக்குறள்) is a classic Tamil language text consisting of 1,330 short couplets, or kurals, of seven words each. The text is divided into three books with aphoristic teachings on virtue (aram), wealth (porul) and love (inbam), respectively. Thirukkural is structured into 133 chapters, each containing 10 couplets (or kurals), for a total of 1,330 couplets. It is widely acknowledged for its universality and secular nature. Its authorship is traditionally attributed to Valluvar, also known in full as Thiruvalluvar. The text has been dated variously from 300 BCE to 5th century CE.
<br><br>
    Written on the ideas of ahimsa, it emphasizes non-violence and moral vegetarianism as virtues for an individual. In addition, it highlights virtues such as truthfulness, self-restraint, gratitude, hospitality, kindness, goodness of wife, duty, giving, and so forth, besides covering a wide range of social and political topics such as king, ministers, taxes, justice, forts, war, greatness of army and soldier's honor, death sentence for the wicked, agriculture, education, abstinence from alcohol and intoxicants.
""", unsafe_allow_html=True)


with col2:
    st.subheader("About Thirukkural.AI")
    st.write("""
Thirukkural.AI is an innovative chatbot deployed using Streamlit, designed to provide an immersive experience in exploring the ancient wisdom and discovering new insights. This chatbot allows you to delve into the timeless wisdom of thirukkural, providing a unique platform to learn and explore.
<br><br>
With Mistral 7B model, you can uncover the depths of specific kural, gaining a deeper understanding of their meanings and relevance. Whether you're a scholar seeking profound insights or a curious mind eager to learn, this chatbot is here to guide you on your journey of discovery.
<br><br>Not only does Thirukkural.AI help you explore individual kural, but it also offers suggestions for similar kural based on advanced sentence transformers. This feature enables you to expand your knowledge and discover related kural that resonate with your interests and inquiries.
<br><br>Let's unlock the timeless truths of kural together!""", unsafe_allow_html=True)

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