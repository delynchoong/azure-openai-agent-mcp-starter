# azure-mcp-starter

This project is a starter template for building Model Context Protocol (MCP) agents using Azure OpenAI, not OpenAI. It demonstrates how to use the MCP protocol with Azure's hosted models, providing a foundation for developing advanced AI agents that can interact with external tools and services.

## What is MCP?

Model Context Protocol (MCP) is an open protocol that standardizes how language models interact with external tools, APIs, and environments. MCP enables models to call functions, access data, and perform actions beyond simple text generation, making them more useful and interactive in real-world applications.

## LangChain MCP Adapter

The LangChain MCP adapter is a library that bridges LangChain agents with MCP servers. It allows you to use LangChain's agent framework to communicate with any MCP-compliant server, enabling seamless integration of tool use, function calling, and advanced agent behaviors.

## MCP Options

There are several MCP server implementations and options available:

- **Python MCP Server**: Run your own MCP server in Python, customizing tool support and logic.
- **LangChain MCP Adapter**: Use LangChain's adapter to connect agents to MCP servers.


## About This Template

This repository is designed as a quick-start template for developers building MCP agents with specifically Azure OpenAI, as other guides only provided template for OpenAI endpoints. It includes sample code for connecting to an MCP server, using the LangChain MCP adapter, and running an agent that can interact with external tools. You can create your own sample MCP Server with MCP tools for your AI to perform agentic actions. It is intended for Azure OpenAI users and requires adaptation to work with OpenAI's public API.

## Quickstart
To run this template follow the steps:
1. pip install -r requirements.txt
2. Populate your .env file with the following: 
3. python math_server.py
4. In another terminal run: python client.py

## Upcoming features
Include more baseline MCP server integration with Azure AI Foundry, Microsoft Copilot, Azure MCP
---

For more information, see the official documentation for MCP, LangChain, and Azure OpenAI.