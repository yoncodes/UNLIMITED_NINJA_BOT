#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import version
import time,os,requests
from os import rmdir, listdir
from os.path import join
from bs4 import BeautifulSoup
import re
import zipfile
from shutil import move
import shutil

class updater:
    def __init__(self):
        self.version = self.client_version()
        self.serverVersion = self.server_version()

    def check(self):
        
        if self.version != self.serverVersion:
            if self.version < self.serverVersion:
                print "Update available"
                print "Latest version {}".format(self.serverVersion)
                print "Downloading update"
                self.download('https://github.com/yoncodes/UNLIMITED_NINJA_BOT/archive/master.zip')
                
                src_dir = os.path.abspath(os.curdir)
                if os.path.isfile(src_dir + '\UNLIMITED_NINJA_BOT.zip'):
                    os.remove('UNLIMITED_NINJA_BOT.zip')
                os.rename('master.zip','UNLIMITED_NINJA_BOT.zip')
                self.setup('UNLIMITED_NINJA_BOT.zip')
                os.remove('UNLIMITED_NINJA_BOT.zip')
        else:
            print "Latest Update"
            print "Current version {}".format(self.version)

    def download(self,url):
        
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter
        browser = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in browser.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return local_filename
    
    def backup(self):
        pass

    def setup(self,filename):
        filelist = []
        fh = open(filename, 'rb')
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            
            src_dir = os.path.abspath(os.curdir)
            z.extract(name, src_dir)
        fh.close()
        
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(os.path.dirname(dname))
        root_src_dir =  src_dir + '\UNLIMITED_NINJA_BOT-Master'
        root_dst_dir = os.path.dirname(dname)       
        if os.path.exists(src_dir + '\UNLIMITED_NINJA_BOT-Master'):
            files = os.listdir(src_dir + '\UNLIMITED_NINJA_BOT-Master')
            for src_dir, dirs, files in os.walk(root_src_dir):
                dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        os.remove(dst_file)
                    shutil.move(src_file, dst_dir)
        else:
            shutil.rmtree(root_src_dir)
          
        try:
            shutil.rmtree(root_src_dir)
        except:
            rmdir(root_src_dir)
    

    def client_version(self):
        current_version = version.__version__
        return current_version

    def server_version(self):
        versions = []
        browser = requests.get('https://github.com/yoncodes/UNLIMITED_NINJA_BOT/releases/latest')
        soup = BeautifulSoup(browser.content,"html5lib")
        
        for header in soup.findAll("div", {"class":"release-header"}):
           for header_sub in header.find_all('h1', attrs={'class': 'release-title'}):
               versions.append(header_sub.text.strip())

        
        m = re.search(r"(v\d.\d.\d.\d|v\d.\d.\d)",versions[0])

        serverVersion = m.group(0)

        
        return serverVersion