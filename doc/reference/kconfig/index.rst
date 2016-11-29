.. _configuration:

Configuration Options Reference Guide
#####################################

Introduction
************

Kconfig files describe the configuration symbols supported in the build
system, the logical organization and structure that group the symbols in menus
and sub-menus, and the relationships between the different configuration
symbols that govern the valid configuration combinations.

The Kconfig files are distributed across the build directory tree. The files
are organized based on their common characteristics and on what new symbols
they add to the configuration menus.

The configuration options' information is extracted directly from :program:`Kconfig`
using the :file:`~/doc/scripts/genrest/genrest.py` script.


Supported Options
*****************

.. list-table:: Configuration Options

   * - :option:`CONFIG_KERNELVERSION`
     - 
   * - :option:`CONFIG_ZOAP`
     - CoAP Support
   * - :option:`CONFIG_HAS_CMSIS`
     - 
   * - :option:`CONFIG_HAS_KSDK`
     - 
   * - :option:`CONFIG_HAS_NORDIC_MDK`
     - 
   * - :option:`CONFIG_HAS_QMSI`
     - 
   * - :option:`CONFIG_QMSI`
     - QMSI driver support
   * - :option:`CONFIG_QMSI_BUILTIN`
     - Enable QMSI drivers through integrated sources
   * - :option:`CONFIG_QMSI_LIBRARY`
     - Enable QMSI drivers using external library
   * - :option:`CONFIG_QMSI_INSTALL_PATH`
     - QMSI install path
   * - :option:`CONFIG_SOC_WATCH`
     - Enable SoCWatch drivers and related instrumentation
   * - :option:`CONFIG_HAS_STM32CUBE`
     - 
   * - :option:`CONFIG_HAS_CC3200SDK`
     - 
   * - :option:`CONFIG_CC3200SDK`
     - TI CC3200 SDK support
   * - :option:`CONFIG_CC3200SDK_BUILTIN`
     - Enable building the CC3200 SDK files stored in the Zephyr tree
   * - :option:`CONFIG_CC3200SDK_LIBRARY`
     - Link with CC3200 SDK static driver library
   * - :option:`CONFIG_CC3200SDK_INSTALL_PATH`
     - CC3200 SDK install path
   * - :option:`CONFIG_TINYCRYPT`
     - Cryptography Support
   * - :option:`CONFIG_TINYCRYPT_CTR_PRNG`
     - PRNG in counter mode
   * - :option:`CONFIG_TINYCRYPT_SHA256`
     - SHA-256 Hash function support
   * - :option:`CONFIG_TINYCRYPT_SHA256_HMAC`
     - HMAC (via SHA256) message auth support
   * - :option:`CONFIG_TINYCRYPT_SHA256_HMAC_PRNG`
     - PRNG (via HMAC-SHA256) support
   * - :option:`CONFIG_TINYCRYPT_ECC_DH`
     - ECC_DH anonymous key agreement protocol
   * - :option:`CONFIG_TINYCRYPT_ECC_DSA`
     - ECC_DSA digital signature algorithm
   * - :option:`CONFIG_TINYCRYPT_AES`
     - AES-128 decrypt/encrypt
   * - :option:`CONFIG_TINYCRYPT_AES_CBC`
     - AES-128 block cipher
   * - :option:`CONFIG_TINYCRYPT_AES_CTR`
     - AES-128 counter mode
   * - :option:`CONFIG_TINYCRYPT_AES_CCM`
     - AES-128 CCM mode
   * - :option:`CONFIG_TINYCRYPT_AES_CMAC`
     - AES-128 CMAC mode
   * - :option:`CONFIG_ZTEST`
     - Zephyr testing framework
   * - :option:`CONFIG_ZTEST_STACKSIZE`
     - Test function thread stack size
   * - :option:`CONFIG_ZTEST_FAIL_FAST`
     - Abort on first failing test
   * - :option:`CONFIG_ZTEST_ASSERT_VERBOSE`
     - Assertion verbosity level
   * - :option:`CONFIG_ZTEST_MOCKING`
     - Mocking support functions
   * - :option:`CONFIG_ZTEST_PARAMETER_COUNT`
     - Count of parameters or return values reserved
