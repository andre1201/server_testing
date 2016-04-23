#!/usr/bin/env python
# coding=utf-8
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_config.settings")

    # DJANGO_DEBUG_MODE = True - develop setting and DEBUG = True
    # DJANGO_DEBUG_MODE = False - production setting and DEBUG = False
    os.environ.setdefault("DJANGO_DEBUG_MODE", "True")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
