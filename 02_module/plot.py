import argparse
from pathlib import Path
from glob import glob
from enum import Enum
import logging
import itertools
from typing import Any, Dict, List, Optional, Tuple

import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np


class Variables(Enum):
    """Enumeration for different variables used in plotting."""
    COIN = "coin"
    BOX = "box"
    DESK = "desk"
    RING = "ring"
    PARIS = "paris"


class ByVars(Enum):
    """Enumeration for variables by which data is grouped."""
    BOOK = "book"
    NOTE = "note"
    TEXT = "text"
    CUP = "cup"
    # 他に追加したい場合はここに定義


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing data_path and output_path.
    """
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


def load_data(data_path: str) -> pl.DataFrame:
    """
    Load and preprocess data from a Parquet file.

    Args:
        data_path (str): Path to the input Parquet data file.

    Returns:
        pl.DataFrame: Preprocessed Polars DataFrame.

    Raises:
        ValueError: If required columns are missing.
        Exception: For any other errors during data loading.
    """
    try:
        # データの読み込みとカラム名の小文字化
        df = pl.read_parquet(data_path)
        df = df.rename({col: col.lower() for col in df.columns})

        # 必要なカラムの存在確認
        required_columns = {"coin", "box", "pen", "book", "note", "text", "point", "cup", "bottle"}
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns in data: {missing_columns}")

        # 'desk' と 'ring' の計算
        df = df.with_columns([
            ((pl.col("pen") // 112) % 5).alias("desk"),
            (pl.col("pen") % 112).alias("ring"),
        ])

        # 'paris' カラムがない場合は作成
        if "paris" not in df.columns:
            df = df.with_columns([
                (pl.col("pen") % 3).alias("paris")
            ])

        return df

    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


def get_unique_values(df: pl.DataFrame, column: str) -> List[Any]:
    """
    Retrieve sorted unique values from a specified column.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        column (str): Column name to retrieve unique values from.

    Returns:
        List[Any]: Sorted list of unique values.

    Raises:
        Exception: If an error occurs during retrieval.
    """
    try:
        values = df.select(pl.col(column).unique()).to_series().to_list()
        values.sort()
        return values
    except Exception as e:
        logging.error(f"Error getting unique values for column '{column}': {e}")
        raise


def get_min_max_values(df: pl.DataFrame, condition_vars: List[str]) -> Dict[str, Dict[str, Any]]:
    """
    Retrieve min and max values for each condition variable.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        condition_vars (List[str]): List of condition variable names.

    Returns:
        Dict[str, Dict[str, Any]]: Dictionary mapping each condition variable to its min and max values.

    Raises:
        Exception: If an error occurs during retrieval.
    """
    try:
        min_max = {}
        for var in condition_vars:
            min_val = df.select(pl.col(var).min()).item()
            max_val = df.select(pl.col(var).max()).item()
            min_max[var] = {"min": min_val, "max": max_val}
        return min_max
    except Exception as e:
        logging.error(f"Error getting min and max values for condition variables: {e}")
        raise


def generate_fixed_condition_patterns(min_max_dict: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Generate fixed condition patterns based on min and max values.

    The patterns are:
        1. {'book': book_min, 'note': note_min, 'text': text_min}
        2. {'book': book_max, 'note': note_min, 'text': text_min}
        3. {'book': book_max, 'note': note_max, 'text': text_min}
        4. {'book': book_max, 'note': note_max, 'text': text_max}

    Args:
        min_max_dict (Dict[str, Dict[str, Any]]): Dictionary mapping condition variables to their min and max values.

    Returns:
        List[Dict[str, Any]]: List of condition dictionaries representing the 4 patterns.

    Raises:
        KeyError: If required keys are missing in min_max_dict.
        Exception: For any other errors during pattern generation.
    """
    try:
        patterns = [
            {'book': min_max_dict['book']['min'], 'note': min_max_dict['note']['min'], 'text': min_max_dict['text']['min']},
            {'book': min_max_dict['book']['max'], 'note': min_max_dict['note']['min'], 'text': min_max_dict['text']['min']},
            {'book': min_max_dict['book']['max'], 'note': min_max_dict['note']['max'], 'text': min_max_dict['text']['min']},
            {'book': min_max_dict['book']['max'], 'note': min_max_dict['note']['max'], 'text': min_max_dict['text']['max']},
        ]
        return patterns
    except KeyError as ke:
        logging.error(f"Missing key in min_max_dict: {ke}")
        raise
    except Exception as e:
        logging.error(f"Error generating condition patterns: {e}")
        raise


