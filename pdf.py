# A min requirement python code to compile latex
# repos without merge errors

# Only use default packages and numpy/scipy/matplotlib

# A latex file is considered solved if it contains
# all the items in 'pdf.solved.conditions' list in json file
# after \solution macro

import os
from pdfsrc.authorcell import *
from pdfsrc.styles import *
from pdfsrc.latexfile import *
from pdfsrc.latexchapter import *

# get a list of chapters as defined in settings json file
def get_chapter_list(config : Settings, style : Styles):
    chapters = {}
    chapter_files = []
    for chapter_data in config['pdf.chapters']:
        chapter_name = get_insensitive_str(config[f'pdf.chapters/{chapter_data}/name'])
        chapter_file = config[f'pdf.chapters/{chapter_data}/file']
        chapter_base = config.getKeyIfExists(f'pdf.chapters/{chapter_data}/base')

        # if chapter has already been added, raise error
        if chapter_name in chapters.keys():
            raise Exception(f'Fatal Error: Duplicate Chapter {chapter_name} found in {config.file}') 

        chapters[chapter_name] = LatexChapter(chapter_base, style, chapter_file)
        chapter_files.append(chapter_file)
    return chapters

# add file to it's chapter, 
# if the chapter does not exist raise an exception
# returns chapters dictionary with the file
def register_latex_file(filename : str, chapters, style : Styles, config : Settings):
    for chapter in chapters.values():
        if chapter.compiledfile == filename:
            return chapters
    if config.isSkippedFile(filename) and (config.skiplist != None):
        config.log(f'Skipped processing file {filename}\n\tReason: in skiplist {config["pdf.skipfile"]}')
        return chapters
    file : LatexFile = LatexFile(filename, style, config)
    if not file.isMainFile:
        config.log(f'Skipped processing file {filename}\n\tReason: Did not match conditions given in key "pdf.conditions.validlatex" in json file {config.file}')
        return chapters
    try:
        chapters[file.chapter].add_file(file)
    except KeyError:
        print(f'Fatal Error: Chapter {file.chapter} is not defined in json file {config.file}')
    return chapters

# registers all latex file in 'latex.root' json key
def get_latex_files(chapters, style : Styles, config : Settings):
    for root, dirs, files in os.walk(config['latex.root']):
        for f in files:
            filename, file_ext = os.path.splitext(f)

            #if the file is latex, then register it
            if file_ext == '.tex':
                chapters = register_latex_file('{}/{}'.format(root, f), chapters, style, config)
    return chapters

def main():
    settings : Settings = Settings('pdfc.json')
    style : Styles = Styles(settings)

    chapters = get_chapter_list(settings, style)

    try:
        chapters = get_latex_files(chapters, style, settings)
        for chapter in chapters:
            chapters[chapter].compile()
    except Exception as exception:
        print(exception.args[0])
        print('The final pdf will not be compiled.')
        if settings.logfile != None:
            print(f'Output written to {settings["pdf.log"]}')

if __name__ == '__main__':
    main()

