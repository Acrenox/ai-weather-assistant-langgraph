from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
from src.llm.llm import llm
from src.tools.tools import tools

# Bind tools to the LLM
llm_with_tools = llm.bind_tools(tools)

def call_llm(state):
    messages = state["messages"]
    user_query = state["user_query"]

    # Add a system message to guide the LLM's response after a tool call
    if any(isinstance(msg, ToolMessage) for msg in messages):
        system_message = SystemMessage(content="""
        You have just received output from a weather tool. 
        Please summarize the weather information concisely and politely for the user, 
        including the location, temperature, and conditions. 
        If there was an error, report it clearly. 
        Do not include any extra information unrelated to weather unless specifically asked. 
        Do not include the raw tool output.
        """)
        messages = messages + [system_message]

    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def call_tool(state):
    messages = state["messages"]
    last_message = messages[-1]
    tool_calls = last_message.tool_calls
    tool_output = ""
    for tool_call in tool_calls:
        if tool_call.get("name") == "get_current_weather":
            output = tools[0].invoke(tool_call.get("args"))
            tool_output += str(output) + "\n"
    return {"messages": [ToolMessage(content=tool_output, tool_call_id=tool_calls[0].get("id"))]}