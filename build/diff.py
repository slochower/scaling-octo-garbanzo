import subprocess as sp
import argparse
import os
import shutil
import glob

ap = argparse.ArgumentParser()
ap.add_argument("--format", required=True, help="Manuscript diff output format.")
ap.add_argument("--first_commit", required=True, help="First commit for `diff`.")
ap.add_argument("--second_commit", required=False, help="Second commit for `diff` (can be '').")

args = vars(ap.parse_args())
fmt = args['format']
first_commit = args["first_commit"]
if args["second_commit"]:
    second_commit = args["second_commit"]
else:
    second_commit = "now"

def prepare():
    if not os.path.exists("diff/content/"):
        os.makedirs("diff/content")

def checkout_commit(commit, file):
    """
    Find the line numbers in a file (in the second commit) that are changed relative to the first commit,
    by checking out two copies of the same file on-the-fly, then calling `diff` and capturing the output.
    This will work best with semantic line feeds.
    """
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
rm diff/content/*.md
"""
    with open("build/build_diff.sh", "w") as f:
        f.write(build_script)
    sp.call("bash build/build_diff.sh", cwd=".", shell=True)


if __name__ == "__main__":
    prepare()
    paths = sorted(glob.glob("content/[0-9]*.md"))
    for commit in [first_commit, second_commit]:
        for path in paths:
            if commit != "now":
                checkout_commit(first_commit, path)
            else:
                sp.call(f"cp {path} diff/{path}", shell=True)
        build_latex(commit)
    sp.call(f"latexdiff diff/output/manuscript-{first_commit[0:7]} diff/output/manuscript-{second_commit[0:7]} > diff/output/diff.tex", shell=True)
    sp.call("xelatex diff/output/diff.tex", shell=True)