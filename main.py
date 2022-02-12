#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import fs_operations

    root = open('root_path.txt', 'r').read()
    list_dirs = fs_operations.get_top_level_folder_names_for_current_path(root)
    with open('versions_to_save.txt', 'r') as f:
        saved_version_list = f.readlines()
        for v in saved_version_list:
            list_dirs.remove(v)

    for directory in list_dirs:
        fs_operations.delete_current_folder(root + '/' + directory)

    report_string = ''
    for e in list_dirs:
        report_string = report_string + '\n' + e

    with open('./log.txt', 'w') as log:
        log.writelines(report_string)


if __name__ == '__main__':
    main()
