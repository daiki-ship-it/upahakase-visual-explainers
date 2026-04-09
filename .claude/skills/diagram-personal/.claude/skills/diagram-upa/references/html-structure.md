# HTML構造ガイド

**完成見本（ビジュアル・寸法のSSOT）**: リポジトリの **`output/ai-daily-report-slack-apr2026/index.html`**。テキストサイズ、`.layout-column`、ヘッダー、`.toc-inline`、`.section-card`、`.char-stack` / `.char-avatar` / `.char-name`、`.bubble-body`、章見出し `.body-chapter-heading`、ブランドの HSL、Lucide の読み込みバージョンとアイコン寸法、ページ背景、吹き出し用の `</body>` 直前スタイルなどは**すべてこのファイルに合わせる**。

このファイルは **Lucide の書き方・対話行の flex 表・コードとセリフのつなぎ**の参照用である。**長い「基本テンプレート」ブロックは、旧デザイン（紫ピンク・`max-w-4xl`・`lucide@latest` 等）が完成見本と矛盾するため削除した。** 数値やクラスが本文中の例と完成見本で食い違う場合は**常に完成見本を優先**する。

## 新規 `index.html` の作り方

### 手順

1. **`output/ai-daily-report-slack-apr2026/index.html` を丸ごと複製**して編集の起点にする。
2. 次だけ台本に合わせて差し替える: `<title>`、`<header>` の見出し、`.toc-inline` のリンク列、`main` 内の `h2.body-chapter-heading` および各 `section.section-card` の対話・図・手順ブロック。
3. **原則として触らない**: Tailwind／Lucide の `<script>`（**`@latest` に変更しない**。完成見本と同じピン留め URL を維持）、Google Fonts の `<link>`、`<head>` 内の `<style>` 全体、`body` のクラス、**`</body>` 直前の `<style>`（`.slack-daily-page` スコープの吹き出し）** と続く `lucide.createIcons()` のスクリプト。順序を入れ替えると Tailwind が吹き出し用 CSS を上書きし、見た目が崩れる。

### diagram-upa で使わないパーツ

- **独立した「用語解説」ボックス**（`.term-explain` など）: diagram-upa では**置かない**。用語の言い換えは [term-dictionary.md](term-dictionary.md) を参照しつつ、**セリフの中**に書く（SKILL・exemplar）。

### 使ってはいけないベース

- **`output/ai-tool-roadmap-apr2026/index.html`**（旧完成見本）
- **`lucide@latest`**（再現性がない）

---

## 対話行のレイアウト（パニっくん左／ウパ博士右）

図解本文は**チャットアプリの会話**のように読ませる。**パニっくんは常に左アバター**、**ウパ博士は常に右アバター**。吹き出しには必ず方向用クラスを付ける。

| 話者 | 行の Flex | 子要素の順 | 吹き出しの修飾 |
|------|-----------|------------|----------------|
| パニっくん | `flex items-start gap-4`（既定の左→右） | `.char-stack`（アバター＋名前）→ 吹き出し | `char-bubble char-bubble--from-left` |
| ウパ博士 | `flex flex-row-reverse items-start gap-4` | 同上（視覚的には右端にアバター） | `char-bubble char-bubble--from-right` |

### 最小例（完成見本と同型）

アバター直下に名前を出す **`.char-stack`** と、本文用 **`.bubble-body`** を使う。行の縦余白は完成見本に合わせる（例: `mb-8`）。しっぽ付き吹き出しの CSS は完成見本の `</body>` 直前ブロックに依存する。

```html
<!-- パニっくん -->
<div class="flex items-start gap-4 mb-8" id="sec-example-pani">
  <div class="char-stack char-stack--panik">
    <img src="./images/パニっくん-疑っている-512×512-透過.png" alt="パニっくん" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
    <p class="char-name">パニっくん</p>
  </div>
  <div class="char-bubble char-bubble--from-left flex-1">
    <p class="bubble-body">…</p>
  </div>
</div>

<!-- ウパ博士 -->
<div class="flex flex-row-reverse items-start gap-4 mb-8" id="sec-example-upa">
  <div class="char-stack char-stack--upa">
    <img src="./images/ウパ博士-諭す-512×512-透過.png" alt="ウパ博士" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
    <p class="char-name">ウパ博士</p>
  </div>
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="bubble-body">…</p>
  </div>
</div>
```

### 吹き出し内の強調（色は吹き出しに付けない）

話者ごとに吹き出しの背景色や枠色を変えない。**要点・結論・いちばん伝えたい一言**は赤＋太字（`.bubble-key` または同等の `font-bold text-red-600`）。**ボタン名・メニュー・画面上的なラベル**は黒＋太字（`.bubble-ui` または `font-bold text-gray-900`）。濫用せず、1吹き出しに赤は1〜2か所程度を目安にする。

**目次との対応**: 台本の大見出しや「このあと深掘りするブロック」単位で、上記のような行のラッパーまたは直前の `section` に **`id` を付与**し、冒頭の `.toc-inline` から `href` で飛べるようにする。サブ項目（プロンプト例・手順のひとかたまりなど）は `.toc-sub` と Lucide `sparkles` でインデント表示する（絵文字は使わない）。

---

## Lucide Icon の使い方

### 読み込み（diagram-upa）

完成見本と**同じ UMD URL・バージョン**を使う（例: `https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js`）。ページ末尾で `lucide.createIcons();` を実行する。

### 基本構文

```html
<i data-lucide="icon-name" class="w-6 h-6"></i>
```

**寸法**: 汎用アイコンは `w-6 h-6` のこともあるが、**`.toc-inline` 内は完成見本に合わせる**——目次見出しの `list` は `w-4 h-4`、`.toc-sub` 内の `sparkles` は `w-3.5 h-3.5` が目安（完成見本のマークアップをコピーするのが確実）。

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
| 目次見出し | `list` | `<i data-lucide="list" class="w-4 h-4 text-[var(--brand-secondary)]" aria-hidden="true"></i>` |
| 目次サブ行（プロンプト等） | `sparkles` | `<i data-lucide="sparkles" class="w-3.5 h-3.5 toc-sub-icon" aria-hidden="true"></i>` |
| ツール | `wrench` | `<i data-lucide="wrench" class="w-6 h-6 text-gray-600"></i>` |
| プレイ | `play` | `<i data-lucide="play" class="w-6 h-6 text-green-500"></i>` |
| 停止 | `square` | `<i data-lucide="square" class="w-6 h-6 text-red-500"></i>` |

### セクションヘッダーでの使用例（参考）

diagram-upa の標準図解では、**完成見本に無い大きなアイコン付きカード見出しを新設しない**方針（対話と章見出しが主）。フローチャート等でアイコンを並べる場合の HTML 例としてのみ参照する。

```html
<div class="section-card">
  <div class="flex items-center gap-3 mb-6">
    <div class="w-12 h-12 bg-slate-100 rounded-xl flex items-center justify-center">
      <i data-lucide="shield-check" class="w-6 h-6 text-[var(--brand-secondary)]"></i>
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
  <div class="char-stack char-stack--upa">
    <img src="./images/ウパ博士-標準-512×512-透過.png"
         alt="ウパ博士" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
    <p class="char-name">ウパ博士</p>
  </div>
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="bubble-body">
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

**補足**: 台本がもともと教材調で「このコードがやること」見出し＋本文になっている場合は、台本に合わせてよい。プロンプト貼り付け UI が必要な場合は完成見本の `.script-prompt-block` 等を優先する。

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

色面は吹き出しとは別の図解パーツ向け。対話の吹き出し本体に話者色を付けないルールとは切り離して使う。
