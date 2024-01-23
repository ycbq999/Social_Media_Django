# Creating a New Project
django-admin startproject projectname

# Add an app to the project
django-admin startapp appname



#Add an app to the project
python manage.py startapp appname

# starting the server

python manage.py runserver

# creating Migrations
python manage.py makemigrations

# Migrate the database

python manage.py migrate

# Creating a Super User for the Admin Panel
python manage.py createsuperuser

# Change Any User's Password
python manage.py changepassword username

# Collecting Static Files Into One Folder
python manage.py collectstatic

# name: ycbq999
# admin ps: pass
# for this project only create a database named food
python manage.py sqlmigrate food 0001

python manage.py shell

# >>> from food.models import Item
# >>> Item.objects.all()
# <QuerySet []>
# >>> a = Item(item_name="Pizza", item_desc="Cheesy Pizza",item_price=20)
# >>> a.save()
# >>> a.id
# 1
# >>> a.pk


git add * -f # add all files to git including .gitignore files