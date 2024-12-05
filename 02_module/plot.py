import argparse
from pathlib import Path
from glob import glob
from enum import Enum
import logging
import itertools

import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


class Variables(Enum):
    COIN = "coin"
    BOX = "box"
    DESK = "desk"
    RING = "ring"
    PARIS = "paris"


class ByVars(Enum):
    BOOK = "book"
    NOTE = "note"
    TEXT = "text"
    CUP = "cup"
    # 他に追加したい場合はここに定義


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process data and generate plots.")
    parser.add_argument(
        "--data_path",
        type=str,
        default="test.parquet",
        help="Path to the input Parquet data file.",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="output_dir/",
        help="Directory to save the output HTML files.",
    )
    return parser.parse_args()


def load_data(data_path):
    try:
        # データの読み込みとカラム名の小文字化
        df = pl.read_parquet(data_path)
        df = df.rename({col: col.lower() for col in df.columns})

        # 必要なカラムの存在確認
        required_columns = {
            "coin",
            "box",
            "pen",
            "book",
            "note",
            "text",
            "point",
            "cup",
            "bottle",
        }
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns in data: {missing_columns}")

        # 'desk' と 'ring' の計算
        df = df.with_columns(
            [
                ((pl.col("pen") // 112) % 5).alias("desk"),
                (pl.col("pen") % 112).alias("ring"),
            ]
        )

        # 'paris' カラムがない場合は作成
        if "paris" not in df.columns:
            df = df.with_columns([(pl.col("pen") % 3).alias("paris")])

        return df

    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


def get_unique_values(df, column):
    try:
        values = df.select(pl.col(column).unique()).to_series().to_list()
        values.sort()
        return values
    except Exception as e:
        logging.error(f"Error getting unique values for column '{column}': {e}")
        raise


def get_conditions(df, condition_vars):
    try:
        conditions = {}
        for var in condition_vars:
            unique_values = get_unique_values(df, var)
            conditions[var] = unique_values
        return conditions
    except Exception as e:
        logging.error(f"Error getting conditions: {e}")
        raise


def generate_condition_combinations(conditions_dict):
    try:
        condition_combinations = list(itertools.product(*conditions_dict.values()))
        conditions = []
        for combination in condition_combinations:
            condition = dict(zip(conditions_dict.keys(), combination))
            conditions.append(condition)
        return conditions
    except Exception as e:
        logging.error(f"Error generating condition combinations: {e}")
        raise


def filter_data(df, filter_dict):
    try:
        condition = pl.all()
        for key, value in filter_dict.items():
            condition &= pl.col(key) == value
        df_filtered = df.filter(condition)
        return df_filtered
    except Exception as e:
        logging.error(f"Error filtering data with {filter_dict}: {e}")
        raise


def aggregate_point_counts(df_filtered):
    try:
        point_counts = (
            df_filtered.groupby("point").agg(pl.count().alias("count")).sort("point")
        )
        return point_counts.to_pandas()
    except Exception as e:
        logging.error(f"Error aggregating point counts: {e}")
        raise


def create_figure(rows=1, cols=2, subplot_titles=None, width=1600, height=800):
    try:
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
        fig.update_layout(width=width, height=height)
        return fig
    except Exception as e:
        logging.error(f"Error creating figure: {e}")
        raise


def add_traces(fig, x, y, name, row=1, col=1, yaxis_types=("log", "linear")):
    try:
        for idx, y_type in enumerate(yaxis_types):
            trace = go.Scatter(
                x=x,
                y=y,
                mode="lines+markers",
                name=name,
            )
            fig.add_trace(trace, row=row, col=col + idx)
            fig.update_yaxes(type=y_type, row=row, col=col + idx)
        return fig
    except Exception as e:
        logging.error(f"Error adding traces: {e}")
        raise


def update_figure_layout(fig, title, xaxis_title, yaxis_title):
    try:
        fig.update_layout(
            title=title,
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
        )
        return fig
    except Exception as e:
        logging.error(f"Error updating figure layout: {e}")
        raise


def save_figure(fig, output_file):
    try:
        fig.write_html(str(output_file), include_plotlyjs="cdn")
    except Exception as e:
        logging.error(f"Error saving figure to {output_file}: {e}")
        raise


def generate_individual_plot(df, day_value, condition_dict, idx, output_dir):
    try:
        condition = {"day": day_value}
        condition.update(condition_dict)
        df_filtered = filter_data(df, condition)
        if df_filtered.is_empty():
            logging.warning(f"No data for condition: {condition}")
            return
        point_counts_pd = aggregate_point_counts(df_filtered)
        fig = create_figure()
        fig = add_traces(
            fig, point_counts_pd["point"], point_counts_pd["count"], name=str(condition)
        )
        title = f"Condition {idx}: {condition}"
        fig = update_figure_layout(fig, title, "point", "Count")
        output_file = output_dir / f"plot_{idx}_day_{day_value}.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(
            f"Error generating individual plot for condition {condition}: {e}"
        )
        raise


def generate_individual_plots(df, day_values, conditions, output_dir):
    for idx, condition_dict in enumerate(conditions, start=1):
        for day_value in day_values:
            generate_individual_plot(df, day_value, condition_dict, idx, output_dir)


def calculate_mean_max_point(df, group_by_vars):
    try:
        agg_df = (
            df.groupby(group_by_vars)
            .agg(
                [
                    pl.col("point").mean().alias("mean_point"),
                    pl.col("point").max().alias("max_point"),
                ]
            )
            .sort(group_by_vars[0])
        )
        return agg_df.to_pandas()
    except Exception as e:
        logging.error(f"Error calculating mean and max point: {e}")
        raise


def generate_subplot_for_variable(fig, df, variable, by_var, row):
    try:
        agg_df = calculate_mean_max_point(df, [variable.value, by_var.value])
        if agg_df.empty:
            logging.warning(
                f"No data available for variable {variable.value} by {by_var.value}"
            )
            return fig
        # max point のプロット
        fig.add_trace(
            go.Scatter(
                x=agg_df[variable.value],
                y=agg_df["max_point"],
                mode="markers",
                marker=dict(size=8),
                name=f"Max point by {by_var.value}",
            ),
            row=row,
            col=1,
        )
        # mean point のプロット
        fig.add_trace(
            go.Scatter(
                x=agg_df[variable.value],
                y=agg_df["mean_point"],
                mode="markers",
                marker=dict(size=8),
                name=f"Mean point by {by_var.value}",
            ),
            row=row,
            col=2,
        )
        fig.update_xaxes(title_text=variable.value, row=row, col=1)
        fig.update_xaxes(title_text=variable.value, row=row, col=2)
        fig.update_yaxes(title_text="Max point", row=row, col=1)
        fig.update_yaxes(title_text="Mean point", row=row, col=2)
        return fig
    except Exception as e:
        logging.error(
            f"Error generating subplot for {variable.value} by {by_var.value}: {e}"
        )
        raise


def generate_subplots(df, variable, output_dir, plot_number, by_vars):
    try:
        num_vars = len(by_vars)
        rows = num_vars
        cols = 2
        subplot_titles = []
        for by_var in by_vars:
            subplot_titles.extend(
                [
                    f"{variable.value} by {by_var.value} (max point)",
                    f"{variable.value} by {by_var.value} (mean point)",
                ]
            )
        fig = create_figure(
            rows=rows, cols=cols, subplot_titles=subplot_titles, height=rows * 400
        )

        for idx, by_var in enumerate(by_vars):
            row = idx + 1
            fig = generate_subplot_for_variable(fig, df, variable, by_var, row)

        title = f"Plot {plot_number}: Analysis by {variable.value}"
        fig = update_figure_layout(fig, title, variable.value, "point")
        output_file = output_dir / f"plot_{plot_number}_{variable.value}.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating subplots for {variable.value}: {e}")
        raise


