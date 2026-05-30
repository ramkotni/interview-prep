from langgraph.graph import StateGraph

from graph.state import PaymentState

from agents.data_loader_agent import load_data
from agents.prediction_agent import predict_risk
from agents.root_cause_agent import analyze_root_causes
from agents.recommendation_agent import (
    generate_recommendations
)
from agents.report_agent import generate_report
from agents.email_agent import send_email

workflow = StateGraph(PaymentState)

workflow.add_node(
    "load_data",
    load_data
)

workflow.add_node(
    "predict_risk",
    predict_risk
)

workflow.add_node(
    "root_cause",
    analyze_root_causes
)

workflow.add_node(
    "recommendations",
    generate_recommendations
)

workflow.add_node(
    "report",
    generate_report
)

workflow.add_node(
    "email",
    send_email
)

workflow.set_entry_point("load_data")

workflow.add_edge(
    "load_data",
    "predict_risk"
)

workflow.add_edge(
    "predict_risk",
    "root_cause"
)

workflow.add_edge(
    "root_cause",
    "recommendations"
)

workflow.add_edge(
    "recommendations",
    "report"
)

workflow.add_edge(
    "report",
    "email"
)

graph = workflow.compile()