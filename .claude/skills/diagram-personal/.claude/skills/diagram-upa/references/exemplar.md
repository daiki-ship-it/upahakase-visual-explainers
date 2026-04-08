# 模範解答パターン（台本忠実・対話中心）

## 完成見本（1ファイル全体）

リポジトリルートから **`output/ai-tool-roadmap-apr2026/index.html`** を開く。ヘッダー・`.toc-inline`・`.section-card`・対話行・CSS 変数・Lucide の使い方など、**このリポジトリで目指す図解の実装見本**とする（断片の説明はこのファイルの下に続く）。

---

図解は**パニっくんとウパ博士の会話のラリー**を主コンテンツとする。台本にない「用語解説コーナー」「まず覚える3つ」「ナレーションだけの説明ブロック」は置かない。たとえ話・定義・コードの意味づけは**ウパ博士の吹き出し**（台本の流れに沿って）に含める。

**レイアウトの本質**: 読者が会話を追いやすいよう、**パニっくんは画面左・ウパ博士は画面右**のメッセンジャー風に固定する（見た目の左右が話者と一致する）。あわせて**ヘッダー直後にインライン目次**を置き、長い台本でも「どこに何があるか」を先に示す。

**吹き出しの見た目**: パニっくん・ウパ博士とも**吹き出しに色面（黄・青など）を付けない**。白背景と細い中立ボーダーは共通。**強調は本文中の span** で行う——結論・いちばん伝えたい点は**赤＋太字**（`.bubble-key`）、ボタン名やメニューなどUI上の呼び名は**黒＋太字**（`.bubble-ui`）。詳細は [html-structure.md](html-structure.md) の「吹き出し内の強調」を参照。

## 成功する図解の構造

```
1. ヘッダー（グラデーション背景）
   └─ タイトル + サブタイトル（図解の主題。台本・依頼に合わせる）

2. 冒頭目次（.toc-inline・main 内の先頭）
   └─ 台本の見出し・話の区切りに対応したアンカー一覧
   └─ サブ項目は .toc-sub でインデント（HTML では Lucide「sparkles」など。絵文字は使わない）

3. メイン本文
   └─ 台本順に、パニっくん（左アバター）／ウパ博士（右アバター）の吹き出しを連ねる
   └─ 必要ならその直下にだけ、コード・図・箇条書き（直前のセリフで文脈がつながること）

4. （任意）フローティング目次（.toc）
   └─ デスクトップのみ。セクション数が非常に多い長編だけ、冒頭目次に加えて併用してよい
```

**やらないこと**

- 冒頭にまとめ用の「用語を全部ここで解説」ブロックを置く
- 「まず覚える3つ」など、台本にない優先度リストを新設する
- セクション見出し＋教科書調の本文だけのブロックを、対話の代わりに量産する
- パニっくんとウパ博士の**アバター左右を入れ替える**（メッセンジャー風の一貫性を崩さない）

---

## 冒頭目次（インライン）

台本側に章立て・ランキング・「このあとプロンプト」などの**階層があるときは、HTML の目次にも同じ階層**を反映する。リンク先は対話ブロックや `section` の `id` と一対一で対応させる。

