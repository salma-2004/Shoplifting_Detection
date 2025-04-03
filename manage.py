#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def execute_tasks():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoplifting_detection.settings')
    try:
        from django.core.management import execute_from_command_line as run_from_cli
    except ImportError as module_error:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from module_error
    run_from_cli(sys.argv)

if __name__ == '__main__':
    execute_tasks()
