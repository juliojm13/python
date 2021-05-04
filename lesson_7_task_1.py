import os

root = os.path.dirname(__file__)
folder_name = 'my_project'
paths_list = [os.path.join(folder_name, "settings"), os.path.join(folder_name, "mainapp"),
              os.path.join(folder_name, "adminapp"), os.path.join(folder_name, "authapp"), ]
for el in paths_list:
    os.makedirs(os.path.join(root, el), exist_ok=True)
