=====
Django Two Factor Face Authentication
=====

Django Two Factor Face Auth is authentication module which provides an extra layer of security using Face recognition. Module provides both backend and frontend code needed for registering and logging user with face detection and recognition.

Built using `face_recognition <https://github.com/ageitgey/face_recognition>`__ and `dlib <http://dlib.net/>`__'s state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark.

Quick start
-----------

1. Add "django-two-factor-face-auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_two_factor_face_auth',
    ]

2. Include the django-two-factor-face-auth URLconf in your project urls.py like this::

    path('/', include('django_two_factor_face_auth.urls')),

3. Run ``python manage.py migrate`` to create the django-two-factor-face-auth models.

4. You are now able to start server and access ``accounts/register`` (to create new account with face id) and ``accounts/login`` urls (to login using username/password and face id)

5. Read detailed documentation to override default templates and configure app properly

Quick start
-----------
The project is licensed under the MIT license.