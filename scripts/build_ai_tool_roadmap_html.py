#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""台本Markdownから diagram-upa 形式の index.html を生成する。"""
from __future__ import annotations

import re
import sys
from pathlib import Path

UI_NAMES = (
    "ChatGPT",
    "Copilot",
    "Genspark",
    "Perplexity",
    "Manus",
    "Claude",
    "Gemini",
    "Notion AI",
    "Midjourney",
    "Googleドキュメント",
    "スプレッドシート",
    "Gmail",
    "Googleカレンダー",
    "NotebookLM",
    "Cowork",
    "Claude Code",
    "Slack",
    "Claude in Chrome",
    "プロンプト",
)


def _span_class_for_inner(inner: str) -> str:
    s = inner.strip()
    bare = s.strip("『』「」")
    if bare in UI_NAMES or s in UI_NAMES:
        return "bubble-ui"
    for u in UI_NAMES:
        if u in s:
            return "bubble-ui"
    return "bubble-key"


def md_to_inline_html(text: str) -> str:
    """台本内の **強調** を span に変換（UI名は bubble-ui、それ以外は bubble-key）。"""
    t = text.replace("\\*\\*", "**")
    while True:
        m = re.search(r"\*\*(.+?)\*\*", t, flags=re.DOTALL)
        if not m:
            break
        inner = m.group(1)
        cls = _span_class_for_inner(inner)
        repl = f'<span class="{cls}">{inner}</span>'
        t = t[: m.start()] + repl + t[m.end() :]
    t = t.replace("**", "")
    t = re.sub(r"(?i)slackに", '<span class="bubble-ui">Slack</span>に', t)
    return t


def normalize_md(md: str) -> str:
    md = md.replace("\\*\\*", "**")
    md = re.sub(
        r"リサーチに強い\*\*『Genspark』\*\*や\*\*『Perplexity』\*\*",
        "リサーチに強い**『Genspark』**や**『Perplexity』**",
        md,
    )
    md = re.sub(
        r"勝手に仕事を進めてくれる\*\*『Manus』\*\*。さらに\*\*『Claude』\*\*や\*\*『Gemini』\*\*",
        "勝手に仕事を進めてくれる**『Manus』**。さらに**『Claude』**や**『Gemini』**",
        md,
    )
    md = re.sub(
        r"他にも\*\*『Notion AI』\*\*や画像を作る\*\*『Midjourney』\*\*など",
        "他にも**『Notion AI』**や画像を作る**『Midjourney』**など",
        md,
    )
    return md


def parse_blocks(md: str) -> list[tuple]:
    lines = md.splitlines()
    blocks: list[tuple] = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        if not line or line == "#### ---":
            i += 1
            continue
        if line.startswith("### ---") or line.startswith("**【"):
            i += 1
            continue
        if line.startswith("####"):
            blocks.append(("chapter", line))
            i += 1
            continue
        if re.match(r"^\*\*第[1-4]章", line):
            blocks.append(("chapter", line))
            i += 1
            continue
        m = re.match(r"^\*\*(パニっくん|ウパ博士)：\*\*\s*「(.+)」\s*$", raw.strip())
        if not m:
            m = re.match(r"^(パニっくん|ウパ博士)\s*[:：]\s*「(.+)」\s*$", raw.strip())
        if m:
            blocks.append(("say", m.group(1), m.group(2)))
            i += 1
            continue
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line)
        if m and m.group(1)[:1] in "①②③":
            blocks.append(("rule_label", m.group(1)))
            i += 1
            continue
        if line.startswith("🎁"):
            title = re.sub(r"^🎁\s*", "", line).replace("**", "").strip()
            desc = ""
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            advance = i + 1
            if j < len(lines):
                nxt = lines[j].strip()
                if not nxt.startswith("🎁") and not nxt.startswith("**"):
                    desc = nxt
                    advance = j + 1
            blocks.append(("gift", title, desc))
            i = advance
            continue
        i += 1
    return blocks


