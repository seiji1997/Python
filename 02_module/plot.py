import polars as pl
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# データの読み込み
df = pl.read_parquet('test.parquet')

# 不要なカラムを除外
columns_to_exclude = ['__index_level_0__', 'Serial', 'Readmode']
df_cleaned = df.drop(columns_to_exclude)

# データフレームを Pandas に変換（Plotly で使用するため）
df_pandas = df_cleaned.to_pandas()

# ユニークな 'Ondr' と 'we' の値を取得し、ソートして順番を固定
ondr_values = sorted(df_pandas['Ondr'].unique())
we_values = sorted(df_pandas['we'].unique())

# 出力ディレクトリを作成
output_dir = Path('output_ondr_plots')
output_dir.mkdir(exist_ok=True)

# カラーマップを定義（プロット内で一貫性を保つため）
colors = [
    'blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan', 'magenta'
]

# `Ondr` ごとにプロットを作成して保存
for ondr in ondr_values:
    # Ondr ごとのデータをフィルタリング
    df_ondr = df_pandas[df_pandas['Ondr'] == ondr]

    # we ごとに fbc のカウントを集計
    count_df = df_ondr.groupby('we').agg({'fbc': 'count'}).reset_index()
    # we の順序を維持するためにソート
    count_df = count_df.sort_values('we')
    # プロット用に we と count のリストを取得
    we_list = count_df['we'].tolist()
    count_list = count_df['fbc'].tolist()
    # カラーを取得
    color = colors[0]  # 単一のプロットなので色は一つで良い

    # サブプロットの設定（1行2列）
    fig = make_subplots(rows=1, cols=2, subplot_titles=('対数スケール', '線形スケール'))

    # 左のサブプロット（対数スケール）
    fig.add_trace(
        go.Scatter(
            x=we_list,
            y=count_list,
            mode='lines+markers',
            name=f'Ondr {ondr}',
            line=dict(color=color),
            showlegend=False
        ),
        row=1,
        col=1
    )

    # 右のサブプロット（線形スケール）
    fig.add_trace(
        go.Scatter(
            x=we_list,
            y=count_list,
            mode='lines+markers',
            name=f'Ondr {ondr}',
            line=dict(color=color),
            showlegend=False
        ),
        row=1,
        col=2
    )

    # 左のサブプロットの設定（対数スケール）
    fig.update_yaxes(
        type='log',
        title_text='FBC カウント数（対数）',
        row=1,
        col=1
    )

    # 右のサブプロットの設定（線形スケール）
    fig.update_yaxes(
        title_text='FBC カウント数（線形）',
        row=1,
        col=2
    )

    # 共通の x 軸設定
    fig.update_xaxes(
        title_text='we 値',
        row=1,
        col=1
    )
    fig.update_xaxes(
        title_text='we 値',
        row=1,
        col=2
    )

    # レイアウトの更新
    fig.update_layout(
        height=600,
        width=1200,
        title_text=f'Ondr {ondr} の we ごとの FBC カウント数',
        template='plotly_dark',
        plot_bgcolor='black'
    )

    # 出力ファイル名を作成
    output_file = output_dir / f'output_ondr_{ondr}.html'

    # プロット結果を HTML ファイルに保存
    fig.write_html(str(output_file), include_plotlyjs='cdn')

    print(f'Ondr {ondr} のプロットを保存しました: {output_file}')