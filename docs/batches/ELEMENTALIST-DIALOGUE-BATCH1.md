# 元素使独立对白第1批：完整文件

2026-11-21。新增 `translation/elementalistdlc-conversations-zh.properties`，对照 `aof3-elementalist-dlc` 中的英文properties、对白XML、关卡及战场资源，完整翻译五组18条内容。

| 完整对白组 | 内容键数 |
| --- | ---: |
| EXX_Welcome | 4 |
| EXX_IronGolemRiddle_CorrectAnswer | 2 |
| EXX_IronGolemRiddle_IncorrectAnswer | 6 |
| E01_GargoyleElder_death | 4 |
| E01_LightningBall_damage | 2 |

合计9条角色名、9条台词，另有2条元数据。文件覆盖18/18（100%），构建要求完整源键集。此前通用第25批中的64条元素使关卡文本保持不变，未新增重复的独立关卡资源。文件全覆盖不代表整个扩展或所有动态英文均已验证。

折翼、闪电球、钢铁魔像及老兵资历沿用术语表。魔像的入侵警报与通用关卡采用同一停顿译法，保留短促机械语气；折翼的碎裂声及闪电球的电流声不增加额外效果说明。六处HTML换行和所有标签顺序保留。

五份对白XML均逐字段对应。三个EXX组共有五处关卡调用：欢迎一次，正确反馈一次，错误反馈三次。`LevelElementalist05` 中恐惧选项播放正确反馈、给予全队各200经验并进入07；鲜血、爱、色欲播放错误反馈，经06a商店进入06b战斗；再想想返回地图。06b胜利同样进入07，失败使用当前战役的失败节点。原有关卡选项与奖励均未改动。

两组战斗反应的完整名称均存在于 `E01_Passage_Guardians.brd` 解压后的Java序列化流。此检查证明资源引用存在，不证明触发时机、单位状态或游戏内显示。

构建、编码、占位符和HTML检查通过。Java解码8,181条运行时条目，四种字体样式及引擎符号覆盖通过；本文件缺键回退为零，所提供参考的481条英文回退仍来自亡灵战役。物品页布局夹具保持497/500像素，面板590×467。游戏内验证继续暂缓。

此前75份可编辑properties及七份运行时properties逐字节不变。简介仅新增元素使独立对话文件进度，保留简洁、无剧透及双语战役名。详见 `inspection/elementalist-dialogue-batch1-validation.json` 和扩展验证报告。本批未安装、提交、推送或上传Steam。
