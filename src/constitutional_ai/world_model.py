import json
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class Entity:
    name: str
    attributes: Dict[str, Any]

@dataclass  
class Rule:
    condition: str
    action: str
    message: str

class WorldModel:
    def __init__(self):
        self.entities: Dict[str, Entity] = {}
        self.rules: List[Rule] = []
    
    @classmethod
    def from_json(cls, file_path: str) -> 'WorldModel':
        """从JSON文件加载世界模型"""
        instance = cls()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # 加载实体
            for entity_data in data.get('entities', []):
                entity = Entity(
                    name=entity_data['name'],
                    attributes=entity_data.get('attributes', {})
                )
                instance.entities[entity.name] = entity
                
            # 加载规则
            for rule_data in data.get('rules', []):
                rule = Rule(
                    condition=rule_data['condition'],
                    action=rule_data['action'],
                    message=rule_data.get('message', '')
                )
                instance.rules.append(rule)
                
        except Exception as e:
            print(f"加载世界模型错误: {e}")
            
        return instance
    
    def validate_entity(self, entity_name: str, attribute: str, value: Any) -> bool:
        """验证实体属性值是否符合约束"""
        if entity_name not in self.entities:
            return False
            
        entity = self.entities[entity_name]
        # 这里可以添加具体的验证逻辑
        return True

# 示例用法
if __name__ == "__main__":
    # 测试代码
    model = WorldModel()
    print("世界模型类创建成功！")
