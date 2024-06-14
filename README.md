![ClusView Banner](assets/clusView_banner.png)

# ClusView
*ClusView* is a [BERTopic](https://maartengr.github.io/BERTopic/index.html) based tool that aims to optimize and visualize document clustering leveraging a configurable cluster quality meter. Essentially, performing ***CLUS***ter ***VIEW***ing in a human-readable way.

## Structure
*ClusView* is maintained and organized in different packages, found under the `packages` directory.

| Package       | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| `clusview`    | Python core functionality implemented as a standalone module.  |
| `ui`          | user interface to ease the creation and use of *ClusView*.     |

## Prerequisites
The current version of *ClusView* packages have the following pre-requisites.

| Package       | Prerequisites                                                       |
| ------------- | ------------------------------------------------------------------- |
| `clusview`    | `Python 3.12.3`. Older versions may work. Not tested.               |
| `ui`          | `Node 20.14.0` & `pnpm 9.3.0`. Older versions may work. Not tested. |


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

## Contributing
Head over to [CONTRIBUTING.md](CONTRIBUTING.md) to read the guidelines on contributing to *Clusview*.