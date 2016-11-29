:orphan:

.. title:: IPM_QUARK_SE_MASTER

.. option:: CONFIG_IPM_QUARK_SE_MASTER:
.. _CONFIG_IPM_QUARK_SE_MASTER:

Enable this for the first CPU that initializes IPM.
Sets up the initial interrupt mask and clears out all
channels. Should be turned on for one CPU only.



:Symbol:           IPM_QUARK_SE_MASTER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE IPM master controller" if IPM_QUARK_SE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: IPM_QUARK_SE (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/ipm/Kconfig:16