def filter_data(df: pl.DataFrame, filter_dict: Dict[str, Any]) -> pl.DataFrame:
    """
    Filter the DataFrame based on a dictionary of conditions.

    Args:
        df (pl.DataFrame): Polars DataFrame to filter.
        filter_dict (Dict[str, Any]): Dictionary of conditions to apply.

    Returns:
        pl.DataFrame: Filtered Polars DataFrame.

    Raises:
        Exception: If an error occurs during filtering.
    """
    try:
        condition = pl.all()
        for key, value in filter_dict.items():
            condition &= (pl.col(key) == value)
        df_filtered = df.filter(condition)
        return df_filtered
    except Exception as e:
        logging.error(f"Error filtering data with {filter_dict}: {e}")
        raise


def aggregate_point_counts(df_filtered: pl.DataFrame) -> pd.DataFrame:
    """
    Aggregate the count of 'point' values in the filtered DataFrame.

    Args:
        df_filtered (pl.DataFrame): Filtered Polars DataFrame.

    Returns:
        pd.DataFrame: Pandas DataFrame with 'point' counts.

    Raises:
        Exception: If an error occurs during aggregation.
    """
    try:
        point_counts = (
            df_filtered.groupby("point")
            .agg(pl.count().alias("count"))
            .sort("point")
        )
        return point_counts.to_pandas()
    except Exception as e:
        logging.error(f"Error aggregating point counts: {e}")
        raise


def create_figure(rows: int =1, cols: int =2, subplot_titles: Optional[List[str]] = None,
                 width: int =1600, height: int =800) -> go.Figure:
    """
    Create a Plotly figure with specified subplots.

    Args:
        rows (int, optional): Number of subplot rows. Defaults to 1.
        cols (int, optional): Number of subplot columns. Defaults to 2.
        subplot_titles (Optional[List[str]], optional): Titles for each subplot. Defaults to None.
        width (int, optional): Width of the figure. Defaults to 1600.
        height (int, optional): Height of the figure. Defaults to 800.

    Returns:
        go.Figure: Created Plotly figure.

    Raises:
        Exception: If an error occurs during figure creation.
    """
    try:
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
        fig.update_layout(width=width, height=height)
        return fig
    except Exception as e:
        logging.error(f"Error creating figure: {e}")
        raise


def add_traces(fig: go.Figure, x: List[Any], y: List[Any], name: str,
               row: int =1, col: int =1, yaxis_types: Tuple[str, ...] =("log", "linear")) -> go.Figure:
    """
    Add traces to the figure for each y-axis type.

    Args:
        fig (go.Figure): Plotly figure to add traces to.
        x (List[Any]): X-axis data.
        y (List[Any]): Y-axis data.
        name (str): Name of the trace.
        row (int, optional): Row number for the subplot. Defaults to 1.
        col (int, optional): Column number for the subplot. Defaults to 1.
        yaxis_types (Tuple[str, ...], optional): Types for the y-axes. Defaults to ("log", "linear").

    Returns:
        go.Figure: Updated Plotly figure.

    Raises:
        Exception: If an error occurs while adding traces.
    """
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


def update_figure_layout(fig: go.Figure, title: str,
                         xaxis_title: str, yaxis_title: str) -> go.Figure:
    """
    Update the layout of the figure with titles.

    Args:
        fig (go.Figure): Plotly figure to update.
        title (str): Main title of the figure.
        xaxis_title (str): Title for the x-axis.
        yaxis_title (str): Title for the y-axis.

    Returns:
        go.Figure: Updated Plotly figure.

    Raises:
        Exception: If an error occurs while updating layout.
    """
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


