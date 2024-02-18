
from .settings import *
from .styles import *
from .latexfile import *

class LatexChapter:
    def __init__(self, basefile : str, style : Styles, chapterFilename : str) -> None:
        self.files = []
        self.chapter = ''
        self.style = style
        self.compiledfile = chapterFilename

        self.base = ''

        if basefile != None:
            with open(basefile) as f:
                self.base = f.read()

    
    # append a file
    def add_file(self, file : LatexFile):
        self.files.append(file)

    # combine all code and make chapter file
    def compile(self):
        chapter_code = self.base

        for file in self.files:
            chapter_code += file.getFileRepr()
        
        with open(self.compiledfile, 'w') as f:
            f.write(self.style.applyChapterStyle(chapter_code))
