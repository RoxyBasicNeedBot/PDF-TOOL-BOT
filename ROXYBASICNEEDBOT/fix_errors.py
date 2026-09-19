import os
import re

directories = [
    'dispatch/reactor/ops',
    'dispatch/reactor'
]

pattern1 = re.compile(r'logger\.error\(\s*\"1️⃣ 🐞 %s: %s\" % \(file_name, Error\),\s*exc_info=True\s*\)')
pattern2 = re.compile(r'logger\.error\(\s*\"2️⃣ 🐞 %s: %s\" % \(file_name, Error\),\s*exc_info=True\s*\)')
pattern3 = re.compile(r'logger\.error\(\s*\"3️⃣ 🐞 %s: %s\" % \(file_name, Error\),\s*exc_info=True\s*\)')
pattern4 = re.compile(r'logger\.error\(\s*\"🐞 %s: %s\" % \(file_name, Error\),\s*exc_info=True\s*\)')
pattern5 = re.compile(r'logger\.error\(\s*\"🐞 %s: %s\" % \(file_name, e\),\s*exc_info=True\s*\)')
pattern6 = re.compile(r'return False, Error')

for d in directories:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.py'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                original = content
                content = pattern1.sub('logger.error(f\"1️⃣ 🐞 Error: {e}\", exc_info=True)', content)
                content = pattern2.sub('logger.error(f\"2️⃣ 🐞 Error: {e}\", exc_info=True)', content)
                content = pattern3.sub('logger.error(f\"3️⃣ 🐞 Error: {e}\", exc_info=True)', content)
                content = pattern4.sub('logger.error(f\"🐞 Error: {e}\", exc_info=True)', content)
                content = pattern5.sub('logger.error(f\"🐞 Error: {e}\", exc_info=True)', content)
                content = pattern6.sub('return False, str(e)', content)
                
                if content != original:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(content)
                    print(f'Fixed {path}')
