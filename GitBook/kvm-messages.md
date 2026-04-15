# KVM Messages

> Initial Implementation: **NewTek**
>
> Location: **Sent via SDK API calls, received as Metadata frames**

## API calls

A variety of API calls can be used by an NDI receive instance to send KVM events
to an NDI sender.  These API calls are briefly listed below.  For further
details refer to the `Processing.NDI.KVM.h` include file provided with the SDK.

### Detecting KVM Support

Senders indicate support for KVM via the `<ndi_capabilities>` connection
metadata element.

Receivers can test to see if the sender supports KVM using the API call:

* `NDIlib_recv_kvm_is_supported()`

### Mouse Button Support

The following API calls are used to send mouse button press and release events
to the NDI sender:

* `NDIlib_recv_kvm_send_left_mouse_click()`
* `NDIlib_recv_kvm_send_middle_mouse_click()`
* `NDIlib_recv_kvm_send_right_mouse_click()`
* `NDIlib_recv_kvm_send_left_mouse_release()`
* `NDIlib_recv_kvm_send_middle_mouse_release()`
* `NDIlib_recv_kvm_send_right_mouse_release()`

### Mouse Scroll Wheel Support

The following API calls are used to send mouse scroll wheel events to the NDI
sender:

* `NDIlib_recv_kvm_send_vertical_mouse_wheel()`
* `NDIlib_recv_kvm_send_horizontal_mouse_wheel()`

The scroll value is scaled such that one wheel click is equal to 120.

### Mouse Position Support

Mouse position updates are sent with the API call:

* `NDIlib_recv_kvm_send_mouse_position()`

Mouse coordinates are absolute with 0.0 representing the top and left side of
the screen and 1.0 representing the bottom and right side of the screen.

### Clipboard Support

Text clipboard content can be sent with the API call:

* `NDIlib_recv_kvm_send_clipboard_contents()`

Clipboard data must be a null terminated text string.

### Touch Support

The following API calls are used to send touch events to the NDI sender:

* `NDIlib_recv_kvm_send_touch_positions()`
* `NDIlib_recv_kvm_send_touch_finish()`

The touch data is an array of positions, with each position defined such that
0.0 represents the top or left side of the screen and 1.0 represents the bottom
or right side of the screen.

### Keyboard Support

The following API calls are used to send keyboard events to the NDI sender:

* `NDIlib_recv_kvm_send_keyboard_press()`
* `NDIlib_recv_kvm_send_keyboard_release()`

Key codes are defined in the file `Processing.NDI.KVM.keysymdef.h`.

## `<ndi_kvm>` Element

NDI KVM messages are received at the sender as a metadata element with a Base64
encoded binary structure sent as an attribute.

```xml
<ndi_kvm u="A7WeJj9e7Tg/AQ=="/>
<ndi_kvm d="eNrjZQCCktTiEgYABqUBzg=="/>
```

#### `<ndi_kvm>` Attributes

| Attribute | Description                                            |
| --------- | -------------------------------------------------------|
| u         | Base64 encoded uncompressed NDI KVM Message struct     |
| d         | Base64 encoded zlibl compressed NDI KVM Message struct |

There must be exactly one `u` or `d` attribute present.  It is an error for
both attributes to be present in the same `<ndi_kvm>` element, or for neither
attribute to be present.

The Base64 data should be decoded into binary.  Uncompressed messages are then
interpreted per the structure and enumeration definitions found in
`Processing.NDI.KVM.h`.  Compressed messages need to be additionally
decompressed using zlib before being interpreted as a KVM message struct.

The example uncompressed message above represents a cursor position message:

```sh
$ echo A7WeJj9e7Tg/AQ== | base64 -d | hexdump -C
00000000  03 b5 9e 26 3f 5e ed 38  3f 01                    |...&?^.8?.|
0000000a
```

The example compressed message above represents a clipboard message with the
contents "test":

```sh
$ echo eNrjZQCCktTiEgYABqUBzg== | base64 -d | zlib-flate -uncompress | hexdump -C
00000000  0d 00 00 00 00 74 65 73  74 00                    |.....test.|
0000000a
```