def save_figure(fig: go.Figure, output_file: Path) -> None:
    """
    Save the Plotly figure as an HTML file.

    Args:
        fig (go.Figure): Plotly figure to save.
        output_file (Path): Path to save the HTML file.

    Raises:
        Exception: If an error occurs while saving the figure.
    """
    try:
        fig.write_html(str(output_file), include_plotlyjs="cdn")
    except Exception as e:
        logging.error(f"Error saving figure to {output_file}: {e}")
        raise


def generate_individual_plot(df: pl.DataFrame, day_value: Any,
                             condition_dict: Dict[str, Any], idx: int,
                             output_dir: Path) -> None:
    """
    Generate an individual plot for a specific 'day' value and condition.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        day_value (Any): Specific 'day' value to plot.
        condition_dict (Dict[str, Any]): Dictionary of conditions.
        idx (int): Condition index for naming.
        output_dir (Path): Directory to save the output HTML file.

    Raises:
        Exception: If an error occurs during plot generation.
    """
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
            fig, point_counts_pd["point"].tolist(), point_counts_pd["count"].tolist(),
            name=str(condition)
        )
        title = f"Condition {idx}: {condition}"
        fig = update_figure_layout(fig, title, "point", "Count")
        output_file = output_dir / f"plot_{idx}_day_{day_value}.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating individual plot for condition {condition}: {e}")
        raise


