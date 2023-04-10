<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

The goal of this project is to create a Python tool that can extract different types of artifacts from EWF (Expert
Witness Compression Format) evidence files. This tool can be useful for forensic investigators who need to analyze
digital evidence and extract relevant information from EWF files.

The tool provides various commands to extract different types of artifacts, such as automatic extraction, browser
artifacts, logs artifacts, registries artifacts, and hives artifacts. The tool also supports commands to list
partitions, list folders, copy files, and print files.

This tool use a Merkle proof to validate the extracted artifacts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Python][Python]][Python]

The tool is implemented using Python and uses libraries such as Pyewf, Pytsk3, and PyYAML to extract and parse data from
EWF files. The tool can be run from the command line by executing the main.py script with the appropriate command and
options.

### Structure

```sh
├── cmds/
│   ├── cmd1.py
├── config/
│   └── config1.yml
├── utils/
│   ├── util1.py
└── main.py
```

#### `cmds/`

This folder is used for all the subcommands

#### `config/`

This folder is used for all the YAML config profile.

#### `utils/`

This folder is used for all the python utils.


### YAML Configuration File

This repository includes a default YAML configuration file located at config/default.yml that can be used to customize certain aspects of the program. 

#### Configuration Options
The following configuration options are available:

##### DATA_PARTITION
A binary-encoded string representing the data partition. This option is used to specify the location of the data partition.

##### CONFIG_DIR_PATH
The path to the configuration directory. This option is used to specify the path to the system configuration directory.

##### LOGS_DIR_PATH
The path to the logs directory. This option is used to specify the path to the logs directory.

##### MFT_PATH
The path to the Master File Table (MFT). This option is used to specify the path to the MFT.

##### USERS_DIR_PATH
The path to the users directory. This option is used to specify the path to the users directory.

##### LOGS_FILES
A list of log files to extract. This option is used to specify which log files should be extracted.

##### REG_FILES
A list of registry files to extract. This option is used to specify which registry files should be extracted.

##### USER_HIVES
A list of user hives to extract. This option is used to specify which user hives should be extracted.

##### EDGE_PREFIX
The prefix used for Microsoft Edge artifacts.

##### CHROME_PREFIX
The prefix used for Chrome artifacts.

##### FIREFOX_PREFIX
The prefix used for Firefox artifacts.

##### IE_PREFIXES
A list of prefixes used for Internet Explorer artifacts.

##### BRAVE_PREFIXES
A list of prefixes used for Brave artifacts.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You will need to install the latest version of Python 3.10, which can be downloaded from the official Python website or
installed using your system's package manager.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MohammedBenhelli/EWFParser
   ```
2. Install python packages
   ```sh
   cd ./EWFParser
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

### Automatic extraction

This command extracts all available artifacts from the EWF file. It can be run using the following command:

```sh
python main.py extract --file <path-to-ewf-evidence> --dest <optional-path-to-destination> --config <optional-path-to-yaml-config>
```

### Extract browsers artifacts

This command extracts browser artifacts from the EWF file. It can be run using the following command:

```sh
python main.py browsers --file <path-to-ewf-evidence> --dest <optional-path-to-destination> --config <optional-path-to-yaml-config>
```

### Extract logs artifacts

This command extracts logs artifacts from the EWF file. It can be run using the following command:

```sh
python main.py logs --file <path-to-ewf-evidence> --dest <optional-path-to-destination> --config <optional-path-to-yaml-config>
```

### Extract registries artifacts

This command extracts registries artifacts from the EWF file. It can be run using the following command:

```sh
python main.py reg --file <path-to-ewf-evidence> --dest <optional-path-to-destination> --config <optional-path-to-yaml-config>
```

### Extract hives artifacts

This command extracts hives artifacts from the EWF file. It can be run using the following command:

```sh
python main.py hives --file <path-to-ewf-evidence> --dest <optional-path-to-destination> --config <optional-path-to-yaml-config>
```

### Get a proof

This command verify the proof of a folder. It can be run using the following command:

```sh
python main.py get-proof <path-to-artifacts-folder>
```

### Verify a proof

This command verify the proof of a folder. It can be run using the following command:

```sh
python main.py verify  --directory <path-to-artifacts-folder> --proof <proof-hash>
```

### List partitions

This command lists the partitions in the EWF file. It can be run using the following command:

```sh
python main.py partition --file <path-to-ewf-evidence>
```

### List folder

This command lists the contents of a folder in the EWF file. It can be run using the following command:

```sh
python main.py ls --file <path-to-ewf-evidence> <path-to-folder>
```

### Copy file

This command copies a file from the EWF file to a destination folder. It can be run using the following command:

```sh
python main.py cp --file <path-to-ewf-evidence> <path-to-file> <path-to-destination>
```

### Print file

This command prints the contents of a file in the EWF file. It can be run using the following command:

```sh
python main.py cat --file <path-to-ewf-evidence> <path-to-file>
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->

## Roadmap

- [x] Extracting system registries and users hives
    - [x] Convert to JSON
- [x] Extracting logs
    - [x] Convert to XML
- [x] Add subcommand
    - [x] `partition` command
    - [x] `ls` command
    - [x] `cp` command
    - [x] `get-proof` command
    - [x] `verify` command
    - [x] `cat` command
    - [x] `browsers` command
    - [x] `logs` command
    - [x] `hives` command
    - [x] `reg` command
- [x] Merkle proof for file signature check
- [x] Extracting Browsers
    - [x] Edge
    - [x] Chrome
    - [x] Internet Explorer
    - [x] Firefox
    - [x] Brave
    - [x] Opera
    - [x] Puffin
- [x] Extracting MFT
    - [ ] Parsing MFT
- [ ] Refactor
    - [ ] Clean code
    - [ ] Add ruff linter

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->

[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=yellow