def generate_additional_plots(df, output_dir):
    variables = [
        Variables.COIN,
        Variables.BOX,
        Variables.DESK,
        Variables.RING,
        Variables.PARIS,
    ]
    plot_number = 9
    by_vars = [ByVars.BOOK, ByVars.NOTE, ByVars.TEXT, ByVars.CUP]

    for variable in variables:
        generate_subplots(df, variable, output_dir, plot_number, by_vars)
        plot_number += 1

    generate_ring_paris_plot(df, output_dir, plot_number, by_vars)


def generate_ring_paris_plot(df, output_dir, plot_number, by_vars):
    try:
        num_vars = len(by_vars)
        rows = num_vars
        cols = 2
        subplot_titles = []
        for by_var in by_vars:
            subplot_titles.extend(
                [
                    f"ring and paris by {by_var.value} (max point)",
                    f"ring and paris by {by_var.value} (mean point)",
                ]
            )
        fig = create_figure(
            rows=rows, cols=cols, subplot_titles=subplot_titles, height=rows * 400
        )

        for idx, by_var in enumerate(by_vars):
            row = idx + 1
            agg_df = calculate_mean_max_point(df, ["ring", "paris", by_var.value])
            if agg_df.empty:
                logging.warning(f"No data available for ring and paris by {by_var.value}")
                continue
            # max point のプロット
            fig.add_trace(
                go.Scatter(
                    x=agg_df["ring"],
                    y=agg_df["max_point"],
                    mode="markers",
                    marker=dict(size=8),
                    name=f"Max point by {by_var.value}",
                ),
                row=row,
                col=1,
            )
            # mean point のプロット
            fig.add_trace(
                go.Scatter(
                    x=agg_df["ring"],
                    y=agg_df["mean_point"],
                    mode="markers",
                    marker=dict(size=8),
                    name=f"Mean point by {by_var.value}",
                ),
                row=row,
                col=2,
            )
            fig.update_xaxes(title_text="ring", row=row, col=1)
            fig.update_xaxes(title_text="ring", row=row, col=2)
            fig.update_yaxes(title_text="Max point", row=row, col=1)
            fig.update_yaxes(title_text="Mean point", row=row, col=2)

        title = f"Plot {plot_number}: Analysis by ring and paris"
        fig = update_figure_layout(fig, title, "ring", "point")
        output_file = output_dir / f"plot_{plot_number}_ring_paris.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating ring and paris plot: {e}")
        raise


