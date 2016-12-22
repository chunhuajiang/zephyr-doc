USB 设备栈
################

USB 设备栈分为如下三层：
   * USB 设备控制器驱动（硬件相关的）
   * USB 设备核心驱动（硬件无关的）
   * USB 设备类驱动（硬件无关的）

USB 设备控制器驱动
*****************************

设备控制器驱动层实现了直接与底层硬件打交道的逻辑。所有的设备控制器驱动都应当实现 usb_dc.h 中描述的 API。这样做的好处是当新的 USB 设备集成到系统中时不需要修改上层内容。目前只支持 Quark SE 的 USB 设备控制器（Designware IP）。

结构体
==========

.. code-block:: c

   struct usb_dc_ep_cfg_data {
      uint8_t ep_addr;
      uint16_t ep_mps;
      enum usb_dc_ep_type ep_type;
   };

这个结构体中包含 USB 终点配置。
   * ep_addr: 终点地址，在设备配置结构中与 EP 关联的数量。
     IN  EP = 0x80 | <endpoint number>. OUT EP = 0x00 | <endpoint number>
   * ep_mps: 终点最大包尺寸。
   * ep_type: 终点类型，可以是 Bulk、Interrupt 或者 Control。当前不支持同步终点。

.. code-block:: c

   enum usb_dc_status_code {
      USB_DC_ERROR,
      USB_DC_RESET,
      USB_DC_CONNECTED,
      USB_DC_CONFIGURED,
      USB_DC_DISCONNECTED,
      USB_DC_SUSPEND,
      USB_DC_RESUME,
      USB_DC_UNKNOWN
   };

由注册的设备状态回调函数返回的状态码。
   * USB_DC_ERROR: 控制器返回的 USB 错误。
   * USB_DC_RESET: USB 复位。
   * USB_DC_CONNECTED: USB 连接已建立 - 硬件枚举已完成。
   * USB_DC_CONFIGURED: USB 配置完成。
   * USB_DC_DISCONNECTED: USB 连接丢失。
   * USB_DC_SUSPEND: USB 连接被主机挂起。
   * USB_DC_RESUME: USB 连接被主机恢复。
   * USB_DC_UNKNOWN: 初始化的 USB 连接状态。

.. code-block:: c

   enum usb_dc_ep_cb_status_code {
      USB_DC_EP_SETUP,
      USB_DC_EP_DATA_OUT,
      USB_DC_EP_DATA_IN,
   };

由注册的终点回调函数返回的状态码。
   * USB_DC_EP_SETUP: SETUP packet received.
   * USB_DC_EP_DATA_OUT: Out transaction on this endpoint. Data is available
     for read.
   * USB_DC_EP_DATA_IN: In transaction done on this endpoint.

API
====

下列 API 是由设备控制器驱动程序提供的：

:c:func:`usb_dc_attach()`
   
   该函数负责附着（连接） USB 设备。附着成功后，USB 的 PLL 被使能，且 USB 设备能够在 USB 总线上收发数据、产生中断。
   

:c:func:`usb_dc_detach()`
   该函数用于卸载 USB 设备。卸载成功后，USB 的 PLL 被关电，且 USB 通信功能被禁止。
   
:c:func:`usb_dc_reset()`
   
   该函数用于将 USB 设备返回到初始化状态。
   
:c:func:`usb_dc_set_address()`
   
   该函数用于设置 USB 设备的地址。
   
:c:func:`usb_dc_set_status_callback()`
   
   该函数用于设置 USB 设备控制器的状态回调。所注册的回调函数用于报告设备控制器产生的状态变化。状态码由枚举 usb_dc_status_code 进行描述。
   
:c:func:`usb_dc_ep_configure()`

   该函数用于配置一个终点。结构体 usb_dc_ep_cfg_data 用于提供终点配置参数：终点地址、终点最大包尺寸和终点类型。
   

:c:func:`usb_dc_ep_set_stall()`
   
   该函数用于为所选定的终点设置 stall 条件。
   
:c:func:`usb_dc_ep_clear_stall()`

   该函数用于为所选定的终点清除 stall 条件。
   