def generate_individual_plots(df: pl.DataFrame, day_values: List[Any],
                              conditions: List[Dict[str, Any]],
                              output_dir: Path) -> None:
    """
    Generate individual plots for all 'day' values across all conditions.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        day_values (List[Any]): List of unique 'day' values.
        conditions (List[Dict[str, Any]]): List of condition dictionaries.
        output_dir (Path): Directory to save the output HTML files.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    for idx, condition_dict in enumerate(conditions, start=1):
        for day_value in day_values:
            generate_individual_plot(df, day_value, condition_dict, idx, output_dir)


def calculate_mean_max_point(df: pl.DataFrame, group_by_vars: List[str]) -> pd.DataFrame:
    """
    Calculate the mean and max of 'point' grouped by specified variables.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        group_by_vars (List[str]): List of variables to group by.

    Returns:
        pd.DataFrame: Pandas DataFrame with mean and max 'point'.

    Raises:
        Exception: If an error occurs during calculation.
    """
    try:
        agg_df = df.groupby(group_by_vars).agg([
            pl.col("point").mean().alias("mean_point"),
            pl.col("point").max().alias("max_point"),
        ]).sort(group_by_vars[0])
        return agg_df.to_pandas()
    except Exception as e:
        logging.error(f"Error calculating mean and max point: {e}")
        raise


def generate_subplot_for_variable(fig: go.Figure, df: pl.DataFrame,
                                  variable: Variables, by_var: ByVars, row: int) -> go.Figure:
    """
    Generate a subplot for a specific variable and by_var.

    Args:
        fig (go.Figure): Plotly figure to add the subplot to.
        df (pl.DataFrame): Polars DataFrame.
        variable (Variables): Variable enumeration.
        by_var (ByVars): ByVars enumeration.
        row (int): Row number for the subplot.

    Returns:
        go.Figure: Updated Plotly figure.

    Raises:
        Exception: If an error occurs during subplot generation.
    """
    try:
        agg_df = calculate_mean_max_point(df, [variable.value, by_var.value])
        if agg_df.empty:
            logging.warning(f"No data available for variable {variable.value} by {by_var.value}")
            return fig
        # max point のプロット
        fig.add_trace(
            go.Scatter(
                x=agg_df[variable.value].tolist(),
                y=agg_df["max_point"].tolist(),
                mode="markers",
                marker=dict(size=8),
                name=f"Max point by {by_var.value}",
            ),
            row=row, col=1
        )
        # mean point のプロット
        fig.add_trace(
            go.Scatter(
                x=agg_df[variable.value].tolist(),
                y=agg_df["mean_point"].tolist(),
                mode="markers",
                marker=dict(size=8),
                name=f"Mean point by {by_var.value}",
            ),
            row=row, col=2
        )
        # 軸のタイトル設定
        fig.update_xaxes(title_text=variable.value, row=row, col=1)
        fig.update_xaxes(title_text=variable.value, row=row, col=2)
        fig.update_yaxes(title_text="Max point", row=row, col=1)
        fig.update_yaxes(title_text="Mean point", row=row, col=2)
        return fig
    except Exception as e:
        logging.error(f"Error generating subplot for {variable.value} by {by_var.value}: {e}")
        raise


def generate_subplots(df: pl.DataFrame, variable: Variables,
                     output_dir: Path, plot_number: int,
                     by_vars: List[ByVars]) -> None:
    """
    Generate subplots for a specific variable across all by_vars.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        variable (Variables): Variable enumeration.
        output_dir (Path): Directory to save the output HTML file.
        plot_number (int): Plot number for naming.
        by_vars (List[ByVars]): List of ByVars enumerations.

    Raises:
        Exception: If an error occurs during subplot generation.
    """
    try:
        num_vars = len(by_vars)
        rows = num_vars
        cols = 2
        subplot_titles = []
        for by_var in by_vars:
            subplot_titles.extend([
                f"{variable.value} by {by_var.value} (max point)",
                f"{variable.value} by {by_var.value} (mean point)"
            ])
        fig = create_figure(rows=rows, cols=cols, subplot_titles=subplot_titles,
                           height=rows * 400)

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


def generate_additional_plots(df: pl.DataFrame, output_dir: Path) -> None:
    """
    Generate additional plots (plots 9-14) for various variables.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        output_dir (Path): Directory to save the output HTML files.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    variables = [Variables.COIN, Variables.BOX, Variables.DESK, Variables.RING, Variables.PARIS]
    plot_number = 9
    by_vars = [ByVars.BOOK, ByVars.NOTE, ByVars.TEXT, ByVars.CUP]

    for variable in variables:
        generate_subplots(df, variable, output_dir, plot_number, by_vars)
        plot_number += 1

    # プロット14: ringとparisの組み合わせ
    generate_ring_paris_plot(df, output_dir, plot_number, by_vars)


