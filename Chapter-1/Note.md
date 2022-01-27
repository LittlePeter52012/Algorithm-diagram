Chapter-1 算法简介  
===================

## 1. 引言

算法：
  一组完成任务的指令。  

* 性能方面:  
  学习比较不同算法间的优缺点。
* 问题解决技巧：
  熟悉一些使用最为广泛的算法。本书的示例将使用Python进行编写。

## 2. [二分查找（Binary search）](Chapter-1\Binary search.ipynb)

> 举例：在电话簿中找一个以K打头的人，可以从中间开始翻。  

* 二分查找：一种算法，输入有序的元素列表（**必须是有序的**）。如果要查找的元素包含在列表中，二分查找返回其位置；否则返回null。
* 使用“二分查找”时，每次都排除一般的数字。
* 一般而言，对于包含n个元素的列表，用二分查找最多需要
  $log_2^n$
步，而简单查找最多需要$n$步。  

_本文使用大O表示法****讨论运行时间时，$log$指的都是$log_2$。_