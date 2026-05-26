from typing import TypedDict, List #class
from langgraph.graph import StateGraph, START, END


class GraphState(TypedDict):
    query: str
    tool_needed: bool
    result: str

#tool
def calculator_tool(expression: str) -> str:
    print("\n[Calculator Tool Called]")

    return str(eval(expression))

#node
def understand_query(state: GraphState) -> GraphState:
    query = state["query"]

    print("\n[Understand Query]")
    print("User query:", query)
    
    math_symbols = ["+", "-", "*", "/"]
    arr=[]
    
    # for symbol in math_symbols:
    #     if symbol in query:
    #         arr.append(True)
    #     else:
    #         arr.append(False)

    # for symbol in math_symbols:
    #     arr.append(symbol in query)
    
    if any((symbol in query) for symbol in math_symbols):
        state["tool_needed"] = True
    else:
        state["tool_needed"] = False

    return state

#node
def use_tool(state: GraphState) -> GraphState:
    print("\n[Using Tool]")
    query = state["query"]
    result = calculator_tool(query)

    state["result"] = result

    return state

#node
def normal_response(state: GraphState) -> GraphState:
    print("\n[Normal Response]")
    
    state["result"] = "This is a LLM response."

    return state

#router
def router(state: GraphState):
    if state["tool_needed"]:
        return "use_tool"
    else:
        return "normal_response"

#graph
graph = StateGraph(GraphState)

graph.add_node("understand_query", understand_query)
graph.add_node("use_tool", use_tool)
graph.add_node("normal_response", normal_response)

graph.set_entry_point("understand_query")

graph.add_conditional_edges("understand_query", router, {"use_tool":"use_tool", "normal_response": "normal_response"})

graph.set_finish_point("normal_response")
graph.set_finish_point("use_tool")

app = graph.compile()

result = app.invoke({"query": "hi"})

print(result)



    









#Question : why we need to add typehint for a graphstate?