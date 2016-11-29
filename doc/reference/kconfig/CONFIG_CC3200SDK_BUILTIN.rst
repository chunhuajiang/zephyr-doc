:orphan:

.. title:: CC3200SDK_BUILTIN

.. option:: CONFIG_CC3200SDK_BUILTIN:
.. _CONFIG_CC3200SDK_BUILTIN:

Link with local CC3200 SDK driverlib sources.



:Symbol:           CC3200SDK_BUILTIN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable building the CC3200 SDK files stored in the Zephyr tree"
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
 * ../ext/hal/ti/cc3200sdk/Kconfig:15