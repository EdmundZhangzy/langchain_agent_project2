from langchain.tools import Tool

def analyze_sentiment(text):
    if "好" in text or "喜欢" in text:
        return "Positive"
    elif "差" in text or "讨厌" in text:
        return "Negative"
    else:
        return "Neutral"

local_tool = Tool(
    name="LocalAnalysisTool",
    func=analyze_sentiment,
    description="进行情绪分析。例如：'这家餐厅服务很差'"
)