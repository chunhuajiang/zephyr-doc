:orphan:

.. title:: CC3200SDK_LIBRARY

.. option:: CONFIG_CC3200SDK_LIBRARY:
.. _CONFIG_CC3200SDK_LIBRARY:

The CC3200 SDK provides a static library (libdriver.a)
which implements peripheral APIs for the CC3200.



:Symbol:           CC3200SDK_LIBRARY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Link with CC3200 SDK static driver library"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CC3200SDK`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_CC3200SDK (value: "n")
:Locations:
 * ../ext/hal/ti/cc3200sdk/Kconfig:22