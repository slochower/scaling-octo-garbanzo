import re
import subprocess as sp
import argparse
import os
import shutil
import glob

ap = argparse.ArgumentParser()
ap.add_argument("--format", required=True, help="Manuscript diff output format.")
ap.add_argument("--first_commit", required=True, help="First commit for `diff`.")
ap.add_argument("--second_commit", required=True, help="Second commit for `diff` (can be '').")

args = vars(ap.parse_args())
fmt = args['format']
first_commit = args["first_commit"]
second_commit = args["second_commit"]


def find_changed_line_numbers(first_commit, second_commit, file):
    """
    Find the line numbers in a file (in the second commit) that are changed relative to the first commit,
    by checking out two copies of the same file on-the-fly, then calling `diff` and capturing the output.
    This will work best with semantic line feeds.
    """
    if not os.path.exists("diff/content/"):
        os.makedirs("diff/content")
    else:
        for file in os.listdir("diff/content/"):
            file_path = os.path.join("diff/content/", the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)

    base = os.path.splitext(file)[0]
    # Grab a copy of the file from the two commits and write them to the subdirectory `diff`
    if second_commit == "":
        second_commit = "current"
    for commit in [first_commit, second_commit]:
        if not commit == "current":
            command = f"git show {commit}:{file} > diff/{base}-{commit[0:7]}.md"
        else:
            command = f"cp {file} diff/{base}-{commit[0:7]}.md"
        print(f"Runing {command}")
        sp.call(command, shell=True)

    # Get the changed lines between the two files, printing only the line numbers.
    command = f'diff --unchanged-line-format="" --old-line-format="" --new-line-format="%dn " diff/{base}-{first_commit[0:7]}.md diff/{base}-{second_commit[0:7]}.md'
    # `diff` returns a 1 if differences are found, but we can can still grab the output and skip the exception.
    try:
        p = sp.check_output(command, shell=True)
    except sp.CalledProcessError as e:
        if e.returncode == 1 and e.output:
            lines = e.output.decode("utf-8").split()
            return [int(i) - 1 for i in lines]
        else:
            print("Problem running diff.")
            # Can happen if a file is deleted between commits.
            pass

def write_colored_diff(first_commit, second_commit, file, lines, color="CornflowerBlue",
output=fmt):
    """
    Given the changed lines as a list, rewrite the line to begin and 
    end with a span that will color the text. In my limited testing,
    this seems to work well with both HTML and PDF output, but I am 
    by no means an HTML expert, so I don't know if this will have unintended
    consequences.
    """
    base = os.path.splitext(file)[0]
    with open(f"diff/{base}-{second_commit[0:7]}.md", "r") as f:
        content = f.readlines()
    if lines:
        for line in lines:
            if content[line].isspace():
                print(f"Skipping blank line")
                continue
            if content[line][0] == "#":
                print("Skipping header line")
                continue
            if content[line][0] == "\\":
                print("Skipping LaTeX directive line")
                continue
            if content[line][0] == "<" and content[line][1] == "!":
                print("Skipping HTML directive line")
                continue
            if content[line][0] == "!":
                print("Skipping image directive line")
                continue
            if output == "html":
                # Rewrite the line, trimming `\n`, with a specific color.
                content[line] = (
                    f"<span style='color:{color}'>" + content[line][:-1] + "</span>\n"
                )
            elif output == "latex":
                content[line] = (
                    # f"\\color{{{color}}}" + content[line][:-1] + "\\color{black}\n"
                    f"\\textcolor{{{color}}}{{" + content[line][:-1] + "} \n"
                    # This can cause a problem because putting the LaTeX directive means that
                    # pandoc will no longer parse the line, it will just pass it along.
                    # Therefore, something like Ca^2+^ will go straight to LaTeX which will
                    # complain about math mode.
                    # Same thing with citations.
                )

        with open(f"diff/{base}-{second_commit[0:7]}.md", "w") as f:
            [f.write(i) for i in content]
    os.remove(f"diff/{base}-{first_commit[0:7]}.md")

