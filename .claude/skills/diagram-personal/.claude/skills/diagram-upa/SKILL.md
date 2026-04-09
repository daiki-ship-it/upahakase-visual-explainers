---
name: diagram-upa
description: ユーザーが用意した台本を起点に、AI関連情報の検証と読者視点のブラッシュアップを経て、パニっくんとウパ博士の会話ラリーをメッセンジャー風HTMLに写すスキル。見た目はリポジトリの完成見本（output/ai-daily-report-slack-apr2026/index.html）を複製して遵守する（パニっくん左・ウパ博士右、吹き出しは白＋中立ボーダー、要点は赤太字・UI名は黒太字、main 先頭のインライン目次で読み順はヘッダー直後に相当）。教材型の用語ボックスや「まず覚える3つ」などの挿入はしない。surge.sh にデプロイする。「台本から図解して」「図解して」など対話形式の図解HTML向け。
---

# Diagram Upa

ユーザーが用意した**台本**を唯一の主ソースとして、事実・表現を整えたうえで、**技術に詳しくない一般の人**向けの対話形式HTML図解にし、デプロイまで行う。

**図解の理想形**: パニっくんとウパ博士の**会話のラリーを台本どおり**並べること（**台本をそのまま図解にする**イメージ）。**画面ではパニっくんを左・ウパ博士を右**に固定し、チャットのように読めるレイアウトにする。吹き出しは**話者ごとに色を付けず**白＋細い中立ボーダーに統一し、伝えたい強弱は**セリフ内の赤太字（核心）・黒太字（UI名）**で示す。あわせて **`main` 要素内の先頭**にインライン目次（`.toc-inline`、台本の見出し・区切りに対応したアンカー）を置き、読み順ではヘッダーの直後に相当する位置で全体像を先に示す（`</header>` と `<main>` の間には置かない。完成見本どおり）。教材向けの挿入物——「まず覚える3つ」、独立した「用語解説」ブロック、ナレーション調の見出しだけの説明文、対話と無関係な補足段落——は**置かない**。用語やたとえ、コードの意味づけはすべて**ウパ博士のセリフ**（必要なら続けてパニっくんの反応）として表現する。

## 依存

定義の**SSoT**は次の表どおりに**役割分担**する（長い HTML/CSS の全文は SKILL.md に書かない）。

**優先順位（食い違ったらこう解決する）**

