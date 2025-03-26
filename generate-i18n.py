import os
import json
from pathlib import Path

def find_annotated_files(directory="src", annotation="@i18n-generate"):
    """查找所有包含标注的文件"""
    annotated_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                path = Path(root) / file
                if annotation in path.read_text(encoding="utf-8"):
                    annotated_files.append(path)
    return annotated_files

def parse_languages(file_paths, annotation="@i18n-generate"):
    """解析目标语言列表"""
    languages = set()
    for file in file_paths:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if annotation in line:
                    langs = line.split("target:")[1].strip().split(", ")
                    languages.update(langs)
                    break
    return sorted(languages)

def generate_i18n_files(languages, template_dir="templates", output_dir="i18n"):
    """根据模板生成多语言文件"""
    Path(output_dir).mkdir(exist_ok=True)
    for lang in languages:
        template_path = Path(template_dir) / f"{lang}.json"
        output_path = Path(output_dir) / f"{lang}.json"
        
        if template_path.exists():
            try:
                data = json.loads(template_path.read_text(encoding="utf-8"))
                output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
                print(f"✅ 生成成功: {output_path}")
            except json.JSONDecodeError as e:
                print(f"❌ 模板解析失败 ({template_path}): {e}")
        else:
            print(f"⚠️ 模板不存在: {template_path}")

if __name__ == "__main__":
    print("=== 开始生成多语言文件 ===")
    files = find_annotated_files()
    if not files:
        print("⚠️ 未找到标注文件，请检查代码中的 @i18n-generate 注释")
        exit()

    langs = parse_languages(files)
    if not langs:
        print("⚠️ 未解析到目标语言，请确认标注格式（如：// @i18n-generate target: en, fr）")
        exit()

    generate_i18n_files(langs)
    print("=== 生成完成 ===")
