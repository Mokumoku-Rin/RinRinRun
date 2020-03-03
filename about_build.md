# ビルド方法について

## Dockerイメージの作成

このプロジェクトではDockerを使用して開発を行っています．Dockerで開発環境を作成するには，まず，Dockerイメージの作成が必要です．このリポジトリで必要となるイメージの作成はプロジェクトのルートディレクトリ直下で次のコマンドを入力することで作成することができます．

```shell
$ docker-compose build
```

### イメージの確認

イメージのビルドに成功したかどうかは`docker image ls`で確認できます．

```shell
$ docker image ls | grep rinrin
rinrinrun_vue           latest              52d8f155963c        9 minutes ago       375MB
rinrinrun_python        latest              939b54fae244        11 minutes ago      118MB
```

2020年3月3日現在は，`rinrinrun_vue`と`rinrinrun_python`が確認できれば成功です．

## クライアントのDockerイメージについて

クライアントのイメージのビルドでは，npmのパッケージのインストールを行っています．具体的には，以下の処理が行われています．

1. 作業ディレクトリを`/app`に設定する．
2. `$project_root/client/src`の`package*.json`をイメージ内の`/app`にコピーする．
3. npmのパッケージ`http-server`をインストールする．
4. コピーしてきた`package*.json`をもとに，npmのパッケージをイメージの`/app/node_modules`内にインストールする．
5. 起動コマンドとして`npm run server`を指定する．

ここで注意していただきたいことは，`node_modules`は`$project_root/client/src`内に保存・同期を行っていないことです．その代わりに，名前付きボリュームを使用して`node_modules`を管理しています．