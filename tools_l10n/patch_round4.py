# -*- coding: utf-8 -*-
import io, os

BASE = r"F:\desktop\code\SystemInformer"

# 文件级精确替换（完整 L"..." 字面量）
FIXES = {
    r"plugins\ExtendedTools\fwtab.c": {
        'L"Firewall"': 'L"防火墙"',
        'L"Country"': 'L"国家"',
    },
    r"plugins\NetworkTools\main.c": {
        'L"Country"': 'L"国家"',
    },
    r"plugins\NetworkTools\tracetree.c": {
        'L"Country"': 'L"国家"',
    },
    r"plugins\NetworkTools\update.c": {
        'L"Country"': 'L"国家"',
    },
    r"plugins\ToolStatus\main.c": {
        'L"Search Processes (Ctrl+K)"': 'L"搜索进程 (Ctrl+K)"',
        'L"Search Services (Ctrl+K)"': 'L"搜索服务 (Ctrl+K)"',
        'L"Search Network (Ctrl+K)"': 'L"搜索网络 (Ctrl+K)"',
    },
    r"plugins\ToolStatus\toolbar.c": {
        'L"Search Processes (Ctrl+K)"': 'L"搜索进程 (Ctrl+K)"',
    },
    r"plugins\DotNetTools\asmpage.c": {
        'L"Search Assemblies (Ctrl+K)"': 'L"搜索程序集 (Ctrl+K)"',
    },
    r"plugins\ExtendedTools\namedpipes.c": {
        'L"Search Named Pipes (Ctrl+K)"': 'L"搜索命名管道 (Ctrl+K)"',
    },
    r"plugins\ExtendedTools\objmgr.c": {
        'L"Search Objects (Ctrl+K)"': 'L"搜索对象 (Ctrl+K)"',
    },
    r"plugins\ExtendedTools\pooldialog.c": {
        'L"Search Pool Tags (Ctrl+K)"': 'L"搜索池标记 (Ctrl+K)"',
    },
    r"plugins\WindowExplorer\wnddlg.c": {
        'L"Search Windows (Ctrl+K)"': 'L"搜索窗口 (Ctrl+K)"',
    },
    r"plugins\ExtendedTools\disktab.c": {
        'L"Search Disk (Ctrl+K)"': 'L"搜索磁盘 (Ctrl+K)"',
    },
    r"plugins\HardwareDevices\devicetree.c": {
        'L"Search Devices (Ctrl+K)"': 'L"搜索设备 (Ctrl+K)"',
    },
}

total = 0
for rel, mapping in FIXES.items():
    p = os.path.join(BASE, rel)
    with io.open(p, "r", encoding="utf-8-sig") as f:
        text = f.read()
    n = 0
    for old, new in mapping.items():
        if old in text:
            n += text.count(old)
            text = text.replace(old, new)
    if n:
        with io.open(p, "w", encoding="utf-8-sig", newline="") as f:
            f.write(text)
        total += n
        print("%-45s %d" % (rel, n))
print("TOTAL:", total)
