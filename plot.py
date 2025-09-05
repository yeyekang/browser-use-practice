import json
import matplotlib.pyplot as plt
import glob
import os
from matplotlib import font_manager

# 找到最新的 JSON 文件
files = glob.glob("/var/folders/_k/j6shw5sj369f5_3g7w9614vw0000gn/T/browser_use_agent_068baca5-c58a-7c5c-8000-7ac392a24095_1757071964/browseruse_agent_data/movie_type_counts.json")
if not files:
    raise FileNotFoundError("没有找到 movie_type_counts.json，请先运行 BrowserUse 脚本生成数据")

json_path = max(files, key=os.path.getctime)
print(f"正在读取: {json_path}")

# 读取数据
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 取前100个电影的类型统计
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
data_top100 = dict(sorted_items[:100]) if len(sorted_items) > 100 else dict(sorted_items)
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
top13 = dict(sorted_items[:13])
others_sum = sum(v for _, v in sorted_items[13:])
if others_sum > 0:
    top13["其他"] = others_sum

labels = list(top13.keys())
sizes = list(top13.values())

# ✅ 设置中文字体（这里用系统宋体，防止乱码）
font_path = "/System/Library/Fonts/Supplemental/Songti.ttc"  # macOS 自带字体
font_prop = font_manager.FontProperties(fname=font_path)

# 绘制爆炸饼图
fig, ax = plt.subplots(figsize=(10, 10))

# 每个扇区都轻微爆炸，确保小类不会挤一起
explode = [0.05] * len(sizes)

wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 9, 'fontproperties': font_prop},
    wedgeprops=dict(width=0.5, edgecolor="w")
)

# 标题
plt.title("豆瓣推荐TOP100电影类型占比图", fontproperties=font_prop, fontsize=16)

# 图例放右边
ax.legend(
    wedges,
    labels,
    title="电影类型",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    prop=font_prop
)

plt.savefig("movie_type_pie.png", dpi=300, bbox_inches="tight")
print("✅ 图表已保存为 movie_type_pie.png")

plt.show()