def generate_ring_paris_plot(df: pl.DataFrame, output_dir: Path,
                             plot_number: int, by_vars: List[ByVars]) -> None:
    """
    Generate plot 14, which analyzes 'ring' and 'paris' together across all by_vars.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        output_dir (Path): Directory to save the output HTML file.
        plot_number (int): Plot number for naming.
        by_vars (List[ByVars]): List of ByVars enumerations.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    try:
        num_vars = len(by_vars)
        rows = num_vars
        cols = 2
        subplot_titles = []
        for by_var in by_vars:
            subplot_titles.extend([
                f"ring and paris by {by_var.value} (max point)",
                f"ring and paris by {by_var.value} (mean point)"
            ])
        fig = create_figure(rows=rows, cols=cols, subplot_titles=subplot_titles,
                           height=rows * 400)

        for idx, by_var in enumerate(by_vars):
            row = idx + 1
            try:
                agg_df = calculate_mean_max_point(df, ["ring", "paris", by_var.value])
                if agg_df.empty:
                    logging.warning(f"No data available for ring and paris by {by_var.value}")
                    continue
                # max point のプロット
                fig.add_trace(
                    go.Scatter(
                        x=agg_df["ring"].tolist(),
                        y=agg_df["max_point"].tolist(),
                        mode="markers",
                        marker=dict(size=8),
                        name=f"Max point by {by_var.value}",
                    ),
                    row=row, col=1
                )
                # mean point のプロット
                fig.add_trace(
                    go.Scatter(
                        x=agg_df["ring"].tolist(),
                        y=agg_df["mean_point"].tolist(),
                        mode="markers",
                        marker=dict(size=8),
                        name=f"Mean point by {by_var.value}",
                    ),
                    row=row, col=2
                )
                # 軸のタイトル設定
                fig.update_xaxes(title_text="ring", row=row, col=1)
                fig.update_xaxes(title_text="ring", row=row, col=2)
                fig.update_yaxes(title_text="Max point", row=row, col=1)
                fig.update_yaxes(title_text="Mean point", row=row, col=2)
            except Exception as e:
                logging.error(f"Error processing ring and paris by {by_var.value}: {e}")
                continue

        title = f"Plot {plot_number}: Analysis by ring and paris"
        fig = update_figure_layout(fig, title, "ring", "point")
        output_file = output_dir / f"plot_{plot_number}_ring_paris.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating ring and paris plot: {e}")
        raise


def calculate_mean_fbc(df: pl.DataFrame, day_value: Any,
                      condition_vars: Dict[str, Any]) -> Tuple[Any, Optional[float]]:
    """
    Calculate the mean 'point' for a specific 'day' value and conditions.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        day_value (Any): Specific 'day' value.
        condition_vars (Dict[str, Any]): Dictionary of additional conditions.

    Returns:
        Tuple[Any, Optional[float]]: Tuple containing the 'day' value and its mean 'point',
                                     or (day_value, None) if no data is available.

    Raises:
        Exception: If an error occurs during calculation.
    """
    try:
        condition = {"day": day_value}
        condition.update(condition_vars)
        df_filtered = filter_data(df, condition)
        if df_filtered.is_empty():
            logging.warning(f"No data for condition: {condition}")
            return day_value, None
        mean_point = df_filtered.select(pl.mean("point")).item()
        return day_value, mean_point
    except Exception as e:
        logging.error(f"Error calculating mean point: {e}")
        raise


def generate_combined_plot(df: pl.DataFrame, day_values: List[Any],
                           conditions: List[Dict[str, Any]], output_dir: Path) -> None:
    """
    Generate a combined plot of all conditions, plotting mean 'point' against 'day'.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        day_values (List[Any]): List of unique 'day' values.
        conditions (List[Dict[str, Any]]): List of condition dictionaries.
        output_dir (Path): Directory to save the output HTML file.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    try:
        fig = create_figure()
        for idx, condition_dict in enumerate(conditions, start=1):
            x_values = []
            y_values = []
            for day_value in day_values:
                day, mean_point = calculate_mean_fbc(df, day_value, condition_dict)
                if mean_point is not None:
                    x_values.append(day)
                    y_values.append(mean_point)
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


def combine_html_files(output_dir: Path) -> None:
    """
    Combine all individual HTML plot files into a single HTML file.

    Args:
        output_dir (Path): Directory containing the individual HTML plot files.

    Raises:
        Exception: If an error occurs during file combination.
    """
    try:
        # プロット番号順にHTMLファイルを取得
        html_files = sorted(
            glob(str(output_dir / "plot_*.html")),
            key=lambda x: int(Path(x).stem.split('_')[1])
        )
        combined_html = ""
        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # <body> の中身を抽出
                try:
                    body_content = content.split('<body>')[1].split('</body>')[0]
                    combined_html += body_content
                except IndexError:
                    logging.warning(f"Unexpected HTML format in file: {html_file}")
                    continue
        # ヘッダーとフッターを追加
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
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(combined_html)
    except Exception as e:
        logging.error(f"Error combining HTML files: {e}")
        raise


