## Development

```bash
git clone git@github.com:amccloud/launchkey-django.git
cd launchkey-django
make virtualenv
source .env/bin/activate
make install-dev
python example/manage.py syncdb
python example/manage.py runserver
```
