# 自然言語処理学習プロジェクト

## 概要
このプロジェクトは「自然言語処理の基礎」に基づく包括的な学習用プログラム集です。文系学部から理系大学院への進学を目指し、自然言語処理の基礎技術を体系的に学習することを目的としています。

書籍の各章に対応した実装を通じて、以下の技術を段階的に習得します：
- テキスト前処理と正規化
- 形態素解析と分かち書き
- 統計的言語モデル
- 情報検索とランキング
- テキスト分類と機械学習
- 語義曖昧性解消
- 文書要約と情報抽出

## 現在の実装項目

### ジップの法則の検証（3ans.py）
テキスト中の単語の出現頻度とその頻度順位が反比例する関係を検証します。Wikipediaから取得した日本語テキストを用いて、MeCabによる形態素解析を行い、統計的な言語現象を観察します。

### TF-IDF分析（2ans.py）
文書間での単語の重要度を測定するTF-IDF（Term Frequency-Inverse Document Frequency）を実装し、情報検索の基礎技術を学習します。

### 正規表現学習（re_match.py, re_search.py）
テキスト処理の基盤となる正規表現の使用法を学び、パターンマッチングの技術を習得します。

## 参考書籍
本プロジェクトは以下の書籍に基づいて作成されています：
- **書籍名**: 自然言語処理の基礎
- **著者**: [東北大学の岡崎教授など]
- **学習目的**: 理系大学院入試対策および研究基盤構築

## 使用技術
- **Python 3.x**
- **MeCab**: 日本語形態素解析
- **requests**: Wikipedia API通信
- **collections.Counter**: 単語頻度カウント
- **matplotlib**: グラフ描画（予定）
- **re**: 正規表現による数字フィルタリング

## ファイル構成
```
standard_nlp_problem/
├── 1ans.py          # 基礎的なNLP問題
├── 2ans.py          # TF-IDFを使用したテキスト分析
├── 2ans_sub.py      # 2ans.pyのサブモジュール
├── 3ans.py          # ジップの法則検証（メインプログラム）
├── re_match.py      # 正規表現学習用
├── re_search.py     # 正規表現学習用
├── requirements.txt # 必要ライブラリ一覧
├── README.md        # このファイル
└── CLAUDE.md        # Claude Code設定ファイル
```

## セットアップ

### 必要なライブラリのインストール
```bash
pip install -r requirements.txt
```

### MeCabのインストール（必要に応じて）
```bash
# macOS (Homebrew)
brew install mecab mecab-ipadic
pip install mecab-python3

# Ubuntu/Debian
sudo apt-get install mecab mecab-ipadic-utf8 libmecab-dev
pip install mecab-python3
```

## 実行方法

### ジップの法則検証（現在のメインプログラム）
```bash
python 3ans.py
```

### その他のプログラム
```bash
python 2ans.py  # TF-IDF分析
python 1ans.py  # 基礎NLP問題
```

## プログラムの流れ（3ans.py）
1. **データ収集**: Wikipedia APIから日本関連記事を取得
2. **前処理**: テキストの結合と清浄化
3. **形態素解析**: MeCabによる単語分割
4. **フィルタリング**: 名詞のみを抽出、数字を除外
5. **頻度分析**: 単語の出現回数をカウント
6. **可視化**: ジップの法則に従うかグラフで確認（実装予定）

## 学習目的
このプロジェクトは、文系学部から理系大学院への進学を目指す学習の一環として作成されています。自然言語処理の基礎技術習得を目的としています。

## 注意事項
- Wikipedia APIの利用制限を考慮し、リクエスト間隔を調整しています
- 学習・研究目的でのみ使用してください

## 学習進捗と今後の実装予定

### 完了済み
- [x] 基礎的なテキスト処理（1ans.py）
- [x] TF-IDF実装（2ans.py）
- [x] 正規表現学習（re_match.py, re_search.py）
- [x] MeCab形態素解析の基礎（3ans.py）
- [x] Wikipedia API活用

### 進行中
- [ ] ジップの法則のグラフ化
- [ ] 統計的有意性検定

### 今後の実装予定（書籍の章立てに沿って）
- [ ] N-gramモデルの実装
- [ ] 隠れマルコフモデル（HMM）
- [ ] ナイーブベイズ分類器
- [ ] SVM（Support Vector Machine）
- [ ] ニューラル言語モデル
- [ ] Word2Vec/FastText
- [ ] 文書分類システム
- [ ] 情報抽出システム
- [ ] 質問応答システム

### 研究応用目標
- [ ] 学術論文での手法比較
- [ ] オリジナル研究課題の設定
- [ ] 大学院入試対策問題の実装 
