import streamlit as st
import pandas as pd
st.set_page_config(page_title="Delivery ETA Intelligence Dashboard", layout="wide")
st.sidebar.title("🚚 Dashboard Navigation")
st.sidebar.info( """ Delivery ETA Intelligence Dashboard Predict ETA, identify bottlenecks and analyze logistics networks.""" )
page = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Hub Analytics",
        "Bottleneck Analytics",
        "Network Analytics",
        "Network Summary",
        "Model Performance",
        "Graph Enhanced ETA",
        "Transportation Strategy"
    ]
)
st.title("🚚 Delivery ETA Intelligence Dashboard")

st.subheader(
    "ETA Prediction, Bottleneck Detection and Network Intelligence Platform" )
st.markdown(""" This platform combines Machine Learning, Business Analytics and Network Science to predict delivery ETAs, identify bottlenecks and analyze logistics network performance. """)
if page == "Overview":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Hubs", "1657")

    with col2:
        st.metric("Total Corridors", "2783")

    with col3:
        st.metric("Best Model", "Node2Vec + XGBoost")

    with col4:
        st.metric("R² Score", "0.9987")

    st.divider()


elif page == "Hub Analytics":

    top_source_hubs = pd.read_csv(
        "reports/top_source_hubs.csv"
    )

    st.header("🏢 Hub Analytics")

    st.subheader("Top Source Hubs")
    top_source_hubs.index = top_source_hubs.index + 1
    st.dataframe(
        top_source_hubs.head(10),
        use_container_width=True
    )

    chart_data = top_source_hubs.head(10).set_index("source_center")

    st.bar_chart(
        chart_data["shipments"]
    )

    top_destination_hubs = pd.read_csv(
        "reports/top_destination_hubs.csv"
    )

    st.subheader("Top Destination Hubs")
    top_destination_hubs.index = top_destination_hubs.index + 1
    st.dataframe(
        top_destination_hubs.head(10),
        use_container_width=True
    )

    destination_chart = top_destination_hubs.head(10).set_index(
        "destination_center"
    )

    st.bar_chart(
        destination_chart["shipments"]
    )

    st.divider()


elif page == "Bottleneck Analytics":

    bottlenecks = pd.read_csv(
        "reports/bottleneck_corridors.csv"
    )
    bottlenecks.index = bottlenecks.index + 1
    st.header("⚠️ Bottleneck Analytics")

    st.subheader("Top Bottleneck Corridors")

    st.dataframe(
        bottlenecks.head(10),
        use_container_width=True
    )

    corridor_chart = bottlenecks.head(10).copy()

    corridor_chart = corridor_chart.set_index("corridor")

    st.subheader("Average Delay by Corridor")

    st.bar_chart(
        corridor_chart["avg_delay"]
    )

    st.divider()


elif page == "Network Analytics":

    degree = pd.read_csv(
        "reports/degree_centrality_hubs.csv"
    )
    degree.index = degree.index + 1
    betweenness = pd.read_csv(
        "reports/betweenness_centrality_hubs.csv"
    )
    betweenness.index = betweenness.index + 1

    st.header("🌐 Network Analytics")

    degree_chart = degree.head(10).set_index("hub")

    st.subheader("Top Degree Centrality Hubs")

    st.bar_chart(
        degree_chart["degree_centrality"]
    )

    between_chart = betweenness.head(10).set_index("hub")

    st.subheader("Top Betweenness Centrality Hubs")

    st.bar_chart(
        between_chart["betweenness_centrality"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Degree Centrality")
        degree.index = degree.index + 1
        st.dataframe(
            degree.head(10),
            use_container_width=True
        )

    with col2:
        st.subheader("Betweenness Centrality")
        betweenness.index = betweenness.index + 1
        st.dataframe(
            betweenness.head(10),
            use_container_width=True
        )

    st.divider()


elif page == "Network Summary":

    network_summary = pd.read_csv(
        "reports/network_summary.csv"
    )

    st.header("📊 Network Summary")
    network_summary.index = network_summary.index + 1
    st.dataframe(
        network_summary,
        use_container_width=True
    )

    st.divider()
elif page == "Graph Enhanced ETA":

    st.header("🕸️ Graph Enhanced ETA Prediction")

    st.markdown("""
    This module extends ETA prediction using Node2Vec graph embeddings
    generated from the logistics network.

    Network Statistics:
    • 1,657 Logistics Hubs
    • 2,783 Corridors
    • 32-dimensional Node2Vec embeddings
    • 64 graph embedding features
    """)

    comparison = pd.DataFrame({
        "Metric": [
            "MAE",
            "RMSE",
            "R²",
            "Within 15% Accuracy"
        ],
        "Baseline XGBoost": [
            5.399,
            21.858,
            0.998669,
            99.535
        ],
        "Node2Vec + XGBoost": [
            5.177,
            21.272,
            0.998739,
            99.610
        ]
    })

    st.subheader("Benchmark Comparison")
    comparison.index = comparison.index + 1
    st.dataframe(
        comparison,
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "MAE Improvement",
            "4.1%"
        )

    with col2:
        st.metric(
            "RMSE Improvement",
            "2.7%"
        )

    with col3:
        st.metric(
            "Within 15% Gain",
            "+0.08%"
        )

    st.success(
        "Graph-enhanced ETA prediction achieved measurable improvements "
        "over the baseline model across all evaluation metrics."
    )

elif page == "Transportation Strategy":

    st.header("🚛 Transportation Strategy")

    st.subheader("FTL vs Carting Performance Comparison")

    route_summary = pd.read_csv(
        "reports/ftl_vs_carting_summary.csv"
    )
    route_summary.index = route_summary.index + 1
    st.dataframe(
        route_summary,
        use_container_width=True
    )

    st.divider()

    st.subheader("Transportation Mode Decision Framework")

    decision_framework = pd.read_csv(
        "reports/ftl_carting_decision_framework.csv"
    )

    st.dataframe(
        decision_framework,
        use_container_width=True
    )

    st.info(
        """
        Recommended Transportation Strategy:

        • Carting → Local distribution and last-mile deliveries

        • FTL → Long-haul and high-volume corridors

        • Distance < 50 km → Prefer Carting

        • Distance > 150 km → Prefer FTL
        """
    )

    comparison_chart = route_summary.copy()
    comparison_chart = comparison_chart.set_index("route_type")

    st.subheader("Average Distance Comparison")

    st.bar_chart(
        comparison_chart["avg_distance"]
    )

    st.divider()

elif page == "Model Performance":

    model_comparison = pd.read_csv(
        "reports/model_comparison.csv"
    )

    st.header("🤖 Model Performance")

    model_comparison.index = model_comparison.index + 1

    st.dataframe(
        model_comparison,
        use_container_width=True
    )

    st.success(
        "Best Production Model: Node2Vec + XGBoost | "
        "MAE = 5.18 | RMSE = 21.27 | R² = 0.9987"
    )