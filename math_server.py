from mcp.server.fastmcp import FastMCP

# Initialize the server
mcp = FastMCP("Math")

# Register the addition tool
@mcp.tool(name="Addition", description="Adds two integers")
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

# Register the multiplication tool
@mcp.tool(name="Multiplication", description="Multiplies two integers")
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")