import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# データの読み込みとカラム名の小文字化
df = pl.scan_parquet('test.parquet').collect()
df = df.rename({col: col.lower() for col in df.columns})

# ユニークな 'day' の値を取得
day_values = df.select(pl.col('day').unique()).to_series().to_list()

for day_value in day_values:
    # 'day' ごとのデータをフィルタリング
    df_day = df.filter(pl.col('day') == day_value)

    # 各カラムの最小値と最大値を取得
    book_min, book_max = df_day.select(pl.min('book'), pl.max('book')).row(0)
    note_min, note_max = df_day.select(pl.min('note'), pl.max('note')).row(0)
    text_min, text_max = df_day.select(pl.min('text'), pl.max('text')).row(0)

    # パターンの組み合わせを定義
    patterns = [
        {'book': book_min, 'note': note_min, 'text': text_min},
        {'book': book_max, 'note': note_min, 'text': text_min},
        {'book': book_max, 'note': note_max, 'text': text_min},
        {'book': book_max, 'note': note_max, 'text': text_max},
    ]

    for idx, pattern in enumerate(patterns, start=1):
        # パターンに基づいてデータをフィルタリング
        df_filtered = df_day.filter(
            (pl.col('book') == pattern['book']) &
            (pl.col('note') == pattern['note']) &
            (pl.col('text') == pattern['text'])
        )

        # データが存在しない場合はエラーを発生
        if df_filtered.is_empty():
            raise ValueError(
                f"No data for day={day_value}, book={pattern['book']}, "
                f"note={pattern['note']}, text={pattern['text']}"
            )

        # 'point' ごとにカウントを集計
        point_counts = (
            df_filtered.groupby('point')
            .agg(pl.count())
            .sort('point')
        ).rename({'count': 'count'})

        point_counts_pd = point_counts.to_pandas()

        # サブプロットの作成
        fig = make_subplots(
            rows=1,
            cols=2,
            subplot_titles=('Log Plot', 'Normal Plot')
        )

        # プロットの追加
        for col_idx, yaxis_type in enumerate(['log', 'linear'], start=1):
            trace = go.Scatter(
                x=point_counts_pd['point'],
                y=point_counts_pd['count'],
                mode='lines+markers',
                name=f'day={day_value}, Pattern {idx}'
            )
            fig.add_trace(trace, row=1, col=col_idx)
            fig.update_yaxes(type=yaxis_type, row=1, col=col_idx)

        # レイアウトの更新
        fig.update_layout(
            title=(
                f"day={day_value}, Pattern {idx}: book={pattern['book']}, "
                f"note={pattern['note']}, text={pattern['text']}"
            ),
            xaxis_title='point',
            yaxis_title='Count'
        )

        # プロット結果を保存
        fig.write_html(
            f'output_day_{day_value}_pattern_{idx}.html',
            include_plotlyjs='cdn'
        )