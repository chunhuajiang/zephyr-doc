:orphan:

.. title:: HMC5883L_THREAD_PRIORITY

.. option:: CONFIG_HMC5883L_THREAD_PRIORITY:
.. _CONFIG_HMC5883L_THREAD_PRIORITY:

Priority of thread used by the driver to handle interrupts.



:Symbol:           HMC5883L_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread priority" if HMC5883L && HMC5883L_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: HMC5883L && HMC5883L_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:89