:c:func:`usb_dc_ep_is_stalled()`

   该函数用于检查所选终点是否被 install。
   
:c:func:`usb_dc_ep_halt()`

   该函数用于停止（halt）所选终点。
   
:c:func:`usb_dc_ep_enable()`

   该函数用于使能所选终点。使能成功后，相应终点的中断会被使能，并且收发数据已就绪。

:c:func:`usb_dc_ep_disable()`

   该函数用于禁止所选终点。禁止成功后，相应终点的终点被禁止，且不能够再收发数据。

:c:func:`usb_dc_ep_flush()`

   该函数用于冲刷所选终点的 FIFO。
   
:c:func:`usb_dc_ep_write()`

   该函数用于向指定的终点写数据。当数据传输出去后，所设置的回调函数 usb_ep_callback 会被调用。
   
:c:func:`usb_dc_ep_read()`

   当某个点接收到 OUT 中断胡，终点处理函数会调用该函数。应用程序只能使用所提供的 usb_ep_callback 函数间接调用本函数。
   
:c:func:`usb_dc_ep_set_callback()`

   当接收到数据，且该数据对应用程序有效是，或者所选终点的传输完成时，调用该函数设置回调函数。
   
USB 设备核心层
*********************

USB 设备核心层是介于 USB 设备控制器驱动和 USB 设备类驱动或应用层之间的与硬件无关的接口。它是 LPCUSB 设备栈的一部分。它提供下面的功能：

   * 响应标准设备请求并返回标准描述符，从根本上处理‘第 9 章’过程，尤其是通用串行规范 2.0 的表 9-3。
   * 提供 USB 设备类或者应用程序所用的编程接口。这些 API 在文件 usb_device.h 中进行描述。
   * 使用设备控制器驱动提供的 API 与 USB 设备控制器交互。

结构体
==========

.. code-block:: c

   typedef void (*usb_status_callback)(enum usb_dc_status_code status_code);

设备状态的回调函数签名。

.. code-block:: c

   typedef void (*usb_ep_callback)(uint8_t ep,
      enum usb_dc_ep_cb_status_code cb_status);

USB 终点的回调函数签名。

.. code-block:: c

   typedef int (*usb_request_handler) (struct usb_setup_packet *setup,
      int *transfer_len, uint8_t **payload_data);

类指定请求的回调函数签名。从主机到设备方向，‘len’表示所接收数据的长度，‘payload_data’指向所接收的数据。从设备到主机类请求，回调函数应当将‘len’和‘payload_data’设置为所传输缓冲的数据长度和地址。


.. code-block:: c

   struct usb_ep_cfg_data {
      usb_ep_callback ep_cb;
      uint8_t ep_addr;
   };

这个结构体包含了终端的配置。
   * ep_cb: 接收到数据且对应用程序有效时，或传输完成时进行通知的回调函数。NULL 表示应用程序不需要回调。
   * ep_addr: 终点地址。终点地址，在设备配置结构中与 EP 关联的数量。

.. code-block:: c

   struct usb_interface_cfg_data {
      usb_request_handler class_handler;
      usb_request_handler custom_handler;
      uint8_t *payload_data;
   };

这个结构体包含 USB 接口配置。
   * class_handler: USB 类相关控制（EP 0）通信的处理者。
   * custom_handler: 自定义请求处理者最先有机会在被移交给‘第 9 章’的请求处理者前处理请求。
   * payload_data: 这段由应用程序分配的数据区用于存放类相关的命令，它必须能够容纳与所支持的最大命令集相关联的最大载荷。
   
.. code-block:: c

   struct usb_cfg_data {
      const uint8_t *usb_device_description;
      usb_status_callback cb_usb_status;
      struct usb_interface_cfg_data interface;
      uint8_t num_endpoints;
      struct usb_ep_cfg_data *endpoint;
   };

这个结构体包含 USB 设备配置。
   * usb_device_description: USB 设备描述，参考 http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors。
   * cb_usb_status: USB 连接状态改变时被通知的回调。
   * interface:  USB 类处理者和存储空间。
   * num_endpoints: 设备配置中终点的数量。
   * endpoint: 指向一个的终点配置结构体的数组，该数组的长度等于与设备描述相关联的终点数量。不包括控制终点。

