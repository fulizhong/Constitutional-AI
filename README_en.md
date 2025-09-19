# Constitutional-AI Framework 🛡️

> A framework for providing provably reliable guarantees for Large Language Models (LLMs), utilizing an external 'World Model Constitution' to constrain generation, and exploring a path toward an endogenous layered architecture.  
> **中文**: 一个为大型语言模型（LLM）提供可证明可靠性保证的框架，通过外部"世界模型宪法"约束生成，并探索通向内生分层式架构的路径。

## 📖 Table of Contents
- [✨ Features](#-features)
- [🎯 Motivation](#-motivation)
- [🏗️ Core Architecture](#️-core-architecture)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🔮 Future Vision](#-future-vision)
- [🙏 Acknowledgments](#-acknowledgments)

---

## ✨ Features
- **🧠 Provable Reliability**: Based on a formal "generate-validate" cycle, mathematically guaranteeing output consistency with the world model and eliminating factual hallucinations.
- **📚 External Knowledge Integration**: Supports flexible definition of domain-specific "World Model Constitutions" (e.g., knowledge graphs, rule engines, business databases).
- **⚙️ Engineering Friendly**: Provides clear APIs and modular design for easy integration into existing production pipelines.
- **🔬 Research Forward-looking**: Offers not only short-term solutions but also a clear evolutionary path toward next-generation "Layered LLMs".

## 🎯 Motivation
The hallucination problem in Large Language Models (LLMs) is a core obstacle to their deployment in high-risk domains (e.g., healthcare, finance, judiciary). Existing methods like Retrieval-Augmented Generation (RAG) and Fine-tuning operate solely within probabilistic frameworks and cannot provide deterministic guarantees.

This framework aims to achieve a **paradigm shift**: from focusing on "correcting the model internally" to "architecturally guaranteeing output", and ultimately moving toward "reconstructing the model itself".

## 🏗️ Core Architecture
This framework is based on a dual-path evolutionary strategy:

### 1. Short-term Paradigm: Constitutional Constraint Architecture
```text
User Request
    │
    ▼
[LLM Generator] ───Generate──→ Candidate Text ────→ [Constitution Validator] ←─── World Model Constitution (W)
    │                             │                           │
    │                             │                           ▼
    │                             └─── Compliant? ──── Yes ────→ Output Reliable Result
    │                                                 │
    └─────── Learn & Adjust ←─────── No ←─────────────┘
```

### 2. Long-term Vision: Layered LLM Architecture
The long-term goal is to achieve fundamental architectural innovation, internalizing external constraints into the model's inherent layered knowledge structure.
```text
User Request
    │
    ▼
[Meta-Router] ────→ Distribute to Specialized Knowledge Layers ────→ Integrate Final Output
    │ 
    ├───→ [Attribute Layer] (Encodes static concepts, entity attributes)
    │
    ├───→ [Information Layer] (Encodes dynamic facts, event relationships)
    │
    └───→ [Behavior Layer] (Encodes procedural methods, operational protocols)
```

#### Core Functions of Each Layer
- **Foundation Layer**: Inherits existing Transformer architecture, responsible for general language understanding and basic reasoning, providing underlying language capability support.
- **Attribute Layer**: Encodes **static, declarative knowledge** (e.g., concepts, entities, attributes). Example: "The boiling point of water is 100°C", "Aspirin contraindicated population = gastric ulcer patients".
- **Information Layer**: Encodes **dynamic, event-based knowledge** (e.g., facts, relationships, events). Example: "Company A acquired Company B in 2023", "Patient's 2024-10-01 blood pressure = 160/100mmHg".
- **Behavior Layer**: Encodes **procedural, methodological knowledge** (e.g., operational steps, algorithms, protocols). Example: "3 steps to configure a web server", "Grade 1 hypertension: lifestyle intervention first, then medication".
- **Meta-Router**: Intelligent dispatcher that analyzes input query intent (e.g., "medication recommendation" requires calling Attribute + Information + Behavior layers), distributes to appropriate knowledge layers, and integrates results, ensuring coherent reasoning logic.

#### Evolutionary Relationship
This vision is a natural evolution of the "Constitutional Paradigm", achieving an upgrade from "external constraints → internal modularization":
- `External World Model (W)` —Evolves→ `Internal Attribute/Information/Behavior Layers` (Structured knowledge internalized into modules)
- `External Validation Function (C)` —Evolves→ `Internal Meta-Router and Inter-layer Coordination Mechanism` (Post-hoc validation → Preemptive scheduling)

## 🚀 Quick Start
### Installation
```bash
# Install from source (recommended)
git clone https://github.com/your-username/Constitutional-AI.git
cd Constitutional-AI
pip install -e .
```

### Basic Usage
#### Example 1: Load World Model and Validate Proposition
```python
from constitutional_ai import WorldModel, Validator

# 1. Load a domain-specific World Model Constitution (example: medical domain rules)
# Example World Model JSON format (can be saved separately as medical_rules.json):
# {
#   "entities": [
#     {
#       "name": "Ibuprofen",
#       "attributes": {
#         "contraindicated_population": "infants <6 months",
#         "pediatric_dosage": "5-10mg/kg/dose"
#       }
#     }
#   ],
#   "rules": [
#     "IF patient_age <6 months THEN contraindicate ibuprofen",
#     "IF recommending pediatric medication THEN must specify dosage range"
#   ]
# }
constitution = WorldModel.from_json('./world_models/medical_rules.json')

# 2. Validate an LLM-generated proposition (e.g., "Recommend ibuprofen for a 2-year-old child")
validation_result = Validator.check(
    proposition="Recommend ibuprofen for a 2-year-old child, 8mg/kg per dose",
    world_model=constitution
)

# 3. Output validation results
print(f"Compliant: {validation_result.compliant}")  # Output: Compliant: True
print(f"Reason: {validation_result.reason}")        # Output: Reason: 1. Patient age 2 years ≥6 months, meets ibuprofen usage conditions; 2. Specified pediatric dosage 8mg/kg, complies with dosage specification rules
print(f"Related entities: {validation_result.related_entities}")  # Output: Related entities: [{"name": "Ibuprofen", "used_attribute": "contraindicated_population, pediatric_dosage"}]
```

#### Example 2: Integrated LLM Generation Pipeline
```python
from constitutional_ai import LLMGenerator, ConstitutionalPipeline

# 1. Initialize LLM Generator (supports connecting to APIs like GPT-4, Wenxin Yiyan, etc.)
llm_generator = LLMGenerator(
    model_name="gpt-4",
    api_key="your-api-key"  # Replace with your actual API key
)

# 2. Build "generate-validate" pipeline (reuse the medical domain world model above)
pipeline = ConstitutionalPipeline(
    llm_generator=llm_generator,
    world_model=constitution
)

# 3. Process user request (generate compliant result)
user_request = "Recommend antipyretic medication and usage for a 2-year-old febrile child"
final_output = pipeline.run(user_request)

# Output results
print(f"User request: {user_request}")
print(f"Compliant generation result: {final_output}")
# Expected output:
# User request: Recommend antipyretic medication and usage for a 2-year-old febrile child
# Compliant generation result: Recommended antipyretic: Ibuprofen. Usage: 8mg/kg per dose (e.g., 80mg per dose for a 10kg child), every 6-8 hours, not exceeding 4 times in 24 hours.
# Note: 2-year-old child meets ibuprofen age condition (≥6 months), dosage within recommended range (5-10mg/kg/dose).
```

## 📁 Project Structure
```
Constitutional-AI/
├── docs/                      # Project documentation (incl. World Model construction guide, API manual)
│   ├── world_model_guide.md   # World Model (Attribute/Information/Behavior) definition specifications
│   └── api_reference.md       # Framework API interface documentation
├── src/                       # Framework core source code
│   ├── constitutional_ai/     # Main package
│   │   ├── world_model.py     # World Model (entity/rule/state) definition and loading
│   │   ├── validator.py       # Constitution Validator (compliance check logic)
│   │   ├── llm_generator.py   # LLM Generator (interface with third-party LLM APIs)
│   │   └── pipeline.py        # "Generate-Validate" pipeline
│   └── __init__.py            # Package initialization
├── world_models/              # Example World Model Constitution library
│   ├── medical_rules.json     # Medical domain rules (e.g., drug contraindications, clinical pathways)
│   ├── finance_rules.json     # Finance domain rules (e.g., compliance clauses, risk control logic)
│   └── game_rules.json        # Gaming domain rules (e.g., character attributes, quest logic)
├── examples/                  # Scenario-based usage examples
│   ├── medical_demo.py        # Medical medication recommendation example
│   ├── finance_demo.py        # Financial compliance review example
│   └── game_demo.py           # Game NPC dialogue generation example
├── tests/                     # Unit tests
│   ├── test_world_model.py    # World Model loading and parsing tests
│   └── test_validator.py      # Compliance validation logic tests
├── CONTRIBUTING.md            # Contribution guidelines (incl. code standards, PR process)
├── LICENSE                    # MIT License file
└── README.md                  # Project documentation (this document)
```

## 🤝 Contributing
We welcome contributions of any form, including but not limited to:
1. **Code Contributions**: Bug fixes, new features (e.g., support for more LLM interfaces, extended World Model formats);
2. **Documentation Improvements**: Additional use cases, optimized API documentation, World Model construction tutorials;
3. **Scenario Expansion**: Submit World Model Constitutions for new domains (e.g., education, legal domain rules);
4. **Issue Reporting**: Submit bug reports or feature suggestions in GitHub Issues.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before contributing to understand code standards, branch management, and the PR process.

## 📜 License
This project uses the **MIT License** (Massachusetts Institute of Technology License), allowing individuals or companies to freely use, modify, and distribute this framework without paying licensing fees, only requiring retention of the original license notice in derivative works. See the [LICENSE](LICENSE) file for details.

## 🔮 Future Vision
This project aims to build a bridge from current engineering practices to the next generation of trustworthy AI models. The short-term goal is to become a "compliance toolkit for LLM deployment in high-risk scenarios", with long-term goals including:
1. Building a cross-domain World Model Constitution library (healthcare, finance, judiciary, etc.), forming standardized structured knowledge assets;
2. Implementing prototype validation of the Layered LLM architecture, exploring efficient collaboration mechanisms for "Attribute-Information-Behavior" modules;
3. Developing automated World Model construction tools (e.g., extracting entities/rules from domain documents), lowering the barrier to ontology construction.

## 🙏 Acknowledgments
The core ideas of this project originate from research results and practical experience in the following areas, for which we extend our gratitude:
1. "Neuro-symbolic fusion" research in trustworthy AI (e.g., neuro-symbolic AI, knowledge graph-enhanced LLMs);
2. "World Model constrained generation" practices in the gaming industry (e.g., NPC behavior rules, plot logic consistency control);
3. "Compliance validation" engineering solutions in healthcare/finance domains (e.g., digitized clinical guidelines, regulatory rule engines).

We also thank all developers who contribute tools to the open-source community (e.g., LangChain, Hugging Face Transformers), which provided foundational support for the rapid development of this framework.
