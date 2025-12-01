from fastmcp import FastMCP, Context

mcp = FastMCP("Portfolio Assistant - Helping users explore a portfolio of projects.")

# Get contents of portfolio.md into a variable
portfolio_contents = ""
with open("portfolio.md", "r") as file:
    portfolio_contents = file.read()


@mcp.tool
def get_introduction() -> str:
    """Return a brief introduction about the portfolio."""
    return f"This portfolio showcases various projects demonstrating skills in software development, data analysis, and machine learning."


@mcp.tool
def get_questions_for_user() -> list[str]:
    """Return a list of potential questions to ask the user about their interests to help make the conversation more personalized."""
    return [
        "What are your main areas of interest in technology?",
        "What is your role or background in the tech industry?",
    ]


@mcp.tool
async def find_relevant_connection(interests: str, ctx: Context) -> str:
    """Find a relevant connection in the portfolio based on user interests."""
    prompt = f"""You are to support a lively conversation for a user that is learning about the portfolio.Find relevant projects and skills in the following portfolio based on the user's interests and generate an intriguing connection between them with a surprising twist.
        # users interests
        {interests}
        # portfolio
        {portfolio_contents}
    """

    # Request LLM response from context
    response = await ctx.sample(prompt)

    return response.text


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
