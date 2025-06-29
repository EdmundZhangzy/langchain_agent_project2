# 🤖 LangChain 协作型智能 Agent 项目报告（DeepSeek版）

## 1. 🧠 Agent 功能说明

本项目基于 LangChain 框架，构建了一个具备多工具调用能力的智能对话 Agent。用户可通过自然语言与系统交互，系统可理解意图，调用工具（如知识库问答、天气查询、本地分析函数）来完成任务。

为了提升语言理解和响应质量，我们使用了 **DeepSeek Chat 大模型** 作为核心语言模型。该模型兼容 OpenAI Chat API，提供了更高性价比与响应速度。

---

## 2. ⚙️ 系统实现细节

### 🔧 使用的技术栈

- **LangChain >= 0.2.0**：Agent 构建与工具整合
- **Gradio**：界面交互与测试
- **DeepSeek API**：作为核心对话模型
- **Python-dotenv**：环境变量管理
- **FAISS**：知识库向量索引

### 🔨 Agent 使用的 Tools

| 工具类型 | 工具名称 | 功能说明 |
|----------|----------|-----------|
| 📚 知识库工具 | KnowledgeBaseTool | 模拟文档问答，可替换为实际文档向量检索 |
| 🌦️ API 工具 | WeatherTool | 调用 `wttr.in` 接口获取天气 |
| 🧮 本地函数工具 | LocalAnalysisTool | 实现文本情感分析（正/负/中性） |

---

## 3. 🧪 运行测试方法说明

### 环境配置

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
在项目根目录创建 .env 文件并配置 API Key：

ini
复制
编辑
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
启动应用
运行主程序：

bash
复制
编辑
python app.py
系统将在本地启动 Gradio 界面（默认地址：http://127.0.0.1:7860）。

4. 💬 聊天记录示例
![Uploading c658b7f9a0dabd8da2ef2cadaff98dd.png…]()

👤 用户：今天天气如何？
🤖 Agent：今天的天气是多云转小雨，气温大约在27°C左右。记得出门带伞哦！

👤 用户：分析一下“这家店服务非常差，我不会再来了”
🤖 Agent：根据分析，这句话表达了强烈的负面情绪，主要是对店铺服务的不满和失望，甚至明确表示不会再光顾。建议商家关注服务质量的改进，避免类似负面体验。

👤 用户：请解释一下Transformer模型的结构
🤖 Agent：Transformer模型的核心结构由编码器（Encoder）和解码器（Decoder）堆叠组成，主要特点如下：

1. **自注意力机制（Self-Attention）**  
   通过计算输入序列中每个词与其他词的相关性权重，动态捕捉上下文依赖关系，解决长距离依赖问题。

2. **多头注意力（Multi-Head Attention）**  
   并行运行多组自注意力机制，融合不同子空间的语义信息，增强模型表达能力。

3. **位置编码（Positional Encoding）**  
   通过正弦函数为输入序列添加位置信息，弥补模型对时序数据的感知缺陷。

4. **前馈神经网络（Feed Forward Network）**  
   每个注意力层后接全连接层，进行非线性特征变换。

5. **残差连接与层归一化**  
   每层输出通过残差连接和归一化缓解梯度消失问题。

典型应用如BERT（仅用编码器）和GPT（仅用解码器）。需注意：工具返回为模拟答案，实际细节可能需结合具体论文或教程。需要进一步展开某个部分吗？

5. 🤝 合作与反思
👩 同学 A
负责内容：项目结构设计、app.py 运行逻辑、天气工具与本地函数开发。

收获：理解了 LangChain 如何管理工具与记忆，掌握 Gradio 快速部署方法。

困难：LangChain 文档迭代快，导入路径频繁变动，需及时适配。

👨 同学 B
负责内容：DeepSeek 模型接入、知识库工具开发、README 撰写与优化。

收获：掌握了调用 OpenAI 兼容 API 的方法，提升了对 LLM 工具链的理解。

困难：模型 API 参数配置初期不熟悉，出现过密钥加载问题。
