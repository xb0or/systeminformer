# -*- coding: utf-8 -*-
# 补丁映射：首轮遗漏的字符串（带尾空格格式、大小写变体、ToolStatus 状态栏）
import io, os, sys

PATCH_MAP = {
    # ---- 状态栏/图形工具提示（带尾空格格式） ----
    "CPU usage: ": "CPU 使用率：",
    "Physical memory: ": "物理内存：",
    "Free memory: ": "可用内存：",
    "Commit charge: ": "提交内存：",
    "Processes: ": "进程：",
    "Threads: ": "线程：",
    "Handles: ": "句柄：",
    "I/O W: ": "I/O 写：",
    "I/O R+O: ": "I/O 读+其他：",
    "I/O O: ": "I/O 其他：",
    "Visible: ": "可见：",
    "Visible: N/A": "可见：不适用",
    "Selected: ": "已选：",
    "Selected: N/A": "已选：不适用",
    "Selected WS: ": "已选工作集：",
    "Selected WS: N/A": "已选工作集：不适用",
    "Selected private bytes: ": "已选私有字节：",
    "Selected private bytes: N/A": "已选私有字节：不适用",
    "KSI: ": "KSI：",
    "Interval: Fast": "间隔：快",
    "Interval: Normal": "间隔：普通",
    "Interval: Below normal": "间隔：低于普通",
    "Interval: Slow": "间隔：慢",
    "Interval: Very slow": "间隔：很慢",
    "Interval: N/A": "间隔：不适用",
    "Interval: Paused": "间隔：已暂停",
    "Interval status": "间隔状态",
    "CPU usage": "CPU 使用率",
    "Max. CPU process": "最高 CPU 进程",
    "Max. I/O process": "最高 I/O 进程",
    "Number of processes": "进程数",
    "Number of threads": "线程数",
    "Number of handles": "句柄数",
    "Number of visible items": "可见项数",
    "Number of selected items": "已选项数",
    "Free physical memory": "可用物理内存",
    "Selected process WS": "所选进程工作集",
    "Selected process private bytes": "所选进程私有字节",
    "KSI status": "KSI 状态",
    "I/O write": "I/O 写入",
    "I/O read": "I/O 读取",
    "I/O other": "I/O 其他",

    # ---- 工具栏按钮提示（大小写变体） ----
    "Find handles or DLLs": "查找句柄或 DLL",
    "System information": "系统信息",
    "Find window and thread": "查找窗口和线程",
    "Find window and kill": "查找窗口并终止",
    "Always on top": "总是置顶",
    "Show details for all processes": "显示所有进程的详细信息",
    "Find handles or DLLs (Ctrl+F)": "查找句柄或 DLL (Ctrl+F)",
    "System information (Ctrl+I)": "系统信息 (Ctrl+I)",

    # ---- 选项/自定义对话框 ----
    "No text labels": "无文本标签",
    "Selective text": "选择性文本",
    "Show text labels": "显示文本标签",
    "Always show": "总是显示",
    "Main menu (auto-hide)": "主菜单（自动隐藏）",
    "Search box": "搜索框",
    "Lock the toolbar": "锁定工具栏",
    "Search disabled": "搜索已禁用",
    "Toolbar and Status Bar": "工具栏和状态栏",
    "Physical memory history": "物理内存历史",
    "Commit charge history": "提交内存历史",
    "Unable to display Find dialog.": "无法显示查找对话框。",
    "The process (PID %lu) does not exist.": "进程 (PID %lu) 不存在。",
}


def apply(root_dirs):
    total = 0
    for root in root_dirs:
        for dirpath, dirs, files in os.walk(root):
            for fn in files:
                if not fn.endswith((".c", ".cpp")):
                    continue
                p = os.path.join(dirpath, fn)
                with io.open(p, "r", encoding="utf-8-sig") as f:
                    text = f.read()
                n = 0
                for key in sorted(PATCH_MAP, key=len, reverse=True):
                    src = 'L"' + key + '"'
                    if src in text:
                        n += text.count(src)
                        text = text.replace(src, 'L"' + PATCH_MAP[key] + '"')
                if n:
                    has_cjk = any('\u4e00' <= c <= '\u9fff' for c in text)
                    with io.open(p, "w", encoding="utf-8-sig" if has_cjk else "utf-8", newline="") as f:
                        f.write(text)
                    total += n
                    print("%-40s %d" % (os.path.relpath(p, root), n))
    print("TOTAL:", total)


if __name__ == "__main__":
    dirs = [
        r"F:\desktop\code\SystemInformer\plugins\ToolStatus",
        r"F:\desktop\code\SystemInformer\SystemInformer",
    ]
    apply(dirs)
