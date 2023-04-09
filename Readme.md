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


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


[![Python][Python]][Python]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You will need to install the latest version of Python 3.10, which can be downloaded from the official Python website or installed using your system's package manager.

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
  - [ ] `cp` command
  - [ ] `info` command
  - [x] `verify` command
  - [x] `cat` command
  - [ ] `browsers` command
  - [ ] `logs` command
  - [ ] `hives` command
  - [ ] `reg` command
- [x] Merkle proof for file signature check
- [ ] Extracting Browsers
    - [x] Edge
    - [x] Chrome
    - [x] Internet Explorer
    - [ ] Firefox
    - [ ] Brave
    - [ ] Opera
    - [ ] Puffin
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