类驱动程序使用 "usb_set_config" 所给的参数来实例化它。

API
====

:c:func:`usb_set_config()`

   该函数用于配置 USB 设备。
   
:c:func:`usb_deconfig()`

   该函数用于将 USB 设备返回到初始状态。
   
:c:func:`usb_enable()`

   该函数用于使能 USB 主机/设备连接。使能成功后，USB 模型在硬件上的时钟会开启，之后能够在 USB 总线上收发数据，且能够产生中断。
   
:c:func:`usb_disable()`
   该函数用于禁止 USB 是被。禁止成功后，USB 模块的始终在硬件上被关闭，之后就不能产生中断。
   
:c:func:`usb_write()`
   
   向指定终点写数据。当传输完成时会调用所提供的 usb_ep_callback。
   
:c:func:`usb_read()`
   
   当 OUT 中断被终点接收首，终点处理函数会调用该函数。应用程序只能通过所提供的函数 usb_ep_callback 间接调用该函数。
   

USB 设备类驱动
************************

初始化设备类驱动实例时，USB 设备类驱动程序应当 usb_set_config()，作为参数传递实例的配置结构。

例如，对于 CDC_ACM 例程应用：

.. code-block:: c

   static const uint8_t cdc_acm_usb_description[] = {
      /* Device descriptor */
      USB_DEVICE_DESC_SIZE,           /* Descriptor size */
      USB_DEVICE_DESC,                /* Descriptor type */
      LOW_BYTE(USB_1_1),
      HIGH_BYTE(USB_1_1),             /* USB version in BCD format */
      COMMUNICATION_DEVICE_CLASS,     /* Class */
      0x00,                           /* SubClass - Interface specific */
      0x00,                           /* Protocol - Interface specific */
      MAX_PACKET_SIZE_EP0,            /* Max Packet Size */
      LOW_BYTE(VENDOR_ID),
      HIGH_BYTE(VENDOR_ID),           /* Vendor Id */
      LOW_BYTE(CDC_PRODUCT_ID),
      HIGH_BYTE(CDC_PRODUCT_ID),      /* Product Id */
      LOW_BYTE(BCDDEVICE_RELNUM),
      HIGH_BYTE(BCDDEVICE_RELNUM),    /* Device Release Number */
      0x01,                           /* Index of Manufacturer String Descriptor */
      0x02,                           /* Index of Product String Descriptor */
      0x03,                           /* Index of Serial Number String Descriptor */
      CDC_NUM_CONF,                   /* Number of Possible Configuration */

      /* Configuration descriptor */
      USB_CONFIGURATION_DESC_SIZE,    /* Descriptor size */
      USB_CONFIGURATION_DESC,         /* Descriptor type */
      LOW_BYTE(CDC_CONF_SIZE),
      HIGH_BYTE(CDC_CONF_SIZE),       /* Total length in bytes of data returned */
      CDC_NUM_ITF,                    /* Number of interfaces */
      0x01,                           /* Configuration value */
      0x00,                           /* Index of the Configuration string */
      USB_CONFIGURATION_ATTRIBUTES,   /* Attributes */
      MAX_LOW_POWER,                  /* Max power consumption */

      /* Interface descriptor */
      USB_INTERFACE_DESC_SIZE,        /* Descriptor size */
      USB_INTERFACE_DESC,             /* Descriptor type */
      0x00,                           /* Interface index */
      0x00,                           /* Alternate setting */
      CDC1_NUM_EP,                    /* Number of Endpoints */
      COMMUNICATION_DEVICE_CLASS,     /* Class */
      ACM_SUBCLASS,                   /* SubClass */
      V25TER_PROTOCOL,                /* Protocol */
      0x00,                           /* Index of the Interface String Descriptor */

      /* Header Functional Descriptor */
      USB_HFUNC_DESC_SIZE,            /* Descriptor size */
      CS_INTERFACE,                   /* Descriptor type */
      USB_HFUNC_SUBDESC,              /* Descriptor SubType */
      LOW_BYTE(USB_1_1),
      HIGH_BYTE(USB_1_1),             /* CDC Device Release Number */

      /* Call Management Functional Descriptor */
      USB_CMFUNC_DESC_SIZE,           /* Descriptor size */
      CS_INTERFACE,                   /* Descriptor type */
      USB_CMFUNC_SUBDESC,             /* Descriptor SubType */
      0x00,                           /* Capabilities */
      0x01,                           /* Data Interface */

      /* ACM Functional Descriptor */
      USB_ACMFUNC_DESC_SIZE,          /* Descriptor size */
      CS_INTERFACE,                   /* Descriptor type */
      USB_ACMFUNC_SUBDESC,            /* Descriptor SubType */
      /* Capabilities - Device supports the request combination of:
       *	Set_Line_Coding,
       *	Set_Control_Line_State,
       *	Get_Line_Coding
       *	and the notification Serial_State
       */
      0x02,

      /* Union Functional Descriptor */
      USB_UFUNC_DESC_SIZE,            /* Descriptor size */
      CS_INTERFACE,                   /* Descriptor type */
      USB_UFUNC_SUBDESC,              /* Descriptor SubType */
      0x00,                           /* Master Interface */
      0x01,                           /* Slave Interface */

      /* Endpoint INT */
      USB_ENDPOINT_DESC_SIZE,         /* Descriptor size */
      USB_ENDPOINT_DESC,              /* Descriptor type */
      CDC_ENDP_INT,                   /* Endpoint address */
      USB_DC_EP_INTERRUPT,            /* Attributes */
      LOW_BYTE(CDC_INTERRUPT_EP_MPS),
      HIGH_BYTE(CDC_INTERRUPT_EP_MPS),/* Max packet size */
      0x0A,                           /* Interval */

      /* Interface descriptor */
      USB_INTERFACE_DESC_SIZE,        /* Descriptor size */
      USB_INTERFACE_DESC,             /* Descriptor type */
      0x01,                           /* Interface index */
      0x00,                           /* Alternate setting */
      CDC2_NUM_EP,                    /* Number of Endpoints */
      COMMUNICATION_DEVICE_CLASS_DATA,/* Class */
      0x00,                           /* SubClass */
      0x00,                           /* Protocol */
      0x00,                           /* Index of the Interface String Descriptor */

      /* First Endpoint IN */
      USB_ENDPOINT_DESC_SIZE,         /* Descriptor size */
      USB_ENDPOINT_DESC,              /* Descriptor type */
      CDC_ENDP_IN,                    /* Endpoint address */
      USB_DC_EP_BULK,                 /* Attributes */
      LOW_BYTE(CDC_BULK_EP_MPS),
      HIGH_BYTE(CDC_BULK_EP_MPS),     /* Max packet size */
      0x00,                           /* Interval */

      /* Second Endpoint OUT */
      USB_ENDPOINT_DESC_SIZE,         /* Descriptor size */
      USB_ENDPOINT_DESC,              /* Descriptor type */
      CDC_ENDP_OUT,                   /* Endpoint address */
      USB_DC_EP_BULK,                 /* Attributes */
      LOW_BYTE(CDC_BULK_EP_MPS),
      HIGH_BYTE(CDC_BULK_EP_MPS),     /* Max packet size */
      0x00,                           /* Interval */

      /* String descriptor language, only one, so min size 4 bytes.
       * 0x0409 English(US) language code used
       */
      USB_STRING_DESC_SIZE,           /* Descriptor size */
      USB_STRING_DESC,                /* Descriptor type */
      0x09,
      0x04,
      /* Manufacturer String Descriptor "Intel" */
      0x0C,
      USB_STRING_DESC,
      'I', 0, 'n', 0, 't', 0, 'e', 0, 'l', 0,
      /* Product String Descriptor "CDC-ACM" */
      0x10,
      USB_STRING_DESC,
      'C', 0, 'D', 0, 'C', 0, '-', 0, 'A', 0, 'C', 0, 'M', 0,
      /* Serial Number String Descriptor "00.01" */
      0x0C,
      USB_STRING_DESC,
      '0', 0, '0', 0, '.', 0, '0', 0, '1', 0,
   };

