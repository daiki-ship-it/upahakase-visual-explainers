# 模範解答パターン（台本忠実・対話中心）

## 参照の優先順位（SSOT）

[SKILL.md](../SKILL.md) の「依存」と同じ解決順を、ここでも短く示す。

1. **唯一のビジュアル正本**: リポジトリの **`output/ai-daily-report-slack-apr2026/index.html`**（必ず複製してから編集する）。
2. **利用条件・著作権フッター（条文・`<footer>` マークアップ）の正本**: [legal-footer-snippet.html](legal-footer-snippet.html)。完成見本のフッターはこれにプレースホルダを埋めたものと一致させる。運用は [legal-footer.md](legal-footer.md)。**条文の要約・削除・言い換えはしない**（[SKILL.md](../SKILL.md#legal-footer-required) の必須フッター節）。
3. **品質チェックの正本**: [SKILL.md](../SKILL.md) の「品質チェックリスト」。チェック項目の列挙は SKILL のみ（このファイル末尾はリンク＋要約のみ）。
4. **説明・断片**: **この exemplar.md** と [html-structure.md](html-structure.md)。構成の型・HTML 断片・Lucide の書き方など。**1〜3 と食い違う具体的な記述**（クラス・余白・数値・検証の解釈）は、**完成見本・snippet および SKILL を優先**する。

## 完成見本（1ファイル全体・ビジュアルのSSOT）

リポジトリルートから **`output/ai-daily-report-slack-apr2026/index.html`** を開く。**テキストの大きさ、配置、色、余白、フォント、ヘッダー、目次、セクションカード、対話行（`.char-stack`／`.bubble-body`）、章見出し、Lucide のサイズ感・読み込み URL、ページ背景、`</main>` 直後の利用条件・著作権フッター、`</body>` 直前の吹き出し用 CSS**など、**これから作る図解の見た目はすべてこのファイルに合わせる**（新規はこの HTML を複製して中身だけ差し替えるのが最短。断片の説明はこのファイルの下に続く）。フッターの条文・構造の**編集正本**は [legal-footer-snippet.html](legal-footer-snippet.html)（完成見本は展開済みの参照実装）。

**レイアウトの要点（完成見本に実装済み）**

- **中央の狭いカラム**: `body` 直下のヘッダーと `main` は `.layout-column` で max-width を抑え、スマホ縦読みに近い幅に統一する。
- **ページ背景**: 完成見本どおり、グラデーション地＋必要ならページ用クラスで吹き出し用 CSS をスコープする（Tailwind CDN との詳細は完成見本の `</body>` 直前コメント参照）。
- **ヘッダー**: タイトルはコンパクト（例: `text-base md:text-lg`）。旧見本の特大見出し＋サブタイトル行に自動で戻さない。
- **章立て**: 大見出しは `main` 直下の `.body-chapter-heading`（左赤ライン）、その下に `.section-card` で対話ブロックを包むパターンが完成見本の型。
- **対話行**: アバターは `.char-stack`（`.char-stack--panik` / `.char-stack--upa`）で縦積みし、`.char-avatar`（幅は完成見本の CSS に従う）とその下に `.char-name` の実テキスト。吹き出し内の本文は **`.bubble-body`**（`text-lg` 直書きにしない）。行間は `mb-6` ではなく完成見本に合わせる（例: `mb-8`）。
- **Lucide**: 完成見本と同じバージョンを読み込む（例: `lucide@0.469.0`）。目次見出しアイコンは `w-4 h-4`、`.toc-sub` 内は `w-3.5 h-3.5` など、完成見本のクラスに揃える。

---

図解は**パニっくんとウパ博士の会話のラリー**を主コンテンツとする。台本にない「用語解説コーナー」「まず覚える3つ」「ナレーションだけの説明ブロック」は置かない。たとえ話・定義・コードの意味づけは**ウパ博士の吹き出し**（台本の流れに沿って）に含める。

**レイアウトの本質**: 読者が会話を追いやすいよう、**パニっくんは画面左・ウパ博士は画面右**のメッセンジャー風に固定する（見た目の左右が話者と一致する）。あわせて **`main` 内の先頭**にインライン目次（`.toc-inline`）を置き、読み順ではヘッダーの直後に相当する位置で、長い台本でも「どこに何があるか」を先に示す（`</header>` と `<main>` の間には置かない。完成見本どおり）。

**吹き出しの見た目**: パニっくん・ウパ博士とも**吹き出しに色面（黄・青など）を付けない**。白背景と細い中立ボーダーは共通。**強調は本文中の span** で行う——結論・いちばん伝えたい点は**赤＋太字**（`.bubble-key`）、ボタン名やメニューなどUI上の呼び名は**黒＋太字**（`.bubble-ui`）。詳細は [html-structure.md](html-structure.md) の「吹き出し内の強調」を参照（数値・クラス名は完成見本が優先）。

## 成功する図解の構造

```
1. ヘッダー（グラデーション背景・layout-column 内）
   └─ タイトル（コンパクト。サブタイトルは台本・依頼に応じて任意）

2. 冒頭目次（.toc-inline・main 内の先頭・layout-column 内）
   └─ 台本の見出し・話の区切りに対応したアンカー一覧
   └─ サブ項目は .toc-sub でインデント（Lucide「sparkles」など。絵文字は使わない）
   └─ 台本に章立てがほぼない短い図解では、**「導入／本題／まとめ」など最小3項目**にとどめてよい（SKILL ワークフローと同じ）

3. メイン本文
   └─ （任意）章見出し .body-chapter-heading + id
   └─ .section-card 内に、台本順でパニっくん（左）／ウパ博士（右）の吹き出しを連ねる
   └─ 必要ならその直下にだけ、コード・図・箇条書き（直前のセリフで文脈がつながること）

4. 利用条件・著作権（必須）
   └─ `</main>` の直後に `<footer role="contentinfo" aria-label="利用条件・著作権">…</footer>` を置く（条文・マークアップは [legal-footer-snippet.html](legal-footer-snippet.html) をそのまま。URL・最終更新日のみ資料ごとに置換）。**削除・要約・独自改変は禁止**。漫画風派生版のみ [legal-footer.md](legal-footer.md) のオプション1段落を追加可。

5. （参考・任意）フローティング目次（`.toc` など）
   └─ **現行の完成見本 HTML には含まれていない**。デフォルトは手順 2 の `.toc-inline` のみとする。セクション数が極端に多い長編で、チーム内に別途合意したマークアップがある場合のみ、デスクトップ向けに併用を検討してよい（新規に足すときは完成見本の CSS・トーンと矛盾しないよう、[html-structure.md](html-structure.md) や既存図解の近いパーツに合わせる）
```

**やらないこと**

- 冒頭にまとめ用の「用語を全部ここで解説」ブロックを置く
- 「まず覚える3つ」など、台本にない優先度リストを新設する
- セクション見出し＋教科書調の本文だけのブロックを、対話の代わりに量産する
- パニっくんとウパ博士の**アバター左右を入れ替える**（メッセンジャー風の一貫性を崩さない）
- **旧完成見本**（`output/ai-tool-roadmap-apr2026/` など）の太い max-width・大きい見出し・異なるブランド色に**勝手に戻す**
- **利用条件・著作権**の `<footer>` を削除する、条文を要約・言い換えする、正本（[legal-footer-snippet.html](legal-footer-snippet.html)）にない文を足す（漫画派生の [legal-footer.md](legal-footer.md) 所定の1段落を除く）

---

## 冒頭目次（インライン）

台本側に章立て・ランキング・「このあとプロンプト」などの**階層があるときは、HTML の目次にも同じ階層**を反映する。リンク先は対話ブロックや `section` の `id` と一対一で対応させる。**アイコンサイズ・フォントサイズは完成見本の `.toc-inline` に合わせる。**

```html
<aside class="toc-inline" aria-label="この記事の目次">
  <h2>
    <i data-lucide="list" class="w-4 h-4 text-[var(--brand-secondary)]" aria-hidden="true"></i>
    目次
  </h2>
  <nav>
    <ol>
      <li><a href="#sec-what">テーマの導入</a></li>
      <li>
        <a href="#sec-rank-3">第3位：〇〇</a>
        <ul class="toc-sub">
          <li>
            <i data-lucide="sparkles" class="w-3.5 h-3.5 toc-sub-icon" aria-hidden="true"></i>
            <a href="#sec-rank-3-prompt">〇〇用プロンプト例</a>
          </li>
        </ul>
      </li>
      <li><a href="#sec-summary">まとめ</a></li>
    </ol>
  </nav>
</aside>
```

---

## 対話の連なり（基本形）

**アバター＋名前＋`.bubble-body` は完成見本と同一パターンにする。**

```html
<section class="section-card" id="sec-hook">
  <!-- パニっくん：左アバター -->
  <div class="flex items-start gap-4 mb-8">
    <div class="char-stack char-stack--panik">
      <img src="./images/パニっくん-疑っている-512×512-透過.png" alt="パニっくん" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
      <p class="char-name">パニっくん</p>
    </div>
    <div class="char-bubble char-bubble--from-left flex-1">
      <p class="bubble-body">「フック」って何ですか？プログラムに釣り針でも刺すんですか？</p>
    </div>
  </div>

  <!-- ウパ博士：右アバター（flex-row-reverse） -->
  <div class="flex flex-row-reverse items-start gap-4 mb-8">
    <div class="char-stack char-stack--upa">
      <img src="./images/ウパ博士-諭す-512×512-透過.png" alt="ウパ博士" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
      <p class="char-name">ウパ博士</p>
    </div>
    <div class="char-bubble char-bubble--from-right flex-1">
      <p class="bubble-body">
        良い質問ですね、パニさん。フックとは<span class="bubble-ui">「割り込みポイント」</span>のことです。
        会社のセキュリティゲートを想像してください。通る前に止めて確認する——<span class="bubble-key">あれと同じ役割</span>を、プログラムの中で果たします。
      </p>
    </div>
  </div>

  <div class="flex items-start gap-4 mb-8">
    <div class="char-stack char-stack--panik">
      <img src="./images/パニっくん-驚き-512×512-透過.png" alt="パニっくん" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
      <p class="char-name">パニっくん</p>
    </div>
    <div class="char-bubble char-bubble--from-left flex-1">
      <p class="bubble-body">マジ？　つまり、動く前に「ちょっと待って！」って止められるんですね！</p>
    </div>
  </div>
</section>
```

※ キャラ名を吹き出し内に繰り返すかは**台本のスタイル**に合わせる（SKILL・character-usage の例と矛盾しない範囲でよい）。

---

## コードを台本に含める場合

説明は**別カードの「このコードがやること」見出し**ではなく、**ウパ博士のセリフ**にまとめ、その直後にコードを置く。

```html
<div class="flex flex-row-reverse items-start gap-4 mb-8">
  <div class="char-stack char-stack--upa">
    <img src="./images/ウパ博士-標準-512×512-透過.png" alt="ウパ博士" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
    <p class="char-name">ウパ博士</p>
  </div>
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="bubble-body">
      たとえばこう書きます。<span class="bubble-ui">Write</span>ツール——ファイルを書き込む道具——が使われそうになったら、
      <span class="bubble-key">許可しない</span>と返すルールです。
    </p>
  </div>
</div>
<div class="code-block">
  <pre><code>hook.onPreToolUse((event) => {
  if (event.toolName === 'Write') {
    return { permissionDecision: 'deny' };
  }
});</code></pre>
</div>
```

（`.code-block` の見た目が完成見本の `.script-prompt-block` 等と異なる場合は、**台本にコード／プロンプトのどちらが近いか**で完成見本側の近いパーツを選ぶ。上記の `mb-8` は対話行の行間の例であり、完成見本の当該箇所と異なる場合は**完成見本を優先**する。）

---

## たとえ話を入れる場合

**「たとえ話：〇〇」という教材用の枠**を台本にないのに新設しない。台本にたとえがあるなら、**ウパ博士（または台本の話者）の吹き出し**の中で展開する。

```html
<div class="flex flex-row-reverse items-start gap-4 mb-8">
  <div class="char-stack char-stack--upa">
    <img src="./images/ウパ博士-諭す-512×512-透過.png" alt="ウパ博士" class="char-avatar" width="80" height="80" loading="lazy" decoding="async">
    <p class="char-name">ウパ博士</p>
  </div>
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="bubble-body">
      スマホで「カメラへのアクセスを許可しますか？」と出るあれを思い出してください。
      許可する・しないの前に立ち止まる——<span class="bubble-key">それがまさにこの仕組みに近い</span>です。
    </p>
  </div>
</div>
```

---

<a id="quality-checklist"></a>

## 品質チェックリスト

**正本は [SKILL.md](../SKILL.md) の「品質チェックリスト」**に移した。図解完成後はそちらを**すべて**確認する。

**制作時の心がけ（要約・SKILL にない代替チェックリストではない）**: 完成見本を複製したまま CSS 順序（Tailwind CDN と `</body>` 直前の吹き出し用スタイルの順）を保つこと。見た目は `output/ai-daily-report-slack-apr2026/index.html` と同系統であること。旧完成見本（`ai-tool-roadmap-apr2026`）のレイアウトに戻さないこと。**`</main>` 直後の利用条件・著作権フッター**は [legal-footer-snippet.html](legal-footer-snippet.html) と一致させ、プレースホルダを残さないこと。
