![Clusview Banner](assets/clusview_logo_banner.svg)

<div align="center">
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  ![GitHub Latest Release)](https://img.shields.io/github/v/release/gcalcedo/clusview?include_prereleases&label=pre-release&logo=github)

</div>
<div align="center">
  
  [![Tag and Release](https://github.com/gcalcedo/clusview/actions/workflows/tag_and_release.yml/badge.svg)](https://github.com/gcalcedo/clusview/actions/workflows/tag_and_release.yml)

</div>

# Clusview
*Clusview* is a [BERTopic](https://maartengr.github.io/BERTopic/index.html) based tool that aims to optimize and visualize document clustering leveraging a configurable cluster quality meter. Essentially, performing ***CLUS***ter ***VIEW***ing in a human-readable way.

## Structure
*Clusview* is maintained and organized in different packages, found under the `packages` directory.

| Package       | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| `clusview`    | Python core functionality implemented as a standalone module.  |
| `ui`          | User interface to ease the creation and use of *Clusview*.     |
| `docs`        | Documentation site.                                            |

## Prerequisites
The current version of *Clusview* packages have the following pre-requisites.

| Package       | Prerequisites                                                           |
| ------------- | ----------------------------------------------------------------------- |
| `clusview`    | `Python 3.12.3`. Older versions may work. Not tested.                   |
| `ui`          | `Node 20.14.0` & `pnpm 9.3.0`. Older versions may work. Not tested.     |
| `docs`        | `Starlight 0.24.2` & `pnpm 9.3.0`. Older versions may work. Not tested. |


## Installation
Step-by-step installation process for each package. These steps assume command execution from the root directory of each package.

### `clusview`
1. (Optional) For a cleaner and self-contained installation, make use of a Python virtual environment, like [venv](https://docs.python.org/3/library/venv.html).
```console
python -m venv "name_of_virtual_environment"
source "name_of_virtual_environment"/bin/activate
```

2. Install dependencies in `requirements.txt` via `pip`.
```console
pip install -r requirements.txt
```

### `ui`
1. (If using [`nvm`](https://github.com/nvm-sh/nvm)) Enable corepack.
```console
corepack enable
```

2. Install dependencies in `package.json` via `pnpm`.
```console
pnpm install
```

### `docs`
1. (If using [`nvm`](https://github.com/nvm-sh/nvm)) Enable corepack.
```console
corepack enable
```

2. Install dependencies in `package.json` via `pnpm`.
```console
pnpm install
```

## Contributing
Head over to [CONTRIBUTING.md](CONTRIBUTING.md) to read the guidelines on contributing to *Clusview*.
