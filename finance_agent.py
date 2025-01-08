from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv 

load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search for the information on the Internet",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources "],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True,)],
    insturctions=["Use Tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources ","Use Tables to display the data"],
    model=Groq(id="llama-3.3-70b-versatile"),
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Give a financial analysis of  Tesla INC. (TSLA) stock and provide the latest news about the company.", stream=True)

