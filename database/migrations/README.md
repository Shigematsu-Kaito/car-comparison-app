# データベースマイグレーション

このディレクトリには、データベーススキーマの変更履歴を管理するマイグレーションスクリプトを配置します。

## ディレクトリ構造

```
migrations/
├── 001_initial_schema.sql
├── 002_add_new_feature.sql
└── ...
```

## マイグレーションの実行

SupabaseのSQLエディタまたはCLIを使用してマイグレーションを実行します。

### Supabase CLIを使用する場合

```bash
supabase migration new <migration_name>
supabase db push
```

### 手動実行の場合

1. Supabaseダッシュボードにログイン
2. SQL Editorを開く
3. マイグレーションファイルの内容をコピー&ペースト
4. 実行

## 注意事項

- マイグレーションは順番に実行されるべきです
- 本番環境に適用する前に、必ずテスト環境で検証してください
