import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
for i in os.environ:
    print(i)
