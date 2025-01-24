# NDI Metadata documentation

This repository contains documentation for NDI XML formatted metadata along with
examples, schemas for validation, and a validation utility which can be used to
verify any given XML is or is not valid as NDI metadata.  See the markdown files
in the GitBook directory for details.  This content is also available online at
docs.ndi.video.

The Documents directory contains example valid NDI metadata frames, while the
Schemas directory includes xsd files which can be used to validate NDI metadata.
The validatemeta.py utility uses the xsd schema files along with some program
logic logic to validate NDI metadata passed on the command line, as a file, or
sent by an NDI sender or receiver.  See the documenation in the GitBook
directory or online for full details.
