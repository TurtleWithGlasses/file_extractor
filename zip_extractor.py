import zipfile


def extract_archive(archive_path, des_dir):
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(des_dir)