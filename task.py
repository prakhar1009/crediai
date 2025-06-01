# credai/task.py
from crewai import Task
from agent import news_analyst_pro, cred_checker_ai, source_hunter

def create_summarize_task(news_article):
    return Task(
        description=f"""
        TASK: Summarize the following tech news article clearly and concisely with key takeaways.
        
        ARTICLE:
        {news_article}
        
        INSTRUCTIONS:
        1. Identify the main topic and key points
        2. Extract important facts and figures
        3. Create a structured summary with bullet points
        4. Write a brief overview paragraph
        """.strip(),
        expected_output="""
        # News Summary
        
        ## Key Points
        - [Main point 1]
        - [Main point 2]
        - [Key finding 1]
        - [Key finding 2]
        
        ## Overview
        [A concise 2-3 sentence summary of the article]
        """.strip(),
        agent=news_analyst_pro,
        async_execution=False
    )

def create_credibility_task(news_article):
    return Task(
        description=f"""
        TASK: Analyze the following news content for credibility.
        
        ARTICLE:
        {news_article}
        
        INSTRUCTIONS:
        1. Identify any factual claims made in the article
        2. Check for unsupported or exaggerated statements
        3. Look for potential bias or sensationalism
        4. Provide a credibility score (0-100) with justification
        """.strip(),
        expected_output="""
        # Credibility Assessment
        
        ## Issues Found
        - [Issue 1 with explanation]
        - [Issue 2 with explanation]
        
        ## Credibility Score: XX/100
        
        ### Reasoning:
        [Detailed explanation of the score]
        """.strip(),
        agent=cred_checker_ai,
        async_execution=False,
        context=[]
    )

def create_validate_task(news_article):
    return Task(
        description=f"""
        TASK: Validate claims from the following article using external sources.
        
        ARTICLE:
        {news_article}
        
        INSTRUCTIONS:
        1. Identify key claims that need verification
        2. Search for credible sources to validate each claim
        3. Note whether sources support or contradict each claim
        4. Provide links to sources used
        """.strip(),
        expected_output="""
        # Source Validation
        
        | Claim | Source | Status (Supported/Contradicted) | Notes |
        |-------|--------|--------------------------------|-------|
        | [Claim 1] | [Source URL] | [Status] | [Notes] |
        | [Claim 2] | [Source URL] | [Status] | [Notes] |
        
        ## Summary of Findings
        [Brief summary of the validation results]
        """.strip(),
        agent=source_hunter,
        async_execution=False
    )
