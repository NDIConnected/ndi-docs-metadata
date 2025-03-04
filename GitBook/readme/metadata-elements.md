# Metadata Elements

## `<ndi_product>` Element

* Initial Implementation: Vizrt
* Location: Connection Metadata

Used by both NDI senders and receivers to indicate product details.

```xml
<ndi_product
    long_name="NDILib Receive Example."
    short_name="NDILib Receive"
    manufacturer="CoolCo, Inc."
    model_name="PBX-42Q"
    version="1.000.000"
    serial="ABCDEFG"
    session_name="My Midday Show" />
```

#### `<ndi_product>` Attributes

| Attribute      | Description                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------ |
| `long_name`    | Full human readable product name                                                                       |
| `short_name`   | Abbreviated human readable product name                                                                |
| `manufacturer` | Product manufacturer                                                                                   |
| `version`      | Product firmware version                                                                               |
| `model_name`   | Product model name                                                                                     |
| `serial`       | Product serial number                                                                                  |
| `session_name` | <p>Session name for TriCaster or similar products<br>General product information for other devices</p> |

## `<ndi_capabilities>` Element

* Initial Implementation: Vizrt
* Location: Connection Metadata

Indicated product capabilities for both NDI senders and receivers. Most capabilities are sender specific (ptz and exposure control) but NDI receivers will often have a web\_control URL.

```xml
<ndi_capabilities
    web_control="http://ndi.video/"
    ntk_ptz="true"
    ntk_exposure_v2="true" />
```

#### `<ndi_capabilities>` Attributes

| Attribute                  | Description                                                                                                                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| web\_control="URL"         | The URL to the local device webpage. If %IP% is present in the value, it will be replaced with the local IP of the NIC in which the NDI receiver is connected to.                                                                     |
| ntk\_ptz="true"            | Signifies that this NDI sender is capable of processing PTZ commands sent from the NDI receiver. The NDI receiver will only assume the NDI sender can support PTZ commands if this attribute is received and set to the value “true”. |
| ntk\_pan\_tilt="true"      | The NDI sender supports pan and tilt control.                                                                                                                                                                                         |
| ntk\_zoom="true"           | The NDI sender supports zoom control.                                                                                                                                                                                                 |
| ntk\_iris="true"           | The NDI sender supports iris control.                                                                                                                                                                                                 |
| ntk\_white\_balance="true" | The NDI sender supports white balance control.                                                                                                                                                                                        |
| ntk\_exposure="true"       | The NDI sender supports exposure control.                                                                                                                                                                                             |
| ntk\_exposure\_v2="true"   | The NDI sender supports detailed control over exposure such as iris, gain, and shutter speed.                                                                                                                                         |
| ntk\_focus="true"          | The NDI sender supports manual focus control.                                                                                                                                                                                         |
| ntk\_autofocus="true"      | The NDI sender supports setting auto focus.                                                                                                                                                                                           |
| ntk\_preset\_speed="true"  | The NDI sender has preset speed support.                                                                                                                                                                                              |

## `<ndi_format>` Element

* Initial Implementation: Vizrt
* Location: Connection Metadata

Sent by an NDI receiver to indicate it's preferred or native format.

```xml
<ndi_format>
  <video_format xres="1920" yres="1080"
                frame_rate_n="60000" frame_rate_d="1001"
                aspect_ratio="1.77778" progressive="true"
  />
  <audio_format no_channels="4" sample_rate="48000"/>
</ndi_format>
```

#### `<ndi_format>` Children

At least one of the following child elements is required.

| Child            | Description          |
| ---------------- | -------------------- |
| `<video_format>` | Video format details |
| `<audio_format>` | Audio format details |

**`<video_format>` Attributes**

| Attribute      | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| xres           | Horizontal resolution in pixels                                            |
| yres           | Vertical resolution in lines                                               |
| frame\_rate\_n | Numerator portion of the frame rate                                        |
| frame\_rate\_d | Denominator portion of the frame rate                                      |
| aspect\_ratio  | The picture aspect ratio, 0 means square pixel                             |
| progressive    | Indicates progressive format when "true" or interlaced format when "false" |

**`<audio_format>` Attributes**

| Attribute    | Description                            |
| ------------ | -------------------------------------- |
| no\_channels | The number of audio channels           |
| sample\_rate | The number of audio samples per second |

## `<ndi_color_info>` Element

* Initial Implementation: Vizrt
* Location: Video Frame Metadata
* Initial NDI Version: 6.0

