:orphan:

.. title:: LIS3DH_THREAD_PRIORITY

.. option:: CONFIG_LIS3DH_THREAD_PRIORITY:
.. _CONFIG_LIS3DH_THREAD_PRIORITY:

Priority of thread used by the driver to handle interrupts.



:Symbol:           LIS3DH_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread priority" if LIS3DH && LIS3DH_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: LIS3DH && LIS3DH_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3dh/Kconfig:102