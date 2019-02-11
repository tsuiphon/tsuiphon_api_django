## セットアップ
```
mkdir tsuiphon_project
cd tsuiphon_project
virtualenv --python=/usr/local/bin/python3 --no-site-packages env
source env/bin/activate
git clone https://github.com/tsuiphon/tsuiphon_api_django.git
pip install -r tsuiphon_api_django/requirements.txt
cp tsuiphon_api_django/tsuiphon_api_django/default_secret.json tsuiphon_api_django/tsuiphon_api_django/secret.json
```

```
vi tsuiphon_api_django/tsuiphon_api_django/secret.json
```

secret.jsonを編集。

- consumer keyとconsumer secretを設定。
- django_secretは予測不可能なランダムな文字列を設定。

```
cd tsuiphon_api_django
python manage.py migrate
```

## 起動方法
python manage.py runserver
