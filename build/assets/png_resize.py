import os
import re
import sys
import argparse
import shlex
import subprocess as sp

ap = argparse.ArgumentParser()
ap.add_argument("--svg", required=True, help="SVG")

args = vars(ap.parse_args())
svg = os.path.basename(args["svg"])
svg_name, svg_extension = os.path.splitext(svg)
png = os.path.join(os.path.dirname(args["svg"]), svg_name) + ".png"


def find_height_and_width(svg, filename):
    dimensions = None
    with open(filename, "r") as f:
        content = f.readlines()
    for line in content:
        if svg in line:
            attributes = re.split("{|}", line.strip())[1]
            height, width = attributes.split(" ")
            dimensions = []
            for dimension in [height, width]:
                dimension = dimension.split("=")[1]
                dimension = dimension.replace('"', "")
                if "px" in dimension[-2:]:
                    dimensions.append(int(dimension[:-2]))
    return dimensions


def resize_png(png, dimensions):
    height, width = dimensions[0], dimensions[1]
    command = f"""mogrify -resize {height}x{width} {png}"""
    sp.call(shlex.split(command))


if __name__ == "__main__":
    if os.path.exists(png):
        # Assume that if a PNG exists already, it is appropriately sized.
        sys.stderr.write(f"`png_resize`: Found {png} skipping...\n")
        sys.exit()
    try:
        input_path = os.environ["INPUT_PATH"]
        markdown_file = input_path
    except KeyError:
        markdown_file = "manuscript.md"
    dimensions = find_height_and_width(svg=svg, filename=markdown_file)
    if dimensions:
        sys.stderr.write(f"`png_resize`: Found dimensions, resizing {png}...\n")
        resize_png(png=png, dimensions=dimensions)
