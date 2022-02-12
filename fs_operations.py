#!/usr/bin/env python
# -*- coding: utf-8 -*-

def delete_current_folder(folder_path):
    import os

    # Remove the folder by walking through the files (from the bottom up):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(folder_path)


def get_top_level_folder_names_for_current_path(root_path):
    import os

    return os.listdir(root_path)
