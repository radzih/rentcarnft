import os
import django

def setup_django():
    '''Func that allows to use django models in aiogram'''
    os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE', 'admin_panel.admin_panel.settings'
        )
    django.setup()