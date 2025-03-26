import os
import json
import re
from pathlib import Path
from deep_translator import GoogleTranslator  # 需安装 pip install deep-translator

class I18NGenerator:
    def __init__(self):
        self.translation_dict = self._load_dictionary()
        self.source_files = []
        self.translation_keys = set()

    def _load_dictionary(self):
        """加载翻译词典"""
        dict_path = Path("translations/dictionary.json")
        if dict_path.exists():
            with open(dict_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"en": {}, "fr": {}}

    def _extract_translation_targets(self, file_path):
        """提取待翻译文本"""
        content = Path(file_path).read_text(encoding="utf-8")
        
        # 匹配两种标注格式
        pattern = re.compile(
            r'//\s*@i18n-(?:directive|text)\s+(.*?)\n.*?["\'](.*?)["\']',
            re.DOTALL
        )
        return pattern.findall(content)

    def _translate_text(self, text, target_lang):
        """执行翻译（优先使用词典，其次API）"""
        if target_lang in self.translation_dict:
            if text in self.translation_dict[target_lang]:
                return self.translation_dict[target_lang][text]
        
        # 调用Google翻译API（需配置环境变量）
        try:
            return GoogleTranslator(
                source="auto",
                target=target_lang,
                api_key=os.getenv("GOOGLE_TRANSLATE_API_KEY")
            ).translate(text)
        except Exception as e:
            print(f"⚠️ 翻译失败 [{text}]: {str(e)}")
            return text

    def generate(self):
        """主生成流程"""
        # 1. 扫描源代码
        for root, _, files in os.walk("src"):
            for file in files:
                if file.endswith((".js", ".ts", ".jsx")):
                    full_path = Path(root) / file
                    self.source_files.append(full_path)

        # 2. 提取所有待翻译文本
        translations = {}
        for file in self.source_files:
            for target, text in self._extract_translation_targets(file):
                langs = [lang.strip() for lang in target.split(":")[1].split(",")]
                for lang in langs:
                    if lang not in translations:
                        translations[lang] = {}
                    translations[lang][text] = self._translate_text(text, lang)

        # 3. 生成语言文件
        output_dir = Path("generated/i18n")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for lang, texts in translations.items():
            output_path = output_dir / f"{lang}.json"
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(texts, f, indent=2, ensure_ascii=False)
            print(f"✅ 生成语言文件: {output_path}")

        # 4. 更新词典库
        self._update_dictionary(translations)

    def _update_dictionary(self, new_translations):
        """更新词典文件"""
        for lang, texts in new_translations.items():
            if lang not in self.translation_dict:
                self.translation_dict[lang] = {}
            self.translation_dict[lang].update(texts)
        
        with open("translations/dictionary.json", "w", encoding="utf-8") as f:
            json.dump(self.translation_dict, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generator = I18NGenerator()
    generator.generate()
