"""
17_TMDB-TOP300_case.py
Script version of 16_case.ipynb with reasonable encapsulation.
Creates four subplots that summarize the TMDB Top300 dataset and saves the figure.
"""
from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import os

# NOTE:
# - pandas is used to read and manipulate the CSV data
# - matplotlib is used to create plots and save the final image
# - os is used to check/create output directories
# - Type hints (Optional, Axes) improve readability and editor support

def load_data(csv_path: str) -> pd.DataFrame:
    """Load CSV and return a DataFrame. Raises FileNotFoundError if missing."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Data file not found: {csv_path}")
    # Read only the columns we need
    df = pd.read_csv(csv_path, usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'], dtype={'年份': 'Int64'})
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning and normalization used by the plots.
    - Fill missing 年份 from 上映时间 (first 4 chars)
    - Ensure 类型 and 语言 are strings (fill NA where needed)
    """
    # Work on a copy so caller's DataFrame is not mutated
    df = df.copy()
    # If 年份 is missing, try to extract the year from 上映时间 (assumes 'YYYY...' format)
    if '上映时间' in df.columns:
        # .astype(str) ensures NaN won't break the string slice operation
        df['年份'] = df['年份'].fillna(df['上映时间'].astype(str).str[0:4])
    # Coerce 年份 to pandas nullable integer if possible for consistent grouping
    try:
        df['年份'] = df['年份'].astype('Int64')
    except Exception:
        # If conversion fails, keep existing values (safe fallback)
        pass
    # Ensure 类型 and 语言 are non-null strings to avoid errors during splitting/counting
    df['类型'] = df['类型'].fillna('')
    df['语言'] = df['语言'].fillna('未知')
    return df


def plot_year_count(ax: Axes, df: pd.DataFrame) -> None:
    """Plot movie count by year as a line chart on axes ax.

    Steps:
    1) Group by 年份 to count movies per year
    2) Build a continuous x-range from min to max year so years with zero movies show as 0
    3) Draw a simple line plot and format ticks/grid
    """
    # Count movies per year. The index is the year values (may be pandas IntegerIndex)
    year_count = df.groupby('年份')['年份'].count()
    # Build continuous x range so missing years are represented with zero counts
    min_year = int(year_count.index.min())
    max_year = int(year_count.index.max())
    x = list(range(min_year, max_year + 1))
    # For each year in the continuous range, fetch the count (default 0)
    y = [int(year_count.get(i, 0)) for i in x]
    # Plot and label axes
    ax.plot(x, y, color='green')
    ax.set_title('电影数量变化折线图', fontsize=14)
    ax.set_xlabel('年份')
    ax.set_ylabel('电影数量')
    # Choose sparse x ticks to avoid clutter when range is large
    step = max(1, (max_year - min_year) // 10)
    ax.set_xticks(x[::step])
    ax.grid(linestyle='--', alpha=0.5)


def plot_language_count(ax: Axes, df: pd.DataFrame) -> None:
    """Plot count of movies by language as a bar chart."""
    language_count = df.groupby('语言')['语言'].count().sort_values(ascending=False)
    x_labels = language_count.index.tolist()
    y_vals = language_count.values.tolist()
    ax.bar(x_labels, y_vals, color='orange', width=0.7)
    ax.set_title('不同语言电影数量柱状图', fontsize=14)
    ax.set_xlabel('语言')
    ax.set_ylabel('电影数量')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(linestyle='--', alpha=0.5)


def plot_type_count(ax: Axes, df: pd.DataFrame) -> None:
    """Plot count of movies by type (splitting 类型 by comma).

    The 类型 column may contain multiple comma-separated genres per movie (e.g. "剧情, 犯罪").
    This function splits those strings and aggregates counts for each genre.
    """
    type_count = {}
    # Split the 类型 string for each row and count each genre separately
    for types in df['类型'].astype(str).str.split(','):
        for t in types:
            t = t.strip()
            if not t:
                # Skip empty values resulting from missing data or trailing commas
                continue
            type_count[t] = type_count.get(t, 0) + 1
    # Sort genres by count descending for clearer plotting
    items = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    if not items:
        ax.text(0.5, 0.5, '无 类型 数据', ha='center', va='center')
        return
    labels, counts = zip(*items)
    ax.bar(labels, counts, color='b', width=0.7)
    ax.set_title('不同类型电影数量柱状图', fontsize=14)
    ax.set_xlabel('类型')
    ax.set_ylabel('电影数量')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(linestyle='--', alpha=0.5)


def plot_score_pie(ax: Axes, df: pd.DataFrame) -> None:
    """Plot pie chart of movie counts by score, merge small slices into '其他'."""
    score_count = df.groupby('评分')['评分'].count()
    total = score_count.sum()
    if total == 0:
        ax.text(0.5, 0.5, '无 评分 数据', ha='center', va='center')
        return
    large = score_count.loc[score_count / total >= 0.02].copy()
    small = score_count.loc[score_count / total < 0.02]
    if small.shape[0] > 0:
        large['其他'] = small.sum()
    labels = large.index.tolist()
    values = large.values.tolist()
    ax.pie(values, labels=labels, autopct='%.1f%%', startangle=30, radius=1.0)
    ax.set_title('不同评分电影数量占比饼状图', fontsize=14)
    ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2))


def generate_and_save_figure(df: pd.DataFrame, out_path: str, dpi: int = 100, show: bool = False) -> None:
    """Create the 2x2 figure, render plots and save to out_path.

    Responsibilities:
    - configure fonts for Chinese labels
    - create a 2x2 matplotlib figure and dispatch plotting functions
    - ensure output directory exists and save the final image
    - optionally display the figure
    """
    # Configure font to support Chinese characters on the plots
    plt.rcParams['font.sans-serif'] = ['SimHei']  # support Chinese
    # Create a 2x2 grid of axes for our four summary charts
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=dpi)
    fig.suptitle('TMDB-TOP300电影榜单数据统计', fontsize=20, x=0.5, y=0.93)
    fig.subplots_adjust(wspace=0.3, hspace=0.4)
    # Unpack axes for readability
    ax1 = axes[0][0]
    ax2 = axes[0][1]
    ax3 = axes[1][0]
    ax4 = axes[1][1]

    # Draw each subplot using the helper functions
    plot_year_count(ax1, df)
    plot_language_count(ax2, df)
    plot_type_count(ax3, df)
    plot_score_pie(ax4, df)

    # Ensure output directory exists before saving
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    # Save the composed figure to disk
    fig.savefig(out_path, dpi=dpi, bbox_inches='tight')
    if show:
        # Show the interactive window when requested (useful for local debugging)
        plt.show()
    # Close the figure to free memory
    plt.close(fig)


def main(csv_path: str = 'data/movies.csv', out_image: str = 'data/TMDB-TOP300.png', show: bool = False) -> None:
    df = load_data(csv_path)
    df = preprocess_data(df)
    generate_and_save_figure(df, out_image, show=show)
    print(f'图表已保存到: {out_image}')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='生成 TMDB-TOP300 数据统计图')
    parser.add_argument('--csv', '-c', default='data/movies.csv', help='输入 CSV 文件路径')
    parser.add_argument('--out', '-o', default='data/TMDB-TOP300.png', help='输出图片路径')
    parser.add_argument('--show', action='store_true', help='显示图形窗口')
    args = parser.parse_args()
    main(csv_path=args.csv, out_image=args.out, show=args.show)
