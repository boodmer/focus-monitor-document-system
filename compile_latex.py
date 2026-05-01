import os, re, glob, config

IMG_DIR = config.IMG_DIR
DOC_DIR = config.DOC_DIR
CONTENT_DIR = config.CONTENT_DIR
OUT_DIR = config.OUT_DIR
OUT_TEX = os.path.join(OUT_DIR, 'thesis.tex')

PREAMBLE = r"""\documentclass[12pt,a4paper]{extreport}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\renewcommand{\normalsize}{\fontsize{13}{16.5}\selectfont}
\usepackage[vietnamese]{babel}
\usepackage[top=2.5cm, bottom=2.0cm, left=3.5cm, right=2.0cm]{geometry}
\usepackage{setspace}
\setstretch{1.3}
\usepackage{graphicx}
\usepackage{float}
\usepackage[font=it]{caption}
\usepackage{longtable}
\usepackage{unicode-math}
\setmathfont{Cambria Math}
\usepackage{indentfirst}
\setlength{\parindent}{1.27cm}
\setlength{\parskip}{2pt}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage[bookmarksnumbered=false]{hyperref}
\hypersetup{colorlinks=false,pdfborder={0 0 0}}
\usepackage{titlesec}
\titleformat{\chapter}[block]{\normalfont\fontsize{""" + str(config.STYLES['chapter_title_size']) + r"""}{""" + str(config.STYLES['chapter_title_size'] + 4) + r"""}\bfseries\centering}{CHƯƠNG \thechapter.\quad}{0pt}{}
\titlespacing*{\chapter}{0pt}{-10pt}{4pt}
\titleformat{\section}{\normalfont\fontsize{""" + str(config.STYLES['heading2_size']) + r"""}{""" + str(config.STYLES['heading2_size'] + 3) + r"""}\bfseries}{\thesection.}{0.4em}{}
\titlespacing*{\section}{0pt}{4pt}{1pt}
\titleformat{\subsection}[block]{\normalfont\fontsize{""" + str(config.STYLES['heading3_size']) + r"""}{""" + str(config.STYLES['heading3_size'] + 3) + r"""}\bfseries\itshape}{\thesubsection.}{0.4em}{}
\titlespacing*{\subsection}{0pt}{4pt}{2pt}
\usepackage{tocloft}
\setlength{\cftbeforechapskip}{0pt}
\setlength{\cftbeforesecskip}{0pt}
\setlength{\cftbeforesubsecskip}{0pt}
\setlength{\cftbeforefigskip}{0pt}
\usepackage{etoolbox}
\makeatletter
\patchcmd{\@chapter}{\addtocontents{lof}{\protect\addvspace{10\p@}}}{}{}{}
\patchcmd{\@chapter}{\addtocontents{lot}{\protect\addvspace{10\p@}}}{}{}{}
\makeatother
\renewcommand{\cfttoctitlefont}{\hfill\fontsize{""" + str(config.STYLES['chapter_title_size']) + r"""}{""" + str(config.STYLES['chapter_title_size'] + 4) + r"""}\bfseries}
\renewcommand{\cftaftertoctitle}{\hfill}
\setlength{\cftbeforetoctitleskip}{-10pt}
\setlength{\cftaftertoctitleskip}{6pt}
\renewcommand{\cftloftitlefont}{\hfill\fontsize{""" + str(config.STYLES['chapter_title_size']) + r"""}{""" + str(config.STYLES['chapter_title_size'] + 4) + r"""}\bfseries}
\renewcommand{\cftafterloftitle}{\hfill}
\setlength{\cftbeforeloftitleskip}{-10pt}
\setlength{\cftafterloftitleskip}{6pt}
\renewcommand{\cftfigpresnum}{Hình }
\setlength{\cftfignumwidth}{2.2cm}
\renewcommand{\cftchappresnum}{CHƯƠNG }
\renewcommand{\cftchapaftersnum}{.}
\setlength{\cftchapnumwidth}{2.8cm}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\chaptername}{CHƯƠNG}

\begin{document}
\renewcommand{\contentsname}{MỤC LỤC}
\renewcommand{\listfigurename}{DANH SÁCH HÌNH VẼ}
"""

