# Week 6 工作报告

1. 完成 rest0 软件包的测试，得到测试结果 [mergeCause.csv](./mergeCause.csv)
2. 分析了 rest0 软件包的 fail 分析，得到分析的简短结果 [mergeFailed.csv](./mergeFailed.csv)
3. 将 rest0 软件包的测试结果 [pr](https://github.com/KotorinMinami/res_list/pull/9)

## 遇到的问题

1. mugen 在测试 ocaml-22.03 时坏掉了
   ```
   Traceback (most recent call last):
     File "/root/mugen/mugen_riscv.py", line 270, in <module>
       test_res = test_target.Run(xpara=args.x,addDisk=args.addDisk,multiMachine=args.multiMachine,addNic=args.addNic)
     File "/root/mugen/mugen_riscv.py", line 189, in Run
       log_found = re.search(r'See "systemctl status (.*)" and "journalctl -xe(.*)" for details.' , log_data.read())
     File "/usr/lib64/python3.10/codecs.py", line 322, in decode
       (result, consumed) = self._buffer_decode(data, self.errors, final)
   UnicodeDecodeError: 'utf-8' codec can't decode byte 0x84 in position 2031: invalid start byte
   ```
2. 遇到和杨栋一样的 ``machine num`` 不 work 的问题， 配置了 ``machine num`` 的测试用例被直接跳过