def generate_parallel_coordinates_plot(df: pl.DataFrame,
                                      condition_vars: Dict[str, Any],
                                      output_dir: Path) -> None:
    """
    Generate a parallel coordinates plot based on specified conditions.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        condition_vars (Dict[str, Any]): Dictionary of conditions to filter data.
        output_dir (Path): Directory to save the output HTML file.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    try:
        df_filtered = filter_data(df, condition_vars)
        if df_filtered.is_empty():
            logging.warning("No data available for Parallel Coordinates Plot")
            return
        # 'point'ごとにカウントを集計
        point_counts = (
            df_filtered.groupby(["day", "point"])
            .agg(pl.count().alias("count"))
            .sort("day")
        )
        df_px = point_counts.to_pandas()
        # パラレルコーディネートプロットを作成
        fig = px.parallel_coordinates(
            df_px, dimensions=["day", "point", "count"]
        )
        # プロットを保存
        output_file = output_dir / "parallel_coordinates_plot.html"
        fig.write_html(str(output_file), include_plotlyjs="cdn")
    except Exception as e:
        logging.error(f"Error generating parallel coordinates plot: {e}")
        raise


def generate_tempx_tempxd_plot(df: pl.DataFrame, output_dir: Path) -> None:
    """
    Generate a scatter plot for 'bottle' and 'cup' based on specified conditions.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        output_dir (Path): Directory to save the output HTML file.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    try:
        df_filtered = df.filter(
            ((pl.col("bottle") == 0) & (pl.col("cup") == 0)) |
            ((pl.col("bottle") == 1) & (pl.col("cup") != 0))
        )
        if df_filtered.is_empty():
            logging.warning("No data available for bottle and cup plot")
            return
        df_pd = df_filtered.to_pandas()
        # プロットを作成
        fig = px.scatter(
            df_pd, x="cup", y="point", color="bottle",
            title="bottle and cup Plot"
        )
        # プロットを保存
        output_file = output_dir / "bottle_cup_plot.html"
        fig.write_html(str(output_file), include_plotlyjs="cdn")
    except Exception as e:
        logging.error(f"Error generating bottle and cup plot: {e}")
        raise


def generate_offdr_plots(df: pl.DataFrame, day_values: List[Any],
                         output_dir: Path) -> None:
    """
    Generate plots based on 'text' for each 'day' value.

    Args:
        df (pl.DataFrame): Polars DataFrame.
        day_values (List[Any]): List of unique 'day' values.
        output_dir (Path): Directory to save the output HTML file.

    Raises:
        Exception: If an error occurs during plot generation.
    """
    try:
        cols = len(day_values)
        if cols == 0:
            logging.warning("No 'day' values available for text plots.")
            return
        fig = create_figure(rows=1, cols=cols,
                           subplot_titles=[f"day={day}" for day in day_values],
                           width=1600, height=400)
        for idx, day_value in enumerate(day_values, start=1):
            df_day = df.filter(pl.col("day") == day_value)
            if df_day.is_empty():
                logging.warning(f"No data for day={day_value}")
                continue
            point_counts = (
                df_day.groupby("point")
                .agg(pl.count().alias("count"))
                .sort("point")
            )
            point_counts_pd = point_counts.to_pandas()
            # プロットを追加
            trace = go.Scatter(
                x=point_counts_pd["point"].tolist(),
                y=point_counts_pd["count"].tolist(),
                mode="lines+markers",
                name=f"day={day_value}"
            )
            fig.add_trace(trace, row=1, col=idx)
        # レイアウトの更新
        title = "text-based Plots"
        fig = update_figure_layout(fig, title, "point", "Count")
        output_file = output_dir / "text_plots.html"
        save_figure(fig, output_file)
    except Exception as e:
        logging.error(f"Error generating text plots: {e}")
        raise


def generate_fixed_condition_patterns(min_max_dict: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Generate fixed condition patterns based on min and max values.

    The patterns are:
        1. {'book': book_min, 'note': note_min, 'text': text_min}
        2. {'book': book_max, 'note': note_min, 'text': text_min}
        3. {'book': book_max, 'note': note_max, 'text': text_min}
        4. {'book': book_max, 'note': note_max, 'text': text_max}

    Args:
        min_max_dict (Dict[str, Dict[str, Any]]): Dictionary mapping condition variables to their min and max values.

    Returns:
        List[Dict[str, Any]]: List of condition dictionaries representing the 4 patterns.

    Raises:
        KeyError: If required keys are missing in min_max_dict.
        Exception: For any other errors during pattern generation.
    """
    try:
        patterns = [
            {'book': min_max_dict['book']['min'], 'note': min_max_dict['note']['min'], 'text': min_max_dict['text']['min']},
            {'book': min_max_dict['book']['max'], 'note': min_max_dict['note']['min'], 'text': min_max_dict['text']['min']},
            {'book': min_max_dict['book']['max'], 'note': min_max_dict['note']['max'], 'text': min_max_dict['text']['min']},
            {'book': min_max_dict['book']['max'], 'note': min_max_dict['note']['max'], 'text': min_max_dict['text']['max']},
        ]
        return patterns
    except KeyError as ke:
        logging.error(f"Missing key in min_max_dict: {ke}")
        raise
    except Exception as e:
        logging.error(f"Error generating condition patterns: {e}")
        raise


def main() -> None:
    """
    Main function to orchestrate data processing and plot generation.
    """
    # ロギングの設定
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    args = parse_arguments()
    data_path = Path(args.data_path)
    output_dir = Path(args.output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    # サンプルデータの生成（必要に応じてコメントアウト）
    # generate_sample_data(output_dir / "test.parquet", num_records=1000)

    try:
        df = load_data(str(data_path))
        day_values = get_unique_values(df, "day")

        # 条件変数のリスト
        condition_vars_list = ["book", "note", "text"]
        # 各条件のminとmaxを取得
        min_max_dict = get_min_max_values(df, condition_vars_list)

        # 固定された条件のパターンを作成
        conditions = generate_fixed_condition_patterns(min_max_dict)

        # 個別のプロットを生成（プロット1〜4）
        generate_individual_plots(df, day_values, conditions, output_dir)

        # 組み合わせたプロットを生成（プロット5）
        generate_combined_plot(df, day_values, conditions, output_dir)

        # パラレルコーディネートプロットを生成（プロット6）
        if conditions:
            generate_parallel_coordinates_plot(df, conditions[-1], output_dir)
        else:
            logging.warning("No conditions available to generate Parallel Coordinates Plot.")

        # bottle と cup のプロットを生成（プロット7）
        generate_tempx_tempxd_plot(df, output_dir)

        # text に基づくプロットを生成（プロット8）
        generate_offdr_plots(df, day_values, output_dir)

        # 追加のプロットを生成（プロット9〜14）
        generate_additional_plots(df, output_dir)

        # HTML ファイルをまとめる
        combine_html_files(output_dir)

        logging.info("All plots generated successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


def generate_sample_data(output_path: Path, num_records: int = 1000) -> None:
    """
    Generate sample data and save it as a Parquet file for testing purposes.

    Args:
        output_path (Path): Path to save the sample Parquet file.
        num_records (int, optional): Number of records to generate. Defaults to 1000.
    """
    try:
        np.random.seed(0)
        data = {
            "coin": [f"coin_{i%10}" for i in range(num_records)],
            "box": [f"box_{i%5}" for i in range(num_records)],
            "pen": np.random.randint(0, 336, size=num_records),  # 112*3 = 336
            "book": np.random.randint(0, 5, size=num_records),
            "note": np.random.randint(0, 3, size=num_records),
            "text": np.random.randint(0, 4, size=num_records),
            "point": np.random.uniform(0, 100, size=num_records),
            "cup": np.random.choice([0, 8, 15, 35], size=num_records),
            "bottle": np.random.choice([0, 1], size=num_records, p=[0.5, 0.5]),
        }
        df_pd = pd.DataFrame(data)
        # Adjust 'cup' based on 'bottle'
        df_pd.loc[df_pd["bottle"] == 0, "cup"] = 0
        df = pl.from_pandas(df_pd)
        df.write_parquet(str(output_path))
        logging.info(f"Sample data generated at {output_path}")
    except Exception as e:
        logging.error(f"Error generating sample data: {e}")
        raise


if __name__ == "__main__":
    main()