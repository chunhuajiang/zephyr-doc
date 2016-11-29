:orphan:

.. title:: AIO_COMPARATOR_QMSI

.. option:: CONFIG_AIO_COMPARATOR_QMSI:
.. _CONFIG_AIO_COMPARATOR_QMSI:

QMSI AIO/Comparator driver.



:Symbol:           AIO_COMPARATOR_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable QMSI AIO/comparator driver" if AIO_COMPARATOR && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: AIO_COMPARATOR && QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 AIO_COMPARATOR && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/aio/Kconfig:28
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:235
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:135
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:174