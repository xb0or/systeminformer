# -*- coding: utf-8 -*-
import re, io, os, sys
sys.stdout.reconfigure(encoding="utf-8")

# 扫描指定目录 .c 文件里剩余的英文 UI 字符串（未被汉化的）
root = sys.argv[1] if len(sys.argv) > 1 else r"F:\desktop\code\SystemInformer\plugins\ToolStatus"
pat = re.compile(r'L"((?:[^"\\\n]|\\.)*)"')
skip = re.compile(r"^(#|\\\\|Software\\|HKEY|https?:|%|ntdll|kernel32|[0-9A-Fa-f\-]{8,}$)")
seen = set()
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith((".c", ".cpp")):
            continue
        with io.open(os.path.join(dirpath, fn), "r", encoding="utf-8-sig", errors="replace") as f:
            for line in f:
                if line.strip().startswith("//"):
                    continue
                for m in pat.finditer(line):
                    s = m.group(1)
                    # 英文 UI 特征：字母开头、含空格或冒号、没有中文
                    if not re.search(r"[\u4e00-\u9fff]", s) and re.match(r"^[A-Z][A-Za-z .:/()%\\-]+$", s) and (" " in s) and len(s) > 3:
                        if s not in seen:
                            seen.add(s)
                            print("%-16s %s" % (fn, s))
