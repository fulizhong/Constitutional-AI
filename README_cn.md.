# Constitutional-AI Framework 🛡️

> 一个为大型语言模型（LLM）提供可证明可靠性保证的框架，通过外部"世界模型宪法"约束生成，并探索通向内生分层式架构的路径。  
> **English**: A framework for providing provably reliable guarantees for Large Language Models (LLMs), utilizing an external 'World Model Constitution' to constrain generation, and exploring a path toward an endogenous layered architecture.

## 📖 目录
- [✨ 特性](#✨-特性)
- [🎯 项目动机](#🎯-项目动机)
- [🏗️ 核心架构](#🏗️-核心架构)
- [🚀 快速开始](#🚀-快速开始)
- [📁 项目结构](#📁-项目结构)
- [🤝 如何贡献](#🤝-如何贡献)
- [📜 许可证](#📜-许可证)
- [🔮 未来愿景](#🔮-未来愿景)
- [🙏 致谢](#🙏-致谢)

---

## ✨ 特性
- **🧠 可证明的可靠性**：基于形式化的"生成-验证"循环，从数学上保证输出与世界模型的一致性，消除事实性幻觉。
- **📚 外部知识集成**：支持灵活定义领域特定的"世界模型宪法"（如知识图谱、规则引擎、业务数据库）。
- **⚙️ 工程友好**：提供清晰的API与模块化设计，便于集成到现有生产流程中。
- **🔬 研究前瞻性**：不仅提供短期解决方案，更为通向下一代"分层式大模型"提供清晰的演进路径。

## 🎯 项目动机
大型语言模型（LLM）的幻觉问题是其在高风险领域（如医疗、金融、司法）部署的核心障碍。现有方法如检索增强生成（RAG）和微调（Fine-tuning）仅在概率框架内进行优化，无法提供确定性保证。

本框架旨在实现一次**范式转移**：从专注于"修正模型内部"转向"架构层面担保输出"，并最终迈向"重构模型本身"。

## 🏗️ 核心架构
本框架基于双路径演进策略：

### 1. 短期范式：宪法约束架构 (The Constitutional Paradigm)
```text
用户请求
    │
    ▼
[LLM 生成器] ───生成──→ 候选文本 ────→ [宪法验证器] ←─── 世界模型宪法 (W)
    │                      │               │
    │                      │               ▼
    │                      └─── 合规? ──── 是 ────→ 输出可靠结果
    │                                      │
    └─────── 学习与调整 ←─────── 否 ←──────┘
```

### 2. 长期愿景：分层式大模型 (The Layered Vision)
长期目标是实现架构层面的根本性革新，将外部约束**内化**为模型固有的分层知识结构。
```text
用户请求
    │
    ▼
[元路由网络] ────→ 分发至专属知识层 ────→ 集成最终输出
    │ 
    ├───→ [属性层] (编码静态概念、实体属性)
    │
    ├───→ [信息层] (编码动态事实、事件关系)
    │
    └───→ [行为层] (编码流程方法、操作协议)
```

#### 各层核心功能
- **基础层（Foundation Layer）**：继承现有Transformer架构，负责通用语言理解与基础推理，提供底层语言能力支撑。
- **属性层（Attribute Layer）**：编码**静态、陈述性知识**（如概念、实体、属性）。例如："水的沸点是100°C"、"阿司匹林禁忌人群=胃溃疡患者"。
- **信息层（Information Layer）**：编码**动态、事件性知识**（如事实、关系、事件）。例如："公司A于2023年收购了公司B"、"患者2024-10-01血压=160/100mmHg"。
- **行为层（Behavior Layer）**：编码**流程性、方法性知识**（如操作步骤、算法、协议）。例如："配置Web服务器的3个步骤"、"高血压1级先生活干预再用药"。
- **元路由网络（Meta-Router）**：智能调度器，分析输入查询意图（如"用药推荐"需调用属性层+信息层+行为层），分发至对应知识层并集成结果，确保推理逻辑连贯。

#### 演进关系
此愿景是"宪法范式"的自然进化，实现"外部约束→内部模块化"的升级：
- `外部世界模型 (W)` —演进→ `内部属性/信息/行为层`（结构化知识内化为模块）
- `外部验证函数 (C)` —演进→ `内部元路由与层间协调机制`（事后验证→事前调度）

## 🚀 快速开始
### 安装
```bash
# 从源码安装（推荐）
git clone https://github.com/your-username/Constitutional-AI.git
cd Constitutional-AI
pip install -e .
```

### 基本用法
#### 示例1：加载世界模型并验证命题
```python
from constitutional_ai import WorldModel, Validator

# 1. 加载领域特定的世界模型宪法（示例：医疗领域规则）
# 世界模型JSON格式示例（可单独保存为 medical_rules.json）：
# {
#   "entities": [
#     {
#       "name": "布洛芬",
#       "attributes": {
#         "禁忌人群": "＜6个月婴儿",
#         "儿童剂量": "5-10mg/kg/次"
#       }
#     }
#   ],
#   "rules": [
#     "IF 患者年龄＜6个月 THEN 禁用布洛芬",
#     "IF 推荐儿童用药 THEN 需标注剂量范围"
#   ]
# }
constitution = WorldModel.from_json('./world_models/medical_rules.json')

# 2. 验证LLM生成的命题（如"为2岁儿童推荐布洛芬"）
validation_result = Validator.check(
    proposition="为2岁儿童推荐布洛芬，每次剂量8mg/kg",
    world_model=constitution
)

# 3. 输出验证结果
print(f"是否合规: {validation_result.compliant}")  # 输出：是否合规: True
print(f"验证依据: {validation_result.reason}")     # 输出：验证依据: 1. 患者年龄2岁≥6个月，符合布洛芬使用条件；2. 标注儿童剂量8mg/kg，符合剂量标注规则
print(f"关联实体: {validation_result.related_entities}")  # 输出：关联实体: [{"name": "布洛芬", "used_attribute": "禁忌人群、儿童剂量"}]
```

#### 示例2：集成LLM生成流程
```python
from constitutional_ai import LLMGenerator, ConstitutionalPipeline

# 1. 初始化LLM生成器（支持对接GPT-4、文心一言等API）
llm_generator = LLMGenerator(
    model_name="gpt-4",
    api_key="your-api-key"  # 替换为你的实际API密钥
)

# 2. 构建"生成-验证"流水线（复用上述医疗领域世界模型）
pipeline = ConstitutionalPipeline(
    llm_generator=llm_generator,
    world_model=constitution
)

# 3. 处理用户请求（生成合规结果）
user_request = "给2岁发烧儿童推荐退烧药及用法"
final_output = pipeline.run(user_request)

# 输出结果
print(f"用户请求: {user_request}")
print(f"合规生成结果: {final_output}")
# 预期输出：
# 用户请求: 给2岁发烧儿童推荐退烧药及用法
# 合规生成结果: 推荐退烧药：布洛芬。用法：每次剂量8mg/kg（如体重10kg儿童每次服用80mg），每6-8小时一次，24小时不超过4次。
# 注：2岁儿童符合布洛芬使用年龄条件（≥6个月），剂量在推荐范围（5-10mg/kg/次）内。
```

## 📁 项目结构
```
Constitutional-AI/
├── docs/                      # 项目文档（含世界模型构建指南、API手册）
│   ├── world_model_guide.md   # 世界模型（属性/信息/行为）定义规范
│   └── api_reference.md       # 框架API接口说明
├── src/                       # 框架核心源代码
│   ├── constitutional_ai/     # 主包
│   │   ├── world_model.py     # 世界模型（实体/规则/状态）定义与加载
│   │   ├── validator.py       # 宪法验证器（合规性检查逻辑）
│   │   ├── llm_generator.py   # LLM生成器（对接第三方LLM API）
│   │   └── pipeline.py        # "生成-验证"流水线
│   └── __init__.py            # 包初始化
├── world_models/              # 示例世界模型宪法库
│   ├── medical_rules.json     # 医疗领域规则（如药品禁忌、临床路径）
│   ├── finance_rules.json     # 金融领域规则（如合规条文、风控逻辑）
│   └── game_rules.json        # 游戏领域规则（如角色属性、任务逻辑）
├── examples/                  # 场景化使用示例
│   ├── medical_demo.py        # 医疗用药推荐示例
│   ├── finance_demo.py        # 金融合规审查示例
│   └── game_demo.py           # 游戏NPC对话生成示例
├── tests/                     # 单元测试
│   ├── test_world_model.py    # 世界模型加载与解析测试
│   └── test_validator.py      # 合规性验证逻辑测试
├── CONTRIBUTING.md            # 贡献指南（含代码规范、PR流程）
├── LICENSE                    # MIT许可证文件
└── README.md                  # 项目说明文档（本文档）
```

## 🤝 如何贡献
我们欢迎任何形式的贡献，包括但不限于：
1. **代码贡献**：修复bug、新增功能（如支持更多LLM接口、扩展世界模型格式）；
2. **文档完善**：补充使用案例、优化API文档、编写世界模型构建教程；
3. **场景扩展**：提交新领域的世界模型宪法（如教育、法律领域规则）；
4. **问题反馈**：在GitHub Issues中提交bug报告或功能建议。

贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，了解代码规范、分支管理与PR流程。

## 📜 许可证
本项目采用 **MIT License**（麻省理工许可证），允许个人或企业自由使用、修改、分发本框架，无需支付许可费用，仅需在衍生作品中保留原许可证声明。详见 [LICENSE](LICENSE) 文件。

## 🔮 未来愿景
本项目旨在架设一座从当前工程实践通往下一代可信AI模型的桥梁，短期目标是成为"LLM高风险场景落地的合规工具包"，长期目标是：
1. 构建跨领域的世界模型宪法库（医疗、金融、司法等），形成标准化的结构化知识资产；
2. 实现分层式大模型的原型验证，探索"属性-信息-行为"模块的高效协同机制；
3. 开发自动化世界模型构建工具（如从领域文档中提取实体/规则），降低本体构建门槛。

## 🙏 致谢
本项目的核心思想源于以下领域的研究成果与实践经验，在此致谢：
1. 可信AI领域的"神经符号融合"研究（如神经符号AI、知识图谱增强LLM）；
2. 游戏行业的"世界模型约束生成"实践（如NPC行为规则、剧情逻辑一致性控制）；
3. 医疗/金融领域的"合规性验证"工程方案（如临床指南数字化、监管规则引擎）。

同时感谢所有为开源社区贡献工具的开发者（如LangChain、Hugging Face Transformers），为本框架的快速开发提供了基础支持。
