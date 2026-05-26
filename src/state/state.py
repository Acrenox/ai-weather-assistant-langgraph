#Every node in LangGraph reads from this state and writes back into this state.

from typing import TypedDict, Annotated, List
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """Represents the state of our agent."""
    messages: Annotated[List[BaseMessage], operator.add] #Annotated in exp: langgraph now how to update this field
    user_query: str
    tool_output: str