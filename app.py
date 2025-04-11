# using this command install this LLM
# pip install streamlit langchain-openai langchain-community langchain-core python-dotenv langgraph tavily-python

import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()
openai_apikey = os.getenv("OPENAI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo-1106", api_key=openai_apikey)

tool = TavilySearchResults(
    max_results=100,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

news_articles = [
    {
        "title": "Insurance risks will be a proxy carbon tax",
        "source": "Reuters",
        "date": "2024-12-27",
        "summary": "In 2025, the insurance sector is expected to reflect climate impacts via higher premiums, effectively acting as a proxy carbon tax.",
        "tags": ["parametric insurance", "basis risk", "climate change"]
    },
    {
        "title": "Monday briefing: What if the climate crisis makes disaster insurance unaffordable?",
        "source": "The Guardian",
        "date": "2025-01-27",
        "summary": "Wildfires and floods are challenging the viability of disaster insurance, with major markets in the US and UK adjusting to increased risks.",
        "tags": ["disaster insurance", "home insurance", "climate risk"]
    },
]

research_papers = [
    {
        "title": "Managing Basis Risks in Weather Parametric Insurance",
        "authors": "Hang Gao, Shuohua Yang, Xinli Liu",
        "date": "2024-09-25",
        "abstract": "This paper uses Monte Carlo simulations to demonstrate that portfolio diversification can significantly reduce basis risk in weather parametric insurance.",
        "tags": ["basis risk", "parametric insurance", "Monte Carlo"]
    },
    {
        "title": "Data-driven Parametric Insurance Framework Using Bayesian Neural Networks",
        "authors": "Subeen Pang, Chanyeol Choi",
        "date": "2022-09-22",
        "abstract": "This work employs a deep sigma point process—a Bayesian neural network approach—to improve risk predictions for parametric insurance, providing uncertainty estimates alongside improved accuracy.",
        "tags": ["Bayesian neural networks", "parametric insurance", "risk modeling"]
    },
]

def filter_by_tag(data, selected_tag):
    return [item for item in data if selected_tag in item["tags"]]

def get_all_tags(datasets):
    tags = set()
    for data in datasets:
        for item in data:
            tags.update(item["tags"])
    return sorted(tags)

st.title("Climate Risk Insurance Dashboard")

st.sidebar.header("Filter by Tag")
all_tags = get_all_tags([news_articles, research_papers])
selected_tag = st.sidebar.selectbox("Select a tag", all_tags)

st.header(f"News Articles Tagged: {selected_tag}")
filtered_news = filter_by_tag(news_articles, selected_tag)
if filtered_news:
    for article in filtered_news:
        st.subheader(article["title"])
        st.caption(f"{article['source']} | {article['date']}")
        st.write(article["summary"])
        st.markdown("---")
else:
    st.write("No news articles match this tag.")

st.header(f"Research Papers Tagged: {selected_tag}")
filtered_research = filter_by_tag(research_papers, selected_tag)
if filtered_research:
    for paper in filtered_research:
        st.subheader(paper["title"])
        st.caption(f"{paper['authors']} | {paper['date']}")
        st.write(paper["abstract"])
        st.markdown("---")
else:
    st.write("No research papers match this tag.")

st.sidebar.markdown("### About")
st.sidebar.info(
    "This dashboard integrates news and academic research on climate risk insurance. "
    "Select a tag to see related items from both news and arXiv research."
)



# use this command to run the project

# streamlit run app.py
