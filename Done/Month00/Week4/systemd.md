# systemd 排查

汇总表格 [systemd.csv](./systemd.csv)

## 测试结果不符合预期但是原因不明

+ ``oe_test_service_console-getty`` ： restart 有错误日志：Failed with result 'start-limit-hit'
+ ``oe_test_service_initrd-switch-root`` ： ``/sysroot`` 不存在
+ ``oe_test_service_systemd-ask-password-wall`` ： restart 有错误日志
+ ``oe_test_service_systemd-fsck-root`` ： ``systemd-fsck-root.service`` 初始状态不符合预期
+ ``oe_test_service_systemd-initctl`` ： restart 正常但是该进程自动退出导致后续检查出错
+ ``oe_test_service_systemd-udevd`` ： restart 返回 130 但是没有看到错误日志
+ ``oe_test_socket_systemd-journald-dev-log`` ： ``Failed to listen on Journal Socket``
+ ``oe_test_target_initrd-switch-root`` ：初始状态不符合预期
+ ``oe_test_service_systemd-network-generator`` ：初始状态不符合预期

## 缺失 ``.service`` ``.socket`` ``.target``

+ ``oe_test_service_dbus-org.freedesktop.portable1`` ： 没有软件包提供 ``dbus-org.freedesktop.portable1.service``
+ ``oe_test_service_quotaon`` ：没有软件包提供 ``quotaon.service``
+ ``oe_test_service_systemd-importd`` ：没有软件包提供 ``systemd-importd.service``
+ ``oe_test_service_systemd-journal-gatewayd`` ： 待测软件包 systemd-journal-remote 不存在
+ ``oe_test_service_systemd-journal-remote`` ： 待测软件包 systemd-journal-remote 不存在
+ ``oe_test_service_systemd-journal-upload`` ： 待测软件包 systemd-journal-remote 不存在
+ ``oe_test_service_systemd-networkd`` ：没有引入待测软件包 systemd-networkd
+ ``oe_test_service_systemd-networkd-wait-online`` ：没有引入待测软件包 systemd-networkd
+ ``oe_test_service_systemd-portabled`` ：没有软件包提供 ``systemd-portabled.service``
+ ``oe_test_service_systemd-quotacheck`` ：没有软件包提供 ``systemd-quotacheck.service``
+ ``oe_test_service_systemd-resolved`` ：没有引入待测软件包 ``systemd-resolved``
+ ``oe_test_service_systemd-sysext`` ：没有软件包提供 ``systemd-sysext.service``
+ ``oe_test_service_systemd-userdbd`` ：没有软件包提供 ``systemd-userdbd.service``
+ ``oe_test_socket_systemd-rfkill`` ：没有软件包提供 ``systemd-rfkill.socket``
+ ``oe_test_socket_systemd-userdbd`` ：没有软件包提供 ``systemd-userdbd.socket``
+ ``oe_test_target_cryptsetup`` ：没有软件包提供 ``cryptsetup.target``
+ ``oe_test_target_cryptsetup-pre`` ：没有软件包提供 ``cryptsetup-pre.target``
+ ``oe_test_target_remote-cryptsetup`` ：没有软件包提供 ``remote-cryptsetup.target``
+ ``oe_test_target_remote-veritysetup`` ：没有软件包提供 ``remote-veritysetup.target``
+ ``oe_test_target_usb-gadget`` ：没有软件包提供 ``usb-gadget.target``
+ ``oe_test_target_veritysetup`` ：没有软件包提供 ``veritysetup.target``
+ ``oe_test_target_veritysetup-pre`` ：没有软件包提供 ``veritysetup-pre.target``
