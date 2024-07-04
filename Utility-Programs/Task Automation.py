import os
import shutil
import pandas as pd
import datetime

def file_organizer(folder_path):
    extensions = {
        'txt': 'Text Files',
        'docx': 'Word Documents',
        'pdf': 'PDF Files',
        'jpg': 'Images',
        'mp3': 'Audio Files'
    }

    for folder in extensions.values():
        if not os.path.exists(os.path.join(folder_path, folder)):
            os.makedirs(os.path.join(folder_path, folder))

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1][1:]
            for extension, folder in extensions.items():
                if file_extension == extension:
                    shutil.move(file_path, os.path.join(folder_path, folder, file))

    print('Files have been organized!')

def data_cleaner(data_file):
    data = pd.read_csv(data_file)
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    data['column1'] = data['column1'].astype(int)
    data['column2'] = data['column2'].astype(float)

    data.to_csv('cleaned_data.csv', index=False)

    print('Data has been cleaned!')

def system_maintenance(data_folder, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    backup_file = os.path.join(backup_folder, f'backup-{current_date}.zip')
    shutil.make_archive(backup_file, 'zip', data_folder)

    print('Backup has been created!')

folder_path = "A:\Python-Programming\Utility-Programs\files"
data_file = 'data.csv'
data_folder = 'data'
backup_folder = 'backup'

file_organizer(folder_path)
data_cleaner(data_file)
system_maintenance(data_folder, backup_folder)