def build_diff(first_commit, second_commit):
    """
    Write a slightly modified build script (based off `build.sh`) that will create
    `manuscript_diff.html` and `manuscript_diff.pdf` in the output directory. In the future,
    this I imagine this can be a flag, like we currently have for `$BUILD_DOCX` to automatically
    create a manuscript `diff` when desired.
    """
    for file in ["citation-tags.tsv", "manual-references.json", "metadata.yaml"]:
        shutil.copy(f"content/{file}", "diff/content")
    build_script = f"""
set -o errexit

# Set timezone used by Python for setting the manuscript's date
export TZ=Etc/UTC
# Default Python to read/write text files using UTF-8 encoding
export LC_ALL=en_US.UTF-8

# Generate reference information
echo "Retrieving and processing reference metadata"
manubot \
  --content-directory=diff/content/ \
  --output-directory=diff/output \
  --cache-directory=ci/cache \
  --log-level=INFO

CSL_PATH=build/assets/journal-of-chemical-theory-and-computation.csl
BIBLIOGRAPHY_PATH=diff/output/references.json
INPUT_PATH=diff/output/manuscript.md

# Make output directory
mkdir -p output
cp -r content/images diff/content/images

# Create PDF output
echo "Exporting PDF manuscript"
FONT="Helvetica"
COLORLINKS="true"
pandoc \
    --from=markdown \
    --filter=pandoc-eqnos \
    --filter=pandoc-tablenos \
    --filter=pandoc-img-glob \
    --filter=pandoc-chemfig \
    --filter=pandoc-fignos \
    --bibliography=$BIBLIOGRAPHY_PATH \
    --csl=$CSL_PATH \
    --template=build/assets/nih4.tex \
    --metadata link-citations=true \
    --number-sections \
    --resource-path=.:content:../content \
    --pdf-engine=xelatex \
    --variable mainfont="${{FONT}}" \
    --variable sansfont="${{FONT}}" \
    --variable colorlinks="${{COLORLINKS}}" \
    --output=diff/output/manuscript.tex \
    $INPUT_PATH
echo "Build complete"
"""
    with open("build/build_diff.sh", "w") as f:
        f.write(build_script)
    p = sp.Popen(["bash", "build/build_diff.sh"], cwd=".", stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = p.communicate()

def checkout_commit(commit, file):
    """
    Find the line numbers in a file (in the second commit) that are changed relative to the first commit,
    by checking out two copies of the same file on-the-fly, then calling `diff` and capturing the output.
    This will work best with semantic line feeds.
    """
    if not os.path.exists("diff/content/"):
        os.makedirs("diff/content")
    base = os.path.splitext(file)[0]
    command = f"git show {commit}:{file} > diff/{base}-{commit[0:7]}.md"
    print(f"Runing {command}")
    sp.call(command, shell=True)

def build_latex(commit):
    """
    Write a slightly modified build script (based off `build.sh`) that will create
    `manuscript_diff.html` and `manuscript_diff.pdf` in the output directory. In the future,
    this I imagine this can be a flag, like we currently have for `$BUILD_DOCX` to automatically
    create a manuscript `diff` when desired.
    """
    for file in ["citation-tags.tsv", "manual-references.json", "metadata.yaml"]:
        shutil.copy(f"content/{file}", "diff/content")
    build_script = f"""
set -o errexit

# Set timezone used by Python for setting the manuscript's date
export TZ=Etc/UTC
# Default Python to read/write text files using UTF-8 encoding
export LC_ALL=en_US.UTF-8

# Generate reference information
echo "Retrieving and processing reference metadata"
manubot \
  --content-directory=diff/content/ \
  --output-directory=diff/output \
  --cache-directory=ci/cache \
  --log-level=INFO

mv diff/output/manuscript.md diff/output/manuscript-{commit[0:7]}.md
CSL_PATH=build/assets/journal-of-chemical-theory-and-computation.csl
BIBLIOGRAPHY_PATH=diff/output/references.json
INPUT_PATH=diff/output/manuscript-{commit[0:7]}.md

# Make output directory
mkdir -p output
cp -r content/images diff/content/images

# Create PDF output
echo "Exporting PDF manuscript"
FONT="Helvetica"
COLORLINKS="true"
pandoc \
    --from=markdown \
    --filter=pandoc-eqnos \
    --filter=pandoc-tablenos \
    --filter=pandoc-img-glob \
    --filter=pandoc-chemfig \
    --filter=pandoc-fignos \
    --bibliography=$BIBLIOGRAPHY_PATH \
    --csl=$CSL_PATH \
    --template=build/assets/nih4.tex \
    --metadata link-citations=true \
    --number-sections \
    --resource-path=.:content:../content \
    --pdf-engine=xelatex \
    --variable mainfont="${{FONT}}" \
    --variable sansfont="${{FONT}}" \
    --variable colorlinks="${{COLORLINKS}}" \
    --output=diff/output/manuscript-{commit[0:7]}.tex \
    $INPUT_PATH
echo "Build complete"
"""
    with open("build/build_diff.sh", "w") as f:
        f.write(build_script)
    p = sp.Popen(["bash", "build/build_diff.sh"], cwd=".", stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = p.communicate()


if __name__ == "__main__":
    paths = sorted(glob.glob("content/[0-9]*.md"))
    for path in paths:
        checkout_commit(first_commit, path)
        # changed_lines = find_changed_line_numbers(first_commit, second_commit, path)
        # write_colored_diff(first_commit, second_commit, path, changed_lines)
    build_latex(first_commit)
    for path in paths:
        checkout_commit(second_commit, path)
    build_latex(second_commit)
    # Then copy images and...
    # THen latexdiff

    # build_diff(first_commit, second_commit)
