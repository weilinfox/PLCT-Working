# cli0 测试结果

[riscv/result.csv](./riscv/result.csv) [riscv/failureCause.csv](./riscv/failureCause.csv)

[x86/result.csv](./x86/result.csv) [x86/failureCause.csv](./x86/failureCause.csv)

汇总结果 [mergeCause.csv](./mergeCause.csv) [riscvCause.csv](./riscvCause.csv)

## 主要问题

1. 大部分 riscv 上失败的用例在 x86 上也失败了
   在 riscv 上
   |总测试套数|总测试用例数|总通过用例数|总未通过用例数|
   |:-------:|:----------:|:---------:|:-----------:|
   |39|372|244|128|
   
   失败用例分布在 17 个测试套中，将这些测试套在 x86 上进行测试
   |总测试套数|总测试用例数|总通过用例数|总未通过用例数|
   |:-------:|:----------:|:---------:|:-----------:|
   |17|311|205|106|

   128 个未通过用例中 106 个在 x86 上也不能测试通过。
