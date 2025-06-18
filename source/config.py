from pathlib import Path

# The file you are looking for
FILE_KEY = ""

# P4 repo root
REPO_PATH = Path("")

# List of paths to search in relative to REPO_PATH
PATHS_FILTER = [Path("")]

# List of extensions to ignore
EXTENSION_BLACKLIST = [".swatches"]

# Inclusion blacklist, do not add files in "!"
INCLUSION_PATHS_BLACKLIST = ["!"]

# Inclusion filter for specific paths and file types
INCLUSION_FILTER = {Path(""): [""]}

# Enable inclusion filter, like cgf files for hair, files in "!"...
IS_INCLUSION = False

OUTPUT_PATH = Path("Paths.txt")
