import subprocess
import sys

def run_script(script_name):
    print(f"\n=============================================")
    print(f"Bat dau chay: {script_name}")
    print(f"=============================================")
    result = subprocess.run([sys.executable, script_name], capture_output=False)
    if result.returncode == 0:
        print(f"Hoan thanh: {script_name}")
    else:
        print(f"Loi khi chay: {script_name}")
        sys.exit(1)

def run_xelatex():
    print(f"\n=============================================")
    print(f"Bat dau chay: xelatex thesis.tex")
    print(f"=============================================")
    
    # Reload environment to ensure xelatex is found
    cmd = 'powershell.exe -Command "$env:Path = [System.Environment]::GetEnvironmentVariable(\'Path\',\'Machine\') + \';\' + [System.Environment]::GetEnvironmentVariable(\'Path\',\'User\'); xelatex -interaction=nonstopmode -output-directory=\'d:\\graduation-thesis\\document\\out\' \'d:\\graduation-thesis\\document\\out\\thesis.tex\'"'
    
    result = subprocess.run(cmd, shell=True, capture_output=False)
    if result.returncode == 0:
        print(f"Hoan thanh: xelatex thesis.tex")
    else:
        print(f"Loi khi chay: xelatex (kiem tra thesis.log)")

if __name__ == "__main__":
    print("Bat dau qua trinh bien dich toan bo tai lieu (PDF va Word)...")
    
    # Run LaTeX compilation (generates thesis.tex)
    run_script('compile_latex.py')
    
    # Run xelatex to build PDF from thesis.tex
    # Run twice to ensure TOC and bookmarks are updated
    run_xelatex()
    run_xelatex()
    
    # Run Word compilation
    run_script('compile_v5.py')
    
    print("\nXONG! Da tao thanh cong ca hai ban PDF va Word tu cau hinh chung.")
