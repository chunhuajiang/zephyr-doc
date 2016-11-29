:orphan:

.. title:: XIP

.. option:: CONFIG_XIP:
.. _CONFIG_XIP:

This option allows the kernel to operate with its text and read-only
sections residing in ROM (or similar read-only memory). Not all boards
support this option so it must be used with care; you must also
supply a linker command file when building your image. Enabling this
option increases both the code and data footprint of the image.




:Symbol:           XIP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Execute in place"
:Default values:

 *  n (value: "n")
 *   Condition: NSIM (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_D2000 || SOC_SERIES_QUARK_SE || SOC_SERIES_NRF51X || SOC_SERIES_NRF52X (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/arc/Kconfig:154
 * ../arch/x86/Kconfig:269
 * ../arch/arm/core/cortex_m/Kconfig:162
 * ../arch/nios2/Kconfig:46
 * ../kernel/Kconfig:66