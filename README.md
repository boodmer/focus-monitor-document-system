# Graduation Thesis Document System

This repository contains the automated build system for generating my graduation thesis in both **Microsoft Word (.docx)** and **LaTeX/PDF** formats from a single source of content.

## 📁 Project Structure

- `content/`: Contains the thesis content in text/markdown format (chapters, abstract, etc.).
- `images/`: Stores all diagrams and figures used in the document.
- `references/`: Reference documents and guidelines.
- `out/`: Build output directory (ignored by git).
- `config.py`: Central configuration for styles, meta-information, abbreviations, and symbols.
- `compile_v5.py`: Script to generate the Word document and update the Table of Contents.
- `compile_latex.py`: Script to generate the LaTeX source (`thesis.tex`).
- `build_all.py`: Master script to run the full build pipeline.

## 🚀 How to Use

### 1. Setup Environment
Ensure you have Python installed and create a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Prerequisites
- **For Word**: Microsoft Word must be installed (used for TOC automation).
- **For PDF**: A TeX distribution with `xelatex` (like MiKTeX or TeX Live) must be installed and available in your PATH.

### 3. Build Documents
To build both Word and PDF versions at once:
```powershell
python build_all.py
```
The output files will be saved in the `out/` directory.

## 🛠️ Individual Build Scripts
- `python compile_v5.py`: Builds only the Word document.
- `python compile_latex.py`: Generates only the `thesis.tex` file.

## 📝 Editing Content
Edit the files in the `content/` folder. The scripts handle:
- Automatic numbering (Chapters, Sections, Subsections).
- LaTeX equation rendering in Word (OMML).
- Cross-references and Table of Contents generation.
- Dynamic lists of abbreviations and symbols.
