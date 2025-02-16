#!/usr/bin/env python3

import getopt, sys
from enum import Enum, auto
import xml.etree.ElementTree as ET
import xmlschema
import re

class e_mode(Enum):
    ANY = auto()
    RECV = auto()
    SEND = auto()
    VIDEO = auto()
    AUDIO = auto()

usage_text=f"""Usage:
{sys.argv[0]} This is a test
    line 2
    line 3
{sys.argv[0]} [-a | -r | -s | -v] -f <filename>
{sys.argv[0]} [-a | -r | -s | -v] <xml_data>
    Verify contents of <filename> or <xml_data> string is proper NDI Metadata
    default : Check against all valid Metadata elements
    -a : Limit check to elements valid for Audio frames
    -r : Limit check to elements valid for NDI receive instance
    -s : Limit check to elements valid for NDI send instance
    -v : Limit check to elements valid for Video frames
"""

def usage():
    print(usage_text)

# Make schemas global so we only have to load them once
schema_all = None
schema_recv = None
schema_send = None
schema_video = None

# Make error counters global so we can update them from multiple functions
count_badxml = 0
count_valid = 0
count_user = 0
count_invalid = 0
count_product = 0
count_capabilities = 0
count_format = 0

# Global regualr expression to match illegal element names,
# so we only compile it once
# No user defined element names can start with ndi or ntk, ignoring case
invalid_re = re.compile ('^(ndi|ntk).*$', re.IGNORECASE)

def check_user(element):
    name = element.tag
    if invalid_re.match(name) == None:
        print (f"Valid user element: {name}")
        global count_user
        count_user += 1
    else:
        print (f"Inalid user element: {name}")
        global count_invalid
        count_invalid += 1

def check_one(element, schema):

    if schema != None and schema.is_valid(element):
        print ("XML is valid")
        global count_valid
        count_valid += 1

        # Track if we've seen various connection metadata elements
        match element.tag:
            case 'ndi_capabilities':
                print (ET.tostringlist(element, 'utf-8'))
                global count_capabilities
                count_capabilities += 1
            case 'ndi_product':
                print (ET.tostringlist(element, 'utf-8'))
                global count_product
                count_product += 1
            case 'ndi_format':
                print (ET.tostringlist(element, 'utf-8'))
                global count_format
                count_format += 1
    else:
        check_user(element)

def parse_multi(root, schema=None):
    # See if we have multiple elements in an ndi_metadata_group
    if root.tag != 'ndi_metadata_group':
        # Just one tag, see if it's valid
        check_one(root, schema)
    else:
        # We have multiple elements wrapped in an ndi_metadata_group
        for child in root:
            check_one(root, schema)

def parse_xml(xml):
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        print ("XML is NOT well formed!")
        print (xml)
        global count_badxml
        count_badxml += 1
        return None

    print ("XML is well formed")
    return root

def print_stats():
    print(f"Bad XML: {count_badxml}")
    print(f"Valid packets: {count_valid}")
    print(f"User packets : {count_user}")
    print(f"Invalid packets : {count_invalid}")
    print(f"Product packets : {count_product}")
    print(f"Capabilities packets : {count_capabilities}")
    print(f"Format packets : {count_format}")

def main():

    # Defaults
    mode = e_mode.ANY
    filename = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "arsvf:h", ["help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == "-a":
            mode = e_mode.AUDIO
        elif o == "-r":
            mode = e_mode.RECV
        elif o == "-s":
            mode = e_mode.SEND
        elif o == "-v":
            mode = e_mode.VIDEO
        elif o == "-f":
            filename = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    global schema_all
    global schema_recv
    global schema_send
    global schema_video

    # Read the schema(s) required for our operating mode
    match mode:
        case e_mode.ANY:
            schema_all = xmlschema.XMLSchema11('Schemas/ndi_metadata_all.xsd')
        case e_mode.RECV:
            schema_recv = xmlschema.XMLSchema11('Schemas/ndi_metadata_recv.xsd')
            schema_video = xmlschema.XMLSchema11('Schemas/ndi_metadata_video.xsd')
        case e_mode.SEND:
            schema_send = xmlschema.XMLSchema11('Schemas/ndi_metadata_send.xsd')
        case e_mode.VIDEO:
            schema_video = xmlschema.XMLSchema11('Schemas/ndi_metadata_video.xsd')
        # Nothing to do for audio yet!
        # case e_mode.AUDIO:

    # FIXME: Check for NDI operation!

    if filename:
        with open(filename, 'r') as file:
            xml = file.read()
    else:
        xml = args[0]

    root = parse_xml(xml)

    if root == None:
        print_stats()
        sys.exit()

    match mode:
        case e_mode.ANY:
            parse_multi(root, schema_all)
        case e_mode.RECV:
            parse_multi(root, schema_recv)
        case e_mode.SEND:
            parse_multi(root, schema_send)
        case e_mode.VIDEO:
            parse_multi(root, schema_video)
        case e_mode.AUDIO:
            # No official metadata for audio, just check for valid user tags
            parse_multi(root)


    print_stats()

if __name__ == "__main__":
    main()