.. code-block:: c

   static struct usb_ep_cfg_data cdc_acm_ep_data[] = {
      {
         .ep_cb = cdc_acm_int_in,
         .ep_addr = CDC_ENDP_INT
      },
      {
         .ep_cb = cdc_acm_bulk_out,
         .ep_addr = CDC_ENDP_OUT
      },
      {
         .ep_cb = cdc_acm_bulk_in,
         .ep_addr = CDC_ENDP_IN
      }
   };

.. code-block:: c

   static struct usb_cfg_data cdc_acm_config = {
      .usb_device_description = cdc_acm_usb_description,
      .cb_usb_status = cdc_acm_dev_status_cb,
      .interface = {
      .class_handler = cdc_acm_class_handle_req,
      .custom_handler = NULL,
      .payload_data = NULL,
      },
      .num_endpoints = CDC1_NUM_EP + CDC2_NUM_EP,
      .endpoint = cdc_acm_ep_data
   };

.. code-block:: c

   ret = usb_set_config(&cdc_acm_config);
   if (ret < 0) {
      DBG("Failed to config USB\n");
      return ret;
   }

要使能 USB 设备主机/设备连接：

.. code-block:: c

   ret = usb_enable(&cdc_acm_config);
   if (ret < 0) {
      DBG("Failed to enable USB\n");
      return ret;
   }