def generate_cover_page_latex():
    """Hàm tạo trang bìa chuẩn cho LaTeX (Anh có thể chỉnh sửa text ở đây)"""
    return r"""
% === BÌA ===
\begin{titlepage}
\begin{tikzpicture}[remember picture,overlay]
    \draw[line width=1pt] 
        ($(current page.north west) + (3.0cm,-2.0cm)$) 
        rectangle 
        ($(current page.south east) + (-2.0cm,2.0cm)$);
\end{tikzpicture}
\begin{center}
\vspace*{-1.5cm}
{\large\textbf{""" + config.META['department'] + r"""}} \\[0.2cm]
{\large\textbf{""" + config.META['university'] + r"""}} \\
\rule{6cm}{1pt} \\
\vspace{2.5cm}
{\LARGE\textbf{""" + config.META['degree'] + r"""}} \\[0.4cm]
{\large Ngành: """ + config.META['major'] + r"""} \\
\vspace{2.5cm}
{\LARGE\textbf{""" + config.META['title'].upper() + r"""}}
\vspace{3.5cm}
\end{center}

\begin{center}
\begin{tabular}{ll}
\textbf{Giảng viên hướng dẫn:} & TS. Phạm Huy Thông \\
\textbf{Sinh viên thực hiện:} & """ + config.META['student_name'] + r""" \\
\textbf{Mã số sinh viên:} & """ + config.META['student_id'] + r""" \\
\textbf{Lớp:} & """ + config.META['class_name'] + r""" \\
\end{tabular}
\end{center}

\vfill
\begin{center}
{\large\textbf{""" + config.META['location'] + """ - """ + config.META['year'] + r"""}}
\end{center}
\end{titlepage}
"""

PREAMBLE += generate_cover_page_latex()

PREAMBLE += r"""
\pagenumbering{arabic}
\tableofcontents
\newpage
\addcontentsline{toc}{chapter}{\listfigurename}
\listoffigures

% === DANH MỤC CÁC TỪ VIẾT TẮT ===
\newpage
\chapter*{DANH MỤC CÁC TỪ VIẾT TẮT}
\addcontentsline{toc}{chapter}{DANH MỤC CÁC TỪ VIẾT TẮT}
\renewcommand{\arraystretch}{1.4}
\begin{longtable}{|c|p{2.5cm}|p{10cm}|}
\hline
\textbf{STT} & \textbf{Viết tắt} & \textbf{Ý nghĩa} \\
\hline
\endfirsthead
\hline
\textbf{STT} & \textbf{Viết tắt} & \textbf{Ý nghĩa} \\
\hline
\endhead
\hline
\endfoot
"""

for i, (abbr, meaning) in enumerate(config.ABBREVIATIONS):
    PREAMBLE += f"{i+1} & {abbr} & {meaning} \\\\\n\\hline\n"
    
PREAMBLE += r"""\end{longtable}

% === DANH MỤC CÁC KÝ HIỆU ===
\newpage
\chapter*{DANH MỤC CÁC KÝ HIỆU}
\addcontentsline{toc}{chapter}{DANH MỤC CÁC KÝ HIỆU}
\renewcommand{\arraystretch}{1.4}
\begin{longtable}{|c|p{3.5cm}|p{9cm}|}
\hline
\textbf{STT} & \textbf{Ký hiệu} & \textbf{Ý nghĩa} \\
\hline
\endfirsthead
\hline
\textbf{STT} & \textbf{Ký hiệu} & \textbf{Ý nghĩa} \\
\hline
\endhead
\hline
\endfoot
"""

for i, (sym, meaning) in enumerate(config.SYMBOLS_LATEX):
    PREAMBLE += f"{i+1} & {sym} & {meaning} \\\\\n\\hline\n"
    
PREAMBLE += r"""\end{longtable}

\newpage
"""

def escape_latex(text):
    """Escape special LaTeX characters but keep intended formatting."""
    math_blocks = []
    def repl(m):
        math_blocks.append(m.group(0))
        return f"@@MATH{len(math_blocks)-1}@@"
    
    import re
    text = re.sub(r'\$.*?\$', repl, text)

    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('{', r'\{')
    text = text.replace('}', r'\}')
    text = text.replace('~', r'\textasciitilde{}')
    text = text.replace('^', r'\textasciicircum{}')

    for i, block in enumerate(math_blocks):
        text = text.replace(f"@@MATH{i}@@", block)
        
    return text

def strip_number_prefix(title):
    """Remove leading number prefix like '1.1. ', '2.3.2. ', 'Chương 1. ' from title."""
    # Strip "Chương X. " prefix
    title = re.sub(r'^Chương\s+\d+[\.\s]*', '', title)
    # Strip "X.Y.Z. " number prefix  
    title = re.sub(r'^\d+(\.\d+)*\.?\s*', '', title)
    return title.strip()

