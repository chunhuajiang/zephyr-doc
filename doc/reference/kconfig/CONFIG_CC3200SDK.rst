:orphan:

.. title:: CC3200SDK

.. option:: CONFIG_CC3200SDK:
.. _CONFIG_CC3200SDK:

Set when CC3200SDK_BUILTIN or CC3200SDK_LIBRARY



:Symbol:           CC3200SDK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TI CC3200 SDK support" if HAS_CC3200SDK (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: HAS_CC3200SDK (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 CC3200SDK_BUILTIN && HAS_CC3200SDK || CC3200SDK_LIBRARY && HAS_CC3200SDK (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/hal/ti/cc3200sdk/Kconfig:6