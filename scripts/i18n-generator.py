import json
import os
from pathlib import Path

class JsonI18NGenerator:
    def __init__(self):
        self.translations = {
            "en": {},
            "fr": {},
            "zh": {},
            "ja": {},
            "is": {}
        }
        
    def _extract_translatable_fields(self, data, current_path=""):
        """递归提取需要国际化的字段"""
        if isinstance(data, dict):
            for key, value in data.items():
                new_path = f"{current_path}.{key}" if current_path else key
                if key in ["label", "title", "name", "description"] and isinstance(value, str):
                    self._add_translation(value, new_path)
                self._extract_translatable_fields(value, new_path)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                self._extract_translatable_fields(item, f"{current_path}[{index}]")

    def _add_translation(self, text, path):
        """添加到翻译字典"""
        if text and text.strip():
            for lang in self.translations:
                self.translations[lang][path] = text

    def generate(self, input_path, output_dir):
        """生成多语言文件"""
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            self._extract_translatable_fields(data)
            
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            for lang, translations in self.translations.items():
                output_file = output_dir / f"{lang}.json"
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(translations, f, indent=2, ensure_ascii=False)
                print(f"✅ 生成: {output_file}")
                
        except FileNotFoundError:
            print(f"❌ 错误：配置文件不存在 - {input_path}")
            print("请确认：")
            print(f"1. 文件路径是否正确（当前工作目录: {os.getcwd()}）")
            print(f"2. 文件是否存在于以下位置之一: {[str(p) for p in Path('.').rglob('*.json')]}")
        except json.JSONDecodeError as e:
            print(f"❌ JSON解析错误: {str(e)}")
        except Exception as e:
            print(f"❌ 未知错误: {str(e)}")

if __name__ == "__main__":
    # 使用示例（根据实际情况修改路径）
    config_path = "config/dashboard.json"  # 改为您实际的配置文件路径
    
    generator = JsonI18NGenerator()
    generator.generate(config_path, "generated/i18n")
