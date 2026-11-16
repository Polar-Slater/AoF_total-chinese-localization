# 亡灵战役第2批：骨河桥与雾磨镇

2026-11-16。推进战役剧情，通用事件与通用对话仍由另一位协作者负责。

## 范围与进度

- 新增50条内容键：Level05、Level06、Level07共14条；六组U02对话共26条；UXX_Krill_impatient、UXX_PlayerUnit_death、UXX_Vision_1共10条。
- `undeadcampaign`：49/344；`undeadcampaign-conversations`：46/388；合计95/732（13.0%），另有4条元数据。按条目计数，不代表字数或整章完成。
- 内容包括伪装香料商人、骨河桥交战、亡灵招募与唤起、撤回沼泽及战后幻象。原有45条内容及元数据全部保留。
- 地名沿用暗影沼泽 (Shadowmarshes)、雾磨镇 (Mistmill)，新增骨河 (Bone River)；卫兵玩笑中的艾泽拉斯 (Azeroth) 保留原文专名。步兵、弓箭手、憎恶、僵尸和魔法戒指沿用术语表。

## 原文与依赖核对

- 核对本地亡灵战役XML、英文properties，以及同一亡灵归档中的六组U02和三组UXX对话XML；未改动原文或脚本。
- Level04仅为向后兼容的空商店，退出到Level05，无可翻译内容键。实际流程为Level05 → Level05b → Level06 → Level07；Level05b调用U02_Shop_enter，招募名称和物品名称使用已有正文译文。两个商店不虚增为已译资源组。
- Level06初始化调用UXX_PlayerUnit_death、UXX_Krill_impatient、U02_Zombie_impatient及U02_Zombie_raise，本批全部覆盖。另解压骨河桥BRD内部的zlib数据，检查序列化内容中的U02_Abomination_raise、U02_Footman_death、U02_Footman_raise引用；这属于静态资源检查，不是游戏实测。
- Level06胜利进入Level07，失败转入变量指定的通用失败关卡；本批未将通用失败流程计入战役新增覆盖。此段没有新增选项分支。
- 魔法戒指英文目标写作“before turn ten”，脚本实际判断战斗结束且回合数LESS_EQUAL_10。中文按实际条件写作“在第十回合结束前赢得战斗”；不改脚本。
- Level07退出时解锁Level09，并在show-visions-enabled为yes时播放UXX_Vision_1；本批包含整组幻象对话。对应图片节点没有文本键，不补造文本。
- UXX组属于战役对话文件，不能算入通用对话覆盖。小游戏脚本英文等既有通用资源限制不因本批而改变。

## 构建与验证

- `build_translation.py`通过：完整声明组、键、占位符及次数、HTML、=BR=、元数据、运行时命名冲突、ASCII Java properties校验。
- 使用游戏自带Java运行`inspection/CheckPilot.java`：成功解码5,906条运行时条目；静态Noto Sans SC四种字形覆盖译文、NBSP／项目符号及2,218条剩余英文回退。
- 与HEAD逐键比对，两份战役文件的旧译文全部保留；正文、通用事件、通用对话运行时文件内容不变。更新生成的战役覆盖和共享报告总条目数，共享内容覆盖保持1,582/3,163。
- Workshop简介仅更新本地可编辑进度行，保留双语战役名和预览，UTF-8字节数低于7,999上限。
- 未安装、上传、提交或推送；游戏内排版测试继续按用户要求暂缓。自动验证不证明显示布局或所有运行时分支正确。

## 下一批

从Level09沼泽遇袭和U03系列继续，核对后续战斗、战后叙事与商店／幻象依赖，再声明完整资源组。
