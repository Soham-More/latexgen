import json

# Maintains data about contributor
from .authorcell import *

# Handles error when getting settings by key
# also manages logging
class Settings:
    def __init__(self, settingJsonFile : str):
        self.file = settingJsonFile
        with open(settingJsonFile) as f:
            self.config = json.load(f)
        
        # enable logging if pdf.log setting exists
        try:
            self.logfile = open(self.config['pdf.log'], 'w')
        except KeyError:
            self.logfile = None
        except Exception as exception:
            raise exception
        
        # enable checking authors, if pdf.authorslist setting exists
        try:
            self.authorfile = open(self.config['pdf.authorslist'], 'w')
            self.authordict = {}
        except KeyError:
            self.authorfile = None
            self.authordict = None
        except Exception as exception:
            raise exception
        
        # enable skipping files, if pdf.skipfile setting exists
        try:
            with open(self.config['pdf.skipfile']) as f:
                self.skiplist = f.read().splitlines()
        except KeyError:
            self.skiplist = None
        except Exception as exception:
            raise exception
        
    def getKeyIfExists(self, key):
        key_list = key.split('/')

        # if key ends with '/'
        # ignore it
        if len(key_list[-1]) == 0:
            key_list.pop()

        config = self.config
        for key in key_list:
            if key in config.keys():
                config = config[key]
            else:
                return None

        return config
        
    def getSetting(self, setting : str):
        setting_list = setting.split('/')

        # if setting id ends with '/'
        # ignore it
        if len(setting_list[-1]) == 0:
            setting_list.pop()

        config = self.config
        for key in setting_list:
            try:
                config = config[key]
            except KeyError:
                raise Exception(f'Fatal Error: Setting {key} not defined in {self.file}.')

        return config
    
    def log(self, text: str):
        if self.logfile != None:
            self.logfile.write(text + '\n')
        print(text)
    
    def getAuthor(self, author : str) -> AuthorCell:
        if self.authorfile != None:
            if author in self.authordict.keys():
                return self.authordict[author]
            else:
                self.authordict[author] = AuthorCell(author)
                return self.authordict[author]
    
    def isSkippedFile(self, filepath : str) -> bool:
        if self.skiplist == None:
            return False
        return filepath in self.skiplist

    def __getitem__(self, key):
        return self.getSetting(key)
    
    def __del__(self):
        self.logfile.close()
        
        for author in self.authordict.values():
            self.authorfile.write(str(author))
        
        self.authorfile.close()
