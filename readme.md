# Web Application for Deepfake Detection

### Running Project Locally 
First clone the repository to your local
```bash
git clone https://github.com/Uttirna/DetectFake_WebApp.git
```
Install the requirements:

```bash
pip install -r requirements.txt
```

Make Migrations

```bash
python manage.py makemigrations
```

Create the database:

```bash
python manage.py migrate
```
Finally, run the development server:

```bash
python manage.py runserver
```
The project will be available at **127.0.0.1:8000**.

## ScreenShots  
Processing page
---
![](Screenshots/homepage.png)

Home page
---
![](Screenshots/intermediate.png)

Result- if real 
---
![](Screenshots/Result_Real.png)

Result- if fake
---
![](Screenshots/Result_Real.png)

