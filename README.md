Membuat RESTful API & JWT Auth
------------------------------
- Flask Microframework python
- SqlAlchemy ORM python

## Installation

  1. Install requirements
    ```
    pip install -r requirements.txt
    ```

  2. Copy file .**env.example** to **.env** dan sesuaikan configurasinya
    ```
    DATABASE_URI=postgresql+psycopg2://postgres:root@localhost/dbname
    SECRET_KEY=31c2tfrdjyfuyh7rb5645wv4355gr6h8
    DEBUG=True
    ```
  3. Migrate database dengan perintah di bawah
    ```
    ~$ python manage.py db init
    ~$ python manage.py db migrate -m "first migrate"
    ~$ python manage.py db upgrade 
    ```
  4. Jalankan aplikasi
    ```
    python server.py
    ```


## Struktur folder
```
|   .env (Environtment)
|   manage.py (Manage version database &  migration database )
|   server.py (Run server debug / untuk Wsgi server porduction)
|   
+---api
|   |   application.py (Initial flask app)
|   |   config.py (Config file flask)
|   |   
|   +---base
|   |   |   repository.py (Base repository )
|   |   |   response.py (Base response)
|   |   |   transformer.py (Untuk transformer / conveter data)
|   |   |   __init__.py (Loader)
|   |   |
|   +---models (Folder Models atau schema database)
|   |   |   posts.py
|   |   |   users.py
|   |   |   
|   +---v1 (Folder versioning api)
|   |   |   api.py (Dafta router api)
|   |   |   
|   |   +---controllers (Folder untuk controllers / action resource)
|   |   |   |   auth.py
|   |   |   |   posts.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   +---middlewares (Folder untuk middlewares)
|   |   |       ResponseMiddleware.py
|   |   |       
|   |   +---repository (Folder untuk repository )
|   |   |   |   posts.py
|   |   |   |   users.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   +---validators (Untuk validators data request response)
```
        
