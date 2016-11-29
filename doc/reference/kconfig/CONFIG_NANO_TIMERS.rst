:orphan:

.. title:: NANO_TIMERS

.. option:: CONFIG_NANO_TIMERS:
.. _CONFIG_NANO_TIMERS:

Only here for common (ie. non-unified kernel) code that rely on this.
Unified kernel uses SYS_CLOCK_EXISTS everywhere instead.



:Symbol:           NANO_TIMERS
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  y (value: "y")
 *   Condition: SYS_CLOCK_EXISTS (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GPIO && I2C && GPIO && GPIO_PCAL9535A || NETWORKING (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:168