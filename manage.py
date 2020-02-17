#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    if sys.argv[-1] == 'dev':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datatau.settings')
    else:
        if sys.argv[-1] != 'prod':
            sys.argv.append('prod')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datatau.settings_prod')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv[:-1])


if __name__ == '__main__':
    main()
