:orphan:

.. title:: BOARD

.. option:: CONFIG_BOARD:
.. _CONFIG_BOARD:

This option holds the name of the board and is used to located the files
related to the board in the source tree (under boards/).
The Board is the first location where we search for a linker.ld file,
if not found we look for the linker file in
arch/<arch>/soc/<family>/<series>



:Symbol:           BOARD
:Type:             string
:Value:            "qemu_x86"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  "arduino_101_sss"
 *   Condition: (none)
 *  "em_starterkit"
 *   Condition: (none)
 *  "quark_se_c1000_ss_devboard"
 *   Condition: (none)
 *  qemu_x86 (value: "qemu_x86")
 *   Condition: (none)
 *  "arduino_101"
 *   Condition: (none)
 *  minnowboard (value: "minnowboard")
 *   Condition: (none)
 *  galileo (value: "galileo")
 *   Condition: (none)
 *  "quark_se_c1000_devboard"
 *   Condition: (none)
 *  "quark_d2000_crb"
 *   Condition: (none)
 *  96b_nitrogen (value: "96b_nitrogen")
 *   Condition: (none)
 *  arduino_due (value: "arduino_due")
 *   Condition: (none)
 *  nrf52_pca10040 (value: "nrf52_pca10040")
 *   Condition: (none)
 *  v2m_beetle (value: "v2m_beetle")
 *   Condition: (none)
 *  96b_carbon (value: "96b_carbon")
 *   Condition: (none)
 *  stm32_mini_a15 (value: "stm32_mini_a15")
 *   Condition: (none)
 *  bbc_microbit (value: "bbc_microbit")
 *   Condition: (none)
 *  olimexino_stm32 (value: "olimexino_stm32")
 *   Condition: (none)
 *  nrf51_pca10028 (value: "nrf51_pca10028")
 *   Condition: (none)
 *  nucleo_f401re (value: "nucleo_f401re")
 *   Condition: (none)
 *  nucleo_f103rb (value: "nucleo_f103rb")
 *   Condition: (none)
 *  quark_se_c1000_ble (value: "quark_se_c1000_ble")
 *   Condition: (none)
 *  hexiwear_k64 (value: "hexiwear_k64")
 *   Condition: (none)
 *  nrf51_blenano (value: "nrf51_blenano")
 *   Condition: (none)
 *  cc3200_launchxl (value: "cc3200_launchxl")
 *   Condition: (none)
 *  arduino_101_ble (value: "arduino_101_ble")
 *   Condition: (none)
 *  qemu_cortex_m3 (value: "qemu_cortex_m3")
 *   Condition: (none)
 *  frdm_k64f (value: "frdm_k64f")
 *   Condition: (none)
 *  "qemu_nios2"
 *   Condition: (none)
 *  "altera_max10"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_ALTERA_MAX10 (value: "n")
:Locations:
 * ../arch/Kconfig:101
 * ../boards/arc/arduino_101_sss/Kconfig.defconfig:4
 * ../boards/arc/em_starterkit/Kconfig.defconfig:4
 * ../boards/arc/quark_se_c1000_ss_devboard/Kconfig.defconfig:4
 * ../boards/x86/qemu_x86/Kconfig.defconfig:4
 * ../boards/x86/arduino_101/Kconfig.defconfig:4
 * ../boards/x86/minnowboard/Kconfig.defconfig:4
 * ../boards/x86/galileo/Kconfig.defconfig:4
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:4
 * ../boards/x86/quark_d2000_crb/Kconfig.defconfig:5
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:19
 * ../boards/arm/arduino_due/Kconfig.defconfig:4
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:19
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:21
 * ../boards/arm/96b_carbon/Kconfig.defconfig:20
 * ../boards/arm/stm32_mini_a15/Kconfig.defconfig:20
 * ../boards/arm/bbc_microbit/Kconfig.defconfig:19
 * ../boards/arm/olimexino_stm32/Kconfig.defconfig:20
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:19
 * ../boards/arm/nucleo_f401re/Kconfig.defconfig:20
 * ../boards/arm/nucleo_f103rb/Kconfig.defconfig:20
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:19
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:20
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:19
 * ../boards/arm/cc3200_launchxl/Kconfig.defconfig:6
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:19
 * ../boards/arm/qemu_cortex_m3/Kconfig.defconfig:4
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:20
 * ../boards/nios2/qemu_nios2/Kconfig.defconfig:3
 * ../boards/nios2/altera_max10/Kconfig.defconfig:3