1. **ビジュアル・寸法・CSS・読み込みバージョン・マークアップ上の具体クラス**の正本は **`output/ai-daily-report-slack-apr2026/index.html` のみ**。新規図解は**必ずこのファイルを複製**してから、タイトル・目次・本文・`id` を差し替える。
2. **利用条件・著作権フッター**の日本語条文および `<footer>…</footer>` のマークアップの正本は **[references/legal-footer-snippet.html](references/legal-footer-snippet.html)**。完成見本 HTML のフッターは、プレースホルダを埋めた結果と**一致**させる。**条文の食い違いは常に snippet を正**とし、完成見本・`output/` 内の他 HTML を追従させる。プレースホルダの意味・漫画派生版・部分生成時の扱いは **[references/legal-footer.md](references/legal-footer.md)**。
3. **品質チェック（完成後に照らす項目）**の正本は **この SKILL の「[品質チェックリスト](#品質チェックリスト)」**。[references/exemplar.md](references/exemplar.md#quality-checklist) には SKILL へのリンクと制作時の**短い要約**があるが、チェック項目の列挙は **SKILL のみ**とする。
4. [references/html-structure.md](references/html-structure.md) は **Lucide・対話行の flex 表・コードとセリフのつなぎ**などの**説明用**。[references/exemplar.md](references/exemplar.md) は **構成の型・断片サンプル**（完成見本と同型のマークアップ）。いずれも **1〜3 と矛盾する具体的な記述**（数値・クラス・余白・検証の解釈など）があれば、**完成見本・snippet およびこの SKILL を優先**する。

**ベースにしてはいけないもの**

- **`output/ai-tool-roadmap-apr2026/index.html`**（旧完成見本。レイアウト・配色が現行と異なる）
- 別スキル `sample/majiai-diagram/.claude/skills/diagram-maji/`（パス・仕様が異なる。**混同しない**）

| 内容 | パス（リポジトリルートから） |
|------|------------------------------|
| **完成見本HTML（実装の型・ビジュアルの唯一の正本）** | `output/ai-daily-report-slack-apr2026/index.html` |
| HTMLの書き方・Lucide・対話レイアウトの説明（正本は上の完成見本） | `.claude/skills/diagram-personal/.claude/skills/diagram-upa/references/html-structure.md` |
| キャラ役割・トーン・表情・対話HTML例（マークアップは完成見本と同型） | `.claude/skills/diagram-personal/.claude/skills/diagram-upa/references/character-usage.md` |
| 用語のやさし替え・たとえ（セリフへの取り込み用。HTML用語ボックス用ではない） | `.claude/skills/diagram-personal/.claude/skills/diagram-upa/references/term-dictionary.md` |
| 模範・成功パターン（本文・構成の型） | `.claude/skills/diagram-personal/.claude/skills/diagram-upa/references/exemplar.md` |
| **利用条件・著作権（条文・フッター HTML の唯一の正本）** | `.claude/skills/diagram-personal/.claude/skills/diagram-upa/references/legal-footer-snippet.html`（運用・プレースホルダ: [legal-footer.md](references/legal-footer.md)） |

- 上表と同じ内容は、この SKILL と同じ `diagram-upa/references/` からの相対パスでも開ける（例: [references/html-structure.md](references/html-structure.md)）。
- `.claude/skills/diagram-personal/docs/charactor-images/` — キャラクター画像（PNG）

---

<a id="legal-footer-required"></a>

## 利用条件・著作権（必須フッター）

すべての図解 HTML の最終成果物に、**正本どおり**の「利用条件・著作権」ブロックを含める（省略・要約・「要点だけ」への差し替えは不可）。

| 項目 | 内容 |
|------|------|
| **正本** | [references/legal-footer-snippet.html](references/legal-footer-snippet.html) |
| **置換してよいもの** | `__UPA_LEGAL_OFFICIAL_URL__`（「この資料の公式配布ページ」の **2 箇所の `href` で同一の絶対 URL**）、`__UPA_LEGAL_LAST_UPDATED__`（最終更新の日付表示部分のみ） |
| **禁止** | 条文の AI による言い換え・短縮・リーガル調の再執筆。正本にない文をフッターに足す（**漫画派生版のオプション1段落を除く**）。プレースホルダの未置換のまま納品する。 |

- **デフォルトの作り方**: 完成見本 `output/ai-daily-report-slack-apr2026/index.html` を複製すればフッター付き。差し替えるのは原則として **公式 URL** と **最終更新日** だけ。
- **`main` のみ生成・チャンク結合する場合**: 最終結合後、**`</main>` の直後**（`</body>` 直前の吹き出し用 `<style>` より前）に、正本フルブロックを貼り付け、プレースホルダをすべて埋める。
- **漫画風派生版**（同一内容の見た目バリエーション）: [references/legal-footer.md](references/legal-footer.md) に従い、正本の著作権第1段落の直後に**だけ**オプション段落を追加してよい。リンクは派生ページ自身の公式 URL を使う。通常の `index.html` にはその段落を**入れない**。

条文やフッター構造を変更したときは **snippet を編集**し、[references/legal-footer.md](references/legal-footer.md) の手順で `output/` の完成見本などリポジトリ内の該当 HTML を揃える。

---

## ユーザーへの提示（成果物の扱い）

- **ユーザーに見せる最終成果物は、デプロイ後の図解URLと短い要約に絞る。** 検証メモ、台本の改稿全文、第1版HTMLのURLなどの中間成果物は、ユーザーが求めない限り報告に含めない。
- 作業の一貫性のため、台本やHTMLをワークスペース内に置いてよい（ファイル名・場所は任せる）。

---

## ワークフロー

全体は **台本入力 → 検証リサーチ → 台本修正 → 図解設計 → HTML第1版 → 読者視点で台本レビュー → 台本再修正 → HTML最終版 → デプロイ** である。読者レビューで**改善不要**と判断した場合は、台本の変更とHTML再生成を省略し、**第1版をそのまま最終としてデプロイ**してよい。

### 1. 台本の受領

- **主入力は台本**（見出し・ナレーション・想定セリフなど、図解に落とし込む文章）。チャット貼り付けでも、既存ファイルでもよい。
- 参照用URLや補足ドキュメントがある場合のみ `WebFetch` 等で取得し、**台本と矛盾しない範囲**で補強に使う。台本にない論点を勝手に増やさない。

### 2. AI関連の検証リサーチ（サブエージェント）

**explore** サブエージェントで、台本に現れる**AI・技術・製品・数値・時期・バージョン・固有名詞**などを洗い出し、信頼できる情報源に照らして検証する。

```
Task({
  subagent_type: "explore",
  description: "台本内AI・技術情報の検証リサーチ",
  prompt: `
    以下の台本に登場する、AI・機械学習・クラウド・開発ツール・製品名・統計・日付・バージョンなど、事実確認が必要な記述を列挙してください。
    それぞれについて、公的ドキュメント・一次情報・権威ある解説などを用いて検証し、
    誤り・誇張・曖昧さ・時代錯誤があれば指摘し、修正案の方向性を短く示してください。
    台本に触れられていない論点を新たに「追加すべき」と提案する必要はありません（台本の忠実な検証が目的）。

    【台本】
    {台本全文またはファイルパス}

    出力は箇条書きで、見出しは「確認した記述 / 結論 / 根拠の種類（公式・報道・解説など）」がわかるように整理してください。
  `
})
```

### 3. 台本のファクト・表現ブラッシュアップ

- Phase 2 の結果を反映し、**誤り・リスクのある表現を修正**する。必要なら「断定→条件付き」などトーンも調整する。
- この時点の台本を、以降の図解設計・HTMLの**唯一のストーリー正**とする。

### 4. 図解設計

台本の**発話順・内容**を主軸にする。図解用に「章立ての要約」や「覚えておく3点」を**新設しない**。

1. **目次**: 台本に見出し・ランキング・大きな話の区切りがある場合は、**`main` 内の先頭**に置くインライン目次（`.toc-inline`）へ同じ階層で反映する（`</header>` の次が `main` で、その**最初の子**が `.toc-inline` になる。完成見本どおり）。各ブロックに `id` を付け、`href` で対応させる。サブ行（プロンプト例など）は [references/html-structure.md](references/html-structure.md) の `.toc-sub` でインデントし、装飾は **Lucide**（例: `list` / `sparkles`）を使う（絵文字は使わない）。現行の完成見本 HTML にはフローティング目次（別要素の `.toc`）は含まれない。**デフォルトは `.toc-inline` のみ**とする。極端に長い長編でチーム内に別パターンがある場合のみ、[references/exemplar.md](references/exemplar.md) の「成功する図解の構造」の（参考）記述を参照してよい。
2. **用語・たとえ**: 台本に出てくる用語のやさしい言い換えは、[references/term-dictionary.md](references/term-dictionary.md) を**ブラッシュアップ用**に参照し、**ウパ博士のセリフの中**へ取り込む（独立した用語ボックスは作らない）。
3. **対話の連なり**: パニっくん（読者代弁）とウパ博士（説明は直接セリフで）のラリーを、台本の並びに近い形でHTMLに写す。**パニっくんは左アバター、ウパ博士は右アバター**のメッセンジャー風に固定する。役割・トーン・表情は [references/character-usage.md](references/character-usage.md) に従う。
4. **視覚補助のみ**: 台本の間にダイアグラム・コード・箇条書きを置く場合は、**直前のウパ博士（または台本どおりの話者）の発話**で文脈がつながるようにし、教材用の見出し＋解説だけのブロックを増やさない。

### 5. HTML（第1版）

- **必ず**リポジトリ内の完成見本 **`output/ai-daily-report-slack-apr2026/index.html` を複製**して `index.html` の土台とする。ゼロから書き起こしたり、旧完成見本や `max-w-4xl` の広い記事レイアウトに戻さない。
- 複製後、`<title>`・ヘッダー・`.toc-inline`・`main` 内の章見出し・対話・補助ブロックだけを台本に合わせて差し替える。**`<head>` の CSS（`:root`・`.layout-column` 等）と、`</body>` 直前の吹き出し用 `<style>`・Lucide 初期化は完成見本のまま維持**する（Tailwind CDN より後に吹き出し CSS が効く順序を崩さない）。
- **`</main>` から `</body>` 直前の吹き出し `<style>` まで**のあいだに、完成見本どおり **[利用条件・著作権](#legal-footer-required)** の `<footer>` ブロックを残す。削除・要約・条文の独自改変をしない。URL・日付は当該デプロイに合わせて置換する。複製を経由しない生成では [references/legal-footer-snippet.html](references/legal-footer-snippet.html) をそのまま貼り付け、プレースホルダを埋める。
- [references/html-structure.md](references/html-structure.md) は **Lucide の data 属性・対話行の flex 表**などの参照用。[references/exemplar.md](references/exemplar.md) は **目次・対話の断片サンプル**用。いずれも**見た目の数値は完成見本が正**。
- **`main` の最初の子として `.toc-inline` を置く**（台本に章立てがほぼない短編では、目次を「導入／本題／まとめ」など**最小3項目**にとどめてよい。[references/exemplar.md](references/exemplar.md) に同じ緩和を記載）。
- **本文は対話（吹き出し）中心**。**パニっくん**は `.char-stack--panik`＋`char-bubble char-bubble--from-left`、**ウパ博士**は `flex-row-reverse`＋`.char-stack--upa`＋`char-bubble char-bubble--from-right`。本文は **`.bubble-body`**（完成見本どおり）。吹き出しで話者色分けしない（白＋中立ボーダー）。要点は**赤太字**（`.bubble-key`）、UI 名は**黒太字**（`.bubble-ui`）。コードや図の意味づけは**吹き出し内のセリフ**に含める。
- **長文吹き出しの改行（可読性）**: 台本の発話を増やさず、HTML 上だけ意味の区切りで読みやすくする。**同一 `.bubble-body` 内なら `<br>`**、塊が分かれる場合は同一吹き出し内に **`<p class="bubble-body">` を複数**（完成見本の複数段落パターンに合わせる）。**新しい吹き出しに分ける**のは台本のラリーに合うときだけ。

### 6. 読者視点の台本レビュー（サブエージェント）

**第1版HTMLが表現している内容**と**現行台本**をセットで渡し、[references/character-usage.md](references/character-usage.md) の**パニっくん像**（ITが苦手な読者の代弁者）に近い視点で、台本のわかりやすさ・違和感をレビューさせる。HTMLの細部のマークアップより、**セリフの順序、難しさ、たとえの噛み合い、情報量**を優先する。

```
Task({
  subagent_type: "generalPurpose",
  description: "読者視点の台本レビュー",
  readonly: true,
  prompt: `
    あなたは「パニっくん」に近い読者です。ITは苦手だが、AIには興味がある。専門用語の羅列や説明不足には敏感。
    この図解は「台本の対話をそのまま並べる」方針です。レビューで「用語解説ボックスを足せ」「まず覚える3つを入れろ」など、対話以外の教材パーツ追加を提案しないでください。改善はセリフの中身・順序・前提の補足に限定する。
    以下の【現行台本】と、それをもとに作られた【第1版HTMLのパス】を読み、台本側を主に評価してください（HTMLは内容の参照用）。

    【現行台本】
    {台本全文またはファイルパス}

    【第1版HTML】
    {path}

    ## 観点
    1. どこで意味がつながらなくなるか（前提が抜けている箇所）
    2. 難しい言葉・一度に来る概念の多さ
    3. たとえ話の違和感・順序の悪さ
    4. パニっくんのセリフが読者らしくない箇所
    5. 読後に説明できるか（ゴールの明確さ）

    ## 出力形式
    ### 致命的（このままでは読者が置いていかれる）
    - ...
    ### 改善したい（直すと一気に良くなる）
    - ...
    ### 良い（残すべき）
    - ...
    ### 総評（短く）
  `
})
```

### 7. 台本の再ブラッシュアップ

- Phase 6 のうち**致命的・改善したい**に対し、台本を改稿する。**良い**は維持する。
- 改稿が軽微でHTMLの構造変更が不要と判断できる場合でも、方針としては**台本とHTMLの内容を一致**させる（必要ならHTML側のテキストのみ差し替え）。

### 8. HTML（最終版）

- Phase 7 で台本に変更があった場合、**HTMLを再生成または差分更新**し、最終版とする。変更がなかった場合は第1版を最終版とする。
- 品質の最終確認は [品質チェックリスト](#品質チェックリスト) に照らして行う。
- **最終 HTML に正本どおりの利用条件・著作権フッターが含まれ、プレースホルダが残っていない**ことを必ず確認する（部分編集で `</footer>` が落ちていないか含む）。

### 9. デプロイ

```bash
# 1. 一時ディレクトリ作成
DEPLOY_DIR=$(mktemp -d)

# 2. 最終版 index.html を $DEPLOY_DIR に書き込む

# 3. キャラクター画像をコピー
mkdir -p "$DEPLOY_DIR/images"
cp .claude/skills/diagram-personal/docs/charactor-images/パニっくん-*.png "$DEPLOY_DIR/images/"
cp .claude/skills/diagram-personal/docs/charactor-images/ウパ博士-*.png "$DEPLOY_DIR/images/"

# 4. surge.shにデプロイ
cd "$DEPLOY_DIR" && surge . --domain {ドメイン名}.surge.sh
```

デプロイ完了後、**ユーザーには URL と短い要約**を返す。

---

## 品質チェックリスト

### 必須

- [ ] **`</main>` の直後に**、[references/legal-footer-snippet.html](references/legal-footer-snippet.html) と**同一構造・同一条文**の `<footer role="contentinfo" aria-label="利用条件・著作権">…</footer>` がある（省略・要約・言い換えなし）。`__UPA_LEGAL_OFFICIAL_URL__` / `__UPA_LEGAL_LAST_UPDATED__` が**未置換で残っていない**
- [ ] **表示テキストは原則パニっくん／ウパ博士のセリフのみ**（台本にないナレーション・用語辞典パネル・「まず覚えるN個」を挟んでいない）
- [ ] 用語の説明は**ウパ博士の発話**（または台本で決まった話者）に含めている
- [ ] 台本のラリー順序を崩していない（勝手に章の再構成で中身を差し替えていない）
- [ ] コードや図を置く場合、その直前の文脈が**対話で**つながっている

### デザイン

- [ ] Lucide iconを使用（絵文字禁止）
- [ ] **レイアウト・フォントサイズ・ヘッダー／目次／カード／対話行**が完成見本 `output/ai-daily-report-slack-apr2026/index.html` と同系統（例: `.layout-column`、`.char-stack`＋`.char-avatar`＋`.char-name`、本文は `.bubble-body`、吹き出しスタイルのページスコープなど）
- [ ] **ブランド色・CSS・Lucide の URL**は完成見本ファイルを**そのまま維持**している（[html-structure.md](references/html-structure.md) の説明と食い違う場合は完成見本側が正）
- [ ] **対話の吹き出しに話者別の背景色・色付き枠を付けていない**（白＋中立ボーダーのみ）
- [ ] 最重要の一言・結論は**赤太字**、画面操作の指し示しは**黒太字**で区別し、赤の濫用をしていない
- [ ] **パニっくんは左・ウパ博士は右**（`.char-stack`＋`char-bubble--from-left` / `flex-row-reverse`＋`.char-stack`＋`char-bubble--from-right`）で配置されている
- [ ] **インライン目次**（`.toc-inline`）が **`main` 内の先頭**にあり、本文の `id` とリンクが対応している
- [ ] **長いセリフ**は意味の区切りで `<br>` または同一吹き出し内の複数 `<p>` により改行・段落分けし、スキャンしやすくしている（台本の発話数を勝手に増やしていない）
- [ ] スマホでも読みやすいレスポンシブ対応

---

## 模範解答

- **完成見本（コピー元・ビジュアルの唯一の正本）**: `output/ai-daily-report-slack-apr2026/index.html`
- **利用条件・著作権フッター（条文・マークアップの唯一の正本）**: [references/legal-footer-snippet.html](references/legal-footer-snippet.html)（運用: [references/legal-footer.md](references/legal-footer.md)）
- 構成の型・HTML 断片サンプル → [references/exemplar.md](references/exemplar.md)
- **品質チェックの正本** → この SKILL の [品質チェックリスト](#品質チェックリスト)（[exemplar 側](references/exemplar.md#quality-checklist)は SKILL へのリンクと制作時の**短い要約**のみ。項目の複写はしない）
