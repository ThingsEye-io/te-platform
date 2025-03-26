import os
import json
import re
import sys
from pathlib import Path

class I18NGenerator:
    def __init__(self):
        self.translation_dict = self._load_dictionary()
        
    def _load_dictionary(self):
        dict_path = Path("translations/dictionary.json")
        if dict_path.exists():
            with open(dict_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"en": {}, "fr": {}}

    def _validate_annotation(self, annotation):
        """验证标注格式是否正确"""
        if not annotation.startswith("// @"):
            return False
        if "target:" not in annotation:
            print(f"⚠️ 错误标注: 缺少 'target:' - {annotation}")
            return False
        return True

    def _extract_translation_targets(self, file_path):
        """更安全地提取翻译目标"""
        try:
            content = Path(file_path).read_text(encoding="utf-8")
            pattern = re.compile(
                r'//\s*@i18n-directive\s+(target:[^\n]+)\n.*?'
                r'//\s*@i18n-text\s+([^\n]+)\n.*?["\']([^"\']+)["\']',
                re.DOTALL
            )
            
            for match in pattern.finditer(content):
                target, _, text = match.groups()
                if not self._validate_annotation(match.group(0)):
                    continue
                    
                try:
                    langs_part = target.split(":")[1].strip()
                    langs = [lang.strip() for lang in langs_part.split(",") if lang.strip()]
                    if langs:
                        yield langs, text.strip()
                except IndexError:
                    print(f"❌ 格式错误: {target}")
                    
        except Exception as e:
            print(f"⚠️ 处理文件 {file_path} 时出错: {str(e)}")

    def generate(self):
        translations = {}
        
        for file in Path("src").glob("**/*.js"):
            for langs, text in self._extract_translation_targets(file):
                for lang in langs:
                    translations.setdefault(lang, {}).update(
                        {text: self.translation_dict.get(lang, {}).get(text, text)}
        
        output_dir = Path("generated/i18n")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for lang, texts in translations.items():
            output_file = output_dir / f"{lang}.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(texts, f, indent=2, ensure_ascii=False)
            print(f"✅ 生成: {output_file}")

if __name__ == "__main__":
    try:
        I18NGenerator().generate()
    except Exception as e:
        print(f"❌ 生成失败: {str(e)}")
        sys.exit(1)
