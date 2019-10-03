# A minimal example of an LTI provider with Flask + PyLTI

```sh
pipenv install
pipenv run gunicorn minimal_example:app
```

In Moodle, set the consumer key to `lticonsumerkey` and the secret key to `ltisecretkey` when you add an external tool.
