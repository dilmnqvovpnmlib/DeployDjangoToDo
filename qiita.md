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

#### GitHub Actions の導入

- working-directory では相対パスで ../actions-milestone とかはできない。あくまで相対パスは\$GITHUB_WORKSPACE の配下
- [業務で GitHubActions を取り入れる上で苦労した点](https://qiita.com/iyu/items/87a6f255bc7e5beb9a40)

#### Todo 一覧

- 一覧表示
- 詳細ページへ飛ばす
- [ManyToMany フィルターなどのオブジェクト操作一覧](https://djangobrothers.com/blogs/many_to_many_objects/)

#### Todo 詳細

- 編集画面
- [Django DetailView で詳細画面を作成](https://noumenon-th.net/programming/2019/11/16/django-detailview/)

#### Todo 削除機能

一覧画面、詳細画面と同様に CCBV の`DeleteView`を確認する。
削除の処理をするにあたって、経る過程としては、`GETメソッドで`削除の確認画面に遷移する。
その後、削除確認画面から`POSTメソッド`を呼び出すことで、対象のオブジェクトを削除することができる。

これらを踏まえて、まず、URL を設定する。削除対象は一意に決まるので、`<int:pk>`が必要なのが直感的にもわかるが、ソースコード的には、`get_object`が肝である。`get_object`の`pk = self.kwargs.get(self.pk_url_kwarg)`から、`pk`を取得していると考えられる。従って、`<int:pk>`を含めて DeleteView を呼び出すような URL を作成する。

削除確認画面で表示する HTML は`template_name_suffix = '_confirm_delete'`にもあるように、`app名/model名_confirm_delete.html`のテンプレートを配置しておくと自動的に呼び出される。

削除確認画面から、削除するには、`POSTメソッド`を呼び出す必要がある。なぜなら、CCDV の`post`を見ると、その内部で`delete`を呼び出すような実装になっているからである。

```python
def post(self, request, *args, **kwargs):
    return self.delete(request, *args, **kwargs)
```

従来の実装のままでは、`delete`メソッドを呼び出すと、物理削除をするので、論理削除に変更するために、DeleteView で`delete`メソッドをオーバーライドするようにメソッドを修正する。

- success_url がないと怒られる
- [【Django】「No URL to redirect to. Either provide a url or define a get_absolute_url method on the Model.」の対処](https://remonote.jp/django-no-url-to-redirect-to)
- `python manage.py shell`で ManyToMany のフィールドのあるデータを作成しようとすると、注意が必要
- [Many-to-many relationships](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/)
- [Django DeleteView で削除確認画面を作成](https://noumenon-th.net/programming/2019/11/20/django-deleteview/)
- [Django の CRUD ジェネリックビュー (ListView, DetailView, CreateView, UpdateView, DeleteView) の簡単な使い方](https://tech.torico-corp.com/blog/django-crud-generic-view/)

#### Todo 新規登録

- 新規登録フォーム
- [Django、フォームセットでの commit=False の注意点](https://narito.ninja/blog/detail/37/)
- ModelForm の save()と Model の save()の違いについて
- [Creating forms from models](https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/)
- [Django で view から Form オブジェクトに値を渡す : kwargs 活用](https://hideharaaws.hatenablog.com/entry/2017/02/05/021111)
- save()のオーバーライドについて
- [The save() method](https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method)
- [source code of save() method](https://github.com/django/django/blob/3b1cb78063466e996cbb042e44aadfac30df73fa/django/forms/models.py#L445)

- [Django の Form(CreateView、UpdateView など)について](https://qiita.com/felyce/items/5042db0792c9f7d01c1e#createview-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%B8%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B)
- [get_form_kwargs()](https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form_kwargs)
- [Python の super() 関数の使い方](https://www.lifewithpython.com/2014/01/python-super-function.html?m=1)

#### ToDo 編集

- url と UpdateView を継承させた View を作成するだけ

#### Tag 一覧

- 一覧表示
- 詳細ページへ飛ばす

#### Tag 詳細

- 編集画面
- 削除機能

#### Tag 新規登録

- 新規登録フォーム

#### Deploy

- ベースとして必要な知識は[DeployFlask](https://github.com/dilmnqvovpnmlib/DeployFlask)と[DeployDjango](https://github.com/dilmnqvovpnmlib/DeployDjango)を参考にする。
- settings.py の`INSTALLED_APPS`には、きちんと startapp で作成したアプリの設定はしておく。
-
- 最終的に足りていなかったのは、uwsgi.ini の module に`:application`を記述する必要があった。

- [Django, uwsgi and nginx - Internal Server Error](https://stackoverrun.com/ja/q/8294189)
- uwsgi のプロセスとスレッド数を決める際に参考になる
- [Python+uWSGI+Docker で環境に応じて uwsgi プロセス/スレッド数を動的変更する](https://qiita.com/muff1225/items/40141e4661411ca1bc7b)

#### 気になった点を解消と今後の課題

- [【初心者チュートリアル】Django2 でブログ作成（Part12）〜get_absolute_url()～](https://marsquai.com/745ca65e-e38b-4a8e-8d59-55421be50f7e/05f253f8-c11b-4c91-8091-989eb2600a7b/2a7b42c6-3048-4754-8d0c-0101d16afeec/)

```
DjangoではModelにはそのModelの詳細ページのURLを返すget_absolute_url()というメソッドを定義することが推奨されています。
1.URLパラメータの変更に強い

今回のPartではview関数がurlから受け取るパラメータをidからuuidに変更しました。実際にwebサイトを作っていく際にはこのような変更は何度も体験するでしょう。その時{% url %}タグでurlを定義していると、そのurlを毎回変更しなくてはいけません。
実際には同じurlの定義を同一ページ内で何度も使ったりする（最新記事一覧とか、関連記事一覧とか同じページにあるよね？）ため、変更のたびに大きな労力を使う事になるでしょう。
その点HTMLのurlもget_absolute_urlを使っておけば、urls.pyとmodelのget_absolute_url()関数の内部の処理の変更だけすればOKです。
2.HTMLをより簡素にできる

HTMLはただでさえ複雑になりがちです。特にDjangoのテンプレート言語を使っていると余計ややこしくなるでしょう。Python側でまとめられる処理はそちらに書いてしまえるほうが確かに良さそうですね
3.同じtemplateを使いまわせる

例えば以下の様なtemplateがあったとしましょう。
```

- context_object_name
- [The Django template language: for Python programmers](https://docs.djangoproject.com/en/3.0/ref/templates/api/)

- [Python クラスについて](https://qiita.com/motoki1990/items/376fc1d1f3d59c960f5c)

- context_object_name とも関係するが、CCBV を読み込みたい
- パスワードリセット機能の作成
- href="{% url 'todoapp:create' %}"

#### その他

自動デプロイ系統

- [GitHub への push 時に自動デプロイする方法まとめ](https://qiita.com/taka-tactical/items/7ce5ea6e6d2430f20166)
- [GitHub Webhooks で自動デプロイ](https://www.blog.danishi.net/2019/05/22/post-1195/)
- [GitHub Actions を用いて issue が更新されたら LINE に通知する方法](https://qiita.com/osakiy/items/dd77a31bf25d27dd0679)

#### 今後読みたい記事

- Django Advent Calender 2019
- [DjangoBrothers BLOG](https://djangobrothers.com/blogs/)
