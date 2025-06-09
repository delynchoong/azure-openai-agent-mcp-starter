from mcp.server.fastmcp import FastMCP
import sys

# Initialize the server
mcp = FastMCP("Math")

# Register the addition tool
@mcp.tool(name="Addition", description="Adds two integers")
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

# Register the subtraction tool
@mcp.tool(name="Subtraction", description="Subtracts two integers")
def subtract(a: int, b: int) -> int:
    """Subtract two integers."""
    return a - b

# Register the multiplication tool
@mcp.tool(name="Multiplication", description="Multiplies two integers")
def multiply(a: int, b: int) -> int:
    print(f"Multiplying {a} and {b}", file=sys.stderr)
    """Multiply two integers."""
    return a * b

# Register the division tool
@mcp.tool(name="Division", description="Divides two integers")
def divide(a: int, b: int) -> float:
    """Divide two integers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Register the square tool
@mcp.tool(name="Square", description="Calculates the square of an integer")
def square(a: int) -> int:
    """Calculate the square of an integer."""
    return a * a

if __name__ == "__main__":
    mcp.run(transport="stdio")
    # This server will run and listen for requests on standard input/output. 
    # Change to SSE if required
