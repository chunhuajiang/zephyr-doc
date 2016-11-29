:orphan:

.. title:: ARC_STACK_CHECKING

.. option:: CONFIG_ARC_STACK_CHECKING:
.. _CONFIG_ARC_STACK_CHECKING:

ARCV2 has a special feature allowing to check stack overflows. This
enables code that allows using this debug feature



:Symbol:           ARC_STACK_CHECKING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Stack Checking" if CPU_ARCV2 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CPU_ARCV2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARC (value: "n")
:Locations:
 * ../arch/arc/Kconfig:122