# What does this do?

Merge confits are caused due to confilting changes on same line of code, latexgen solves this issue by preventing from everyone editing the same file.

Latexgen auto-generates chapter files(Eg. laplace.tex for laplace transfrom), by walking through all the latex files in all the directories, and adding them to their respective chapter latex files.

In addition to this, it also maintains a list of all contributors.

# Using latexgen

Run 
```
python3 latexgen.py
```
to make auto-generated files, followed by
```
pdflatex main.tex
pdflatex main.tex
```
to generate the pdf.

## Configuring latexgen

latexgen can be configured by changing the pdfc.json json file.

Here is a documentation of all the settings supported by latexgen as of now, all settings are compulsory unless mentioned.

### General Purpose

1. Root Directory:
```json
"latex.root":"roodirname"
``` 
This setting specifies which directory latexgen starts searching for latex files. For example if it is set to "Root", then it will use "Root/file.tex" and "Root/subdir/file.tex", but not "./file.tex"

2. Chapter List:
```json
"pdf.chapters":{
    "Chapter1": {
        "name":"Chapter1",
        "file":"file to generate for chapter1",
        "base":"file to use as base for chapter1"
    },
    "Chapter1": {
        "name":"Chapter2",
        "file":"file to generate for chapter2",
        "base":"file to use as base for chapter2"
    },
}
``` 
This setting lists all the Chapters the latex file will use. 

+ name: chapter name to use inside chapter macro
+ file: path to file to make for this chapter
+ base\[optional\]: path to file containing code to use by default

3. Skip Files\[Optional\]: latexgen allows skipping latex files whose path is written in the skipfile, as specified in this setting:
    ```json
    "pdf.skipfile":"styles/skip.txt"
    ```

4. Author List\[Optional\]: This setting describes the file to write list of contributors and their solved and unsolved questions:
    ```json
    "pdf.authorslist":"styles/authors.txt"
    ```

5. Logging\[Optional\]: This settings describes the file to write logging info to. This can be used to get reasons for which a file was skipped
    ```json
    "pdf.log":"styles/pycompile.log"
    ```

### Hints

These settings tell latexgen which latex macros to use to detect/get information from latex file.

If any of these the macros from these hints is not in a file, latexgen terminates with an error with the filename. 

1. **latex.hints.chapter**: Decribes which macro to get chapter information from:

    Example: 
    
    pdfc.json
    ```json
    "latex.hints.chapter":"\\chapter",
    ```
    And in latex file:
    ```latex
    \chapter{xyz}
    ```
    includes this latex file in xyz chapter

2. **latex.hints.question/solution**: Hints the start and end of a question respectively. **latex.hints.solution** also hints the start of a solution

    Example: 
    
    pdfc.json
    ```json
    "latex.hints.question":"\\question",
    "latex.hints.solution":"\\solution"
    ```
    
    latex file:
    ```latex
    \question some question ...
    \solution
    ```
    Causes latexgen to consider "some question ..." as a question

3. **latex.hints.author\[Optional\]**: Hints the author of this latex file. Used to generate info about all the contributions.

    Example: 
    
    pdfc.json
    ```json
    "latex.hints.author":"\\author"
    ```
    
    latex file:
    ```latex
    \author{ee15btech00000}
    ```

### Conditions

These settings define a list of macros that a file must contain to mark a latex file.

1. **latex.conditions.solved**: List of macros a file must contained to be considered solved.

    Example: 
    
    a.tex:
    ```latex
    \solution
    \begin{align}
        math code
    \end{align}
    \begin{table}
        table code
    \end{table}
    \begin{figure}
        figure code
    \end{figure}
    ```

    b.tex:
    ```latex
    \solution
    \begin{align}
        math code
    \end{align}
    ```

    pdfc.json:
    ```json
    "pdf.conditions.solved" : [
        "\\begin{align}",
        "\\begin{table}",
        "\\begin{figure}"
    ]
    ```
    this will mark a.tex as solved, and b.tex as not solved.

2. **latex.conditions.validlatex**: List of macros a file must contained to be considered as a main latex file.

    Example: 
    
    a.tex:
    ```latex
    \iffalse
    ...
    \fi
    ...
    ```

    b.tex:
    ```latex
    \iffalse
    ...
    ```

    pdfc.json:
    ```json
    "pdf.conditions.validlatex" : [
        "\\fi",
        "\\iffalse"
    ]
    ```
    This will cause latexgen to ignore b.tex, whereas a.tex will be further processed by latexgen

    If a file is ignored info about it is written to the console and in the logfile.

    


