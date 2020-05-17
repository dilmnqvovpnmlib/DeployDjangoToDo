## Django の CCBV でアプリケーションを作成する

#### templates について

- View から読み込ませるテンプレートのディレクトリについて参考になった記事
- [【Django】templates フォルダを任意の場所に設置する](https://canon1ky.hatenablog.com/entry/2018/12/02/190253)

#### 手順について

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

#### SignUp(ユーザーの新規登録)機能の作成

- [django で簡単なユーザー登録の実装](https://qiita.com/hayata-yamamoto/items/00072091caa5921fc819)
- [Django で base.html を用いたブログを作成する。](https://qiita.com/k7daiki/items/59ed1d5fc91c639e2284)

#### VSCode の設定

- [Unibeautify](https://github.com/Unibeautify/vscode)をインストールした。

#### Login 機能の作成

- [How to log a user in](https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-in)
- [Django2 でユーザー認証（ログイン認証）を実装するチュートリアル -2- サインアップとログイン・ログアウト](https://it-engineer-lab.com/archives/544)
- [Django の認証システムを使用する](https://docs.djangoproject.com/ja/2.0/topics/auth/default/#all-authentication-views)

#### モデルの作成

- settings.py の INSTALLED_APPS に追加したアプリケーションを書かないと、python manage.py makemigrations に認識されない。
- [Django、on_delete を使う(2.0 から必須) ](https://narito.ninja/blog/detail/73/)

#### Bootstrap の導入

- 公式の Introduction に記載されている CDN を使用
- [Bootstrap4](https://getbootstrap.com/)

- [Django のログインフォームで簡単 Bootstrap](https://qiita.com/ShortArrow/items/d5aa536feb12296b1b30)

#### Todo 一覧

- 一覧表示
- 詳細ページへ飛ばす

#### Todo 詳細

- 編集画面
- 削除機能

#### Tag 新規登録

- 新規登録フォーム

#### Tag 一覧

- 一覧表示
- 詳細ページへ飛ばす

#### Tag 詳細

- 編集画面
- 削除機能

#### Tag 新規登録

- 新規登録フォーム

#### 今後の課題

- パスワードリセット機能の作成
- href="{% url 'todoapp:create' %}"

#### 今後読みたい記事

- Django Advent Calender 2019
