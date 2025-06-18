from pathlib import Path

# The file you are looking for
FILE_KEY = ""

# P4 repo root
REPO_PATH = Path(r"")

# List of paths to search in relative to REPO_PATH
# [Path("")]
PATHS_FILTER = []

# List of extensions to ignore
EXTENSION_BLACKLIST = [".swatches"]

# Inclusion blacklist, do not add files in "!"
INCLUSION_PATHS_BLACKLIST = ["!"]

# Inclusion filter for specific paths and file types
# {Path(""): [""]}
INCLUSION_FILTER = {}

# Enable inclusion filter, like cgf files for hair, files in "!"...
IS_INCLUSION = False

OUTPUT_PATH = Path("paths.txt")
