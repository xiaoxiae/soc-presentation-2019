import os
import subprocess

# easier to change for running the tex commands
file_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_dir + os.sep + "..")

# this makes it so that the name of the tex file isn't hardcoded
file_name = [f for f in os.listdir(".") if f.endswith(".tex")][0][:-len(".tex")]

# clean-up files from the previous compilation to perform a clean one
for file in [f for f in os.listdir(".") if os.path.isfile(f)]:
    if file.startswith(file_name) and not file.endswith(("tex", "bib", "xoj")):
            os.remove(file)

# run xelatex twice to correctly typeset cross-reference-related text
for _x in range(3):
    os.system("lualatex --shell-escape " + file_name + ".tex")
