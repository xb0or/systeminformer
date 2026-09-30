# -*- coding: utf-8 -*-
# 插件汉化脚本：.rc 用 RC_MAP+PLUGIN_MAP，.c 用 C_MAP+PLUGIN_MAP

import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translate_rc import RC_MAP
from c_map_1 import C_MAP
from c_map_2 import M2
from c_map_3 import M3
from plugin_map import PLUGIN_MAP

M2(C_MAP)
M3(C_MAP)

RC_ALL = dict(RC_MAP)
RC_ALL.update(PLUGIN_MAP)
C_ALL = dict(C_MAP)
C_ALL.update(PLUGIN_MAP)

ROOT = r"F:\desktop\code\SystemInformer\plugins"


def apply_map(text, mapping, prefix=""):
    count = 0
    for key in sorted(mapping, key=len, reverse=True):
        src = prefix + '"' + key + '"'
        if src in text:
            count += text.count(src)
            text = text.replace(src, prefix + '"' + mapping[key] + '"')
    return text, count


def has_cjk(text):
    return any('\u4e00' <= c <= '\u9fff' for c in text)


def main():
    rc_total = rc_files = c_total = c_files = 0
    for dirpath, dirs, files in os.walk(ROOT):
        for fn in files:
            p = os.path.join(dirpath, fn)
            if fn.endswith(".rc") and "version" not in fn.lower():
                with io.open(p, "r", encoding="utf-8-sig", errors="strict") as f:
                    text = f.read()
                text, n = apply_map(text, RC_ALL)
                if n:
                    with io.open(p, "w", encoding="utf-8-sig", newline="") as f:
                        f.write(text)
                    rc_total += n
                    rc_files += 1
                    print("RC  %-50s %d" % (os.path.relpath(p, ROOT), n))
            elif fn.endswith((".c", ".cpp")):
                with io.open(p, "r", encoding="utf-8-sig", errors="strict") as f:
                    text = f.read()
                text, n = apply_map(text, C_ALL, prefix="L")
                if n:
                    enc = "utf-8-sig" if has_cjk(text) else "utf-8"
                    with io.open(p, "w", encoding=enc, newline="") as f:
                        f.write(text)
                    c_total += n
                    c_files += 1
                    print("C   %-50s %d" % (os.path.relpath(p, ROOT), n))
    print("\nRC: %d replacements in %d files" % (rc_total, rc_files))
    print("C:  %d replacements in %d files" % (c_total, c_files))


if __name__ == "__main__":
    main()
