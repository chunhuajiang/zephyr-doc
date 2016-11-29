:orphan:

.. title:: BOARD_EM_STARTERKIT

.. option:: CONFIG_BOARD_EM_STARTERKIT:
.. _CONFIG_BOARD_EM_STARTERKIT:

The DesignWare ARC EM Starter Kit board is a board
that can host up to 3 different SOC FPGA bit files.
Version 2.2 firmware supports EM7D, EM9D and EM11D configurations.
EM9D using CCM memories and is a Harvard Architecture.
EM7D and EM11D have access to 128MB DRAM and use i-cache and d-cache.



:Symbol:           BOARD_EM_STARTERKIT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ARC EM Starter Kit" if SOC_EM7D || SOC_EM9D || SOC_EM11D (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../boards/arc/em_starterkit/Kconfig.board:17