from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    llm = ChatGoogle(model="gemini-2.5-flash", api_key="把这里改成自己的api key")
    task = "请抓取豆瓣 TOP100 每部电影的类型，统计每种类型数量，然后自动生成饼图显示各类型占比。数据抓取、分析和可视化步骤全部自动完成。网站是这个：https://www.douban.com/doulist/3936288/ "
    agent = Agent(task=task, llm=llm, output_dir="/Users/kangqiman/代码库/基于browseruse开发的爬虫demo")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
