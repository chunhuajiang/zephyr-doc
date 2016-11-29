:orphan:

.. title:: DEVICE_POWER_MANAGEMENT

.. option:: CONFIG_DEVICE_POWER_MANAGEMENT:
.. _CONFIG_DEVICE_POWER_MANAGEMENT:

This option enables the device power management interface.  The
interface consists of hook functions implemented by device drivers
that get called by the power manager application when the system
is going to suspend state or resuming from suspend state. This allows
device drivers to do any necessary power management operations
like turning off device clocks and peripherals. The device drivers
may also save and restore states in these hook functions.



:Symbol:           DEVICE_POWER_MANAGEMENT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device power management" if MICROKERNEL && SYS_POWER_MANAGEMENT (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: MICROKERNEL && SYS_POWER_MANAGEMENT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SYS_POWER_MANAGEMENT (value: "n")
:Locations:
 * ../kernel/Kconfig:266