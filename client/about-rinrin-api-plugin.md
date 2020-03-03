# rinrin-apiプラグインドキュメント

## 使用方法
  Vueのインスタンス内で使用する

### POST

#### 基本的な使用方法

```javascript
this.$postApi([path], {deta})
```

例) 

```javascript
this.$postApi('/test', {name:'this is post test'})
```



#### オプション

トークンに手動で取得したものを使用する

```javascript
this.$postApi([path], {deta}, false, [token])
```

例) 

```javascript
let testToken = 'token string'
this.$postApi('/test', {name:'this is post test'}, false, testToken)
```



### GET

#### 基本的な使用方法

```javascript
this.$getApi([path], {deta})
```

例) 

```javascript
this.$getApi('/test', {name:'this is get test'})
```



#### オプション

トークンに手動で取得したものを使用する

```javascript
this.$getApi([path], {deta}, false, [token])
```

例) 

```javascript
let testToken = 'token string'
this.$getApi('/test', {name:'this is get test'}, false, testToken)
```



## 内部の動作

本体は client/src/plugins/rinrin-api.js

client/src/main.jsでimort  Vue.useすることで全てのインタンスで使用可能にしている

### rinrin-api.jsの動作

Get, Post両方のメソッドは基本的に現在同じ動作

1. tokenを新たに取得するかのフラグを確認（デフォルトはTrue）
   1. Tokenを取得するフラグがTrueであれば、Firebaseにアクセスし、Tokenを取得
   2. Tokenを取得するフラグがFalseであれば、引数のTokenを使用
2. ヘッダーを作成
3. 引数のパスに対してリクエストを送る

