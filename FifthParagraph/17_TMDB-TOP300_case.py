"""
17_TMDB-TOP300_case.py
将 16_case.ipynb 的逻辑封装为脚本形式。
生成 4 个子图，汇总 TMDB Top300 数据并保存为图片。
"""
from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import os

# 说明：
# - pandas 用于读取和处理 CSV 数据
# - matplotlib 用于绘图并保存最终图片
# - os 用于检查/创建输出目录
# - 类型注解（Optional, Axes）提升可读性与编辑器提示

def load_data(csv_path: str) -> pd.DataFrame:
    """读取 CSV 并返回 pandas DataFrame。如文件不存在则抛出 FileNotFoundError。"""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"未找到数据文件: {csv_path}")
    # 只读取需要的列以节省内存和 I/O
    df = pd.read_csv(csv_path, usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'], dtype={'年份': 'Int64'})
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """对数据进行基础清洗与标准化，用于绘图。
    - 当 '年份' 缺失时，从 '上映时间' 的前 4 个字符提取年份
    - 确保 '类型' 和 '语言' 为字符串，并填充缺失值
    """
    # 复制 DataFrame，避免修改调用者传入的对象
    df = df.copy()
    # 如果 '年份' 缺失，尝试从 '上映时间' 中提取年份（假定格式为 'YYYY...'）
    if '上映时间' in df.columns:
        # 使用 astype(str) 避免 NaN 导致的切片错误
        df['年份'] = df['年份'].fillna(df['上映时间'].astype(str).str[0:4])
    # 尝试将 '年份' 转为 pandas 的可空整型（Int64），以便分组操作行为一致
    try:
        df['年份'] = df['年份'].astype('Int64')
    except Exception:
        # 转换失败时保留原始值（安全回退）
        pass
    # 确保 '类型' 和 '语言' 为非空字符串，便于后续的拆分与统计
    df['类型'] = df['类型'].fillna('')
    df['语言'] = df['语言'].fillna('未知')
    return df


def plot_year_count(ax: Axes, df: pd.DataFrame) -> None:
    """绘制按年份统计的电影数量折线图。

    步骤：
    1）按 '年份' 分组统计电影数量
    2）构建从最小到最大年份的连续横坐标，缺失年份以 0 显示
    3）绘制折线并设置刻度与网格样式
    """
    # 按年份统计电影数量，结果索引为年份（可能为 pandas 的 IntegerIndex）
    year_count = df.groupby('年份')['年份'].count()
    # 构建连续的年份范围，保证中间没有电影的年份也显示为 0
    min_year = int(year_count.index.min())
    max_year = int(year_count.index.max())
    x = list(range(min_year, max_year + 1))
    # 对于连续年份中的每一年，取出对应计数；若不存在则返回 0
    y = [int(year_count.get(i, 0)) for i in x]
    # 绘制折线并添加标签
    ax.plot(x, y, color='green')
    ax.set_title('电影数量变化折线图', fontsize=14)
    ax.set_xlabel('年份')
    ax.set_ylabel('电影数量')
    # 选择稀疏的 x 刻度以防止刻度过密
    step = max(1, (max_year - min_year) // 10)
    ax.set_xticks(x[::step])
    ax.grid(linestyle='--', alpha=0.5)


def plot_language_count(ax: Axes, df: pd.DataFrame) -> None:
    """绘制不同语言电影数量的柱状图。"""
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
    """统计并绘制电影类型的柱状图（将 '类型' 按逗号拆分）。

    说明：'类型' 列可能包含多个以逗号分隔的类型（例如："剧情, 犯罪"），
    需要拆分后对每个类型分别计数并汇总。
    """
    type_count = {}
    # 对每一行的 '类型' 执行拆分并累加每个类型的计数
    for types in df['类型'].astype(str).str.split(','):
        for t in types:
            t = t.strip()
            if not t:
                # 跳过空字符串（可能由缺失值或末尾逗号产生）
                continue
            type_count[t] = type_count.get(t, 0) + 1
    # 按计数降序排序，便于展示
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
    """绘制不同评分电影数量占比的饼状图，并将占比很小的评分合并为“其他”。"""
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
    """创建 2x2 的画布，绘制子图并保存到指定路径。

    职责：
    - 配置中文字体以支持中文标签
    - 创建 2x2 的 matplotlib 画布并调用各绘图函数
    - 确保输出目录存在并保存最终图片
    - 可选：显示图形窗口便于调试
    """
    # 配置中文字体以支持图中中文显示
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
    # 创建 2x2 的子图画布，用于放置四个汇总图表
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=dpi)
    fig.suptitle('TMDB-TOP300电影榜单数据统计', fontsize=20, x=0.5, y=0.93)
    fig.subplots_adjust(wspace=0.3, hspace=0.4)
    # 解包子图句柄，便于后续调用
    ax1 = axes[0][0]
    ax2 = axes[0][1]
    ax3 = axes[1][0]
    ax4 = axes[1][1]

    # 使用各个辅助绘图函数绘制子图
    plot_year_count(ax1, df)
    plot_language_count(ax2, df)
    plot_type_count(ax3, df)
    plot_score_pie(ax4, df)

    # 保存前确保输出目录存在
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    # 将合成的画布保存到磁盘
    fig.savefig(out_path, dpi=dpi, bbox_inches='tight')
    if show:
        # 根据请求显示交互窗口（用于本地调试）
        plt.show()
    # 关闭画布释放内存
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
