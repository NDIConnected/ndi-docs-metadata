# XML Validation

## Schema Files

Example XML files and XSD files are provided allowing standard XML validation
tools to be used to validate NDI metadata messages.  A parser which understands
XSD version 1.1 is required.  Freely available tools which support XSD 1.1
include Xerces2 (Java) from Apache.org and the Python3 xmlschema library by
SISSA (Scuola Internazionale Superiore di Studi Avanzati).  The community
version of the Liquid Studio XML editor is a convient editing and validation
environment for the Xerces2 Java library.  Validation using python can be as
simple as a few lines of code (tested on Debian Bookworm with the
python3-xmlschema package installed):

```python
$ python3 -q
>>> import xmlschema
>>> schema = xmlschema.XMLSchema11('Schemas/ndi_metadata_all.xsd')
>>> schema.is_valid('Documents/ndi_color_info.xml')
True
>>> schema.is_valid('Documents/vancData.Multiple.xml')
True
>>> exit()
```

Several top-level schema files are provided to assist with validating the
various metadata streams available.

`ndi_metadata_all` : A collection of all valid NDI metadata messages, regardless of how or where they are sent

`ndi_metadata_recv` : Valid metadata messages received by an NDI receiver

`ndi_metadata_send` : Valid metadata messages received by an NDI sender

`ndi_metadata_video` : Valid metadata messages received with an NDI video frame

The remaining file in the `Schemas` directory define specific metadata elements
and are pulled in by the top-level files listed above.

There is a Liquid Studio project file `NDI_Metadata.lxsproj` in the top level
directory which can be used with the community (or paid) version of Liquid
Studio to assist with editing and validation of the NDI metadata and schema
files.

## Schema Limitations

There are a few known limitations to the schema files:

1. The logic for the use of the various attributes available under the `ndi_capabilities` element is currently (2025.02.03) incomplete and under review.
2. No user defined element name should ever match the regex `[nN][dD][iI].*` or `[nN][tT][kK].*`, which is not currently expressed in the schema files. The python validation script does check for this programatically.
3. There are currently no specific metadata elements defined for sending with an NDI audio frame.

## XML Files

Typical examples of various NDI metadata frames are provided in the `Documents` directory.

### Validation Application

A python application is provided that will listen for metadata from an NDI
sender or receiver and can be used to validate the formatting and in some cases
the content of an NDI metadata frame.  This application can also validate XML
metadata from a file or provided on the command line (be careful with shell
expansion and quoting when passing metadata on the command line).

The python validation app requires the xmlschema and ndi-python libraries.  The
xmlschema library can typically be installed via OS packages or using pip, but
the ndi-python library currently needs to be installed from source.  Since the
source repository includes a git submodule, it does not install properly using
pip.

```sh
# Build and install ndi-python library from source

# Linux users may need to provide a path to the NDI SDK directory
export NDI_SDK_DIR="/path/to/NDI SDK Directory"

# Download the source code from github and populate git submodules
git clone --recursive https://github.com/buresu/ndi-python.git

# Build the wheel package for installation
cd ndi-python
python3 setup.py bdist_wheel

# Install the wheel package
python3 -m pip install dist/ndi_python-*.whl
```
