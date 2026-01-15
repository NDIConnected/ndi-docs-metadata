# Metadata & XML

## NDI Metadata and XML

While NDI metadata is formatted as XML, there are some differences between XML used for NDI metadata frames and a more conventional stand-alone XML file. This section discusses how XML standards apply to NDI metadata frames.

## XML Prolog

NDI metadata frames should not contain an XML prolog. Each NDI Metadata frame can be assumed to have the following prolog, indicating XML version 1.0 compliance and UTF-8 encoding.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

## XML Syntax

NDI metadata frames should be "Well Formed" XML documents with correct syntax. Please check the following:

* [x] Metadata should have one and only one root element
* [x] XML elements must have a closing tag
* [x] XML tags are case sensitive
* [x] XML elements must be properly nested
* [x] XML attribute values must be quoted

## XML Root Element

As a "Well Formed" XML document, an NDI metadata frame can only have one root element. If there is a need to pass more than one XML element in an NDI metadata frame, the root element should be set to `<ndi_metadata_group>` and the required XML elements can be passed as children to this root element.

{% hint style="info" %}
See the documentation for the `<ndi_metadata_group>` element, below, for example usage.
{% endhint %}

## XML Comments

XML comments are allowed but **discouraged** in NDI metadata frames.

## XML Namespaces

XML namespaces are **not supported** in NDI metadata frames.

## XML Element Names

With the exception of element names defined in this document, no XML element passed in a metadata frame to the NDI SDK should begin with the string `ndi` or `ntk` (or any permutation of capitalization,eg: `Ndi`).
