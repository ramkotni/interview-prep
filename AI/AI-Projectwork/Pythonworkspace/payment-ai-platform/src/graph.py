from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from agents.search_agent import search_agent
from agents.rca_agent import rca_agent
from agents.recommendation_agent import recommendation_agent
from agents.summary_agent import summary_agent

class GraphState(TypedDict):

    question: str
    context: str
    root_cause: str
    recommendation: str
    answer: str

workflow = StateGraph(GraphState)

workflow.add_node(
    "search",
    search_agent
)

workflow.add_node(
    "rca",
    rca_agent
)

workflow.add_node(
    "recommend",
    recommendation_agent
)

workflow.add_node(
    "summary",
    summary_agent
)

workflow.set_entry_point("search")

workflow.add_edge(
    "search",
    "rca"
)

workflow.add_edge(
    "rca",
    "recommend"
)

workflow.add_edge(
    "recommend",
    "summary"
)

workflow.add_edge(
    "summary",
    END
)

graph = workflow.compile()