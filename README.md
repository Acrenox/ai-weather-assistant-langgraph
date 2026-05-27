# AI Weather Assistant using LangGraph

An AI-powered weather assistant built with LangGraph that can understand natural language weather queries, call weather tools dynamically, and return concise, conversational responses.

This project demonstrates how to build a graph-based AI workflow with tool calling, state management, and modular design.

---

## Features

- Natural language weather queries
- Dynamic tool calling for weather data retrieval
- Graph-based workflow using LangGraph
- Stateful execution for multi-step interactions
- Modular and extensible project structure
- Easy integration with external weather APIs
- Designed for future expansion into a full AI assistant

---

## Project Overview

The assistant accepts user questions related to weather, such as:

- What is the weather in Bangalore?
- Will it rain tomorrow in Delhi?
- Compare the temperature in Mumbai and Chennai
- What is the humidity in Hyderabad right now?

The LangGraph workflow determines whether a tool needs to be called, executes the required weather function, and then generates a final response in natural language.

---

## Architecture

The project follows a simple graph-based flow:

1. The user submits a query.
2. LangGraph processes the request.
3. The agent decides whether a weather tool is needed.
4. The weather tool fetches the required data.
5. The assistant formats and returns the final response.

### Workflow Diagram

```text
User Query
    |
    v
LangGraph Agent
    |
    v
Tool Decision Node
    |
    v
Weather API Tool
    |
    v
Final Response Node
