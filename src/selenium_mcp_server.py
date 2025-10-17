# file: selenium_mcp_server.py
import asyncio
import uvicorn
import os
from datetime import datetime

from mcp.server.fastmcp import FastMCP
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastMCP("SeleniumMCP")

browser = None

@app.tool()
def open_browser(headless: bool = False):
    """Start a new Selenium browser session."""
    global browser
    options = Options()
    if headless:
        options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    return {"status": "Browser started"}

@app.tool()
def go_to_url(url: str):
    """Navigate to a URL."""
    if browser is None:
        return {"error": "Browser not started"}
    browser.get(url)
    return {"title": browser.title}

@app.tool()
def get_page_text():
    """Get all visible text on the current page."""
    if browser is None:
        return {"error": "Browser not started"}
    text = browser.find_element("tag name", "body").text
    return {"text": text[:2000]}  # limit for safety

@app.tool()
def click_element(selector: str):
    """Click an element on the page by CSS selector."""
    if browser is None:
        return {"error": "Browser not started"}

    try:
        elem = browser.find_element("css selector", selector)
        elem.click()
        return {"status": "Element clicked", "selector": selector}
    except Exception as e:
        return {"error": str(e)}

@app.tool()
def screenshot(save_to_disk: bool = True):
    """Take a screenshot of the current page (base64 or file)."""
    if browser is None:
        return {"error": "Browser not started"}

    if save_to_disk:
        # Create a 'screenshots' folder in the project directory
        os.makedirs("screenshots", exist_ok=True)
        filename = f"screenshots/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        browser.save_screenshot(filename)
        return {"status": "Screenshot saved", "path": os.path.abspath(filename)}
    else:
        img = browser.get_screenshot_as_base64()
        return {"image_base64": img}

@app.tool()
def close_browser():
    """Close the Selenium browser session."""
    global browser
    if browser:
        browser.quit()
        browser = None
        return {"status": "Browser closed"}
    return {"status": "No browser running"}

if __name__ == "__main__":
    import sys
    
    # Check if we should run in HTTP mode
    if len(sys.argv) > 1 and sys.argv[1] == "--http":
        print("🚀 Starting Selenium MCP Server (HTTP mode)...", file=sys.stderr)
        uvicorn.run(app.sse_app, host="127.0.0.1", port=5003)
    else:
        print("🚀 Starting Selenium MCP Server (stdio mode)...", file=sys.stderr)
        # Run in stdio mode for MCP clients (default)
        app.run(transport="stdio")