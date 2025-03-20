import os
import json

# 1. 查找所有标注了 @i18n-generate 的文件
annotated_files = []
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".js"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read()
                if "@i18n-generate" in content:
                    annotated_files.append(path)

# 2. 解析目标语言（如 en, fr）
languages = []
for file in annotated_files:
    with open(file, "r") as f:
        for line in f:
            if "@i18n-generate" in line:
                parts = line.split("target:")[1].strip().split(", ")
                languages = parts
                break

# 3. 根据模板生成文件
for lang in languages:
    template_path = f"templates/{lang}.json"
    output_path = f"i18n/{lang}.json"
    
    if os.path.exists(template_path):
        with open(template_path, "r") as f:
            data = json.load(f)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as out_file:
                json.dump(data, out_file, indent=2)
                print(f"Generated {output_path}")

print("多语言文件生成完成！")
