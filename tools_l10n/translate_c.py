# -*- coding: utf-8 -*-
# SystemInformer .c 文件汉化主脚本
# 用法: python translate_c.py [目录]
# 完整字面量替换 L"english" -> L"中文"，含中文的文件写 UTF-8 with BOM（MSVC 需要）

import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c_map_1 import C_MAP
from c_map_2 import M2
from c_map_3 import M3

M2(C_MAP)
M3(C_MAP)

# 排除的目录（phsvc 是服务端无UI，sdk 是公共头）
EXCLUDE_DIRS = {"phsvc", "sdk", "tools_l10n"}


def translate_file(path):
    with io.open(path, "r", encoding="utf-8-sig", errors="strict") as f:
        text = f.read()

    count = 0
    # 按键长度降序，避免前缀误配（完整引号匹配本身安全，双保险）
    for key in sorted(C_MAP, key=len, reverse=True):
        src = 'L"' + key + '"'
        dst = 'L"' + C_MAP[key] + '"'
        if src in text:
            n = text.count(src)
            text = text.replace(src, dst)
            count += n

    if count == 0:
        return 0, False

    # 语法安全检查：引号数量必须保持偶数配对（简单校验）
    # 每次替换都是 "..." -> "..."，引号数不变，天然安全

    # 含中文 -> 写 UTF-8 with BOM（MSVC 无 /utf-8 选项时正确解析中文）
    has_cjk = any('\u4e00' <= c <= '\u9fff' for c in text)
    enc = "utf-8-sig" if has_cjk else "utf-8"
    with io.open(path, "w", encoding=enc, newline="") as f:
        f.write(text)
    return count, has_cjk


def main(root):
    total = 0
    files_changed = 0
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in files:
            if not fn.endswith((".c", ".cpp")):
                continue
            p = os.path.join(dirpath, fn)
            try:
                n, bom = translate_file(p)
            except Exception as e:
                print("ERROR %s: %s" % (p, e))
                continue
            if n:
                total += n
                files_changed += 1
                print("%-40s %4d replacements%s" % (os.path.relpath(p, root), n, " [BOM]" if bom else ""))
    print("\nTOTAL: %d replacements in %d files" % (total, files_changed))


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else r"F:\desktop\code\SystemInformer\SystemInformer"
    main(root)
