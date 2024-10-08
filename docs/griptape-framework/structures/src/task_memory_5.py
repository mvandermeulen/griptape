from griptape.structures import Agent
from griptape.tools import QueryTool, WebScraperTool

agent = Agent(
    tools=[
        WebScraperTool(off_prompt=True),
        QueryTool(off_prompt=False),
    ]
)

agent.run(
    "According to this page https://en.wikipedia.org/wiki/Elden_Ring, how many copies of Elden Ring have been sold?"
)
