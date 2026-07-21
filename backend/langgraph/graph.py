"""Pipeline graph definition: Webhook -> Documentation -> Risk -> TechDebt -> Summary -> Store -> Q&A.

TODO: build with langgraph.graph.StateGraph once node implementations exist.
"""

NODES = [
    "webhook",
    "documentation",
    "risk",
    "tech_debt",
    "summary",
    "store",
    "qa",
]

EDGES = [
    ("webhook", "documentation"),
    ("documentation", "risk"),
    ("risk", "tech_debt"),
    ("tech_debt", "summary"),
    ("summary", "store"),
    ("store", "qa"),
]


def build_graph():
    """TODO: construct and return the compiled LangGraph pipeline."""
    raise NotImplementedError
