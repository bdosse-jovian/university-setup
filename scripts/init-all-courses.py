#!/bin/python3
from courses import Courses

for course in Courses():
    lectures = course.lectures
    course_title = lectures.course.info["title"]

    lines = [r'\documentclass[a4paper, 11pt]{article}',
             r'\input{./static/preamble.tex}'
             r'\input{./static/article.tex}',
             r'% \input{./static/book.tex}',
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
    (lectures.root / 'static').mkdir(exist_ok=True)
    (lectures.root / 'static' / 'bib').mkdir(exist_ok=True)
    (lectures.root / 'static' / 'figures').mkdir(exist_ok=True)

    lines = [r'\usepackage{subcaption}',
             r'\usepackage{graphicx}',
             r'\graphicspath{ {./static/figures/} }',
             r'\usepackage[usenames,dvipsnames]{xcolor}',
             r'\usepackage{pgfplots}',
             r'\pgfplotsset{compat = newest}',
             r'',
             r'% Formatting packages',
             r'\usepackage[french]{babel}',
             r'\usepackage[utf8]{inputenc}',
             r'\usepackage{csquotes}',
             r'\usepackage[T1]{fontenc}',
             r'',
             r'\usepackage{hyperref}',
             r'\usepackage[shortlabels]{enumitem}',
             r'\usepackage{parskip}',
             r'',
             r'% Bibliographie & ToC',
             r'\setcounter{tocdepth}{3}',
             r'\usepackage[citestyle=numeric,style=./static/bib/iso-fp,backend=biber]{biblatex}',
             r'\addbibresource{./static/bib/sources.bib}',
             r'',
             r'% Paquets math',
             r'\usepackage{amsfonts, amsmath, amsthm, amssymb}',
             r'\usepackage{mathrsfs}',
             r'',
             r'\input{./static/thm-env.tex}',
             r'',
             r'\newcommand{\Set}[1]{\mathbb{#1}}',
             r'\newcommand{\Cal}[1]{\mathcal{#1}}',
             r'\newcommand{\Scr}[1]{\mathscr{#1}}',
             r'\newcommand{\Frak}[1]{\mathfrak{#1}}',
             r'',
             r'\newcommand{\C}{\Set{C}}',
             r'\newcommand{\R}{\Set{R}}',
             r'\newcommand{\N}{\Set{N}}',
             r'\newcommand{\Z}{\Set{Z}}',
             r'\newcommand{\Q}{\Set{Q}}',
             r'\newcommand{\T}{\Set{T}}',
             r'',
             r'\newcommand{\cA}{\Cal{A}}',
             r'\newcommand{\cB}{\Cal{B}}',
             r'\newcommand{\cC}{\Cal{C}}',
             r'\newcommand{\cF}{\Cal{F}}',
             r'',
             r'\newcommand{\sA}{\Scr{A}}',
             r'\newcommand{\sB}{\Scr{B}}',
             r'\newcommand{\sC}{\Scr{C}}',
             r'\newcommand{\sF}{\Scr{F}}',
             r'',
             r'\newcommand{\nP}{\mathbb{P}}',
             r'\newcommand{\nE}{\mathbb{E}}',
             r'\newcommand{\Esp}[1]{\nE\left[#1\right]}',
             r'',
             r'\newcommand{\floor}[1]{\lfloor#1\rfloor}',
             r'\newcommand{\abs}[1]{\left|#1\right|}',
             r'\newcommand{\conj}[1]{\overline{#1}}',
             r'',
             r'\newcommand{\oset}[2]{\left]#1,#2\right[}',
             r'\newcommand{\cset}[2]{\left[#1,#2\right]}',
             r'\newcommand{\ocset}[2]{\left]#1,#2\right]}',
             r'\newcommand{\coset}[2]{\left[#1,#2\right[}',
             r'',
             r'\newcommand{\adh}[1]{\overline{#1}}',
             r'\newcommand{\interieur}[1]{#1^\circ}']
    (lectures.root / 'static' / 'preamble.tex').touch()
    (lectures.root / 'static' / 'preamble.tex').write_text('\n'.join(lines))

    lines = [r'\usepackage[marginparwidth=2.4cm,',
             r'            left=3.2cm, right=3.2cm, top=2.7cm, bottom=3cm,',
             r'            headheight=16pt]{geometry}',
             r'',
             r'\usepackage[Rejne]{fncychap}',
             r'\usepackage{fancyhdr}',
             r'\pagestyle{fancy}',
             r'\fancyhf{}',
             r'\fancyhead[R]{\thelecture}',
             r'\renewcommand{\footrulewidth}{0.4pt}',
             r'\fancyfoot[L]{\textsc{\thetitle}}',
             r'\fancyfoot[R]{\thepage}',
             r'',
             r'% Horodatage',
             r'\def\testdateparts#1{\dateparts#1\relax}',
             r'\def\dateparts#1 #2 #3 #4 #5\relax{',
             r'    \marginpar{\scriptsize\mbox{#1 #2 #3 #5}}',
             r'}',
             r'',
             r'\def\thelecture{}%',
             r'\newcommand{\lecture}[3]{',
             r'    \def\thelecture{Leçon #1 : #3}',
             r'    \subsection*{\thelecture}',
             r'    \selectlanguage{english}',
             r'    \testdateparts{#2}',
             r'    \selectlanguage{french}',
             r'    %\marginpar{\scriptsize #2}',
             r'}',
             r'',
             r'% Pour obtenir une numérotation des équations de la forme',
             r'% Section.Numéro',
             r'\usepackage{chngcntr}',
             r'\counterwithin{equation}{section}']
    (lectures.root / 'static' / 'article.tex').touch()
    (lectures.root / 'static' / 'article.tex').write_text('\n'.join(lines))

    lines = [r'\usepackage[inner=3cm, outer=2.2cm, top=2.7cm, bottom=3cm,',
             r'            headheight=16pt]{geometry}',
             r'',
             r'\renewcommand{\thechapter}{\Roman{chapter}}',
             r'\usepackage[Rejne]{fncychap}',
             r'\usepackage{fancyhdr}',
             r'\pagestyle{fancy}',
             r'\renewcommand{\chaptermark}[1]%',
             r'{\markboth{\MakeUppercase{#1}}{}}',
             r'\renewcommand{\sectionmark}[1]%',
             r'{\markright{#1}}',
             r'\fancyhf{}',
             r'\fancyhead[LE,RO]{\thepage}',
             r'\fancyhead[CO]{\textbf{\thesection.\ \rightmark}}',
             r'\fancyhead[CE]{\textbf{\thechapter.\ \leftmark}}',
             r'\renewcommand{\footrulewidth}{0.4pt}',
             r'\fancyfoot[LE]{\theauthor}',
             r'\fancyfoot[RO]{\thedate}',
             r'',
             r'\def\thelecture{}%',
             r'\newcommand{\lecture}[3]{',
             r'    \def\thelecture{#3}',
             r'    \chapter{\thelecture}',
             r'}',
             r'',
             r'% Pour obtenir une numérotation des équations de la forme',
             r'% Chapitre.Section.Numéro',
             r'\usepackage{chngcntr}',
             r'\counterwithin{equation}{section}']
    (lectures.root / 'static' / 'book.tex').touch()
    (lectures.root / 'static' / 'book.tex').write_text('\n'.join(lines))

    lines = [r'\usepackage{tikz, tikz-cd}',
             r'\usepackage{thmtools}',
             r'\usepackage[framemethod=TikZ]{mdframed}',
             r'\mdfsetup{skipabove=1em,',
             r'  %skipbelow=0em,',
             r'  %innertopmargin=5pt,',
             r'  %innerbottommargin=5pt',
             r'  }',
             r'',
             r'\theoremstyle{definition}',
             r'\makeatletter',
             r'',
             r'\declaretheoremstyle[',
             r'  headfont=\normalfont\bfseries\scshape,',
             r'  bodyfont=\normalfont\itshape,',
             r'  qed=$\blacksquare$,',
             r'  mdframed={ nobreak }]{unprovedthmboxed}',
             r'',
             r'\declaretheoremstyle[',
             r'  headfont=\normalfont\bfseries\scshape,',
             r'bodyfont=\normalfont\itshape,',
             r'mdframed={ nobreak }]{thmboxed}',
             r'',
             r'\declaretheoremstyle[',
             r'  headfont=\normalfont\bfseries\scshape,',
             r'  mdframed={ nobreak }]{defboxed}',
             r'',
             r'\declaretheoremstyle[',
             r'  headfont=\normalfont\bfseries\scshape',
             r'  ]{defunboxed}',
             r'',
             r'\declaretheoremstyle[',
             r'  headfont=\normalfont\bfseries,',
             r'  bodyfont=\normalfont,',
             r'  numbered=no,',
             r'  qed=$\blacksquare$]{proofline}',
             r'',
             r'\declaretheorem[',
             r'  numberwithin=section,',
             r'  style=defboxed,',
             r'  name=Définition',
             r']{definition}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=thmboxed,',
             r'  name=Lemme',
             r']{lemme}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=thmboxed,',
             r'  name=Proposition',
             r']{proposition}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=thmboxed,',
             r'  name=Théorème',
             r']{theoreme}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=thmboxed,',
             r'  name=Corollaire',
             r']{corollaire}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=unprovedthmboxed,',
             r'  name=Lemme',
             r']{ulemme}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=unprovedthmboxed,',
             r'  name=Proposition',
             r']{uproposition}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=unprovedthmboxed,',
             r'  name=Théorème',
             r']{utheoreme}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=unprovedthmboxed,',
             r'  name=Corollaire',
             r']{ucorollaire}',
             r'',
             r'\declaretheorem[',
             r'  sibling=definition,',
             r'  style=defunboxed,',
             r'  name=Remarque',
             r']{remarque}',
             r'',
             r'\declaretheorem[',
             r'  numbered=no,',
             r'  style=defunboxed,',
             r'  name=Exemple',
             r']{exemple}',
             r'',
             r'\declaretheorem[',
             r'  numbered=no,',
             r'  style=defunboxed,',
             r'  name=Notation',
             r']{note}',
             r'',
             r'\declaretheorem[',
             r'  numbered=no,',
             r'  style=proofline,',
             r'  name=Démonstration]{replacementproof}',
             r'',
             r'\renewenvironment{proof}[1][\proofname]',
             r'{\begin{replacementproof}}',
             r'{\end{replacementproof}}',
             r'',
             r'%\newtheorem{exo}{Exercice}[section]',
             r'%\theoremstyle{plain}',
             r'%\newtheorem{lm}[mdef]{Lemme}',
             r'%\newtheorem{pro}[mdef]{Proposition}',
             r'%\newtheorem{cor}[mdef]{Corollaire}',
             r'%\newtheorem{thm}[mdef]{Théorème}',
             r'',
             r'\makeatother']
    (lectures.root / 'static' / 'thm-env.tex').touch()
    (lectures.root / 'static' / 'thm-env.tex').write_text('\n'.join(lines))
