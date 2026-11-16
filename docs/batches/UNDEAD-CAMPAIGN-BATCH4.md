# 亡灵战役第4批：闹鬼教堂

2026-11-16。本批覆盖教堂进入、诺娅入队、教堂战斗及据点解锁，并补齐相关战斗反应和骨龙离队对话。通用事件与通用对话保持协作者原有范围。

## 范围与进度

- 新增89条内容键：Level11b共7条、Level13共20条；U04_Banshee_damage共12条、U04_BoneDragon_raise共10条；UXX_Base_unlocked共10条、UXX_BoneDragon_remove共8条、UXX_Krill_damage共6条、UXX_Noea_damage共8条、UXX_PlagueZombie_detonate共8条。各声明组均完整翻译。
- `undeadcampaign`：94/344；`undeadcampaign-conversations`：112/388；合计206/732（28.1%），另有4条元数据。
- Noea暂译诺娅，Sir Gareth暂译加雷思爵士；沿用圣教会、报丧女妖、骨龙、瘟疫僵尸、混沌护符、寒霜胸针。地点写作闹鬼教堂 (Haunted Church)、废墟 (Ruins)。新增人物译名记入术语表，未改动旧译文。
- 诺娅对主人恭敬，对往事的回应带调侃；克里尔保持傲慢冷酷的口吻。保留没有双腿的笑话与两名幽灵早已死亡的反讽，不补写人物家谱。

## 流程与依赖核对

- 核对本地亡灵归档的战役XML、七份新增对话XML与英文properties。Level11b退出时给予750金币并进入Level12；Level12无独立英文文本键，商店兵种／物品名来自既有正文，不计作新增译文组。
- Level12退出时创建报丧女妖Noea并赋予英雄等属性、装备和法术，然后进入Level13。人物内部名称仍为Noea，脚本及查找标识未改动。第二位英雄的中文提示保留施法者脆弱、应置于近战单位后方的含义。
- 解压U04_Haunted_Church.brd的zlib载荷，按序列化字符串长度确认U04_Banshee_damage及U04_BoneDragon_raise引用。仅作静态检查，不改动战场文件；未把紧随字符串的序列化字节误认作对话名。
- Level13初始化绑定UXX_PlayerUnit_death、UXX_Krill_impatient、UXX_PlagueZombie_detonate、UXX_Krill_damage及UXX_Noea_damage。前两组已译，后三组本批补齐。瘟疫僵尸对话XML的ignore-dead条件保留在原脚本，译文不增加角色必然存活的保证。
- 两项奖励均按脚本核对：混沌护符要求敌方Ghosts种族数量为0且回合数LESS_EQUAL_12；寒霜胸针要求战斗结束且LESS_EQUAL_20。目标名称保留原文的“所有报丧女妖”，时限明确为第十二／第二十回合结束前。自动核对不等于实测奖励触发。
- Level13胜利后设置据点等级1、解锁LevelUndeadPlayerBase01及Level15，播放UXX_Base_unlocked并返回世界地图。该对话第4项只有事件图片，没有name/text；保留原文0–3、5的索引，不编造第4项对白。失败仍跳转变量指定的失败关卡，未计入本批覆盖。
- 据点定义位于亡灵归档的共享关卡XML；其界面文本属于既有shared资源，未修改。进入据点调用SXX_AnyBase_enter；升级选项会调用仍未译的战役对话UXX_LampOfBlood_gain。这是独立的后续工作，不因据点解锁或通用文件覆盖而宣称已译。
- 骨龙召起对话提示不能长期控制。核对Level16胜利后的实际离队条件：持有骨龙／幽灵龙且第三级亡灵据点尚未解锁时，播放UXX_BoneDragon_remove并移除对应单位。本批补齐该组对话，但没有翻译Level16其余内容，也不将其计为已完成关卡。
- 七份新增对话XML没有额外commands分支；Level14是通往Level15的旧版空商店，无文本，未增加覆盖条目。

## 构建与验证

- `build_translation.py`通过：完整声明组、键、占位符及次数、HTML、=BR=、元数据、命名空间及ASCII Java properties检查。新增89条逐一比较HTML标签顺序及属性，与英文一致。
- 游戏自带Java运行`inspection/CheckPilot.java`通过：解码6,017条运行时条目，检查2,107条英文回退；静态Noto Sans SC四种字形覆盖译文、引擎NBSP及项目符号。
- 对照本批开始时的本地快照，所有旧译文键值（包括未提交第2–3批）保持不变；正文与通用译文及其运行时properties保持不变。通用内容仍为1,582/3,163；通用报告仅更新全项目运行时条目总数。
- 已更新覆盖报告、术语表、进度与本地Workshop简介，保留双语战役名及所选预览；简介低于7,999 UTF-8字节上限。
- `git diff --check`通过。未安装、上传、提交或推送；游戏内排版测试继续暂缓，自动检查不证明布局正确。

## 下一批

从Level15王国巡逻队 (Kingdom Patrol) 继续，核对Level15b商店、Level16战斗／U05对话、Level17战后与UXX_Vision_1a，以及Level16失败通往LevelSecret01b的支线。已有骨龙离队译文直接复用；据点升级所调用的独立战役对话另行补齐。继续保持战役资源与通用资源分工。
