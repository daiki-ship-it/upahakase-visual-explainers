# HTML構造ガイド

**完成見本**: 仕様どおりに組み上がった実ページはリポジトリの **`output/ai-tool-roadmap-apr2026/index.html`** を参照する（この章のテンプレートと照らし合わせる）。

## 基本テンプレート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【図解タイトル】- ウパ博士｜AI業務設計の専門家</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* ブランドカラー：パニっくん＝紫 / ウパ博士＝ピンク（ヘッダー・目次・アクセント。吹き出し本体は中立のまま） */
    :root {
      --brand-primary: hsl(328, 73%, 52%);
      --brand-secondary: hsl(262, 55%, 46%);
      --brand-gradient: linear-gradient(90deg, hsl(262, 58%, 42%), hsl(328, 75%, 56%));
    }
    
    body {
      font-family: 'Noto Sans JP', 'Inter', sans-serif;
    }

    /* ヘッダーグラデーション */
    .header-gradient {
      background: var(--brand-gradient);
    }

    /* セクションカード */
    .section-card {
      background: white;
      border-radius: 1rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      padding: 2rem;
      margin-bottom: 2rem;
    }

    /* 用語解説ボックス */
    .term-explain {
      background: linear-gradient(135deg, #fdf2f8 0%, #fae8ff 100%);
      border-left: 4px solid var(--brand-secondary);
      padding: 1.5rem;
      border-radius: 0.75rem;
      margin: 1.5rem 0;
    }

    /*
     * キャラクター吹き出し（メッセンジャー風）
     * — パニっくん／ウパ博士とも背景色は付けない（白＋細い中立ボーダー）。強調は本文の span で行う。
     * — パニっくん：アバター左＋吹き出し右（尾巴は左向き）
     * — ウパ博士：アバター右＋吹き出し左（flex-row-reverse、尾巴は右向き）
     */
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
    .char-bubble--from-left {
      margin-left: 1rem;
    }
    .char-bubble--from-left::before {
      left: -10px;
      border-color: transparent hsl(220, 14%, 82%) transparent transparent;
    }
    .char-bubble--from-right {
      margin-right: 1rem;
    }
    .char-bubble--from-right::before {
      right: -10px;
      left: auto;
      border-color: transparent transparent transparent hsl(220, 14%, 82%);
    }

    /* 吹き出し内の強調（背景色は使わずテキストで差をつける） */
    .bubble-key {
      font-weight: 700;
      color: #dc2626;
    }
    .bubble-ui {
      font-weight: 700;
      color: #111827;
    }

    /* 重要度バッジ */
    .badge-essential {
      background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
      color: white;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.875rem;
      font-weight: 600;
    }
    .badge-recommended {
      background: linear-gradient(135deg, var(--brand-secondary) 0%, var(--brand-primary) 100%);
      color: white;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.875rem;
      font-weight: 600;
    }
    .badge-optional {
      background: linear-gradient(135deg, #6b7280 0%, #9ca3af 100%);
      color: white;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.875rem;
      font-weight: 600;
    }

    /* コードブロック */
    .code-block {
      background: #1e293b;
      color: #e2e8f0;
      padding: 1.5rem;
      border-radius: 0.75rem;
      overflow-x: auto;
      font-family: 'Fira Code', monospace;
      font-size: 0.875rem;
      line-height: 1.7;
    }

    /* 冒頭インライン目次（記事直後・全幅で読める） */
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
    .toc-inline nav > ol {
      list-style: none;
      padding: 0;
      margin: 0;
      counter-reset: toc;
    }
    .toc-inline nav > ol > li {
      counter-increment: toc;
      margin-bottom: 0.85rem;
      line-height: 1.5;
    }
    .toc-inline nav > ol > li > a {
      color: #374151;
      font-weight: 500;
      text-decoration: none;
    }
    .toc-inline nav > ol > li > a:hover {
      color: var(--brand-secondary);
      text-decoration: underline;
    }
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
    .toc-inline .toc-sub a {
      color: inherit;
      font-weight: 400;
      text-decoration: none;
    }
    .toc-inline .toc-sub a:hover {
      text-decoration: underline;
      color: var(--brand-secondary);
    }
    .toc-inline .toc-sub .toc-sub-icon {
      flex-shrink: 0;
      margin-top: 0.15rem;
      color: hsl(328, 55%, 48%);
    }

    /* 目次（長編向け・デスクトップ固定。インライン目次と併用する場合は任意） */
    .toc {
      position: fixed;
      right: 2rem;
      top: 50%;
      transform: translateY(-50%);
      background: white;
      padding: 1rem;
      border-radius: 0.75rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      max-height: 80vh;
      overflow-y: auto;
      z-index: 50;
    }
    @media (max-width: 1280px) {
      .toc { display: none; }
    }
  </style>
</head>
<body class="bg-gray-50">
  <!-- ヘッダー -->
  <header class="header-gradient text-white py-8">
    <div class="max-w-4xl mx-auto px-4">
      <h1 class="text-3xl md:text-4xl font-bold">【タイトル】</h1>
      <p class="mt-2 text-lg opacity-90">サブタイトル</p>
    </div>
  </header>

  <!-- メインコンテンツ -->
  <main class="max-w-4xl mx-auto px-4 py-8">
    <!-- 冒頭目次：台本の見出し・区切りに合わせて id とリンクを対応させる -->
    <aside class="toc-inline" aria-label="この記事の目次">
      <h2>
        <i data-lucide="list" class="w-6 h-6 text-[var(--brand-secondary)]"></i>
        目次
      </h2>
      <nav>
        <ol>
          <li><a href="#sec-intro">導入：テーマの一言</a></li>
          <li>
            <a href="#sec-topic-a">本題の見出し</a>
            <ul class="toc-sub">
              <li>
                <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
                <a href="#sec-topic-a-prompt">補足行（プロンプト例など）へのジャンプ</a>
              </li>
            </ul>
          </li>
          <li><a href="#sec-outro">まとめ</a></li>
        </ol>
      </nav>
    </aside>
    <!-- 以降：対話ブロック（各セクションのラッパーに id を付与） -->
  </main>

  <!-- Lucide初期化 -->
  <script>
    lucide.createIcons();
  </script>
</body>
</html>
```

---

## 対話行のレイアウト（パニっくん左／ウパ博士右）

図解本文は**チャットアプリの会話**のように読ませる。**パニっくんは常に左アバター**、**ウパ博士は常に右アバター**。吹き出しには必ず方向用クラスを付ける。

| 話者 | 行の Flex | 子要素の順 | 吹き出しの修飾 |
|------|-----------|------------|----------------|
| パニっくん | `flex items-start gap-4`（既定の左→右） | 画像 → 吹き出し | `char-bubble char-bubble--from-left` |
| ウパ博士 | `flex flex-row-reverse items-start gap-4` | 画像 → 吹き出し（視覚的には右端にアバター） | `char-bubble char-bubble--from-right` |

### 最小例

```html
<!-- パニっくん -->
<div class="flex items-start gap-4 mb-6" id="sec-example-pani">
  <img src="./images/パニっくん-疑っている-512×512-透過.png" alt="パニっくん" class="w-20 h-20 object-contain flex-shrink-0">
  <div class="char-bubble char-bubble--from-left flex-1">
    <p class="text-lg text-gray-800">…</p>
  </div>
</div>

<!-- ウパ博士 -->
<div class="flex flex-row-reverse items-start gap-4 mb-6" id="sec-example-upa">
  <img src="./images/ウパ博士-諭す-512×512-透過.png" alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="text-lg text-gray-800">…</p>
  </div>
</div>
```

### 吹き出し内の強調（色は吹き出しに付けない）

話者ごとに吹き出しの背景色や枠色を変えない。**要点・結論・いちばん伝えたい一言**は赤＋太字（`.bubble-key` または同等の `font-bold text-red-600`）。**ボタン名・メニュー・画面上的なラベル**は黒＋太字（`.bubble-ui` または `font-bold text-gray-900`）。濫用せず、1吹き出しに赤は1〜2か所程度を目安にする。

**目次との対応**: 台本の大見出しや「このあと深掘りするブロック」単位で、上記のような行のラッパーまたは直前の `section` に **`id` を付与**し、冒頭の `.toc-inline` から `href` で飛べるようにする。サブ項目（プロンプト例・手順のひとかたまりなど）は `.toc-sub` と Lucide `sparkles` でインデント表示する（絵文字は使わない）。

---

## Lucide Icon の使い方

### 基本構文

```html
<i data-lucide="icon-name" class="w-6 h-6"></i>
```

### よく使うアイコン

| 用途 | アイコン名 | コード |
|-----|----------|--------|
| 重要 | `alert-circle` | `<i data-lucide="alert-circle" class="w-6 h-6 text-red-500"></i>` |
| ヒント | `lightbulb` | `<i data-lucide="lightbulb" class="w-6 h-6 text-yellow-500"></i>` |
| チェック | `check-circle` | `<i data-lucide="check-circle" class="w-6 h-6 text-green-500"></i>` |
| 情報 | `info` | `<i data-lucide="info" class="w-6 h-6 text-blue-500"></i>` |
| 警告 | `triangle-alert` | `<i data-lucide="triangle-alert" class="w-6 h-6 text-orange-500"></i>` |
| 設定 | `settings` | `<i data-lucide="settings" class="w-6 h-6 text-gray-500"></i>` |
| コード | `code` | `<i data-lucide="code" class="w-6 h-6 text-purple-500"></i>` |
| ファイル | `file-text` | `<i data-lucide="file-text" class="w-6 h-6 text-blue-500"></i>` |
| フォルダ | `folder` | `<i data-lucide="folder" class="w-6 h-6 text-yellow-600"></i>` |
| 矢印 | `arrow-right` | `<i data-lucide="arrow-right" class="w-6 h-6"></i>` |
| ユーザー | `user` | `<i data-lucide="user" class="w-6 h-6"></i>` |
| ロック | `lock` | `<i data-lucide="lock" class="w-6 h-6 text-gray-600"></i>` |
| 鍵 | `key` | `<i data-lucide="key" class="w-6 h-6 text-yellow-500"></i>` |
| 許可 | `shield-check` | `<i data-lucide="shield-check" class="w-6 h-6 text-green-500"></i>` |
| 禁止 | `shield-x` | `<i data-lucide="shield-x" class="w-6 h-6 text-red-500"></i>` |
| 質問 | `help-circle` | `<i data-lucide="help-circle" class="w-6 h-6 text-blue-500"></i>` |
| 本 | `book-open` | `<i data-lucide="book-open" class="w-6 h-6 text-indigo-500"></i>` |
| 学習 | `graduation-cap` | `<i data-lucide="graduation-cap" class="w-6 h-6 text-purple-500"></i>` |
| 目次見出し | `list` | `<i data-lucide="list" class="w-6 h-6 text-[var(--brand-secondary)]"></i>` |
| 目次サブ行（プロンプト等） | `sparkles` | `<i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon"></i>` |
| ツール | `wrench` | `<i data-lucide="wrench" class="w-6 h-6 text-gray-600"></i>` |
| プレイ | `play` | `<i data-lucide="play" class="w-6 h-6 text-green-500"></i>` |
| 停止 | `square` | `<i data-lucide="square" class="w-6 h-6 text-red-500"></i>` |

### セクションヘッダーでの使用例

```html
<div class="section-card">
  <div class="flex items-center gap-3 mb-6">
    <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
      <i data-lucide="shield-check" class="w-6 h-6 text-purple-600"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-gray-800">セクションタイトル</h2>
      <p class="text-gray-500">サブタイトル</p>
    </div>
  </div>
  <!-- コンテンツ -->
</div>
```

---

## コード例と説明のつなぎ方

**台本忠実・対話中心の図解**（diagram-upa の既定）では、コードの意味づけは**ウパ博士（または台本の話者）の吹き出し**に書き、その直後にコードブロックを置く。台本にない「このコードがやること」見出し＋解説段落だけのパーツは増やさない。

### ❌ 悪い例（説明がなくコードだけ）

```html
<div class="code-block">
  <pre><code>
hook.onPreToolUse((event) => {
  if (event.toolName === 'Write') {
    return { permissionDecision: 'deny' };
  }
});
  </code></pre>
</div>
```

### ✅ 良い例（説明がウパ博士のセリフ・右アバター）

```html
<div class="flex flex-row-reverse items-start gap-4 mb-4">
  <img src="./images/ウパ博士-標準-512×512-透過.png"
       alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="text-lg text-gray-800">
      ここでは、Writeツール——ファイルを書き込む道具——が使われそうになったら、
      <span class="bubble-key">許可しない</span>と返すルールを書いています。
    </p>
  </div>
</div>
<div class="code-block">
  <pre><code>
hook.onPreToolUse((event) => {
  if (event.toolName === 'Write') {
    return { permissionDecision: 'deny' };
  }
});
  </code></pre>
</div>
```

**補足**: 台本がもともと教材調で「このコードがやること」見出し＋本文になっている場合は、台本に合わせてよい。

---

## フローチャートの表現

```html
<div class="flex flex-col md:flex-row items-center justify-center gap-4 my-8">
  <div class="bg-blue-100 px-6 py-4 rounded-xl text-center">
    <i data-lucide="play" class="w-8 h-8 text-blue-600 mx-auto mb-2"></i>
    <div class="font-bold">開始</div>
  </div>
  <i data-lucide="arrow-right" class="w-8 h-8 text-gray-400 hidden md:block"></i>
  <i data-lucide="arrow-down" class="w-8 h-8 text-gray-400 md:hidden"></i>
  <div class="bg-yellow-100 px-6 py-4 rounded-xl text-center">
    <i data-lucide="shield-check" class="w-8 h-8 text-yellow-600 mx-auto mb-2"></i>
    <div class="font-bold">チェック</div>
  </div>
  <i data-lucide="arrow-right" class="w-8 h-8 text-gray-400 hidden md:block"></i>
  <i data-lucide="arrow-down" class="w-8 h-8 text-gray-400 md:hidden"></i>
  <div class="bg-green-100 px-6 py-4 rounded-xl text-center">
    <i data-lucide="check-circle" class="w-8 h-8 text-green-600 mx-auto mb-2"></i>
    <div class="font-bold">完了</div>
  </div>
</div>
```
