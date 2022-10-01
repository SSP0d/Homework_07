from data import IMAGE, VIDEO, DOCUMENT, MUSIC, ARCHIVES, MAP_CHARS
import sys
from os import path, makedirs, replace, rename, rename, remove, listdir, rmdir
import shutil


def main():
    sorting_dir(user_path)
    check_clear_dir(user_path)
    print("Done")


# Забрать параметры запуска
def get_path_name():
    user_path = ''
    args = sys.argv
    if len(args) == 1:
        user_path = input('Enter path to directory: ')
    else:
        user_path = args[1]
    while True:
        if not path.exists(user_path):
            if user_path:
                print(f'{user_path} is not exist')
            user_path = input('Enter path to directory: ')
        else:
            if path.isdir(user_path):
                break
            else:
                print(f'{user_path} is not a directory')
                user_path = ''
    return user_path


# Пути директорий
def is_free_dir(namedir):
    user_path
    lists_free_dir = (
        path.join(user_path, 'images'),
        path.join(user_path, 'video'),
        path.join(user_path, 'documents'),
        path.join(user_path, 'audio'),
        path.join(user_path, 'archives'),
    )
    return namedir in lists_free_dir


# Проверка расширений файлов
def check_file_type(file):
    file_name_arr = file.split('.')
    file_ext = ''
    if len(file_name_arr) > 1:
        file_ext = file_name_arr[-1]
    if not file_ext:
        return None
    else:
        if file_ext in IMAGE:  # ('jpeg', 'png', 'jpg', 'svg'):
            return 'images'
        elif file_ext in VIDEO:  # ('avi', 'mp4', 'mov', 'mkv'):
            return 'video'
        # ('doc', 'docx', 'txt', 'pdf', 'xls', 'xlsx', 'pptx'):
        elif file_ext in DOCUMENT:
            return 'documents'
        elif file_ext in MUSIC:  # ('mp3', 'ogg', 'mov', 'amr'):
            return 'audio'
        elif file_ext in ARCHIVES:  # ('zip', 'gz', 'tar'):
            return 'archives'
        else:
            return None


# Переименвание + распаковка архвов
def rename_file(folder_to, folder_from, file):
    user_path
    path_to = path.join(user_path, folder_to)
    if not path.exists(path_to):
        makedirs(path_to)
    if folder_to != 'archives':
        try:
            rename(path.join(folder_from, file),
                   path.join(path_to, normalize(file)))
        except FileExistsError:
            print(f'File {file} is already exist')
            while True:
                is_rewrite = input(
                    f'Do you want to rewrite file {file} (y/n)').lower()
                if is_rewrite == 'y':
                    replace(path.join(folder_from, file),
                            path.join(path_to, normalize(file)))
                    break
                elif is_rewrite == 'n':
                    rename(path.join(folder_from, file),
                           path.join(path_to, normalize(file, True)))
                    break

    else:
        f = normalize(file).split('.')
        try:
            shutil.unpack_archive(path.join(folder_from, file),
                                  path.join(path_to, f[0]), f[1])
        except shutil.ReadError or shutil.ValueError:
            print(f"Archive {path.join(folder_from, file)} can't be unpack")
        else:
            remove(path.join(folder_from, file))


def normalize(file, is_copy=False):

    lists = file.split('.')
    name_file = '.'.join(lists[0:-1])
    new_name = ''
    for el in name_file:
        if el in MAP_CHARS:
            new_name += MAP_CHARS[el]
        elif (ord('A') <= ord(el) <= ord('Z')) or (ord('a') <= ord(el) <= ord('z')) or el.isdigit():
            new_name += el
        else:
            new_name += '_'
    return new_name + '.' + lists[-1]


# Сортировка
def sorting_dir(namedir):
    lists = listdir(namedir)
    for el in lists:
        path_file = path.join(namedir, el)
        if is_free_dir(path_file):
            continue
        if path.isdir(path_file):
            sorting_dir(path_file)
        else:
            folder = check_file_type(el)
            if folder:
                rename_file(folder, namedir, el)


# Удаление пустых папок
def check_clear_dir(namedir):
    lists = listdir(namedir)
    if not lists and not is_free_dir(namedir):
        rmdir(namedir)
    else:
        for el in lists:
            path_el = path.join(namedir, el)
            if path.isdir(path_el):
                check_clear_dir(path_el)


if __name__ == "__main__":
    user_path = get_path_name()
    main()
