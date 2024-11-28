import polars as pl
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

# フィルタリング条件を変数として定義
we_value = 25000
fbc_threshold = 400

# データの読み込みとフィルタリング
df = (
    pl.scan_parquet('test.parquet')
    .filter(pl.col('we') == we_value)
    .collect()
)

# 統計情報を取得（Polars の describe メソッドを使用）
stats = df.describe()

# 統計情報を Pandas のデータフレームに変換
stats_pd = stats.to_pandas()

# テーブルを HTML 形式に変換（スタイルを適用）
html_table = stats_pd.to_html(classes='table', index=False)

# ユニークなチップ ID のリストを取得し、ソートして順番を固定
chip_ids = df.select(pl.col('chip').unique()).to_series().to_list()
chip_ids.sort()  # チップ ID をソート

# サブプロットの行数と列数を計算
num_chips = len(chip_ids)
cols = 3  # 列数を固定
rows = math.ceil(num_chips / cols)  # 行数を計算

# サブプロットの設定
fig = make_subplots(
    rows=rows,
    cols=cols,
    subplot_titles=[f'Chip {chip}' for chip in chip_ids]
)

max_count = 0  # 全てのデータの中での最大カウントを格納

for i, chip in enumerate(chip_ids):
    chip_data = df.filter(pl.col('chip') == chip)
    # fbc が指定の閾値以上のデータをフィルタリング
    chip_data_filtered = chip_data.filter(pl.col('fbc') >= fbc_threshold)
    # チップ内のユニークな block のリストを取得し、ソート
    block_ids = chip_data.select(pl.col('block').unique()).to_series().to_list()
    block_ids.sort()
    # block の全範囲を含むデータフレームを作成
    block_full_range = pl.DataFrame({'block': block_ids})
    # block ごとに fbc のカウントを集計
    block_counts = (
        chip_data_filtered.groupby('block')
        .agg(pl.count('fbc').alias('count'))
        .sort('block')
    )
    # 全ての block を含めるために、block_full_range と結合
    block_counts_full = block_full_range.join(block_counts, on='block', how='left').fill_null(0)
    # block カラムを文字列型に変換
    block_counts_full = block_counts_full.with_columns([
        pl.col('block').cast(pl.Utf8)
    ])
    # pandas データフレームに変換
    block_counts_pd = block_counts_full.to_pandas()
    # x 軸にブロック ID（文字列型）を使用
    trace = go.Bar(
        x=block_counts_pd['block'],
        y=block_counts_pd['count'],
        name=f'Chip {chip}'
    )
    row = i // cols + 1
    col = i % cols + 1
    fig.add_trace(trace, row=row, col=col)
    # x 軸の設定
    fig.update_xaxes(
        title_text='Block ID',
        showgrid=True,
        gridcolor='gray',
        gridwidth=0.5,
        tickangle=45,  # ラベルを45度傾ける
        row=row,
        col=col,
        type='category'  # x 軸をカテゴリ型に設定
    )
    # y 軸の設定
    fig.update_yaxes(
        title_text='カウント数',
        showgrid=True,
        gridcolor='gray',
        gridwidth=0.5,
        row=row,
        col=col
    )
    # 最大カウントを更新
    current_max = block_counts_pd['count'].max()
    if current_max > max_count:
        max_count = current_max

# y 軸の範囲を全てのサブプロットで共通化
yaxis_max = max_count * 1.1  # 最大カウントに10%の余裕を持たせる
fig.update_yaxes(range=[0, yaxis_max], row=None, col=None)

# タイトルにフィルタリング条件を記載
title_text = f"各チップの Block ごとの FBCカウント（we = {we_value}, fbc >= {fbc_threshold}）"

# レイアウトの更新（テンプレートを 'plotly_dark' に設定）
fig.update_layout(
    height=rows * 300 + 500,  # 行数に応じて高さを調整（テーブルの分を追加）
    width=1200,
    title_text=title_text,
    showlegend=False,
    template='plotly_dark',  # カラースキームを 'plotly_dark' に設定
    margin=dict(l=50, r=50, t=100, b=50)  # マージンを調整
)

# カスタム HTML テンプレートを作成
html_template = f"""
<html>
<head>
    <title>プロットと統計情報</title>
    <style>
        body {{
            background-color: #000000;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
        }}
        .table {{
            width: 1200px;
            margin: 0 auto;
            border-collapse: collapse;
            color: #FFFFFF;
        }}
        .table tbody tr:nth-of-type(odd) {{
            background-color: #404040;  /* 奇数行：暗めのグレー */
        }}
        .table tbody tr:nth-of-type(even) {{
            background-color: #000000;  /* 偶数行：黒 */
        }}
        th, td {{
            padding: 8px 12px;
            border: 1px solid #606060;
            text-align: center;
        }}
        h1, h2 {{
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>{title_text}</h1>
    <!-- 統計情報のテーブルを表示 -->
    <h2>データの統計情報</h2>
    {html_table}
    <!-- プロットを表示 -->
    {fig.to_html(include_plotlyjs='cdn', full_html=False)}
</body>
</html>
"""

# HTML ファイルに保存
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_template)