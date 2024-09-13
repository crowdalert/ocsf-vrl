# Crowdalert OCSF VRL Remaps

Welcome to the OCSF VRL Remaps Collection! This project is a set of [VRL (Vector Remapping Language)](https://vector.dev/docs/reference/vrl/) remaps designed to help you efficiently transform your security data in to the [Open Cybersecurity Schema Framework](https://ocsf.io) normalization schema 

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

[VRL](https://vector.dev/docs/reference/vrl) is a powerful language for data transformation and remapping with a fast, Rust-based interpreter, shipped as part of the [Vector](https://vector.dev) data collection pipeline

[pyVRL](https://github.com/crowdalert/pyvrl) integrates VRL with Python natively, obviating the need for Vector & exposing it to any python-based data pipeline

[OCSF](https://ocsf.io) is an open-source normalization schema for security data analytics supported by several large data & security vendors.

This collection provides a variety of VRL remap programs that can be used to transform data from raw vendor security log sources in to OCSF

## Usage

Each remap program is stored in its own file within the `remaps` directory.

the native VRL command can be used to transform a JSON file:

```sh
vrl --file remaps/example_remap.vrl --input data/input.json --output data/output.json
```

or use [pyVRL](https://github.com/crowdalert/pyvrl) to integrate these transforms in to your Python pipeline.

( **note:** *Like Vector's `remap`, programs expect log data in a Python dict value under a `message` key* )

A command-line utility (`remap.py`) is included as an example & can be used instead of the `vrl` command:

install dependencies:
```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

and invoked with the input VRL and input data arguments (writes to stdout)

```sh
python remap.py aws/cloudtrail/remap.vrl cloudtrail.json
```

## Contributing

We welcome contributions!

If you have a remap that you think would be useful to others or changes to better fit the OCSF schema please submit a pull request. Make sure to include a description of what your remap does and any necessary documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
