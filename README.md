## Alert

This project is a __work in progress__ and not complete by any means. If you would like to assist in completion
of this project, please feel free to fork and submit pull requests.


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

This project is based on the initial work of [Andrew McCloud](https://github.com/amccloud).