```html
<aside class="toc-inline" aria-label="この記事の目次">
  <h2>
    <i data-lucide="list" class="w-6 h-6 text-[var(--brand-secondary)]"></i>
    目次
  </h2>
  <nav>
    <ol>
      <li><a href="#sec-what">テーマの導入</a></li>
      <li>
        <a href="#sec-rank-3">第3位：〇〇</a>
        <ul class="toc-sub">
          <li>
            <i data-lucide="sparkles" class="w-4 h-4 toc-sub-icon" aria-hidden="true"></i>
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

```html
<section class="section-card" id="sec-hook">
  <!-- パニっくん：左アバター -->
  <div class="flex items-start gap-4 mb-6">
    <img src="./images/パニっくん-疑っている-512×512-透過.png"
         alt="パニっくん" class="w-20 h-20 object-contain flex-shrink-0">
    <div class="char-bubble char-bubble--from-left flex-1">
      <p class="text-lg text-gray-800">「フック」って何ですか？プログラムに釣り針でも刺すんですか？</p>
    </div>
  </div>

  <!-- ウパ博士：右アバター（flex-row-reverse） -->
  <div class="flex flex-row-reverse items-start gap-4 mb-6">
    <img src="./images/ウパ博士-諭す-512×512-透過.png"
         alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
    <div class="char-bubble char-bubble--from-right flex-1">
      <p class="text-lg text-gray-800">
        良い質問ですね、パニさん。フックとは<span class="bubble-ui">「割り込みポイント」</span>のことです。
        会社のセキュリティゲートを想像してください。通る前に止めて確認する——<span class="bubble-key">あれと同じ役割</span>を、プログラムの中で果たします。
      </p>
    </div>
  </div>

  <div class="flex items-start gap-4 mb-6">
    <img src="./images/パニっくん-驚き-512×512-透過.png"
         alt="パニっくん" class="w-20 h-20 object-contain flex-shrink-0">
    <div class="char-bubble char-bubble--from-left flex-1">
      <p class="text-lg text-gray-800">マジ？　つまり、動く前に「ちょっと待って！」って止められるんですね！</p>
    </div>
  </div>
</section>
```

※ キャラ名を吹き出し内に繰り返すかは**台本のスタイル**に合わせる（SKILL・character-usage の例と矛盾しない範囲でよい）。

---

## コードを台本に含める場合

説明は**別カードの「このコードがやること」見出し**ではなく、**ウパ博士のセリフ**にまとめ、その直後にコードを置く。

```html
<div class="flex flex-row-reverse items-start gap-4 mb-4">
  <img src="./images/ウパ博士-標準-512×512-透過.png"
       alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="text-lg text-gray-800">
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

---

## たとえ話を入れる場合

**「たとえ話：〇〇」という教材用の枠**を台本にないのに新設しない。台本にたとえがあるなら、**ウパ博士（または台本の話者）の吹き出し**の中で展開する。

```html
<div class="flex flex-row-reverse items-start gap-4 mb-6">
  <img src="./images/ウパ博士-諭す-512×512-透過.png"
       alt="ウパ博士" class="w-20 h-20 object-contain flex-shrink-0">
  <div class="char-bubble char-bubble--from-right flex-1">
    <p class="text-lg text-gray-800">
      スマホで「カメラへのアクセスを許可しますか？」と出るあれを思い出してください。
      許可する・しないの前に立ち止まる——<span class="bubble-key">それがまさにこの仕組みに近い</span>です。
    </p>
  </div>
</div>
```

---

## 品質チェックリスト

作成後、以下を確認する。

- [ ] 本文の言葉は**台本の対話中心**で、用語辞典パネルや「まず覚える3つ」を勝手に挟んでいない
- [ ] 用語の初出説明は**ウパ博士（等）のセリフ**に含めている
- [ ] コードや図の直前が**対話で**つながっている
- [ ] **ヘッダー直後にインライン目次**（`.toc-inline`）があり、`id`／`href` が対応している
- [ ] **パニっくんは左アバター**（`char-bubble char-bubble--from-left`）、**ウパ博士は右アバター**（`flex-row-reverse` + `char-bubble char-bubble--from-right`）
- [ ] 吹き出しに話者別の色面を付けず、要点は赤太字・UI指し示しは黒太字で足りている
- [ ] Lucide iconのみ使用（絵文字なし）
- [ ] ヘッダー・ナビなどにブランドカラーが適用されている（吹き出し本体の色分けはしない）
- [ ] キャラクター画像のパスが正しい
- [ ] スマホで読みやすい（レスポンシブ）
- [ ] 長編では任意で `.toc`（フローティング）を併用している（なくてもよい）
