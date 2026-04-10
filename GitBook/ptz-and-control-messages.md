# PTZ and Control Messages

> Initial Implementation: **NewTek**
>
> Location: **Sent via SDK API calls, received as Metadata frames**

## `<ntk_ptz_zoom>` Element

Set zoom to an absolute value: `NDIlib_recv_ptz_zoom()`

```xml
<ntk_ptz_zoom zoom="0.185000"/>
```

#### `<ntk_ptz_zoom>` Attributes

| Attribute | Description                                                  |
| --------- | ------------------------------------------------------------ |
| zoom      | Absolute value for zoom: 0.0 (zoomed in) to 1.0 (zoomed out) |

## `<ntk_ptz_zoom_speed>` Element

Zoom at a particular speed: `NDIlib_recv_ptz_zoom_speed()`

```xml
<ntk_ptz_zoom_speed zoom_speed="0.005000"/>
```

#### `<ntk_ptz_zoom_speed>` Attributes

| Attribute   | Description                                             |
| ----------- | ------------------------------------------------------- |
| zoom\_speed | Zoom speed: -1.0 (zoom outwards) to +1.0 (zoom inwards) |

## `<ntk_ptz_pan_tilt>` Element

Set the pan and tilt to an absolute value: `NDIlib_recv_ptz_pan_tilt()`

```xml
<ntk_ptz_pan_tilt pan="0.015000" tilt="-0.015000"/>
```

#### `<ntk_ptz_pan_tilt>` Attributes

| Attribute | Description                                                  |
| --------- | ------------------------------------------------------------ |
| pan       | Pan location: -1.0 (left) to 0.0 (centered) to +1.0 (right)  |
| tilt      | Tilt location: -1.0 (bottom) to 0.0 (centered) to +1.0 (top) |

## `<ntk_ptz_pan_tilt_speed>` Element

Pan and tilt at a particular speed: `NDIlib_recv_ptz_pan_tilt_speed()`

```xml
<ntk_ptz_pan_tilt_speed pan_speed="0.015000" tilt_speed="-0.015000"/>
```

#### `<ntk_ptz_pan_tilt_speed>` Attributes

| Attribute   | Description                                                     |
| ----------- | --------------------------------------------------------------- |
| pan\_speed  | Pan speed: -1.0 (pan right) to 0.0 (stopped) to +1.0 (pan left) |
| tilt\_speed | Tilt speed: -1.0 (tilt down) to 0.0 (stopped) to +1.0 (tilt up) |

## `<ntk_ptz_focus>` Element

Set focus mode and distance:

* `NDIlib_recv_ptz_auto_focus()`
* `NDIlib_recv_ptz_focus()`
* `NDIlib_recv_ptz_focus_speed()`

```xml
<ntk_ptz_focus mode="auto"/>
<ntk_ptz_focus mode="manual" distance="0.485000"/>
```

#### `<ntk_ptz_focus>` Attributes

| Attribute | Description                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------- |
| mode      | Sets focus mode: "manual" or "auto"                                                                           |
| distance  | Focus distance: 0.0 (infinity) to 1.0 (focused as close as possible). Optional, only valid when mode="manual" |

## `<ntk_ptz_recall_preset>` Element

Recall settings from a particular preset: `NDIlib_recv_ptz_recall_preset()`

```xml
<ntk_ptz_recall_preset index="1"/>
<ntk_ptz_recall_preset index="2" speed="0.5"/>
```

#### `<ntk_ptz_recall_preset>` Attributes

| Attribute | Description                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| index     | The preset index to recall: 0 to 99                                                                                            |
| speed     | How fast to move to the new preset: 0.0 (slowest) to 1.0 (fastest). Optional, should default to 1.0 (fastest) if not specified |

## `<ntk_ptz_store_preset>` Element

Store current settings to a particular preset: `NDIlib_recv_ptz_store_preset()`

```xml
<ntk_ptz_store_preset index="2"/>
```

#### `<ntk_ptz_store_preset>` Attributes

| Attribute | Description                        |
| --------- | ---------------------------------- |
| index     | The preset index to store: 0 to 99 |

## **`<ntk_ptz_white_balance>` Element**

Sets the white balance:

* `NDIlib_recv_ptz_white_balance_auto()`
* `NDIlib_recv_ptz_white_balance_indoor()`
* `NDIlib_recv_ptz_white_balance_outdoor()`
* `NDIlib_recv_ptz_white_balance_oneshot()`
* `NDIlib_recv_ptz_white_balance_manual()`

```xml
<ntk_ptz_white_balance mode="auto"/>
<ntk_ptz_white_balance mode="manual" red="0.5" blue="0.5"/>
```

#### `<ntk_ptz_white_balance>` Attributes

| Attribute | Description                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| mode      | White balance mode:auto, indoor, outdoor, one\_shot, or manual one\_shot (one\_push?) locks the current white balance setting |
| red       | Manual red value: 0.0 (not red) to 1.0 (very red). Only present when mode="manual"                                            |
| blue      | Manual blue value: 0.0 (not blue) to 1.0 (very blue). Only present when mode="manual"                                         |

## `<ntk_ptz_exposure>` Element

Sets the exposure settings:

* `NDIlib_recv_ptz_exposure_auto()`
* `NDIlib_recv_ptz_exposure_manual()`
* `NDIlib_recv_ptz_exposure_manual_v2()`

```xml
<ntk_ptz_exposure mode="auto"/>
<ntk_ptz_exposure mode="manual" value="0.5"/>
<ntk_ptz_exposure mode="manual" value="0.5" gain="0.75" shutter="0.8"/>
```

#### `<ntk_ptz_exposure>` Attributes

| Attribute | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| mode      | Exposure mode: auto or manual                                          |
| value     | Iris setting: 0.0 (dark) to 1.0 (light). Only valid when mode="manual" |
| gain      | Gain setting: 0.0 (dark) to 1.0 (light). Only valid when mode="manual" |
| shutter   | Shutter speed: 0.0 (slow) to 1.0 (fast). Only valid when mode="manual" |
