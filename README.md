# Django-Examples

A Simple Django Example from Django Girls

**Live Demo:** http://chenjr-jacob.idv.tw:8080/

## What is Django?

**Django** is a powerful and convenient web framework for **Python**.

It's goal is used to develop **database-driven** websites.

According to this goal, it can ease to communicate to the database and manage the database in an easy way.

## About This Examples

The example is from **Django Girls 學習指南**.

You can find the original ceontent: https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/

Thanks to them **Django Girls**.

## How to Use?

I suggest to use **Docker** to create the environment of **Django**.

You can use this **Docker** image: https://github.com/dockerfiles/django-uwsgi-nginx

```$
sudo docker pull dockerfiles/django-uwsgi-nginx
sudo docker run -itd -p 80:80 -v $APP_DIR:/home/docker/code/app/ dockerfiles/django-uwsgi-nginx
```

Then, you have to modify **uwsgi.ini** in container.

```$
sudo docker exec -it $CONTAINER_ID bash
vi /home/docker/code/uwsgi.ini
```

Modify the setting under **base**.
```$
module=$APP_NAME.wsgi:application
```

After the modification, you have to restart you container.

```$
sudo docker restart $CONTAINER_ID
```

Now, you can check the result at: http://localhost
