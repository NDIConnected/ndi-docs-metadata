# Proposed New Metadata Messages

## `<vancData>` Element (CEA-708 & SCTE-104)

* Initial Implementation: ToolsOnAir
* Location: Video Frame Metadata

Legacy close captioning data and SCTE triggers are passed as NDI metadata by
encoding the corresponding SDI vertical ancillary data packets directly as XML.
Note that this method should not be used as a general solution for transitting
SDI Ancillary data via NDI, but is used in this case because workflows using
these protocols are very SDI centric and this method is supported by existing
equipment and workflows.

This mechanism should **NOT** be used to tunnel arbitrary SDI ancillary data which can readily be represented by XML.

```xml
<vancData version="1.0">
  <vancPacket did="97" sdid="1" line="9">lmlZT38BWHL0/ICA...3QBWEY=</vancPacket>
  <vancPacket did="65" sdid="7" line="10">CP//AB4AAQEAAgAAAQEBAA4BAAAAAwAAAAAAAAAAAA==</vancPacket>
</vancData>
```

#### `<vancData>` Attributes

| Attribute | Description                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| version   | <p>The <code>&#x3C;vancData></code> element must have a version attribute.<br>The version attribute supported by this standard is "1.0"</p> |

#### `<vancData>` Children

| Child        | Description                                                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `vancPacket` | This element contains the details for one ancillary data packet. Any number of vancPacket elements may be contained within one vancData element |

##### `vancPacket` Element

The `vancPacket` element provides details for one ancillary data packet. The
ancillary packet data is base64 encoded while the ancillary packet header
details are included as attributes of the vancPacket element.

DID and SDID values and ancillary data content are per SMPTE standards ST-334
(CEA-708) and ST-2010 (SCTE-104)

The following ancillary data packet types are currently supported:

* CEA-708 close caption: did="97" sdid="1"
* SCTE-104 trigger: did="65" sdid="7"

```xml
<vancPacket did="xs:int" sdid="xs:int" line="xs:int">xs:base64Binary</vancPacket>
```

##### `vancPacket` Attributes

| Attribute | Description                                               |
| --------- | --------------------------------------------------------- |
| did       | The ancillary packet DID (Data Identifier)                |
| sdid      | The ancillary packet SDID (Secondary Data Identifier)     |
| line      | The line number the ancillary data packet was received on |

## Midi `<ndi_metadata type="midi">` Element

* Initial Implementation: Lamamix
* Location: Metadata Frame
* Initial NDI Version: 6.1

```xml
<ndi_metadata type="midi">
  <data>903C403D20</data>
</ndi_metadata>
```

#### Midi `<ndi_metadata type="midi">` Children

| Child | Description                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| data  | Hexidecimal representation of a midi message. Data is read left to right (eg: 0x90 is the first byte transmitted and 0x20 is the last byte to be trasmitted) |

## DMX `<ndi_metadata type="dmx">` Element

* Initial Implementation: Salrayworks
* Location: Metadata Frame
* Initial NDI Version: 6.1

{% hint style="info" %}
Some early versions of DMX used the tag `<SALRAY_DMX>` instead of `<ndi_metadata
type="dmx">`. Devices receiving DMX via NDI Metadata should look for both
element names. Devices sending DMX via NDI metadata should use the
`<ndi_metadata type="dmx">` element with NDI SDK version 6.1 or newer.
{% endhint %}

```xml
<!-- Devices receiving DMX should also look for the <SALRAY_DMX> Element -->
<ndi_metadata type="dmx">
  <Universe id="1">
    <Stream>
      <Address>"1"</Address>
      <Data>01FF0304050607</Data>
    </Stream>
    <Stream>
      <Address>"8"</Address>
      <Data>1A10A0023</Data>
    </Stream>
  </Universe>
  <Universe id="2">
    <Stream>
      <Address>2</Address>
      <Data>02FF004567</Data>
    </Stream>
  </Universe>
  <Universe id="3">
    <!-- No streams for this universe -->
  </Universe>
</ndi_metadata>
```

#### DMX `<ndi_metadata type="dmx">` Children

| Child    | Description                                                  |
| -------- | ------------------------------------------------------------ |
| Universe | DMX transmit channel. Multiple universe elements are allowed |

##### **`Universe` Attributes**

| Attribute | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| id        | DMX transmit channel: 1 (first channel) to the capacity of the DMX controller |

##### **`Universe` Children**

| Child  | Description                                               |
| ------ | --------------------------------------------------------- |
| Stream | Represents DMX data. Multiple stream elements are allowed |

##### **`Stream` Children**

| Child   | Description                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Address | Starting DMX channel: 1 to 512                                                                                                       |
| Data    | Hexidecimal representation of DMX data. Data is read left to right (eg: 0x01 is the first byte transmitted for universe 1, address 1 |

## Timed Text Captions

* Initial Implementation: Various standards bodies
* Location: Metadata Frame

Modern captioning solutions are migrating to a variety of XML based timed text formats such as:

* TTML1
* SDP-US
* IMSC1
* SMPTE-TT
* EBU-TT
* CFF-TT

As these formats are natively XML they can be easily incorporated into an NDI
stream as metadata.  As a transport protocol, NDI does not natively prefer any
one of these standards over the others.  The properly formed XML conforming to
one (or more) of these standards should simply be sent as an NDI metadata frame,
optionally as the child of an `<ndi_metadata_group>` element if for some reason
more than one element needs to be sent in the same metadata frame.

W3C has a good overview of the various timed text caption standards including
links to many of the specifications:
https://www.w3.org/AudioVideo/TT/docs/TTML-Profiles.html

As a general rule, it is suggested that applications sending timed-text captions
use the minimum set of features necessary for full operation.  Receivers should
be able to process any Well Formed XML, ignoring any elements or attributes they
do not currenntly implement.

If you are interested in supporting any of the timed-text captioning solutions
in real-world workflows, the NDI team would be happy to coordinate with you to
help insure consistency and interoperability across the NDI ecosystem.
