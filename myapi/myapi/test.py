import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")


import django
if django.VERSION >= (1,7):
    django.setup()

if __name__ == '__main__':
    from hotlist.models import Website
    Website.objects.all().delete()
    print("clear done")