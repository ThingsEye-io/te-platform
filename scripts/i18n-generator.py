import json
import re
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
        
    def _extract_from_json(self, data, path=""):
        """递归提取需要翻译的字段"""
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{path}.{key}" if path else key
                if isinstance(value, str):
                    # 标记需要翻译的字段（包含特定前缀）
                    if key.endswith(("label", "title", "name", "description")):
                        self._add_translation(value, current_path)
                elif isinstance(value, (dict, list)):
                    self._extract_from_json(value, current_path)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                self._extract_from_json(item, f"{path}[{i}]")

    def _add_translation(self, text, path):
        """添加翻译条目"""
        if text and text.strip():
            for lang in self.translations:
                self.translations[lang].setdefault(path, text)

    def generate(self, input_file, output_dir):
        """生成多语言文件"""
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self._extract_from_json(data)
        
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        for lang, texts in self.translations.items():
            output_file = output_dir / f"{lang}.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(texts, f, indent=2, ensure_ascii=False)
            print(f"Generated: {output_file}")

if __name__ == "__main__":
    generator = JsonI18NGenerator()
    generator.generate("path/to/your/config.json", "generated/i18n")
