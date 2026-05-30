def analyze_root_causes(state):

    df = state["df"]

    high_risk = df[
        df["FAILURE_PROBABILITY"] > 0.80
    ]

    causes = (
        high_risk["FAILURE_ROOT_CAUSE"]
        .value_counts()
        .head(5)
    )

    analysis = causes.to_string()

    state["root_causes"] = analysis

    print("Root cause analysis completed")

    return state