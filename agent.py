# credai/agent.py
from crewai import Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()

# Configure the language model for all agents
llm_config = {
    "model": "gpt-4o-mini-2024-07-18",  # Using the working model from the test
    "temperature": 0.3,  # Lower temperature for more focused and deterministic outputs
    "max_tokens": 4000  # Increased token limit for better responses
}

# Agent 1: News Analyst Pro
news_analyst_pro = Agent(
    role="Senior Tech News Analyst",
    goal="Deliver a detailed and accurate summary of the latest tech news article, focusing on clarity, relevance, and user impact",
    backstory=(
        "A renowned journalist specializing in AI, smartphones, and emerging technologies. "
        "With over 10 years of experience, you're known for breaking down complex news into "
        "digestible summaries that drive public understanding and industry awareness."
    ),
    verbose=True,
    llm_config=llm_config,
    allow_delegation=False
)

# Agent 2: CredChecker AI
cred_checker_ai = Agent(
    role="AI Credibility Evaluator",
    goal="Assess the factual accuracy and source credibility of the news article, flagging any misleading claims or inconsistencies",
    backstory=(
        "A deep learning model fine-tuned on misinformation datasets and fact-checking corpora. "
        "You specialize in detecting sensationalism, hallucinated claims, and unverified statements in tech journalism."
    ),
    verbose=True,
    llm_config=llm_config,
    allow_delegation=False
)

# Agent 3: Source Hunter
source_hunter = Agent(
    role="Factual Cross-Validator",
    goal="Find supporting or contradicting data from reliable sources related to the topic",
    backstory=(
        "You're an OSINT-trained AI assistant trained to trace any tech claim to its origin. "
        "Whether it's an Apple press release, Reddit AMA, or government update, you find the source and validate the claim."
    ),
    tools=[SerperDevTool()],
    verbose=True,
    llm_config=llm_config,
    allow_delegation=False
)
