#!/bin/python3
from courses import Courses

for course in Courses():
    lectures = course.lectures
    course_title = lectures.course.info["title"]
    lines = [r'\documentclass[a4paper, 11pt]{article}',
             r'\input{../../latex/header/header.tex}'
             r'\input{../../latex/header/article.tex}',
             r'% \input{../../latex/header/book.tex}',
             r'\makeatletter',
             fr'\title{{{course_title}}}\let\thetitle\@title',
             r'\date{\textsc{Année Académique 2022--2023}}\let\thedate\@date',
             r'% \author{\emph{Notes de cours par} Benjamin Dosse}\let\theauthor\@author',
             r'\makeatother',
             r'\begin{document}',
             r'% \frontmatter',
             r'\maketitle',
             r'\tableofcontents',
             r'% \mainmatter',
             fr'% start lectures',
             fr'% end lectures',
             r'\printbibliography',
             r'\addcontentsline{toc}{section}{Références}',
             r'% \addcontentsline{toc}{chapter}{Bibliographie}',
             r'\end{document}']
    lectures.master_file.touch()
    lectures.master_file.write_text('\n'.join(lines))
    (lectures.root / 'master.tex.latexmain').touch()
    (lectures.root / 'figures').mkdir(exist_ok=True)
