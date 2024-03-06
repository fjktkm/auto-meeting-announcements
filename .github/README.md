# 部会

部会の連絡事項を管理するリポジトリです．
部会に合わせて自動で Discord にメッセージを送信する機能があります．

## 編集方法

部会の連絡事項の記入は，以下の要領で実施してください．

- リポジトリを開く
  - ローカルにクローンしてもよいですが，マークダウンファイルを編集するだけなので github.dev を利用すると便利です
  - github.dev は GitHub のリポジトリのページで `.` を押下すれば利用できます
- src/YYYY/MM/DD/ に `meeting.md` というファイルがあるのでそれを開く
- `meeting.md` をマークダウン形式で編集する
  - [Discord が対応しているマークダウン記法](https://support.discord.com/hc/ja/articles/210298617)
- コミット & プッシュ する

## CI/CD の内容

ワークフローは以下のように設定してあります：

- `Release` ワークフロー
  - 毎日 12:00 に実行
  - もしその日に対応するディレクトリに `meeting.md` が存在したら以下の処理を実行
    - GitHub Releases に公開
    - Discord に送信
- `Add Next Weekly Meeting` ワークフロー
  - 毎週水曜日 12:00 に実行
  - 毎週の部会用のテンプレートを作成

これにより，以下のように柔軟な運用が可能になります：

- 不定期で連絡したいことが発生したときは，その日に応じたディレクトリを作成すればよい
- 部会のスケジュールが変わったときは，`Add Next Weekly Meeting` ワークフローのみを変更すればよい

メッセージを送信するチャンネルは，GitHub の Actions secrets を参照しています．