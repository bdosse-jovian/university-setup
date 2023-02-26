#!/bin/python3
import shutil
from pathlib import Path

from courses import Courses


for course in Courses():
    lectures = course.lectures
    beamers = course.beamers
    course_title = lectures.course.info["title"]

    lines = [r'\documentclass[a4paper, 11pt]{article}',
             r'\input{./static/preamble.tex}',
             r'\input{./static/article.tex}',
             r'% \input{./static/book.tex}',
             r'',
             r'\makeatletter',
             fr'\title{{{course_title}}}\let\thetitle\@title',
             r'\date{\textsc{Année Académique 2022--2023}}\let\thedate\@date',
             r'% \author{\emph{Notes de cours par} Benjamin Dosse}\let\theauthor\@author',
             r'\makeatother',
             r'',
             r'\begin{document}',
             r'',
             r'% \frontmatter',
             r'\maketitle',
             r'\tableofcontents',
             r'',
             r'% \mainmatter',
             fr'% start lectures',
             fr'% end lectures',
             r'',
             r'\printbibliography[heading=bibintoc,title={Références}]',
             r'% \printbibliography[heading=bibintoc,title={Bibliographie}]',
             r'',
             r'\end{document}']

    lectures.master_file.touch()
    lectures.master_file.write_text('\n'.join(lines))
    (lectures.root / 'master.tex.latexmain').touch()
    (lectures.root / 'static').mkdir(exist_ok=True)
    (lectures.root / 'static' / 'bib').mkdir(exist_ok=True)
    (lectures.root / 'static' / 'figures').mkdir(exist_ok=True)

    shutil.copy(Path('../preamble.tex'), lectures.root / 'static')
    shutil.copy(Path('../article.tex'), lectures.root / 'static')
    shutil.copy(Path('../book.tex'), lectures.root / 'static')

    lines = [r'\documentclass[11pt]{beamer}',
             r'\input{./static/beamer-preamble.tex}',
             r'',
             r'\makeatletter',
             fr'\title{{{course_title}}}\let\thetitle\@title',
             r'\subtitle{}',
             r'\date{\textsc{Année Académique 2022--2023}}\let\thedate\@date',
             r'\author{Benjamin Dosse}\let\theauthor\@author',
             r'\makeatother',
             r'',
             r'\begin{document}',
             r'\setbeamertemplate{navigation symbols}{}',
             r'',
             r'\begin{frame}[plain]',
             r'  \maketitle',
             r'\end{frame}',
             r'',
             r'\begin{frame}',
             r'  \frametitle{Plan}',
             r'  \tableofcontents',
             r'\end{frame}',
             r'',
             fr'% start lectures',
             fr'% end lectures',
             r'',
             r'\begin{frame}',
             r'  \frametitle{Références}',
             r'  \printbibliography',
             r'\end{frame}',
             r'',
             r'\end{document}']
    
    beamers.master_file.touch()
    beamers.master_file.write_text('\n'.join(lines))
    (beamers.root / 'master.tex.latexmain').touch()
    (beamers.root / 'static').mkdir(exist_ok=True)
    (beamers.root / 'static' / 'bib').mkdir(exist_ok=True)
    (beamers.root / 'static' / 'figures').mkdir(exist_ok=True)

    shutil.copy(Path('../beamer-preamble.tex'), beamers.root / 'static')
