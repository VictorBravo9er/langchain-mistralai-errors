# tests/integration/test_mcp_mistral_agent_known_failure.py

import pytest
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage


@pytest.mark.asyncio
@pytest.mark.xfail(
    reason="Known failure: agent.ainvoke crashes with MCP tools + Mistral",
    strict=True,
)
async def test_mistral_agent_ainvoke_known_failure():
    """
    This test documents a known failing integration.
    It is expected to error at agent.ainvoke().
    """
    load_dotenv()

    client = MultiServerMCPClient(
        {
            "time": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["mcp-server-time", "--local-timezone=Asia/Kolkata"],
            }
        }
    )

    tools = await client.get_tools()

    agent = create_agent(
        model="mistral-large-latest",
        tools=tools,
    )

    # Expected to fail
    await agent.ainvoke(
        {
            "messages": [
                HumanMessage(content="What is the time in Tokyo?")
            ]
        }
    )
