# Thirukkural.AI

Welcome to Thirukkural.AI, your gateway to the timeless wisdom of Thiruvalluvar powered by cutting-edge AI technology and deployed using Streamlit. This is a chatbot designed to help you delve into the profound teachings of Thiruvalluvar.
<br><br>
With Thirukkural.AI, you can easily find what Thiruvalluvar has said about any topic using RAG (Retrieval-Augmented Generation) model made specifically using the vectors of each kural. Simply enter a keyword, and let Thirukkural.AI uncover the relevant kural for you.
<br><br>
But that's not all... Thirukkural.AI goes beyond mere exploration. It allows you to delve deeper into a specific kural, providing insights and interpretations using Mistral 7B powered chat bot. Want more? Explore similar kural suggestions based on advanced sentence transformers, expanding your understanding and appreciation of Thiruvalluvar's timeless wisdom.

---

## Overview

- Leveraged Mistral 7B Instruct model using the HuggingFace inference API, specifically prompt-engineered for this
application, to explore the profound teachings of Thirukkural.
- Implemented Retrieval Augmented Generation to retrieve relevant lines from the book according to the user query.
- Utilized a Vector database to store the embedding of each couplet and to develop a Recommender system.
