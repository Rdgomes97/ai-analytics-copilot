import plotly.express as px


def numeric_histogram(df, column):
    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Distribution of {column}"
    )
    return fig


def categorical_bar(df, column):
    counts = df[column].value_counts().head(10).reset_index()
    counts.columns = [column, "count"]

    fig = px.bar(
        counts,
        x=column,
        y="count",
        title=f"Top Categories - {column}"
    )
    return fig
