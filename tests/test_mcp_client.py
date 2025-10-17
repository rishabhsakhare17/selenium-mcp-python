#!/usr/bin/env python3
"""
Test script to verify MCP server is working correctly.
This connects via MCP protocol, not HTTP.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the MCP server functionality."""
    # Connect to the MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["../src/selenium_mcp_server.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            print("🔧 Available tools:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            
            # Test opening browser
            print("\n🌐 Testing open_browser...")
            result = await session.call_tool("open_browser", {"headless": True})
            print(f"Result: {result}")
            
            # Test navigating to URL
            print("\n🔗 Testing go_to_url...")
            result = await session.call_tool("go_to_url", {"url": "https://google.com"})
            print(f"Result: {result}")
            
            # Test getting page text
            print("\n📄 Testing get_page_text...")
            result = await session.call_tool("get_page_text", {})
            print(f"Result: {result}")
            
            # Test closing browser
            print("\n❌ Testing close_browser...")
            result = await session.call_tool("close_browser", {})
            print(f"Result: {result}")

if __name__ == "__main__":
    print("🧪 Testing MCP Selenium Server...")
    asyncio.run(test_mcp_server())
