
set -o errexit

# Set timezone used by Python for setting the manuscript's date
export TZ=Etc/UTC
# Default Python to read/write text files using UTF-8 encoding
export LC_ALL=en_US.UTF-8

# Generate reference information
echo "Retrieving and processing reference metadata"
manubot   --content-directory=diff/content/   --output-directory=diff/output   --cache-directory=ci/cache   --log-level=INFO

mv diff/output/manuscript.md diff/output/manuscript-now.md
CSL_PATH=build/assets/journal-of-chemical-theory-and-computation.csl
BIBLIOGRAPHY_PATH=diff/output/references.json
INPUT_PATH=diff/output/manuscript-now.md

# Make output directory
mkdir -p output
cp -r content/images diff/content/images

FONT="Helvetica"
COLORLINKS="true"
pandoc     --from=markdown     --filter=pandoc-eqnos     --filter=pandoc-tablenos     --filter=pandoc-img-glob     --filter=pandoc-chemfig     --filter=pandoc-fignos     --bibliography=$BIBLIOGRAPHY_PATH     --csl=$CSL_PATH     --template=build/assets/nih4.tex     --metadata link-citations=true     --number-sections     --resource-path=.:content:../content     --pdf-engine=xelatex     --variable mainfont="${FONT}"     --variable sansfont="${FONT}"     --variable colorlinks="${COLORLINKS}"     --output=diff/output/manuscript-now.tex     $INPUT_PATH
echo "Build complete"
rm diff/content/*.md
