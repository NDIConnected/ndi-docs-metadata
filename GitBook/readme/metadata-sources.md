# Metadata Sources

## Metadata Frame (NDIlib\_metadata\_frame\_t)

This is the "normal" metadata channel for sending messages between NDI senders
and receivers. This channel is bidirectional and is used for generic
communications which do not have a specific association with a particular audio
or video frame.

## Connection Metadata

Connection metadata is a special class of metadata frames that can be registered
with the NDI SDK for both the sender and receiver. Upon establishing a new NDI
connection, the connection metadata is sent from sender to receiver and from
receiver to sender. There are several standard connection metadata elements
including `<ndi_product>`, `<ndi_capabilities>`, and `<ndi_format>`.

Connection metadata frames are sent automatically to each existing and new
connection after being registerd with the NDI SDK and are received as normal
metadata frames.

## Audio Frame Metadata

Audio frame metadata is used for communicating information that is specific to a
particular audio frame. There are currently no specific metadata elements
defined for audio metadata frames.

## Video Frame Metadata

Video frame metadata is used for communicating information that is specific to a
particular video frame.  Example metadata elements that should be passed as
video frame metadata include `<ndi_tracking_info>`, `<ndi_color_info>`, and
`<vancData>`.

Applications using video frame metadata need to be aware that individual video
frames can be dropped or duplicated, potentially causing missing or replicated
metadata.  This behavior is typically caused by using an NDI frame synchronizer
instance, which will drop or duplicate video frames occasionally to match frame
rates between the NDI sender and receiver.  In addition, prior to NDI 5.x the
preview video stream was limited to 30 fps, so preview streams created from full
streams with greater than 30 fps would drop video frames to meet the 30 fps
maximum.  Starting with NDI 5.0, preview streams are now sent using the same
frame rate as the full stream.  Users of the ASDK need to insure any required
video frame metadata is attached to both the full and the preview frame
submitted to the ASDK.
