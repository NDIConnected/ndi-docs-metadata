# Proposed New Metadata Messages

## `<vancData>` Element (CEA-708 & SCTE-104)

> Initial Implementation: [**ToolsOnAir**](https://www.toolsonair.com/)
>
> Location: **Video Frame Metadata**

Legacy close captioning data and SCTE triggers are passed as NDI metadata by encoding the corresponding SDI vertical ancillary data packets directly as XML. Note that this method should not be used as a general solution for transitting SDI Ancillary data via NDI, but is used in this case because workflows using these protocols are very SDI centric and this method is supported by existing equipment and workflows.

{% hint style="warning" %}
This mechanism should **NOT** be used to tunnel arbitrary SDI ancillary data which can readily be represented by XML.
{% endhint %}

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

**`vancPacket` Element**

The `vancPacket` element provides details for one SMPTE ST-291 ancillary data
packet.  The various ST-291 elements map to the `vancPacket` element as follows:

* ADF: Ancillary Data Flag: Not transmitted
* DID: Data ID: Sent as an attribute
* SDID: Secondary DID: Sent as an attribute
* DC: Data Count: Not transmitted
* UDW: User Data Words: Sent as text content, 8-bit, base64 encoded
* CS: Checksum: Not transmitted

Note that the user data word content of the ancillary data packet is sent as
base64 encoded 8-bit data.  Bits 8 (parity) and 9 (NOT bit 8) are not
transmitted.

DID and SDID values and ancillary data content are per SMPTE standards ST-334
(CEA-708) and ST-2010 (SCTE-104).

The following ancillary data packet types are currently supported:

* CEA-708 close caption: did="97" sdid="1"
* SCTE-104 trigger: did="65" sdid="7"

```xml
<vancPacket did="xs:int" sdid="xs:int" line="xs:int">xs:base64Binary</vancPacket>
```

**`vancPacket` Attributes**

| Attribute | Description                                               |
| --------- | --------------------------------------------------------- |
| did       | The ancillary packet DID (Data Identifier)                |
| sdid      | The ancillary packet SDID (Secondary Data Identifier)     |
| line      | The line number the ancillary data packet was received on |

## Midi `<ndi_metadata type="midi">` Element

> Initial Implementation: [**Lamamix**](https://lamamix.com/)
>
> Location: **Metadata Frame**
>
> Initial NDI Version: **6.1**

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

> Initial Implementation: [**Salrayworks**](https://www.salrayworks.com/)
>
> Location: **Metadata Frame**
>
> Initial NDI Version: **6.1**

{% hint style="info" %}
Some early versions of DMX used the tag `<SALRAY_DMX>` instead of `<ndi_metadata type="dmx">`. Devices receiving DMX via NDI Metadata should look for both element names. Devices sending DMX via NDI metadata should use the `<ndi_metadata type="dmx">` element with NDI SDK version 6.1 or newer.
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

**`Universe` Attributes**

| Attribute | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| id        | DMX transmit channel: 1 (first channel) to the capacity of the DMX controller |

**`Universe` Children**

| Child  | Description                                               |
| ------ | --------------------------------------------------------- |
| Stream | Represents DMX data. Multiple stream elements are allowed |

**`Stream` Children**

| Child   | Description                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Address | Starting DMX channel: 1 to 512                                                                                                       |
| Data    | Hexidecimal representation of DMX data. Data is read left to right (eg: 0x01 is the first byte transmitted for universe 1, address 1 |

## HDR `<ndi_metadata type="hdr">` Element

> Initial Implementation: [**Vizrt**](https://www.vizrt.com/)
>
> Location: **Video Frame Metadata**
>
> Initial NDI Version: **6.1**

This metadata element is used to transport additional metadata required for HDR
beyond what is specified in the `ndi_color_info` element.

```xml
<ndi_metadata type="hdr" version="1.0">
  <mastering_display_color_volume>
    <primaries>
      <green x="13250" y="34500"/>
      <blue x="7500" y="3000"/>
      <red x="34000" y="16000"/>
    </primaries>
    <white_point x="15635" y="16450"/>
    <luminance max="10000000" min="1"/>
  </mastering_display_color_volume>
  <content_light_level maxCLL="1000" maxFALL="400"/>
</ndi_metadata>
```

#### HDR `<ndi_metadata type="hdr">` Attributes

| Attribute | Description                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| version   | <p>The <code>&#x3C;ndi_metadata type="hdr"></code> element must have a version attribute.<br>The version attribute supported by this standard is "1.0"</p> |

#### HDR `<ndi_metadata type="hdr">` Children

| Child    | Description                                                  |
| -------- | ------------------------------------------------------------ |
| mastering_display_color_volume | Mastering display color volume, per SMPTE [ST-2086](https://pub.smpte.org/doc/st2086/). Carries the payload of SEI message 137. One element per `<ndi_metadata type="hdr">` element, sent only when the source signaled the metadata |
| content_light_level            | Content light level information, per [CTA-861](https://members.cta.tech/ctaPublicationDetails/?id=11016f33-3422-e811-90ce-0003ff528c1a). Carries the payload of SEI message 144. One element per `<ndi_metadata type="hdr">` element, sent only when the source signaled the metadata  |

**`mastering_display_color_volume` Element**

The `mastering_display_color_volume` element provides the chromaticity
coordinates and luminance range of the display the content was graded on. This
element is all-or-nothing, every child element and attribute is required.  A
receiver that finds `mastering_display_color_volume` incomplete, out of range,
or malformed **MUST** treat the entire `mastering_display_color_volume` subtree
as absent rather than substituting defaults for the missing parts.

Values are defined by SMPTE [ST-2086](https://pub.smpte.org/doc/st2086/) and are
mapped to integer values per the "Mastering display colour volume" SEI message
(SEI-137) syntax specified in ITU-T
[H.264](https://www.itu.int/rec/T-REC-H.264/en) (D.2.29) and
[H.265](https://www.itu.int/rec/T-REC-H.265/en) (D.2.28).

Chromaticity and luminance values outside of the valid ranges listed below may
be transmitted and can be used for purposes outside the scope of this
specification.

**`mastering_display_color_volume` Children**

| Child  | Description                                               |
| ------ | --------------------------------------------------------- |
| primaries | The normalized chromaticity coordinates of the mastering display |
| white_point | The normalized chromaticity coordinate of the white point of the mastering display |
| luminance | The nominal maximum and minimum display luminance of the mastering display |

**`primaries` Children**

The normalized chromaticity coordinates of the mastering display

| Child  | Description                                               |
| ------ | --------------------------------------------------------- |
| green  | Chromaticity of the green primary<br>Maps to `display_primaries_x[0]` and `display_primaries_y[0]` |
| blue   | Chromaticity of the blue primary<br>Maps to `display_primaries_x[1]` and `display_primaries_y[1]` |
| red   | Chromaticity of the red primary<br>Maps to `display_primaries_x[2]` and `display_primaries_y[2]` |

**`green`, `blue`, and `red` Attributes**

| Attribute  | Description                                               |
| ------ | --------------------------------------------------------- |
| x      | The CIE 1931 x chromaticity coordinate of the primary, as an unsigned 16-bit integer (`xs:unsignedShort`) in units of 0.00002.<br>Valid range: 5 to 37000, inclusive. |
| y      | The CIE 1931 y chromaticity coordinate of the primary, as an unsigned 16-bit integer (`xs:unsignedShort`) in units of 0.00002.<br>Valid range: 5 to 42000, inclusive. |

**`white_point` Attributes**

| Attribute  | Description                                               |
| ------ | --------------------------------------------------------- |
| x      | The CIE 1931 x chromaticity coordinate of the white point, as an unsigned 16-bit integer (`xs:unsignedShort`) in units of 0.00002.<br>Valid range: 5 to 37000, inclusive, 0 indicates unknown.<br>Maps to `white_point_x` |
| y      | The CIE 1931 y chromaticity coordinate of the white point, as an unsigned 16-bit integer (`xs:unsignedShort`) in units of 0.00002.<br>Valid range: 5 to 42000, inclusive, 0 indicates unknown.<br>Maps to `white_point_y` |

**`luminance` Attributes**

| Attribute | Description                                               |
| ------ | --------------------------------------------------------- |
| max    | The peak luminance of the mastering display, as an unsigned 32-bit integer (`xs:unsignedInt`) in units of 0.0001 cd/m².<br>Valid range: 50000000 to 1000000000 inclusive.<br>Maps to `max_display_mastering_luminance` |
| min    | The black level of the mastering display, as an unsigned 32-bit integer (`xs:unsignedInt`) in units of 0.0001 cd/m².<br>Valid range: 1000 to 50000000, inclusive, must be less than max.<br>Maps to `min_display_mastering_luminance` |

**`content_light_level` Element**

The `content_light_level` element provides the peak and frame-average light
levels of the content itself.

Values are defined by
[CTA-861](https://members.cta.tech/ctaPublicationDetails/?id=11016f33-3422-e811-90ce-0003ff528c1a)
and are mapped to integer values per the "Content light level information" SEI
message (SEI-144) syntax specified in ITU-T
[H.264](https://www.itu.int/rec/T-REC-H.264/en) (D.2.31) and
[H.265](https://www.itu.int/rec/T-REC-H.265/en) (D.2.35).

**`content_light_level` Attributes**

| Attribute | Description                                               |
| ------ | --------------------------------------------------------- |
| maxCLL | Maximum Content Light Level: the light level of the brightest pixel in the content, in cd/m², as an unsigned 16-bit integer (`xs:unsignedShort`). Range 0 to 65535, where 0 means unknown.<br>Maps to `max_content_light_level` |
| maxFALL | Maximum Frame-average Light Level: the highest frame-average light level in the content, in cd/m², as an unsigned 16-bit integer (`xs:unsignedShort`). Range 0 to 65535, where 0 means unknown.<br>Maps to `max_pic_average_light_level` |

Both attributes are independently optional, omit the element entirely when both
values are unknown.

A value of 0 means "unknown", as per the SEI message semantics.

## Timed Text Captions

* Initial Implementation: **Various standards bodies**
* Location: **Metadata Frame**

Modern captioning solutions are migrating to a variety of XML based timed text formats such as:

* TTML1
* SDP-US
* IMSC1
* SMPTE-TT
* EBU-TT
* CFF-TT

As these formats are natively XML they can be easily incorporated into an NDI stream as metadata. As a transport protocol, NDI does not natively prefer any one of these standards over the others. The properly formed XML conforming to one (or more) of these standards should simply be sent as an NDI metadata frame, optionally as the child of an `<ndi_metadata_group>` element if for some reason more than one element needs to be sent in the same metadata frame.

W3C has a good overview of the various timed text caption standards including links to many of the specifications: https://www.w3.org/AudioVideo/TT/docs/TTML-Profiles.html

As a general rule, it is suggested that applications sending timed-text captions use the minimum set of features necessary for full operation. Receivers should be able to process any Well Formed XML, ignoring any elements or attributes they do not currenntly implement.

If you are interested in supporting any of the timed-text captioning solutions in real-world workflows, the NDI team would be happy to coordinate with you to help insure consistency and interoperability across the NDI ecosystem.