The `<ndi_color_info>` element provides colorimitry details for the associated video frame.

```xml
<ndi_color_info
    transfer="bt_2100_hlg"
    matrix="bt_2020"
    primaries="bt_2020"
/>
```

#### `<ndi_color_info>` Attributes

| Attribute | Description                                                                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| primaries | <p>Specifies the chromaticity coordinates of the color primaries of the video frame.<br>One of: “bt_601”, “bt_709”, “bt_2020”, or “bt_2100”</p>             |
| transfer  | <p>Specifies the brightness transfer characteristic.<br>One of: “bt_601”, “bt_709”, “bt_2020”, “bt_2100_hlg”, or “bt_2100_pq”</p>                           |
| matrix    | <p>Specifies the matrix coefficients used in deriving luma and chroma from RGB or XYZ primaries.<br>One of: “bt_601”, “bt_709”, “bt_2020”, or “bt_2100”</p> |

## `<ndi_metadata_group>` Element

* Initial Implementation: Vizrt
* Location: Metadata (all flavors)
* Initial NDI Version: 6.0 for video frame metadata, 6.1 for generic metadata frames

Properly formatted XML allows only one root element. If multiple metadata elements need to be attached to a single audio or video frame, they should be grouped together as child elements of an `ndi_metadata_group` root element.

```xml
<ndi_metadata_group>
  <ndi_color_info>
    <!-- ndi_color_info content goes here -->
  </ndi_color_info>
  <ndi_tracking_info>
    <!-- ndi_tracking_info content goes here -->
  </ndi_tracking_info>
  <!-- Additional element tags can go here -->
</ndi_metadata_group>
```

## `<ndi_tracking_info>` Element

* Initial Implementation: Vizrt
* Location: Video Frame Metadata
* Initial NDI Version: 5.x

````xml
<ndi_tracking_info version="1.0.0">
    <package type="binary" protocol="FreeD">
        <!-- Timestamp is optional -->
        <!-- The tag name is optional, if not present we mean capture timestamp -->
        <timestamp
            name="capture"
            type="xs:dateTimeStamp">2022-07-25T13:20:00.123Z
        </timestamp>
        <!-- We expect binary.base64 string here -->
        <data>MTIzNDU2Nzg5MDEyMzQ1Njc4OTA=</data>
    </package>

    <package type="axis" protocol="FreeD">
        <!-- Timestamp is optional -->
        <timestamp
            name="capture"
            type="xs:dateTimeStamp">2004-04-12T13:20:00.123-05:00
        </timestamp>
        <!-- the naming must be present and unique for the package -->
        <!-- The datatype is mandatory! -->
        <axis name="id" type="xs:integer" value="1" />
        <axis name="posx" type="xs:integer" value="237" />
        <axis name="posy" type="xs:integer" value="9356" />
        <axis name="posz" type="xs:integer" value="44" />
        <axis name="rotx" type="xs:integer" value="23" />
        <axis name="roty" type="xs:integer" value="34" />```
        <axis name="rotz" type="xs:integer" value="43" />
        <axis name="zoom" type="xs:integer" value="12" />
        <axis name="focus" type="xs:integer" value="6785" />
        <axis name="iris" type="xs:integer" value="12" />
        <axis name="extender" type="xs:boolean" value="true" />
    </package>

    <package type="axis" protocol="TrackMen">
        <timestamp
            name="capture"
            type="xs:dateTimeStamp">2004-04-12T13:20:00.123Z
        </timestamp>
        <axis name="posx" type="xs:float" value="23.3" />
        <axis name="posy" type="xs:float" value="45.6" />
        <axis name="posz" type="xs:float" value="44.12223" />
        <axis name="rotx" type="xs:float" value="34" />
        <axis name="roty" type="xs:float" value="45" />
        <axis name="rotz" type="xs:float" value="56.006" />
        <axis name="zoom" type="xs:integer" value="23" />
        <axis name="focus" type="xs:integer" value="7877" />
        <axis name="k1" type="xs:float" value="0.123" />
        <axis name="k2" type="xs:float" value="1.4" />
        <axis name="chipX" type="xs:float" value="23" />
        <axis name="chipY" type="xs:float" value="34" />
        <axis name="centerX" type="xs:float" value="233" />
        <axis name="centerY" type="xs:float" value="0.45" />
    </package>
</ndi_tracking_info>
````

#### `<ndi_tracking_info>` Attributes

| Attribute | Description                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| version   | The `<ndi_tracking_info>` element must have a version attribute. The version attribute is defined as string with the regex format: `[0-9]+.[0- 9]+.[0-9]+` |

#### `<ndi_tracking_info>` Children

| Child       | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| `<package>` | `<ndi_tracking_info>` can contain zero or more `<package>` elements |

#### `<package>` Element

The `<package>` element holds one single tracking package. This element contains no text.

```xml
<package
    type="binary"
    protocol="name of protocol">
    <!-- optional --> <timestamp...>
    <data...>
