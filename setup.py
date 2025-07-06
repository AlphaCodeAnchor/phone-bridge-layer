from setuptools import setup
from setuptools.command.install import install
import urllib.request
import zipfile
import os

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        self.download_and_extract_adb()

    def download_and_extract_adb(self):
        ADB_URL = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
        ZIP_NAME = "platform-tools.zip"
        ADB_DIR = "platform-tools"

        if os.path.exists(os.path.join(ADB_DIR, "adb.exe")):
            print("[ADB] Already downloaded.")
            return

        print("[ADB] Downloading...")
        urllib.request.urlretrieve(ADB_URL, ZIP_NAME)

        print("[ADB] Extracting...")
        with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
            zip_ref.extractall(".")

        os.remove(ZIP_NAME)
        print("[ADB] Done.")

setup(
    name='phone-bridge-layer',
    version='0.1',
    packages=['phonebridge'],  # <== use your real package name here
    install_requires=[],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
