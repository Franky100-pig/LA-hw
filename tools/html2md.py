#!/usr/bin/env python3
"""把 la-hw 的题面/解答 HTML 转成 pandoc 能吃的 Markdown（保留 $...$ / $$...$$ 数学）。

用法：
    python3 tools/html2md.py set6/problems.html  [输出 md 路径]

为什么需要这一步：题面 HTML 是源文件（MathJax 渲染），docx / pdf 是二次产物。
pandoc 直接读 HTML 会把数学当普通文本，$ 号虽被保留却不再参与解析；所以先剥标签、
只留 Markdown 骨架与 $...$ 原文，再让 pandoc 用 markdown+tex_math_dollars 去读，
公式才会真的渲染成 Word 原生方程 / LaTeX 排版。
"""
import html
import re
import sys
from pathlib import Path

# 只保留正文所在的 wrap 容器，丢掉 head / style / script
WRAP_RE = re.compile(r'<div class="wrap">(.*)</div>\s*</body>', re.S)
DROP_RE = re.compile(r'<(script|style)\b.*?</\1>', re.S)
COMMENT_RE = re.compile(r'<!--.*?-->', re.S)


# 行内数学：$...$；display 数学：$$...$$。
# 必须先整体保护起来，否则数学里的 "<"（如 $1 < 2$）会被下面的标签剥离规则
# 当成 HTML 标签的开头，把后半段正文整块吞掉 —— 这个坑真踩过（Set 6）。
MATH_RE = re.compile(r'\$\$.*?\$\$|\$[^$\n]*\$', re.S)
PH_RE = re.compile('\x00(\\d+)\x00')


def inline(text: str) -> str:
    """处理行内标签：粗体/斜体/代码/链接；数学段先占位保护，剥完标签再还原。"""
    math = []

    def keep(m):
        math.append(m.group(0))
        return f"\x00{len(math) - 1}\x00"

    text = MATH_RE.sub(keep, text)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.S)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text, flags=re.S)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.S)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text, flags=re.S)
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text, flags=re.S)
    text = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.S)
    text = re.sub(r'<br\s*/?>', r'  ', text)
    text = text.replace("\u00a0", " ")
    # <span class="ans"> 这类只剩语义，不影响正文结构
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    # 数学段原样还原（不参与 unescape，避免把 &amp; 之类写坏）
    text = PH_RE.sub(lambda m: math[int(m.group(1))], text)
    return text.strip()


def convert(src: str) -> str:
    src = COMMENT_RE.sub('', src)
    src = DROP_RE.sub('', src)
    body = WRAP_RE.search(src)
    if not body:
        raise SystemExit('找不到 <div class="wrap"> 正文容器')
    body = body.group(1)

    out = []
    # 按块级标签切：<h1> <h2> <p> <div>
    for tag, content in re.findall(r'<(h1|h2|p|div)\b[^>]*>(.*?)</\1>', body, flags=re.S):
        text = inline(content)
        if not text:
            continue
        if tag == 'h1':
            out.append('# ' + text + '\n')
        elif tag == 'h2':
            out.append('\n## ' + text + '\n')
        else:
            # 数学 display 块（$$ ... $$）独占一段时单独成段，避免被折进正文行里
            if text.startswith('$$') and text.endswith('$$'):
                out.append('\n' + text + '\n')
            else:
                out.append(text + '\n')
    return '\n'.join(out).strip() + '\n'


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit('用法: html2md.py <input.html> [output.md]')
    src_path = Path(sys.argv[1])
    dst_path = Path(sys.argv[2]) if len(sys.argv) > 2 else src_path.with_suffix('.md')
    md = convert(src_path.read_text(encoding='utf-8'))
    dst_path.write_text(md, encoding='utf-8')
    print(f'{src_path} -> {dst_path} ({len(md)} bytes)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
