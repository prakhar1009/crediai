# credai/flow.py
import os
from typing import Optional
from crewai import Crew, Process
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import agents and tasks after environment is loaded
from agent import news_analyst_pro, cred_checker_ai, source_hunter
from task import create_summarize_task, create_credibility_task, create_validate_task

def run_crew(news_article: str) -> str:
    """
    Run the crew with the given news article
    
    Args:
        news_article (str): The news article to analyze
        
    Returns:
        str: The analysis results or error message
    """
    if not news_article.strip():
        return "Error: News article cannot be empty"
    
    try:
        # Create tasks
        tasks = [
            create_summarize_task(news_article),
            create_credibility_task(news_article),
            create_validate_task(news_article)
        ]
        
        # Configure and run the crew
        crew = Crew(
            agents=[news_analyst_pro, cred_checker_ai, source_hunter],
            tasks=tasks,
            process=Process.sequential,  # Run tasks one after another
            verbose=True,
            memory=True,  # Enable memory for context between tasks
            full_output=True  # Get full output including intermediate steps
        )
        
        # Execute the crew's tasks
        result = crew.kickoff()
        
        # Ensure we return a string result
        if isinstance(result, str):
            return result
        elif hasattr(result, 'raw_output'):
            return result.raw_output
        else:
            return str(result)
            
    except Exception as e:
        error_msg = f"An error occurred while processing the article: {str(e)}"
        print(error_msg)  # Log the full error for debugging
        return f"Error: {error_msg}"