def calculate_mean_point(df, day_value, condition_vars):
    try:
        condition = {"day": day_value}
        condition.update(condition_vars)
        df_filtered = filter_data(df, condition)
        if df_filtered.is_empty():
            logging.warning(f"No data for condition: {condition}")
            return None, None
        mean_point = df_filtered.select(pl.mean("point")).item()
        return day_value, mean_point
    except Exception as e:
        logging.error(f"Error calculating mean point: {e}")
        raise


def generate_combined_plot(df, day_values, conditions, output_dir):
    try:
        fig = create_figure()
        for idx, condition_dict in enumerate(conditions, start=1):
            x_values = []
            y_values = []
            for day_value in day_values:
                x, y = calculate_mean_point(df, day_value, condition_dict)
                if x is not None and y is not None:
                    x_values.append(x)
                    y_values.append(y)
            if x_values and y_values:
                fig = add_traces(fig, x_values, y_values, name=f"Condition {idx}")
            else:
                logging.warning(f"No data available for Condition {idx}")
        title = "Combined Plot of All Conditions"
        fig = update_figure_layout(fig, title, "day", "Mean point")
        output_file = output_dir / "all_conditions_combined.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating combined plot: {e}")
        raise


def combine_html_files(output_dir):
    try:
        html_files = sorted(
            glob(str(output_dir / "plot_*.html")), key=lambda x: int(x.split("_")[-2])
        )
        combined_html = ""
        for html_file in html_files:
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()
                body_content = content.split("<body>")[1].split("</body>")[0]
                combined_html += body_content
        combined_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8" />
        <title>Combined Plots</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
        {combined_html}
        </body>
        </html>
        """
        output_file = output_dir / "combined_plots.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(combined_html)
    except Exception as e:
        logging.error(f"Error combining HTML files: {e}")
        raise


def generate_parallel_coordinates_plot(df, condition_vars, output_dir):
    try:
        df_filtered = filter_data(df, condition_vars)
        if df_filtered.is_empty():
            logging.warning("No data available for Parallel Coordinates Plot")
            return
        point_counts = (
            df_filtered.groupby(["day", "point"]).agg(pl.count().alias("count")).sort("day")
        )
        df_px = point_counts.to_pandas()
        fig = px.parallel_coordinates(df_px, dimensions=["day", "point", "count"])
        output_file = output_dir / "parallel_coordinates_plot.html"
        fig.write_html(str(output_file), include_plotlyjs="cdn")
    except Exception as e:
        logging.error(f"Error generating parallel coordinates plot: {e}")
        raise


def generate_bottle_cup_plot(df, output_dir):
    try:
        df_filtered = df.filter(
            ((pl.col("bottle") == 0) & (pl.col("cup") == 0))
            | ((pl.col("bottle") == 1) & (pl.col("cup") != 0))
        )
        if df_filtered.is_empty():
            logging.warning("No data available for bottle and cup plot")
            return
        df_pd = df_filtered.to_pandas()
        fig = px.scatter(
            df_pd, x="cup", y="point", color="bottle", title="bottle and cup Plot"
        )
        output_file = output_dir / "bottle_cup_plot.html"
        fig.write_html(str(output_file), include_plotlyjs="cdn")
    except Exception as e:
        logging.error(f"Error generating bottle and cup plot: {e}")
        raise


def generate_text_plots(df, day_values, output_dir):
    try:
        cols = len(day_values)
        fig = create_figure(
            rows=1,
            cols=cols,
            subplot_titles=[f"day={day}" for day in day_values],
            width=1600,
        )
        for idx, day_value in enumerate(day_values, start=1):
            df_day = df.filter(pl.col("day") == day_value)
            if df_day.is_empty():
                logging.warning(f"No data for day={day_value}")
                continue
            point_counts = df_day.groupby("point").agg(pl.count().alias("count")).sort("point")
            point_counts_pd = point_counts.to_pandas()
            trace = go.Scatter(
                x=point_counts_pd["point"],
                y=point_counts_pd["count"],
                mode="lines+markers",
                name=f"day={day_value}",
            )
            fig.add_trace(trace, row=1, col=idx)
        title = "Text-based Plots"
        fig = update_figure_layout(fig, title, "point", "Count")
        output_file = output_dir / "text_plots.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating text plots: {e}")
        raise


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    args = parse_arguments()
    data_path = Path(args.data_path)
    output_dir = Path(args.output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        df = load_data(data_path)
        day_values = get_unique_values(df, "day")

        # 条件変数のリスト
        condition_vars_list = ["book", "note", "text"]
        # 各条件のユニークな値を取得
        conditions_dict = get_conditions(df, condition_vars_list)

        # 条件の組み合わせを作成
        conditions = generate_condition_combinations(conditions_dict)

        # 個別のプロットを生成（プロット1〜4）
        generate_individual_plots(df, day_values, conditions, output_dir)

        # 組み合わせたプロットを生成（プロット5）
        generate_combined_plot(df, day_values, conditions, output_dir)

        # パラレルコーディネートプロットを生成（プロット6）
        generate_parallel_coordinates_plot(df, conditions[-1], output_dir)

        # bottle と cup のプロットを生成（プロット7）
        generate_bottle_cup_plot(df, output_dir)

        # text に基づくプロットを生成（プロット8）
        generate_text_plots(df, day_values, output_dir)

        # 追加のプロットを生成（プロット9〜14）
        generate_additional_plots(df, output_dir)

        # HTML ファイルをまとめる
        combine_html_files(output_dir)

        logging.info("All plots generated successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()