类设备请求被 USB 栈核心驱动程序通过所注册的类处理者转发给类驱动程序。对于 CDC_ACM 例程类驱动程序，‘cdc_acm_class_handle_req’ 处理 SET_LINE_CODING、CDC_SET_CONTROL_LINE_STATE 和 CDC_GET_LINE_CODING 类请求：

.. code-block:: c

   int cdc_acm_class_handle_req(struct usb_setup_packet *pSetup,
         int32_t *len, uint8_t **data)
   {
      struct cdc_acm_dev_data_t * const dev_data = DEV_DATA(cdc_acm_dev);

      switch (pSetup->bRequest) {
      case CDC_SET_LINE_CODING:
         memcpy(&dev_data->line_coding, *data, sizeof(dev_data->line_coding));
         DBG("\nCDC_SET_LINE_CODING %d %d %d %d\n",
            sys_le32_to_cpu(dev_data->line_coding.dwDTERate),
            dev_data->line_coding.bCharFormat,
            dev_data->line_coding.bParityType,
            dev_data->line_coding.bDataBits);
      break;

      case CDC_SET_CONTROL_LINE_STATE:
         dev_data->line_state = (uint8_t)sys_le16_to_cpu(pSetup->wValue);
         DBG("CDC_SET_CONTROL_LINE_STATE 0x%x\n", dev_data->line_state);
            break;

      case CDC_GET_LINE_CODING:
         *data = (uint8_t *)(&dev_data->line_coding);
         *len = sizeof(dev_data->line_coding);
         DBG("\nCDC_GET_LINE_CODING %d %d %d %d\n",
         sys_le32_to_cpu(dev_data->line_coding.dwDTERate),
            dev_data->line_coding.bCharFormat,
            dev_data->line_coding.bParityType,
            dev_data->line_coding.bDataBits);
            break;

      default:
         DBG("CDC ACM request 0x%x, value 0x%x\n",
            pSetup->bRequest, pSetup->wValue);
            return -EINVAL;
      }

      return 0;
   }

类驱动程序在传输数据区应当等待 USB_DC_CONFIGURED 设备状态码。

数据传输给主机时，类驱动程序应当调用 usb_write()。完成后，所注册的终点回调函数会被调用。在发送另一个包前，类驱动程序应当等待之前的传输完成。

当数据被接收后，所注册的终点回调函数会被调用。usb_read() 会被用于恢复接收到的数据。它必须总是通过所注册的终点回调函数被调用。对于 CDC ACM 例程驱动程序，这是通过终点数组（cdc_acm_ep_data）中所提到的 OUT bluk 终点处理者完成的。

当前只提供了 CDC ACM 和 DFU 类驱动例程。