</package>
```

or

```xml
<package
    type="axis"
    protocol="name of protocol">
    <!-- optional --> <timestamp.../>
    <axis.../>
</package>
```

#### `<package>` Attributes

| Attribute | Description                                                                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type      | The `<package>` element must have an attribute named type with a value of either `binary` or `axis`                                                             |
| protocol  | The value of the attribute `protocol` is the name of the tracking protocol which is embedded in the XML description of `<package>`. This attribute is mandatory |

#### `<package>` Children

| Child         | Description                                                                    |
| ------------- | ------------------------------------------------------------------------------ |
| `<timestamp>` | The `<timestamp>` element is optional                                          |
| `<data>`      | If the type of the is binary then exactly one `<data>` element is mandatory.   |
| `<axis>`      | If the type of the is axis then one or more `<axis>` elements must be present. |

**`<timestamp>` Element**

When present, the element can provide some additional timestamp information different from the timestamp on the NDI video frame. This element contains no text and has no children.

```xml
<timestamp
  name="type of timestamp"
  type="xs:dateTimeStamp">13:20:00.123Z
</timestamp>
```

**`<timestamp>` Attributes**

| Attribute | Description                                                                                                                                                                                                                                                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name      | Is optional and defines the process step when the timestamp was taken. If name is not given, the timestamp will be marked as capture which means the time the video frame was recorded. If the name attribute is not capture, then the timestamp on the NDI video frame is taken as capture timestamp. _Please see Appendix Timestamp names._ |
| type      | Is mandatory and has a fixed value of xs:dateTimeStamp. The timestamp value must follow the xs:dateTimeStamp format. _Please see_ [_https://www.w3.org/TR/xmlschema11-2/#dateTimeStamp_](https://www.w3.org/TR/xmlschema11-2/#dateTimeStamp)_. A UTC timestamp is preferable._                                                                |

**`<data>` Element**

The element contains the binary representation of the protocol. This element has no attributes and no children. The text value must be encoded in the xs:base64Binary format. Please see [https://www.w3schools.com/xml/schema\_dtypes\_misc.asp](https://www.w3schools.com/xml/schema_dtypes_misc.asp)

```xml
<!-- We expect binary.base64 string here -->
<data> MTIzNDU2Nzg5MDEyMzQ1Njc4OTA=</data>
```

**`<axis>` Element**

The `<axis>` element contains data for one axis. This element contains no text and has no children.

```xml
<!-- name and type are mandatory! -->
<axis name="id" type="xs:integer" value="1" />
<axis name="posx" type="xs:integer" value="23" />
```

**`<axis>` Attributes**

| Attribute | Description                                                                                                                                                                                                                                                                                                           |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name      | Identifies the axis. If the name is known by the Tracking Hub, the assignment to the rig axis can be done automatically. If not, the assignment must be done by the operator. Either way, a unique name must be given.                                                                                                |
| type      | <p>Identifies the format of the content of the <code>&#x3C;axis></code> element. The <code>type</code> attribute must be one of the following:</p><ul><li><code>xs:integer</code></li><li><code>xs:float</code></li><li><code>xs:boolean</code></li><li><code>xs:double</code></li><li><code>xs:long</code></li></ul> |
| value     | The value of the axis. The type must match the attribute `type`.                                                                                                                                                                                                                                                      |

## `<ndi_video_codec>` Element

* Initial Implementation: NewTek
* Location: Metadata

Sent via NDIlib\_recv\_send\_metadata() by the application which created the NDI receive instance.

This requests the NDI library use the specified decoding method for H.264 and H.265 NDI video streams. Note that the internal heuristics should generally be allowed to select the codec type in most circumstances.

Note this element can only be sent by an application to an NDI receiver instance, this element will never be received in a Metadata frame by an NDI sender or receiver instance.

```xml
<ndi_video_codec type="hardware"/>
```

#### `<ndi_video_codec>` Attributes

| Attribute | Description                                                 |
| --------- | ----------------------------------------------------------- |
| type      | <p>Video codec type<br>One of: "hardware" or "software"</p> |
