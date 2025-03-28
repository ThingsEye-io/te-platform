import json
import re
from pathlib import Path

class SelectiveTranslator:
    def __init__(self, target_langs=["en", "fr", "zh", "ja", "is"]):
        self.translations = {lang: {} for lang in target_langs}
        self.mark_pattern = r'//\s*@i18n-translate\s*\n'

    def process_file(self, input_path, output_dir):
        content = Path(input_path).read_text(encoding='utf-8')
        
        # 查找所有标记字段
        marked_fields = re.finditer(
            self.mark_pattern + r'.*?"([^"]+)":\s*"([^"]+)"',
            content,
            re.DOTALL
        )

        for match in marked_fields:
            field_path = self._get_field_path(content, match.start())
            text = match.group(2)
            
            # 为每种语言生成翻译（实际使用时应替换为真实翻译）
            for lang in self.translations:
                self.translations[lang][field_path] = {
                    "original": text,
                    "translated": f"[{lang}] {text}"  # 示例翻译
                }

        # 保存翻译文件
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for lang, terms in self.translations.items():
            output_file = output_dir / f"translations_{lang}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(terms, f, indent=2, ensure_ascii=False)
            print(f"Generated: {output_file}")

    def _get_field_path(self, content, pos):
        """获取字段的JSON路径（如 metadata.nodes[0].name）"""
        # 简化的路径追踪实现
        stack = []
        brackets = {'{': '}', '[': ']'}
        in_string = False
        path = []
        
        for i, char in enumerate(content[:pos]):
            if char == '"' and content[i-1] != '\\':
                in_string = not in_string
            elif not in_string:
                if char in brackets:
                    stack.append(char)
                elif char in brackets.values():
                    if stack:
                        stack.pop()
                elif char == ':' and stack[-1] == '{':
                    # 提取键名
                    key_start = content.rfind('"', 0, i-1) + 1
                    key_end = content.find('"', key_start)
                    key = content[key_start:key_end]
                    path.append(key)
                elif char == ',' and stack[-1] == '[':
                    # 数组索引
                    if not path or not path[-1].isdigit():
                        path.append('0')
                    else:
                        path[-1] = str(int(path[-1]) + 1)
        
        return '.'.join(path)

if __name__ == "__main__":
    translator = SelectiveTranslator()
    translator.process_file(
        "src/test2.json",  # 替换为您的文件路径
        "generated/i18n"
    )