def parse_file(filepath):
    """Parse a chapter file and return LaTeX content."""
    if not os.path.exists(filepath):
        return ""
    
    lines = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.rstrip('\n\r')
            stripped = line.strip()
            if not stripped:
                continue
            
            # Chapter titles
            for prefix in ['CH0_TITLE|','CH1_TITLE|','CH2_TITLE|','CH3_TITLE|','CH4_TITLE|','CH5_TITLE|']:
                if stripped.startswith(prefix):
                    title = stripped.split('|', 1)[1]
                    clean_title = strip_number_prefix(title).upper()
                    
                    non_numbered = ['LỜI CẢM ƠN', 'TÀI LIỆU THAM KHẢO', 'TÓM TẮT', 'ABSTRACT', 'PHỤ LỤC']
                    is_numbered = True
                    for nn in non_numbered:
                        if clean_title.startswith(nn):
                            is_numbered = False
                            break
                            
                    if is_numbered:
                        lines.append(f'\n\\chapter{{\\texorpdfstring{{{escape_latex(clean_title)}}}{{CHƯƠNG \\thechapter: {escape_latex(clean_title)}}}}}\n')
                    else:
                        lines.append(f'\n\\chapter*{{{escape_latex(clean_title)}}}\n\\addcontentsline{{toc}}{{chapter}}{{{escape_latex(clean_title)}}}\n')
                    break
            else:
                # H2 - Section
                for prefix in ['CH0_H2|','CH1_H2|','CH2_H2|','CH3_H2|','CH4_H2|','CH5_H2|']:
                    if stripped.startswith(prefix):
                        title = stripped.split('|', 1)[1]
                        clean_title = strip_number_prefix(title)
                        # Sentence case: First letter upper
                        if clean_title:
                            clean_title = clean_title[0].upper() + clean_title[1:]
                        
                        if prefix == 'CH0_H2|':
                            lines.append(f'\n\\section*{{{escape_latex(clean_title)}}}\n')
                        else:
                            lines.append(f'\n\\section{{\\texorpdfstring{{{escape_latex(clean_title)}}}{{\\thesection. {escape_latex(clean_title)}}}}}\n')
                        break
                else:
                    # H3 - Subsection
                    for prefix in ['CH0_H3|','CH1_H3|','CH2_H3|','CH3_H3|','CH4_H3|','CH5_H3|']:
                        if stripped.startswith(prefix):
                            title = stripped.split('|', 1)[1]
                            clean_title = strip_number_prefix(title)
                            # Sentence case
                            if clean_title:
                                clean_title = clean_title[0].upper() + clean_title[1:]
                            
                            if prefix == 'CH0_H3|':
                                lines.append(f'\n\\subsection*{{{escape_latex(clean_title)}}}\n')
                            else:
                                lines.append(f'\n\\subsection{{\\texorpdfstring{{{escape_latex(clean_title)}}}{{\\thesubsection. {escape_latex(clean_title)}}}}}\n')
                            break
                    else:
                        # Images
                        for prefix in ['CH2_IMAGE|','CH3_IMAGE|','CH4_IMAGE|']:
                            if stripped.startswith(prefix):
                                parts = stripped.split('|')
                                img_file = parts[1]
                                caption = parts[2]
                                # Strip "Hình X.X. " prefix since LaTeX auto-numbers
                                caption = re.sub(r'^Hình\s+\d+\.\d+\.?\s*', '', caption)
                                img_path = os.path.join(IMG_DIR, img_file).replace('\\', '/')
                                lines.append(f'''
\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.85\\textwidth]{{{img_path}}}
\\caption{{{escape_latex(caption)}}}
\\end{{figure}}
''')
                                break
                        else:
                            # Screenshot placeholders
                            if stripped.startswith('[SCREENSHOT]'):
                                caption = stripped.replace('[SCREENSHOT]', '').strip()
                                caption = re.sub(r'^Hình\s+\d+\.\d+\.?\s*', '', caption)
                                lines.append(f'''
\\begin{{figure}}[H]
\\centering
\\fbox{{\\parbox{{0.8\\textwidth}}{{\\centering\\vspace{{3cm}}\\textit{{[Chèn ảnh chụp màn hình tại đây]}}\\vspace{{3cm}}}}}}
\\caption{{{escape_latex(caption)}}}
\\end{{figure}}
''')
                            else:
                                # Handle math equations
                                is_math = False
                                for prefix in ['CH2_EQ|','CH3_EQ|','CH4_EQ|']:
                                    if stripped.startswith(prefix):
                                        math_latex = stripped.split('|', 1)[1]
                                        lines.append(f'''
\\begin{{equation}}
{math_latex}
\\end{{equation}}
''')
                                        is_math = True
                                        break
                                
                                if not is_math:
                                    if stripped.startswith('Tổng_mới') or stripped.startswith('Điểm_trung_bình'):
                                        lines.append(f'\n\\texttt{{{escape_latex(stripped)}}}\n\n')
                                    else:
                                        escaped = escape_latex(stripped)
                                        escaped = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', escaped)
                                        lines.append(f'{escaped}\n\n')
    
    return ''.join(lines)

def build():
    chapter_files = [os.path.join(CONTENT_DIR, f) for f in config.CHAPTER_FILES]
    
    content = PREAMBLE
    for cf in chapter_files:
        print(f"  Processing: {cf}")
        content += parse_file(cf)
    
    content += '\n\\end{document}\n'
    
    with open(OUT_TEX, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n=== LaTeX file saved: {OUT_TEX} ===")

if __name__ == '__main__':
    build()
