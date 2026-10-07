<p align="center">
    <a href="https://systeminformer.com">
        <img src="https://github.com/winsiderss/systeminformer/raw/master/SystemInformer/resources/systeminformer-128x128.png"/>
    </a>
    <h1 align="center">System Informer 简体中文汉化版</h1>
    <h5 align="center">A free, powerful, multi-purpose tool that helps you monitor system resources, debug software and detect malware.</h5>
    <h5 align="center">一款免费、强大、多用途的工具，帮助您监视系统资源、调试软件并检测恶意软件。</h5>
    <h6 align="center">Brought to you by Winsider Seminars & Solutions, Inc.</h6>
    <h6 align="center">简体中文社区汉化版 / Simplified Chinese community localization</h6>
</p>

## 简体中文版说明 | About this fork

本仓库是 [winsiderss/systeminformer](https://github.com/winsiderss/systeminformer) 的汉化分支。

This repository is a Simplified Chinese localization fork of the upstream project.

- 界面全面汉化：主程序菜单、对话框、列标题、状态栏，以及全部 12 个官方插件的常用界面，合计约 8800 处翻译。
- Full UI localization: menus, dialogs, column headers, status bar and the common UI of all 12 first-party plugins (~8800 strings).
- 深度硬件信息表（SMBIOS 字段、设备属性树、SMART 属性）按行业惯例保留英文原文。
- Deep hardware tables (SMBIOS fields, device property tree, SMART attributes) intentionally stay in English as technical reference.
- 汉化通过直接修改源码字符串实现（当前上游尚无运行时翻译机制），构建流程与上游一致。
- The localization modifies source strings directly (the upstream project has no runtime translation mechanism yet); the build process is identical to upstream.

## 下载 | Download

从 [Releases](https://github.com/xb0or/systeminformer/releases) 页面下载最新构建：

Download the latest build from the [Releases](https://github.com/xb0or/systeminformer/releases) page:

| 文件 File | 说明 Description |
|---|---|
| `systeminformer-build-win64-bin.zip` | 64 位便携版 / 64-bit portable |
| `systeminformer-build-win32-bin.zip` | 32 位便携版 / 32-bit portable |
| `systeminformer-build-release-setup.exe` | 安装程序 / Setup |

也可以从 [Actions](https://github.com/xb0or/systeminformer/actions/workflows/build-zh-cn.yml) 页面下载每次推送自动生成的构建产物（`systeminformer-zh-cn-bin`）。

Prebuilt artifacts from every push are also available on the [Actions](https://github.com/xb0or/systeminformer/actions/workflows/build-zh-cn.yml) page (artifact `systeminformer-zh-cn-bin`).

## System requirements | 系统要求

Windows 10 or higher, 32-bit or 64-bit.

Windows 10 及以上版本，32 位或 64 位。

## Features | 功能特性

* A detailed overview of system activity with highlighting.
  带高亮显示的详细系统活动总览。
* Graphs and statistics allow you quickly to track down resource hogs and runaway processes.
  图形与统计帮助您快速定位资源占用大户和失控进程。
* Can't edit or delete a file? Discover which processes are using that file.
  无法编辑或删除文件？找出正在使用该文件的进程。
* See what programs have active network connections, and close them if necessary.
  查看哪些程序有活动网络连接，必要时将其关闭。
* Get real-time information on disk access.
  获取磁盘访问的实时信息。
* View detailed stack traces with kernel-mode, WOW64 and .NET support.
  查看详细堆栈跟踪，支持内核模式、WOW64 和 .NET。
* Go beyond services.msc: create, edit and control services.
  超越 services.msc：创建、编辑和控制服务。
* Small, portable and no installation required.
  小巧便携，无需安装。
* 100% [Free Software](https://www.gnu.org/philosophy/free-sw.en.html) ([MIT](https://opensource.org/licenses/MIT))

## Building the project | 构建项目

Requires Visual Studio (2022 or later).

需要 Visual Studio（2022 或更高版本）。

After cloning the repo run `build_init.cmd` located in the `build` directory, this doesn't not run again unless there are updates to the tools or third party libraries.

克隆仓库后，运行 `build` 目录下的 `build_init.cmd`（除非工具或第三方库有更新，否则只需运行一次）。

Execute `build_release.cmd` located in the `build` directory to compile the project or load the `SystemInformer.sln` and `Plugins.sln` solutions if you prefer building the project using Visual Studio.

运行 `build` 目录下的 `build_release.cmd` 编译项目，或使用 Visual Studio 打开 `SystemInformer.sln` 和 `Plugins.sln` 解决方案构建。

You can download the free [Visual Studio Community Edition](https://www.visualstudio.com/vs/community/) to build the System Informer source code.

您可以下载免费的 [Visual Studio Community 版](https://www.visualstudio.com/vs/community/) 来构建 System Informer 源码。

Note: sources containing localized strings are stored as UTF-8 with BOM for MSVC compatibility.

注意：包含汉化字符串的源文件以带 BOM 的 UTF-8 编码保存，以兼容 MSVC。

See the [build readme](./build/README.md) for more information or if you're having trouble building the project.

更多信息或构建遇到问题请查阅[构建说明](./build/README.md)。

## Localization maintenance | 汉化维护

The translation tooling lives in `tools_l10n/`. After merging an upstream update, re-run the patch scripts to re-apply translations.

汉化工具位于 `tools_l10n/` 目录。合并上游更新后，可重新运行补丁脚本恢复翻译。

## Credits | 致谢

* Upstream project: [winsiderss/systeminformer](https://github.com/winsiderss/systeminformer) by Winsider Seminars & Solutions, Inc.
* This localization fork: [xb0or/systeminformer](https://github.com/xb0or/systeminformer)

上游项目版权归 Winsider Seminars & Solutions, Inc. 所有，本汉化分支遵循同一 MIT 许可证。

All trademarks and upstream code belong to their respective owners; this fork is distributed under the same MIT license.
