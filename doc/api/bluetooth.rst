.. _bluetooth_api:

蓝牙 API
#############

.. contents::
   :depth: 1
   :local:
   :backlinks: top

本节包含可用蓝牙 API 的完整集合。注意，该集合中实际有效的 API 依赖于被选择的 Kconfig 选项，因为大多数蓝牙功能实在编译时进行选择的。例如，连接修改的 API 需要 :option:`CONFIG_BLUETOOTH_CONN` ，BR/EDR（蓝牙类）API 需要 :option:`CONFIG_BLUETOOTH_BREDR` 。

Generic Access Profile (GAP)
****************************

.. doxygengroup:: bt_gap
   :project: Zephyr
   :content-only:

连接管理
*********************

.. doxygengroup:: bt_conn
   :project: Zephyr
   :content-only:

Generic Attribute Profile (GATT)
********************************

.. doxygengroup:: bt_gatt
   :project: Zephyr
   :content-only:

Universal Unique Identifiers (UUIDs)
************************************

.. doxygengroup:: bt_uuid
   :project: Zephyr
   :content-only:

Logical Link Control and Adaptation Protocol (L2CAP)
****************************************************

.. doxygengroup:: bt_l2cap
   :project: Zephyr
   :content-only:

Serial Port Emulation (RFCOMM)
******************************

.. doxygengroup:: bt_rfcomm
   :project: Zephyr
   :content-only:

数据缓冲
************

.. doxygengroup:: bt_buf
   :project: Zephyr
   :content-only:

Persistent Storage
******************

.. doxygengroup:: bt_storage
   :project: Zephyr
   :content-only:

HCI Drivers
***********

.. doxygengroup:: bt_hci_driver
   :project: Zephyr
   :content-only:

HCI RAW channel
***************

HCI RAW 通道 API 用于向远程实体暴露 HCI 接口。本地蓝牙控制器被远程实体拥有；主机蓝牙协议栈不会被使用。RAW API 提供了对蓝牙 HCI 驱动程序收发的数据包的直接访问。

.. doxygengroup:: hci_raw
   :project: Zephyr
   :content-only:
