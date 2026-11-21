# 永生之旅独立对白第3批：回归游戏提示

2026-11-21。按用户指定范围翻译剩余七组回归游戏提示，共66条内容键（33条角色名、33条台词）。它们是角色欢迎玩家回归和产品提示，不是战役剧情回顾。

## 范围与来源

| 完整对白组 | 内容键数 | 对白定义核对 |
| --- | ---: | --- |
| AOF1_Long_time_no_see | 8 | aof.jar |
| AOF2_Long_time_no_see | 10 | aof.jar |
| AOF3_Long_time_no_see | 8 | aof.jar |
| AOF4_Long_time_no_see | 12 | aof.jar |
| AOF5_Long_time_no_see | 18 | aof.jar |
| AOFFREE_Long_time_no_see | 8 | 仅英文properties；未找到XML |
| AOFTOTAL_Long_time_no_see | 2 | aof.jar |
| 合计 | 66 | 六组XML、一个仅文本组 |

英文文本均来自 `aof-alchemist-dlc/alchemistdlc-conversations-en.properties`；六组定义位于主程序的 `com/aof/resource/conversation/`，不在炼金术士扩展归档内。当前安装的aof.jar、aof-data.zip及data归档中未找到AOFFREE的对应XML。该组按英文资源完整翻译，不编造XML、不复制英文补缺，不认定未找到定义就是游戏故障。实际加载与显示仍未验证。

`ConversationsObjectFactory` 中存在 `_Long_time_no_see` 命名片段；这只能作为引擎命名来源的静态线索，不能证明七组均会在Total中触发。覆盖声明分别记录外部XML归档及仅能核对文本的例外。检查器报告累计29组XML、267条XML对应内容，另有AOFFREE八条仅文本核对。

## 翻译处理

沿用贝尔卡拉、因杜尔夫、莱克莎及单位术语。珀西瓦尔爵士、吉姆利、多林、埃林暂定音译，已加入术语表。保留卡拉的催促、矮人的醉态、娜迦嘶声、鼠人对人类的称呼及因杜尔夫与莱克莎对“我的／我们的”争执。

产品名Age of Fear及两个完整英文标题保留；其余正文翻译为中文。原有11处HTML换行与标签顺序保留。图片路径和莱克莎肖像变量属于原XML，未改动或新增到文本资源。

## 覆盖与验证

独立对话文件达到275/275条内容（100%），共30个完整组、2条元数据；构建新增完整源键集要求，防止后续遗漏。此前209条扩展内容逐键保留，其他73份可编辑properties及五份运行时properties逐字节不变。正文4,215条、通用文件3,163条、亡灵战役251条保持原进度。文件全覆盖不代表整部扩展、主战役或全部动态文本完成。

构建、占位符、HTML及扩展检查通过；累计两个选项引用、五个纯图片索引、九个战场对白名称引用保持有效。Java解码7,920条运行时条目，四种字体样式和引擎符号通过；本文件缺键回退为零。所提供参考资源余下481条英文回退均属亡灵战役。物品页布局夹具通过：497/500像素，面板590×467；自动检查不证明游戏内布局。

简介保持简洁、无剧透与双语战役名，仅更新本文件进度。详见 `inspection/alchemist-dialogue-batch3-validation.json`、`inspection/expansion-validation.json` 和 `inspection/expansion-xml-validation.json`。本批未安装、提交、推送或上传Steam；游戏内测试继续暂缓。
