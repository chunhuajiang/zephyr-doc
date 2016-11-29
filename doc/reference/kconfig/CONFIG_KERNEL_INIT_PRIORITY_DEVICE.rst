:orphan:

.. title:: KERNEL_INIT_PRIORITY_DEVICE

.. option:: CONFIG_KERNEL_INIT_PRIORITY_DEVICE:
.. _CONFIG_KERNEL_INIT_PRIORITY_DEVICE:

Device driver, that depends on common components, such as
interrupt controller, but does not depend on other devices,
uses this init priority.



:Symbol:           KERNEL_INIT_PRIORITY_DEVICE
:Type:             int
:Value:            "50"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Default init priority for device drivers"
:Default values:

 *  50 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:150