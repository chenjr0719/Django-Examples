# Django-Examples

A Simple Django Example from Django Girls

**Live Demo:** http://chenjr-jacob.idv.tw:8080/

## What is Django?

**Django** is a powerful and convenient web framework for **Python**.

Its goal is used to develop **database-driven** websites.

According to this goal, it can ease to communicate to the database and manage the database in an easy way.

## About This Examples

The first example is from **Django Girls 學習指南**.

You can find the original content: https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/

Thanks to them **Django Girls**.


The second example is about **POST** and **GET**.

You can find the detail explanation at official docs.

https://docs.djangoproject.com/en/1.9/topics/forms/

## How to Use?

I suggest using **Docker** to create the environment of **Django**.

You can use this **Docker** image: https://github.com/dockerfiles/django-uwsgi-nginx

```$
sudo docker pull dockerfiles/django-uwsgi-nginx
sudo docker run -itd -p 80:80 -v $PROJECT_DIR:/home/docker/code/app/ dockerfiles/django-uwsgi-nginx
```

In default, you don't modify any setting.

But, if you want to use your django project, you have to modify **uwsgi.ini** in the container.

```$
sudo docker exec -it $CONTAINER_ID bash
vi /home/docker/code/uwsgi.ini
```

Modify the setting under **base**.
```$
module=$PROJECT_NAME.wsgi:application
```

After the modification, you have to restart your container.

```$
sudo docker restart $CONTAINER_ID
```

Now, you can check the result at: http://localhost

## TO-DO

This example is quite simple.

Maybe I will add some different features when I have any idea.
