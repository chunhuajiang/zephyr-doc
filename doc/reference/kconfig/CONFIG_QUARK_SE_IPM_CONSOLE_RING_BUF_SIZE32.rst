:orphan:

.. title:: QUARK_SE_IPM_CONSOLE_RING_BUF_SIZE32

.. option:: CONFIG_QUARK_SE_IPM_CONSOLE_RING_BUF_SIZE32:
.. _CONFIG_QUARK_SE_IPM_CONSOLE_RING_BUF_SIZE32:

Size of the buffer for the console reciever, for incoming
console messages from the ARC side. Must be a power of 2.


:Symbol:           QUARK_SE_IPM_CONSOLE_RING_BUF_SIZE32
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IPM Console Ring Buffer Size"
:Default values:

 *  256 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 && IPM && IPM_CONSOLE_RECEIVER (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:79