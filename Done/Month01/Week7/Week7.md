# Week 7 工作报告

1. 汇总仅 fail 的测试用例 [baseOSFailed.csv](./baseOSFailed.csv)
2. 重测并提交 rest0 缺失的测试 pr [#12](https://github.com/KotorinMinami/res_list/commit/6fc49cbc70c91a39eaf261a2fef64af8a1314883)
3. 重测并提交之前手动测试通过但是没有保留日志的 ``xmvn_3.0.0-24`` 测试日志，由于一些测试需要一个小时以上才能完成，需要手动调整超时时间才能成功完成。 pr [#13](https://github.com/KotorinMinami/res_list/commit/2dcda539b51a7153a76c640396ea4dd5c03addea)
4. 重测并提交之前手动测试通过但是没有保留日志的  ``rubygem-fluentd_1.14.5`` 测试日志，测试脚本中 ``SLEEP_WAIT`` 设置时间过短导致失败，需要手动单步执行脚本命令，提高延时时间重测得到更新日志。
5. 完成 rest1 部分的日志 fail 部分分析。 pr [#14](https://github.com/KotorinMinami/res_list/commit/eaffea9454b6df1a29d65b3cf3d3d7228f3b05dc)
