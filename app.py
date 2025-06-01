# credai/app.py
import streamlit as st
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the crew function after environment is loaded
from flow import run_crew

# Configure page
st.set_page_config(
    page_title="CredAI - Smart News Analysis",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        max-width: 1000px;
        padding: 2rem;
    }
    .stTextArea textarea {
        min-height: 300px;
    }
    .result-box {
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🧠 CredAI - Smart News Analysis")
    st.markdown("### Analyze the credibility of tech news articles with AI")
    
    with st.form(key='news_form'):
        news_input = st.text_area(
            "Paste a tech news article for analysis:",
            height=300,
            placeholder="Paste your article here... (minimum 100 characters)",
            help="The article should be at least 100 characters long for meaningful analysis."
        )
        
        analyze_btn = st.form_submit_button("🔍 Analyze Article")
    
    if analyze_btn:
        if not news_input.strip():
            st.warning("Please paste a news article to analyze.")
            return
            
        if len(news_input.strip()) < 100:
            st.warning("The article is too short. Please provide a more detailed article (at least 100 characters).")
            return
        
        with st.spinner("🧠 Analyzing article with CredAI... This may take a minute."):
            try:
                start_time = time.time()
                result = run_crew(news_input)
                processing_time = time.time() - start_time
                
                st.success(f"✅ Analysis completed in {processing_time:.1f} seconds!")
                
                # Display results in an expandable section
                with st.expander("📝 View Analysis Results", expanded=True):
                    st.markdown(result)
                
                # Add a download button for the results
                st.download_button(
                    label="📥 Download Analysis",
                    data=result,
                    file_name="credai_analysis.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"❌ An error occurred during analysis: {str(e)}")
                st.error("Please check your API keys and try again.")

if __name__ == "__main__":
    main()