PANIC_IMG = [
    "パニっくん-ひどく慌てる様子-512×512-透過.png",
    "パニっくん-涙ぐむ-512×512-透過.png",
    "パニっくん-驚き-512×512-透過.png",
    "パニっくん-疑っている-512×512-透過.png",
    "パニっくん-マジ？-512×512-透過.png",
    "パニっくん-標準-512×512-透過.png",
    "パニっくん-焦り-512×512-透過.png",
    "パニっくん-強く反発する-512×512-透過.png",
    "パニっくん-調子に乗ってる-512×512-透過.png",
    "パニっくん-自信がない-512×512-透過.png",
]
UPA_IMG = [
    "ウパ博士-諭す-512×512-透過.png",
    "ウパ博士-標準-512×512-透過.png",
    "ウパ博士-思考分析-512×512-透過.png",
    "ウパ博士-真顔-512×512-透過.png",
]


def pick_pani(n: int) -> str:
    return PANIC_IMG[n % len(PANIC_IMG)]


def pick_upa(n: int) -> str:
    return UPA_IMG[n % len(UPA_IMG)]


HEAD = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AIツール迷子からの脱却ロードマップ - ウパ博士｜AI業務設計の専門家</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: hsl(328, 73%, 52%);
      --brand-secondary: hsl(262, 55%, 46%);
      --brand-gradient: linear-gradient(90deg, hsl(262, 58%, 42%), hsl(328, 75%, 56%));
    }
    body { font-family: 'Noto Sans JP', 'Inter', sans-serif; }
    .header-gradient { background: var(--brand-gradient); }
    .section-card {
      background: white;
      border-radius: 1rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      padding: 2rem;
      margin-bottom: 2rem;
    }
    .char-bubble {
      position: relative;
      padding: 1.5rem;
      border-radius: 1rem;
      background: #ffffff;
      border: 1px solid hsl(220, 14%, 82%);
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.06);
    }
    .char-bubble::before {
      content: '';
      position: absolute;
      top: 20px;
      border-width: 10px;
      border-style: solid;
    }
    .char-bubble--from-left { margin-left: 1rem; }
    .char-bubble--from-left::before {
      left: -10px;
      border-color: transparent hsl(220, 14%, 82%) transparent transparent;
    }
    .char-bubble--from-right { margin-right: 1rem; }
    .char-bubble--from-right::before {
      right: -10px;
      left: auto;
      border-color: transparent transparent transparent hsl(220, 14%, 82%);
    }
    .bubble-key { font-weight: 700; color: #dc2626; }
    .bubble-ui { font-weight: 700; color: #111827; }
    .toc-inline {
      background: white;
      border-radius: 1rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      padding: 1.75rem 2rem;
      margin-bottom: 2rem;
    }
    .toc-inline h2 {
      font-size: 1.25rem;
      font-weight: 700;
      color: #1f2937;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .toc-inline nav > ol { list-style: none; padding: 0; margin: 0; counter-reset: toc; }
    .toc-inline nav > ol > li { counter-increment: toc; margin-bottom: 0.85rem; line-height: 1.5; }
    .toc-inline nav > ol > li > a { color: #374151; font-weight: 500; text-decoration: none; }
    .toc-inline nav > ol > li > a:hover { color: var(--brand-secondary); text-decoration: underline; }
    .toc-inline .toc-sub {
      list-style: none;
      padding: 0.35rem 0 0 1.5rem;
      margin: 0;
    }
    .toc-inline .toc-sub li {
      margin-bottom: 0.4rem;
      display: flex;
      align-items: flex-start;
      gap: 0.35rem;
      font-size: 0.9375rem;
      color: hsl(262, 48%, 36%);
    }
    .toc-inline .toc-sub a { color: inherit; font-weight: 400; text-decoration: none; }
    .toc-inline .toc-sub a:hover { text-decoration: underline; color: var(--brand-secondary); }
    .toc-inline .toc-sub .toc-sub-icon {
      flex-shrink: 0;
      margin-top: 0.15rem;
      color: hsl(328, 55%, 48%);
    }
    .gift-list { margin-top: 0.75rem; padding-left: 0; list-style: none; }
    .gift-list li {
      display: flex;
      gap: 0.5rem;
      align-items: flex-start;
      margin-bottom: 0.65rem;
      font-size: 1rem;
      color: #374151;
    }
  </style>
</head>
<body class="bg-gray-50">
  <header class="header-gradient text-white py-8">
    <div class="max-w-4xl mx-auto px-4">
      <h1 class="text-2xl md:text-4xl font-bold leading-tight">AIツール迷子からの脱却ロードマップ</h1>
      <p class="mt-2 text-lg opacity-90">たった5分で読める——「AIを使いこなせない」根本原因と、ツール選びの考え方</p>
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 py-8">
    <aside class="toc-inline" aria-label="この記事の目次">
      <h2>
        <i data-lucide="list" class="w-6 h-6 text-[var(--brand-secondary)]"></i>
        目次
      </h2>
      <nav>
        <ol>
          <li>
            <a href="#sec-ch1">第1章：なぜ「AIツール迷子」になるのか</a>
            <ul class="toc-sub">
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch1-r1">① 言葉を数字のパズルにする</a>
              </li>
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch1-r2">② 最初と最後に注意（アテンション）</a>
              </li>
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch1-r3">③ 次の言葉をドミノのように予測</a>
              </li>
            </ul>
          </li>
          <li><a href="#sec-ch2">第2章：AIツールの「本当の顔」</a></li>
          <li>
            <a href="#sec-ch3">第3章：2つのツールに絞る理由と選び方</a>
            <ul class="toc-sub">
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch3-gemini">最初のステップ：Gemini</a>
              </li>
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch3-claude">次のステップ：Claude</a>
              </li>
            </ul>
          </li>
          <li>
            <a href="#sec-ch4">第4章：言語化力・分解力と伴走</a>
            <ul class="toc-sub">
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch4-cowork">Coworkで一気通貫</a>
              </li>
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-ch4-gifts">無料プレゼント（4弾）</a>
              </li>
            </ul>
          </li>
        </ol>
      </nav>
    </aside>
"""

TAIL = """
  </main>

  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""


def bubble_pani(text: str, img: str, bid: str | None = None) -> str:
    extra = f' id="{bid}"' if bid else ""
    inner = md_to_inline_html(text)
    return f"""      <div class="flex items-start gap-4 mb-6"{extra}>
        <img src="./images/{img}" alt="パニっくん" class="w-20 h-20 object-contain flex-shrink-0">
        <div class="char-bubble char-bubble--from-left flex-1">
          <p class="text-lg text-gray-800">{inner}</p>
        </div>
      </div>
"""


def bubble_upa(text: str, img: str, bid: str | None = None) -> str:
    extra = f' id="{bid}"' if bid else ""
    inner = md_to_inline_html(text)
    return f"""      <div class="flex flex-row-reverse items-start gap-4 mb-6"{extra}>
        <img src="./images/{img}" alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
        <div class="char-bubble char-bubble--from-right flex-1">
          <p class="text-lg text-gray-800">{inner}</p>
        </div>
      </div>
"""


def bubble_upa_rule_label(label: str, text: str, img: str, bid: str | None) -> str:
    inner = md_to_inline_html(text)
    lbl = f'<span class="bubble-ui">{label}</span>'
    return f"""      <div class="flex flex-row-reverse items-start gap-4 mb-6"{f' id="{bid}"' if bid else ""}>
        <img src="./images/{img}" alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
        <div class="char-bubble char-bubble--from-right flex-1">
          <p class="text-lg text-gray-800">{lbl}——{inner}</p>
        </div>
      </div>
"""


def gifts_bubble(titles_descs: list[tuple[str, str]], img: str) -> str:
    lis = []
    for title, desc in titles_descs:
        t_esc = md_to_inline_html(title)
        d_esc = md_to_inline_html(desc) if desc else ""
        body = f'<span class="bubble-ui">{t_esc}</span>'
        if d_esc:
            body += f"——{d_esc}"
        lis.append(
            f"""            <li>
              <i data-lucide="gift" class="w-5 h-5 text-[var(--brand-secondary)] flex-shrink-0 mt-0.5" aria-hidden="true"></i>
              <span>{body}</span>
            </li>"""
        )
    ul = "\n".join(lis)
    return f"""      <div class="flex flex-row-reverse items-start gap-4 mb-6" id="sec-ch4-gifts">
        <img src="./images/{img}" alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
        <div class="char-bubble char-bubble--from-right flex-1">
          <p class="text-lg text-gray-800 mb-3">内容はこちらの4つです。</p>
          <ul class="gift-list" aria-label="無料プレゼント4弾">
{ul}
          </ul>
        </div>
      </div>
"""


def build_html(md_path: Path) -> str:
    md = normalize_md(md_path.read_text(encoding="utf-8"))
    blocks = parse_blocks(md)
    out: list[str] = [HEAD]
    ch = 0
    pani_i = upa_i = 0
    rule_idx = 0
    gifts_pending: list[tuple[str, str]] = []

    for b in blocks:
        if b[0] == "chapter":
            title = b[1]
            if "第1章" in title:
                ch = 1
                rule_idx = 0
                out.append('    <section class="section-card" id="sec-ch1">')
            elif "第2章" in title:
                out.append("    </section>")
                out.append('    <section class="section-card" id="sec-ch2">')
                ch = 2
                rule_idx = 0
            elif "第3章" in title:
                out.append("    </section>")
                out.append('    <section class="section-card" id="sec-ch3">')
                ch = 3
                rule_idx = 0
            elif "第4章" in title:
                out.append("    </section>")
                out.append('    <section class="section-card" id="sec-ch4">')
                ch = 4
                rule_idx = 0
            continue

        if b[0] == "rule_label":
            rule_idx += 1
            continue

        if b[0] == "gift":
            gifts_pending.append((b[1], b[2]))
            continue

        if b[0] != "say":
            continue

        speaker, raw_text = b[1], b[2]

        if speaker == "パニっくん":
            img = pick_pani(pani_i)
            pani_i += 1
            out.append(bubble_pani(raw_text, img))
            continue

        if speaker == "ウパ博士" and raw_text.startswith("これらを順番に実践") and gifts_pending:
            out.append(gifts_bubble(gifts_pending, pick_upa(upa_i)))
            upa_i += 1
            gifts_pending = []

        img = pick_upa(upa_i)
        upa_i += 1
        bid = None
        if ch == 4 and "簡単に言うと" in raw_text and "PCに入り込んで" in raw_text:
            bid = "sec-ch4-cowork"

        if ch == 1 and rule_idx == 1 and raw_text.startswith("まず、AIは"):
            out.append(
                bubble_upa_rule_label(
                    "① 言葉をバラバラの「数字のパズル」にする",
                    raw_text,
                    img,
                    "sec-ch1-r1",
                )
            )
            continue
        if ch == 1 and rule_idx == 2 and raw_text.startswith("次に、AIは長文"):
            out.append(
                bubble_upa_rule_label(
                    '② 「最初」と「最後」にしか注意を払わない（アテンション）',
                    raw_text,
                    img,
                    "sec-ch1-r2",
                )
            )
            continue
        if ch == 1 and rule_idx == 3 and raw_text.startswith("最後は、スマホ"):
            out.append(
                bubble_upa_rule_label(
                    '③ 次の言葉を「ドミノ倒し」で予測する（自己回帰）',
                    raw_text,
                    img,
                    "sec-ch1-r3",
                )
            )
            continue

        if ch == 3 and rule_idx == 1 and raw_text.startswith("まず最初はGemini"):
            out.append(
                bubble_upa_rule_label(
                    '① 最初のステップ：Geminiで「AIで仕事がラクになる感覚」を掴む',
                    raw_text,
                    img,
                    "sec-ch3-gemini",
                )
            )
            continue
        if ch == 3 and rule_idx == 2 and raw_text.startswith("GeminiでAIに慣れたら"):
            out.append(
                bubble_upa_rule_label(
                    '② 次のステップ：Claudeで「業務を一気通貫で自動化」する',
                    raw_text,
                    img,
                    "sec-ch3-claude",
                )
            )
            continue

        out.append(bubble_upa(raw_text, img, bid))

    if gifts_pending:
        out.append(gifts_bubble(gifts_pending, pick_upa(upa_i)))

    out.append("    </section>")
    out.append(TAIL)
    return "\n".join(out)


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: build_ai_tool_roadmap_html.py <input.md> <output.html>", file=sys.stderr)
        sys.exit(1)
    md_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    html = build_html(md_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
