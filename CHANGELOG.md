# Changelog

Project versions describe translation milestones, not game versions.

## [Unreleased]

### 简介战役表格（2026-11-21）
- 将开放战役和扩展剧情的项目列表改为两列表格，保留剧情战役表格、中英双语名称及全部进度数字。
- 仓库与本地模组简介已同步，UTF-8长度3,773字节；完整备份和文件校验通过，其他资源与配置保持不变，未上传Steam。

### 完成扩展与简介本地同步（2026-11-21）
- 按用户要求安装八部扩展的12份已完成运行时文件，共2,377条内容；本地模组增至17份properties、10,044条运行时条目，全部与仓库构建一致。
- 同步最新简洁简介（3,161 UTF-8字节）；安装前完整备份并核对哈希，保留原正文、通用文本、亡灵战役、字体、许可、预览图及简介外配置。
- 暂存包通过Java解码、四种字体和物品页布局检查，安装后逐文件哈希匹配。更新当前安装记录；未上传Steam或推送GitHub，游戏内测试继续暂缓。

### 战争机器扩展第1批（2026-11-21）
- 完成323条当前关卡正文和六组52条独立对白，共375条；两份文件完整覆盖所声明英文基线，既有83份可编辑及15份运行时properties保留。
- 核对当前鼠人主战役源与XML、六处对白调用、四个选项、材料条件和12项任务；排除五个内部字段，记录解毒剂数量差异及工具路线条件疑点，游戏脚本不变。
- Java解码10,044条运行时条目，新文件无缺键回退；四种字体和物品页布局通过。更新术语、进度、问题记录及简洁简介；未安装、提交、推送或上传。

### 生者与死者扩展第1批（2026-11-21）
- 完成293条当前关卡内容及四组41条独立对白，共334条；两份文件均完整覆盖所声明英文基线。保留之前81份可编辑properties和13份运行时properties。
- 核对当前鼠人主战役资源与扩展XML、四个选项、两个对白触发引用及10项战斗任务；记录六个内部字段排除、送玫瑰对白的触发限制及原版蓝宝石奖励数量差异。
- Java解码9,665条运行时条目，新文件无缺键回退，四种字体及物品页布局通过。更新术语、进度、问题记录与简洁简介；未安装、提交、推送或上传。

### 风暴山扩展第1批（2026-11-21）
- 完成当前关卡正文536条及21组独立对白118条，合计654条内容；两份文件均100%覆盖所声明英文基线，保持原有译文及主战役分工。
- 使用当前主战役资源核对旧扩展文件与XML的差异；保留段落，明确排除九条内部XML字段。核对两条洞窟选择路线、10项战斗任务、三处对白调用及17个战场名称引用，记录一组未找到触发引用的对白和未译VXX依赖。
- Java解码9,327条运行时条目，新文件无缺键回退；四种字体及物品页布局通过。更新术语、进度、问题记录与简洁简介；未安装、提交、推送或上传。

### 维克多的实验第1批（2026-11-21）
- 完成27组独立对白238条，以及当前关卡正文、选项和内嵌对白114条，共352条；两份资源分别完整覆盖，不计入既有通用或主战役进度。
- 核对发现旧扩展属性文件落后于关卡XML，改用主战役资源中完全匹配当前XML的114条LevelZombieFranky文本。设置流程可重建该局部英文参考；记录RES-002，不改原版资源。
- 检查14个关卡、34处对白调用、25处对白选项引用和一个战场名称引用，保留密码变量、材料条件、招募及胜败脚本。新关卡资源继续使用原vampirehuntercampaign标记，后续主战役翻译须避免重复键。
- Java解码8,669条运行时条目，两份新资源回退为零；四种字体与物品页布局通过。更新简介和进度，未安装、推送或上传。

### 血与月独立对白第1批（2026-11-21）
- 完成全部21组130条独立对白，`werewolfdlc-conversations` 达到130/130（100%）：七组关卡调用对白76条、14组战斗反应54条。既有通用文本、战役及其他扩展译文保留。
- 核对所有对白XML、七处条件调用及五个战场中的14个完整对白名称引用；分别处理矮人／森林路线和谢拉夫妻对白，保留原HTML和打断语气。
- Java解码8,313条运行时条目，本文件英文回退归零；四种字体与物品页布局检查通过。更新简介、术语和进度；未安装、推送或上传。

### 元素使独立对白第1批（2026-11-21）
- 完成全部五组18条独立对白（含角色名），`elementalistdlc-conversations` 达到18/18（100%）；三组欢迎／谜题反馈12条、两组战斗反应6条。此前所有译文保留。
- 核对五份对白XML、谜题正误路线及一个战场中的两个对白名称引用；保持既有通用文本和脚本不变，构建要求完整英文键集。
- Java解码8,181条运行时条目，本文件英文回退为零；四种字体及物品页布局通过。更新简介和进度，未安装、推送或上传。

### 海盗独立对白第2批（2026-11-21）
- 补齐四组战斗反应10条（5条角色名、5条台词），独立对话文件达到239/239（100%），共18组；构建要求完整源键集。
- 核对四份对白XML和四个战场中的完整对白名称引用，保留三处HTML换行及既有229条内容；其他资源译文不变。
- Java解码8,161条运行时条目，海盗英文回退归零；四种字体与物品页布局检查通过。更新简介及进度记录，未安装、推送或上传。

### 海盗独立对白第1批（2026-11-21）
- 完成14组PXX剧情对白229条，`piratesdlc-conversations` 覆盖229/239（95.8%）；四组战斗反应10条仍回退英文。人类与亡灵路线分别翻译，既有通用事件、永生之旅及主战役译文全部保留。
- 核对全部对白XML、14处关卡调用及刽子手遭遇的逃跑／迎战两个选项；保留英雄变量、HTML和地名英文。检查器以已审核的完整命令列表验证非跳转选项，不改剧情脚本。
- Java解码8,151条运行时条目，四种字体与物品页布局通过；所检资源英文回退491条（亡灵481、海盗10）。更新简洁简介、术语及进度记录；未安装、推送或上传。

### 永生之旅独立对白第3批（2026-11-21）
- 完成七组回归游戏提示66条（33条角色名、33条台词），独立对话文件达到275/275（100%），共30组；构建要求本文件完整覆盖英文键集。此前209条及其他资源译文保持不变。
- 六组回归提示58条与主程序aof.jar内的XML核对；AOFFREE八条未找到对应XML，仅完成英文资源核对并明确记录限制，不据此认定游戏故障或实际显示正常。
- Java解码7,920条运行时条目；本扩展英文回退为零，所检查资源余下481条回退均属于亡灵战役。四种字体与物品页布局检查通过。简介更新为275/275，未安装、推送或上传。

### 永生之旅独立对白第2批（2026-11-21）
- 完成九组战斗反应，共34条内容，独立对话文件累计209/275（76.0%）；仅余七组回归游戏提示66条。此前175条对白及正文、通用资源、亡灵战役译文全部保留。
- 扩展检查覆盖五个压缩战场文件中的九个对白名称引用；与对白XML逐项核对，并保留原HTML。此检查不证明游戏内触发行为。
- Java解码7,854条运行时条目，检查547条英文回退及四种字体样式；物品页布局检查通过。更新仓库简介和进度记录；未安装、推送或上传。

### 永生之旅独立对白第1批（2026-11-21）
- 完成14组AXX对白，共175条内容，独立对话文件覆盖175/275（63.6%）。九组战斗反应34条及七组回归提示66条仍回退英文；不计入已完成的通用文件总数。
- 新增独立扩展对白覆盖声明、构建注册及XML检查，保留5个纯图片索引并核对2个仪式选项及既有结局文本。正文、通用资源和亡灵战役译文不变。
- Java解码7,820条运行时内容（含元数据），检查581条英文回退及四种字体样式；物品页布局检查通过。更新简洁简介、术语与覆盖报告，记录原文封印名称差异TXT-005。未安装、推送或上传本批。

### 进度记录与简介同步（2026-11-21）
- 本地项目同步至已合并通用第31批和亡灵战役第5批的GitHub基线。修正当前进度记录：正文4,215条、通用事件2,144条、通用对话1,019条、亡灵战役251/732条（34.3%）；历史批次记录保留当时状态。
- 按用户提供的简洁版本保存Workshop简介，保留双语战役名、游戏版本、使用方法及资源覆盖范围；同步到本地模组配置前备份并校验，其他配置、译文、字体、许可和预览保持不变。

### 通用事件第31批（2026-11-17）
- 补齐开放世界商店、开放世界战斗、史莱姆巢穴和走私者窝点四条标签。通用事件2,144/2,144、通用对话1,019/1,019，合计3,163/3,163（100%）。这仅指两个通用文件，不代表全游戏或独立战役／扩展对白完成。
- 构建校验现要求两个通用资源与英文基线的键集合完全一致，防止后续漏键。新增四个关卡检查及两组外部战役对白引用。
- 旧译文与战役文件不变；Java解码7,598条，两个通用文件英文回退均为零，四种字体样式和物品页布局检查通过。
- 简介更新进度及完成范围；随后按用户要求同步至本地模组，保留较新的251条战役内容、字体及配置。安装前实际通用内容为2,227条，比旧简介标注少83条；本次补齐936条至3,163条，原因未确定。完整备份、安装后哈希、Java字体及物品页布局检查通过。未提交、推送或上传。

### 通用事件第30批（2026-11-17）
- 完成海盗支线的全部178条通用关卡文本；事件覆盖2,140/2,144（99.8%），通用内容合计3,159/3,163（99.9%），剩余四条地点标签。
- 覆盖酒馆、海战、越狱、寻宝、夜袭及刽子手支线；核对队伍恢复、一次性奖励、任务条件及独立对白中的选择引用。十四组独立扩展对白仍待翻译。
- 新增BUG-003：夜袭任务提示要求消灭潜海者，XML却检查元素生物计数。保留原文目标与脚本，未实测奖励触发。
- 已有译文与战役文件保持不变；Java解码7,594条，四种字体样式和530条英文回退检查通过，物品页布局检查仍为497/500。
- 简介及进度记录已更新；第22–30批尚未安装、提交、推送或上传。

### 通用事件第29批（2026-11-17）
- 完成炼金术士支线的全部181条通用关卡文本；事件覆盖1,962/2,144（91.5%），通用内容合计2,981/3,163（94.2%），剩余182条事件文本。
- 覆盖许愿井、矿洞探索、巨龙雕像、海上传送门、两种结局和失败页；核对投币与物品消耗、矿洞进度、封印合成和仪式选择。十四组独立扩展对白仍待翻译，不宣称整个扩展完成。
- 已有译文与战役文件保持不变；Java解码7,416条，四种字体样式和708条英文回退检查通过，物品页布局检查仍为497/500。
- 简介及进度记录已更新；第22–29批尚未安装、提交、推送或上传。

### 通用事件第28批（2026-11-17）
- 完成狼人支线最终战斗、战后叙述与招募结局，新增96条；事件覆盖1,781/2,144（83.1%），通用内容合计2,800/3,163（88.5%），剩余363条事件文本。
- 通用源文件的251条狼人文本已全覆盖；七组独立扩展对白仍待翻译，未据此宣称整个扩展完成。核对两条战斗分支、四项任务及接受／拒绝招募的结果。
- 已有译文与战役文件保持不变；Java解码7,235条，四种字体样式和889条英文回退检查通过，物品页布局检查仍为497/500。
- 简介及进度记录已更新；第22–28批尚未安装、提交、推送或上传。

### 通用事件第27批（2026-11-17）
- 完成染血的信与绑匪的踪迹，新增101条；事件覆盖1,685/2,144（78.6%），通用内容合计2,704/3,163（85.5%），剩余459条事件文本。
- 补齐矮人／森林两条战斗对白及后续审问，核对任务奖励、队伍暂存与恢复、娜迦战斗胜败汇入同一后续剧情的路线；四组独立扩展战后提示仍未译入。
- 已有译文与战役文件保持不变；Java解码7,139条，四种字体样式和985条英文回退检查通过，物品页布局检查仍为497/500。
- 简介及进度记录已更新；第22–27批尚未安装、提交、推送或上传。

### 通用事件第26批（2026-11-17）
- 完成血与月开场、困境中的狼和关联失败文本，新增54条；事件覆盖1,584/2,144（73.9%），通用内容合计2,603/3,163（82.3%），剩余560条事件文本。
- 核对两个阶段的九个关卡、队伍暂存与恢复、任务奖励及失败路线；三组独立扩展对白仍未译入。后续从染血的信继续，不据本批宣称整条狼人支线完成。
- 旧译文与战役文件保持不变；Java解码7,038条，四种字体样式及1,086条英文回退检查通过，物品页布局检查仍为497/500。
- 简介与进度已更新；第22–26批尚未安装、提交、推送或上传。

### 通用事件第25批（2026-11-17）
- 完成元素使的通用关卡文本与炼金工匠商店，新增67条；事件覆盖1,530/2,144（71.4%），通用内容合计2,549/3,163（80.6%），剩余614条事件文本。
- 核对谜题、五场战斗的任务奖励与回合条件、商店和胜败跳转；新增21个关联关卡检查。三组EXX对白属于独立扩展资源，未计入完成量。
- 保留已有译文、战役文件及占位符；Java解码6,984条，四种字体样式及1,140条英文回退检查通过。
- 更新简介进度并说明扩展剧情与通用文本的边界；第22–25批尚未安装、提交、推送或上传。

### 通用事件第24批（2026-11-17）
- 完成死灵法师公会与隐世修道院，新增107条；事件覆盖1,463/2,144（68.2%），通用内容合计2,482/3,163（78.5%），剩余681条事件文本。
- 核对公会两条人物对白分支与商店解锁、修道院时间条件、战前商店及战后结局；新增人物暂定译名，保留相互讥讽的原文语气。
- 在问题日志登记祈祷入口与草药店伏击叙述不一致，未改动原脚本或以译文掩盖。构建、XML、Java与字体检查通过，既有译文保持不变。
- 简介进度已更新；第22–24批尚未安装、提交、推送或上传。

### 通用事件第23批（2026-11-17）
- 完成训练假人的复仇与暗影之境，新增22条；通用事件1,356/2,144（63.2%），通用内容合计2,375/3,163（75.1%）。通用对话保持100%，剩余788条事件文本。
- 保留假人的谷粒笑话；核对解锁条件、战斗胜败、奖励与传送门封闭，登记两个独立战役入场对白依赖。
- 构建、XML关联、Java解码与字体检查通过，旧译文及战役文件不变；简介进度已更新。第22–23批尚未安装、提交、推送或上传。

### 通用事件第22批（2026-11-17）
- 完成蛮王陵墓与幸福之泉，新增43条通用事件文本；事件覆盖1,334/2,144（62.2%），通用内容合计2,353/3,163（74.4%）。通用对话保持100%，剩余810条事件文本。
- 核对祷词选项、尝试计数、战斗返回与结局，以及喷泉费用和奖励；登记矮人战役专属修复对白依赖，未改动战役译文。
- 构建、XML关联、Java解码及字体检查通过，既有译文保持不变；简介仅更新分类进度。
- 第22批尚未安装、提交、推送或上传，安装版本仍截至通用第21批。

### Local sync through shared batch 21 (2026-11-17)
- Installed shared batches 18–21 at the user’s request: 112 new entries, bringing shared content to 2,310 and shared conversations to 1,019/1,019. Updated the installed description’s shared counts and date.
- Preserved all 251 installed campaign content entries and their description progress, which are newer than the repository baseline; main messages, fonts, preview and ownership metadata remain unchanged.
- Verified a full backup, staged Java decoding of 6,790 entries, four-style font coverage, inventory layout fixture and installed SHA-256 matches. Only the two shared properties files and description in config.xml changed. No Steam upload or new in-game test.

### 通用对话补齐第21批（2026-11-17）
- 补齐7条系列介绍及2条调试文本，通用对话达到1,019/1,019（100%）；同时补译介绍页共用的14条按钮与说明。
- 通用事件累计1,291/2,144，通用内容合计2,310/3,163（73.0%）；剩余853条均来自通用事件文件，不包含独立战役或脚本直接生成的英文。
- 构建新增通用对话全键覆盖检查，核对8个共用选项与10个宣传触发关卡；保留调试变量、链接、显隐条件及关闭逻辑。
- 自动检查通过，旧译文及主消息／战役运行时不变；更新简介与术语。第18–21批尚未安装，本批未提交、推送或上传。

### 通用事件与通用对话第20批（2026-11-17）
- 完成世界之结三项挑战的入口、提示及胜败返回对白，新增34条（8条通用对话、26条地点／选项与提示）。累计2,287/3,163（72.3%），通用对话1,010/1,019（99.1%）。
- 核对三组物品条件、进入时锁定挑战、队伍缓存、三个战前商店及六条胜败返回分支；保留原文一次性挑战和仅英雄进入的说明。
- 更新术语、简介进度及覆盖报告；自动校验通过，旧译文、正文及战役资源保持不变。
- 第18–20批尚未安装；本批未提交、推送或上传，游戏内测试继续暂缓。

### 通用事件与通用对话第19批（2026-11-17）
- 完成马戏团舞者与沙虫遭遇，新增31条：8条通用对话、23条地点／选项及叙述。累计通用内容2,253/3,163（71.2%），通用对话剩余17条。
- 核对演出费用、钻石条件、取回／赠送分支、舞者入队及沙虫战斗的胜败跳转；不修改脚本，不计入沙虫开放战役。
- 构建、XML关联、Java解码与四种字体样式检查通过，旧译文及主消息／战役运行时保留；简介仅更新分类进度。
- 本批尚未安装、提交、推送或上传，游戏内测试继续暂缓。

### 通用事件与通用对话第18批（2026-11-17）
- 完成丛林金字塔与法师集市，新增24条：4条通用对话、20条地点／选项及叙述。累计通用内容2,222/3,163（70.2%）。
- 核对探索、木乃伊入口条件、战前商店、胜败跳转与集市随机开市；独立战役入场对话继续留给战役工作流。
- 构建、XML关联、Java解码与四种字体样式检查通过，旧译文及主消息／战役运行时内容保留。简介仅更新进度与日期，保留双语战役名。
- 本批尚未安装、提交、推送或上传，游戏内排版待集中检查。

### User-approved terminology (2026-11-17)
- Changed the funds display and its recruitment tutorial reference from 财宝 to 资金. Treasure item categories and story text retain their contextual wording.
- Standardized Regular as 正规军 in its label, prestige explanations, effects and shared recruitment text; updated the glossary.
- Rebuilt and validated 22 changed entries, then installed the two affected runtime resources after backup and hash verification. Other mod files, including newer campaign translations and the inventory font fix, remain unchanged.

### Inventory layout font fix (2026-11-17)
- Fixed the reproduced inventory layout overflow by selecting a compact-line-height AoF Han UI derivative for button text. The treasure row and item list now require 497 pixels instead of 502 inside the fixed 500-pixel container. Other font roles and translation content are unchanged.
- Added a reproducible font preparation script, derivative license notice and Swing layout regression check. Original glyph outlines, character mappings, advance widths and shaping tables are preserved.
- Installed the three-file fix after a full backup and SHA-256 verification, preserving all other mod files, including newer campaign translations. Game restart and visual confirmation remain pending; no upload or Git publication.

### Google Fonts Noto Sans SC package
- Prepared the supplied static Regular font without altering its bytes, retaining the existing runtime filename. Included the matching OFL copyright/license and a provenance notice in build staging and the Workshop package.
- Moved obsolete local SimHei test fonts out of staging into a backup, and excluded the downloaded ZIP from Git. Java decoding and four-style glyph checks passed for 6,633 runtime entries and 1,491 English fallback entries.
- Installed the new static font, OFL license and provenance notice into the local Workshop mod at the user's request, after a verified full backup. Removed the unused installed SimHei font; hash checks confirmed all other files unchanged. Java checks passed against the installed folder. No Steam upload.

### Concise, spoiler-free Workshop description
- Replaced detailed event and campaign summaries with category-level progress counts; removed story, recruitment, reward and location details while preserving bilingual campaign names and setup instructions.
- Added a spoiler-free description rule to project instructions. Updated local installed and staged descriptions with metadata backups; no Steam upload.

### Local Workshop sync through Undead batch 4
- Installed the two campaign resources and updated description at the user's request. Installed content now includes 2,198 shared and 206 Undead content entries, with 6,633 total runtime entries.
- Verified a full backup, staged Java decoding and four-style font coverage, and SHA-256 matches after installation. All other installed files, including shared resources, main messages, font, preview and non-description ownership metadata, were preserved.
- Installed description is 4,970 UTF-8 bytes after newline normalization and trimming. No Steam upload or new in-game test; earlier batch notes retain their historical pre-installation state.

### Merge parallel shared and campaign work
- Combined shared batches through 17 (2,198/3,163 content entries) with Undead batches through 4 (206/732), preserving both workstreams' editable translations and runtime resources.
- Resolved progress, batch-index and testing-history conflicts per resource section; retained both changelog histories. Replaced chat-relative assignments with neutral workstream instructions and documented the merge rules in CONTRIBUTING.md.
- Rebuilt reports and validated 6,633 runtime entries plus 1,491 English fallback entries in four font styles. Installation history remains separate; this merge does not install or upload the combined package.

### Undead campaign: Haunted Church
- Added 89 content entries: Level11b/Level13 (27), both U04 dialogue groups (22), and five linked UXX groups (40). Campaign coverage is 206/732 (28.1%).
- Checked the textless Level12 shop, Noea's recruitment, both reward conditions, serialized battle-board dialogue references and the base unlock. Included the bone dragon's later Level16 departure dialogue without counting that level as translated; base-upgrade campaign dialogue remains pending.
- Build and Java decoding/four-style font checks passed: 6,017 runtime entries and 2,107 English fallback entries. All previous translations, including uncommitted batches 2–3, preserved; main/shared translation and runtime files unchanged. New entries preserve source HTML tag structure.
- Updated glossary, coverage/progress records and local Workshop description. No installation, upload, commit or push; in-game layout testing remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH4.md.

### Undead campaign: Night Assault
- Added 22 content entries: Level09–Level11 (18) and both U03 dialogue groups (4). Campaign coverage is 117/732 (16.0%).
- Checked the Level09b shop, battle-board dialogue references, all three reward conditions and the route to Haunted Church. Turn limits follow the inclusive script conditions; existing recurring dialogue is reused.
- Build, Java decoding and four font-style checks passed: 5,928 runtime entries and 2,196 English fallback entries. All previous translations, including uncommitted batch 2, preserved; main/shared translation and runtime files unchanged.
- Updated local coverage/progress records. No installation, upload, commit or push; in-game layout testing remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH3.md.

### Undead campaign: Bone River / Mistmill
- Added 50 content entries: Level05–Level07 (14), all six U02 dialogue groups (26), and three linked UXX groups (10). Campaign coverage is 95/732 (13.0%).
- Checked the legacy Level04 shop, current Level05b shop, battle-board dialogue references, reward condition and post-battle vision against local game resources. The objective wording reflects the script’s inclusive turn-10 limit.
- Build and Java properties/font checks passed: 5,906 runtime entries and 2,218 English fallback entries. Previous translations preserved; main/shared resources unchanged.
- Updated coverage reports and local progress documentation. No installation, upload, commit or push; in-game layout review remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH2.md.

### Local Workshop sync through shared batch 17
- Installed shared batches 13–17 and the latest description at the user’s request. The local mod now contains 6,472 runtime entries, including 2,198 shared content keys and the existing 45 Undead content keys.
- Updated only the two shared properties files and `config.xml`. Full backup and SHA-256 checks passed; all other files and ownership metadata remain unchanged. The installed description is 4,911 UTF-8 bytes after newline normalization and trimming.
- No Steam upload, Git publication or new in-game test. Earlier batch validation reports record their pre-installation state.

### 通用事件与通用对话 batch 17 (2026-11-16)
- Added 24 keys for the Crystal Mine and Cursed Wights: 14 conversation keys and 10 location/choice keys. Shared coverage reaches 2,198/3,163 (69.5%); conversation coverage is 990/1,019 (97.2%).
- Followed the mine battle and daily income branches, plus the hidden Cursed Sword encounter trigger and Wight battle rewards. Included textless levels in XML checks without inventing resource keys or modifying scripts.
- Updated description, terminology and progress records. Existing translations and campaign resources remain unchanged; shared batches 13–17 remain uninstalled and unpublished. See `docs/batches/SHARED-EVENTS-BATCH17.md`.

### 通用事件与通用对话 batch 16 (2026-11-16)
- Added 105 keys for the Pearl Mermaid and Shaman’s Hut: 18 conversation keys and 87 location/choice keys. Shared coverage reaches 2,174/3,163 (68.7%); conversation coverage is 976/1,019 (95.8%).
- Checked daily pearl trading, the one-time Black Pearl reward, and all 36 hero cleansing menus and their 200-gold costs. Recorded the existing hero-107/hero-17 mismatch in the original `on-select-42` command; preserved source placeholders and scripts.
- Updated description, terminology and progress records. Prior translations and campaign resources remain unchanged; shared batches 13–16 are uninstalled and unpublished. See `docs/batches/SHARED-EVENTS-BATCH16.md`.

### 通用事件与通用对话 batch 15 (2026-11-16)
- Added 53 keys for the Tranquil Grove and Well of Souls: 8 conversation keys and 45 location/choice keys. Shared coverage reaches 2,069/3,163 (65.4%); conversation coverage is 958/1,019 (94.0%).
- Checked four seedling costs and progress-dependent unit rewards, plus nine sacrifice choices, cancellation guards, separate one-time flags and item rewards. Recorded two external campaign dialogue dependencies and an existing duplicated dialogue command in the Dwarf sacrifice branch.
- Updated the description and progress records while preserving prior translations and campaign resources. Shared batches 13–15 remain uninstalled; no publication or new game test. See `docs/batches/SHARED-EVENTS-BATCH15.md`.

### 通用事件与通用对话 batch 14 (2026-11-16)
- Added 12 keys for the three Magic Sources and the World Tree: 4 conversation keys and 8 location keys. Shared coverage reaches 2,016/3,163 (63.7%); conversation coverage is 950/1,019 (93.2%).
- Checked independent daily shard availability and the World Tree’s conditional one-apple reward against active XML commands. Preserved the exploration narrative and existing item terminology.
- Updated the description and progress records. Campaign resources remain unchanged; batches 13–14 are not installed or published. See `docs/batches/SHARED-EVENTS-BATCH14.md`.

### 通用事件与通用对话 batch 13 (2026-11-16)
- Added 45 keys for the Moon Well and Mana Obelisks: 8 conversation keys and 37 location/choice keys. Shared coverage reaches 2,004/3,163 (63.4%); conversation coverage is 946/1,019 (92.8%).
- Verified all seven offering costs and per-unit experience rewards. Distinguished the obelisk’s seven-shard entry threshold from its removal of up to 999 shards; recorded inconsistencies in the original obelisk narration.
- Updated file-based description and progress records, preserving prior translations and campaign resources. Batch 13 is built and validated but not installed or published; the installed mod remains at shared batch 12.
- See `docs/batches/SHARED-EVENTS-BATCH13.md`.

### Local Workshop sync through shared batch 12
- Installed the two shared resources, the existing two Undead opening resources and the updated description at the user’s request. Local package now contains 6,233 runtime entries, including 1,959 shared content keys and 45 Undead content keys.
- Full mod backup and SHA-256 verification passed; all other mod files and ownership metadata were preserved. Description is 4,563 UTF-8 bytes and matches the project source. No Steam upload or new in-game test.
- Earlier batch notes record their pre-installation state.

### 通用事件与通用对话 batch 12
- Added 89 keys for the Runesmith and Transmuter's Laboratory: 28 conversation keys and 61 location/choice keys. Shared coverage is 1,959/3,163 (61.9%); conversation coverage is 938/1,019 (92.1%).
- Matched equipment names, prices and materials to the scripts. Corrected the source helmet menu from 500 to the actual 400 gold cost and its tooltip input from armour to helmet; clarified the shared daily transmutation limit and Talnes's permanent departure.
- Updated file-based Workshop progress, terminology and batch notes. Campaign resources and previous translations remain unchanged; no game test, local Workshop installation, Steam upload or Git publication.
- See `docs/batches/SHARED-EVENTS-BATCH12.md`.

### 通用事件与通用对话 batch 11
- Added 43 keys for Demon City: 31 conversation keys and 12 location/choice keys, covering discovery, entry, pact negotiation and post-pact recruitment. Shared coverage reaches 1,870/3,163 (59.1%); conversation coverage is 910/1,019 (89.3%).
- Kept the permanent base-HP cost explicit and distinguished postponing from rejecting the pact. Recorded the separate Chaos campaign entry conversation as an untranslated campaign dependency.
- Updated terminology, file-based Workshop progress and batch notes. Previous translations and campaign files are preserved; no game test, local Workshop installation, Steam upload or Git publication.
- See `docs/batches/SHARED-EVENTS-BATCH11.md`.

### 通用事件与通用对话 batch 10
- Added the complete Dark Castle dinner quest: 76 keys across eight conversation groups plus 13 location/choice keys, totaling 89. Shared coverage is 1,827/3,163 (57.8%); conversation coverage reaches 879/1,019 (86.3%).
- Covered arrival, three delivery stages, menu reminders and departure, preserving the dark comedy and bilingual location name. Verified manual-selection callbacks and cancellation guards against the game XML.
- Updated terminology, file-based Workshop progress and batch documentation. Prior translations and campaign files are preserved; no game test, local Workshop installation, Steam upload or Git publication.
- See `docs/batches/SHARED-EVENTS-BATCH10.md`.

### 通用事件与通用对话 batch 9
- Added 74 keys for the Black Dragon prerequisite encounter and Darius’s recruitment, letter, tower rescue and ending: 41 conversation keys plus 33 shared-level keys. Shared coverage reaches 1,738/3,163 (54.9%); conversation coverage is 803/1,019 (78.8%).
- Preserved bilingual map labels and the bard’s theatrical voice. Declared textless shop/battle intermediates and extended XML checks through story entry/exit and battle-result triggers.
- Updated the file-based Workshop description and progress documents. Prior translations and campaign files are preserved. No game test, local Workshop installation, Steam upload or Git publication for this batch.
- See `docs/batches/SHARED-EVENTS-BATCH9.md`.

### 通用事件与通用对话 batch 8
- Added the complete Djinn wish and Beastmaster Tayah event families: 63 conversation keys and 19 linked choices/follow-up keys, including the petrification ending and battle introduction. Shared coverage is 1,664/3,163 (52.6%); conversation coverage is 762/1,019 (74.8%).
- Extended follow-up validation to conversations queued on the world map after battle, including Tayah’s recruitment offer. Preserved prior shared translations and all campaign resources.
- Updated file-based Workshop progress and collaboration scope: this chat handles shared resources; the user’s friend handles campaigns. No game test, local Workshop installation, Steam upload or Git publication for this batch.
- See `docs/batches/SHARED-EVENTS-BATCH8.md`.

### Documentation layout
- Simplified the main README and replaced the old pilot README with current setup and testing guides.
- Grouped the plan, glossary and batch notes under docs/; added a documentation index and updated references.
- Moved the local modding guide into ignored source/reference/. Build scripts and translation resource paths are unchanged.


### Project instructions and privacy
- Consolidated current agent instructions into AGENTS.md and removed the historical handoff file. Updated documentation references.
- Removed personal account/item identifiers and installation-specific paths from tracked documentation; setup examples use placeholders. Historical backup paths are omitted.
- The legacy pilot bootstrap now requires an explicit --game argument instead of a machine-specific installation path.


### Undead campaign opening and work split
- Assigned shared events/conversations to the user's friend; campaign stories are now our active work. Renamed Chinese labels to 通用事件 / 通用对话 while preserving technical names.
- Added 35 opening story/dialogue entries; Undead coverage is 45/732 (6.1%), excluding metadata. Existing sample translations preserved.
- Added declared campaign coverage and source/placeholder/HTML/namespace checks to the build; both campaign runtime files now regenerate. Total runtime entries: 5,856.
- Updated editable Workshop description and progress documentation. No installation or upload; game layout review pending.


### Description helper review
- Added `-WhatIf` support and a missing-description check; prepare output directories before updating installed metadata.
- Back up both existing configs and restore them on save failure. Document explicit item/owner arguments.
- Tested Windows PowerShell with isolated fixtures: Chinese/Steam markup/XML round trip, wrong owner, oversized UTF-8 description, no-write dry run, missing package folder and repeated updates. Checked the actual target with `-WhatIf` only; no installed metadata changed.

### 创意工坊简介：按文件展示进度
- Replaced batch history in 总体进度 with the main message file and two shared resource files, including source/Chinese filenames, scope and per-file counts. Shared total remains 50.0%.
- Preserved all campaign sections and names. Description is 4,699 UTF-8 bytes; backed up and synced to local/staged config, with all other metadata and mod files unchanged. No Steam upload.

### 共享地点与玩法 batches 6–7 — shared text 50%
- Added 680 content keys: eight faction bases (363), systems/choices (110) and conversations (207). Cumulative shared coverage is 1,582/3,163 (50.0%); all runtime files contain 5,821 entries.
- Includes desertion, cards, cups, dice, fishing, roulette, Windmill, weather invocations and common prompts. Preserved established terminology and bilingual place names; checked fishing and card rules against scripts.
- Extended branch checks across the game's data archives, recording 22 referenced campaign-resource conversations outside shared coverage and remaining script-supplied English fragments.
- Updated the description to 6,164 UTF-8 bytes without changing campaign names. Previous batch 5 was uploaded and tested successfully by the user. New batches have automated validation and local installation only; no new Steam upload or game test.
- See `docs/batches/SHARED-TEXT-50-PERCENT.md` for scope, validation and installation details.

### 通用事件 batch 5 — global-event text milestone
- Added 264 keys across the remaining 40 SGE travel-event families and the gambler event. Cumulative shared coverage: 902/3,163 (28.5%); 5,141 runtime entries.
- Completed all 487 `SGE_` conversation keys and 410 `LevelGlobalEvent*` keys. Shared locations, generic shops and longer side stories remain pending.
- Preserved natural phrasing and bilingual place names; documented the Drunken Dwarf source probability mismatch. Extended branch checking to recursive trigger callbacks and explicitly declared battles with no text.
- Passed source, build, XML, decoding, font and preservation checks. Updated `#5 通用事件` description (5,776 UTF-8 bytes), preserved campaign names, backed up and installed two shared files plus config with hash verification. Game tests remain deferred; no publication.

### 地名格式
- Adopted the user's `中文名 (English)` convention for place names. Updated 三魔峰 (Three Devils) and 冰原 (Iceland) in the shared volcanic-event narration and recorded the rule for future translation.

### 通用事件 batch 4
- Added 156 content keys in 31 event families: 122 conversation keys and 34 choice/follow-up keys. Shared coverage reaches 638/3,163 (20.2%); 4,877 total runtime entries.
- Translated knight rivalry, Vampire/Werewolf dialogue, Orc encounters, Blademaster training and short travel events. Preserved the user's approved natural wording for the batch-3 beggar option and recorded new provisional names.
- Extended XML checking through the Orc feast's manual-unit-selection callback. Passed text, branch, Java decoding, font and preservation checks.
- Updated `#4 通用事件` description (5,578 UTF-8 bytes), preserving campaign names. Backed up and installed two shared resources plus config with hash verification. Game testing remains deferred; no Git or Steam publication.

### 通用事件 batch 3
- Added 226 content keys in 20 event families: 142 conversation keys and 84 choice/follow-up keys. Shared coverage reaches 482/3,163 (15.2%); 4,721 total runtime entries.
- Includes recruitment encounters, Dryad/bear and Unicorn/Undead interactions, stolen gold, archery wagers, old monastery, Prime Source and Undead altar. Preserves linked choices and battle introductions, source costs and established unit/item terminology.
- Passed text, XML branch, Java decoding, four-style font and preservation checks. Updated `#3 通用事件` description to 5,423 UTF-8 bytes with campaign names intact; backed up and installed two shared resources plus config with hash verification.
- User requested prioritizing translation and deferring in-game testing. No game test, Git publication or Steam upload was performed.

### 通用事件 batch 2
- Added 179 content keys across 13 travel-event families: 91 conversation keys and 88 linked choice/description keys. Cumulative shared coverage is 256/3,163 (8.1%), with 4,495 total runtime entries.
- Included caravan encounters, candles, crows, Dwarven runes, ghosts, potions, Troll encounters and the wounded Ogre. Extended XML checking to random-battle opening conversations and documented context-specific unit terminology.
- Passed source/markup/placeholders, 53 conversation groups and 51 XML-linked choices, Java decoding, four-style font coverage and preservation checks. All previous main/campaign/shared translations remain unchanged.
- Updated the description to `#2 通用事件` (5,243 UTF-8 bytes), retaining all campaign names. Backed up and installed only two shared resources and config, verifying hashes and all other files unchanged. In-game review remains pending; no publication was performed.

### 通用事件 batch 1
- Added 77 shared content keys across 13 event families: 61 conversation keys and 16 linked choice/follow-up keys. Includes the ancient temple, drinking contest, acid rain and party interactions. Shared coverage: 77/3,163 (2.4%); 4,316 total runtime entries including metadata.
- Added two shared runtime resources, source coverage declarations, shared metadata/namespace validation and an XML-based choice/outcome check. Preserved variables, placeholders, HTML and `=BR=` markers; added regression checks for rejected malformed input.
- Extended Java font checking to multiple English resources. All 4,316 runtime entries and 3,086 remaining shared fallback entries pass in four styles. Main text and campaign samples remain unchanged.
- Updated the Workshop description to include `#1 通用事件` (5,063 UTF-8 bytes), retaining all campaign names. Backed up config and installed the two shared resources plus config with hash verification. In-game review remains pending; no publication was performed.

### 正文 batch 8 — main messages complete
- Added the remaining 1,065 main entries, including 298 object descriptions, remaining interface/help, effect fragments, combat logs and faction/person names. Main coverage is 4,215/4,215 content keys, plus six metadata keys; 4,235 runtime entries including retained campaign samples. All 326 object descriptions are covered.
- Registered four editable translation files and added an exact main-key coverage requirement to the build. Expanded the glossary to 1,630 keyed rows; retained all prior translations.
- Checked duration arguments and Magic Channel log context against local game code. Repaired malformed source HTML in translated prompts. Translated number words while documenting the engine's remaining English-style spacing/thousand grouping limitation.
- Updated the description to `#8 正文` (4,899 UTF-8 bytes), preserving all 32 bilingual campaign names. Passed key/placeholder/markup, Java decoding, four-style font and preservation checks; backed up and installed two local files with hash verification. No publication was performed. Batches 6–8 still require in-game review; separate shared-event and campaign resources remain pending.

### 正文 batch 7
- Added 297 immunity, status, targeting, damage and spell-restriction entries. Main content coverage: 3,150/4,215 (74.7%), with 3,156 main runtime entries, 3,170 total runtime entries and 1,065 English fallback keys.
- Standardized the existing control-type label COMMAND to 统御; aligned the two mark-effect descriptions with their actual game names, 痛苦印记 and 死亡印记. Added 14 glossary rows (1,543 total).
- Updated `#7 正文` in the Chinese Workshop description while preserving all campaign names. User appearance feedback covers batch 5; batches 6–7 still need in-game review.
- Passed key/placeholder/markup checks, Java decoding and four-style font coverage for 3,170 runtime entries and 1,065 fallbacks. Backed up and installed the runtime/config locally, verifying installed hashes against the package. Description: 4,671 UTF-8 bytes. No publication was performed.

### 正文 batch 6
- User reported normal in-game appearance through batch 5. Added 254 summon, life-transfer, stealth, trap, weather, immunity and restriction entries; new content still requires in-game review.
- Content coverage is 2,853/4,215 (67.7% by entries), with 2,859 main runtime entries, 2,873 total runtime entries and 1,362 English fallback keys.
- Standardized Workshop headings to `#4 正文`, `#5 正文`, `#6 正文`, retained all campaign names and recorded the user's test feedback separately from new-batch validation.
- Passed build/HTML/placeholders, Java decoding and four-style font checks for 2,873 runtime entries and 1,362 English fallbacks. Preserved all prior main values and campaign samples; backed up and installed two local mod files with hash verification. No publication was performed.

### 正文说明 batch 5
- Added 20 battle/world-map tutorial pages and 189 skill/item effect fragments and supporting entries (209 total). Reused terminology, added the Slayer label, and clarified dynamic attack type/value ordering and Parry/Riposte backstab exclusions from local game code.
- Content coverage: 2,599/4,215 (61.7% by entries), with 2,605 main runtime entries, 2,619 total runtime entries and 1,616 English fallback keys. Glossary: 1,529 keyed rows.
- Updated the Chinese Workshop progress description, preserving all campaign names. All named battle/world-map tutorial keys are translated; other help and effect text remains in progress.
- Validated source keys, placeholders, markup, all 21 named tutorial keys, 2,619 Java runtime entries and 1,616 English fallback entries in four font styles. Preserved every prior main value and campaign sample; backed up and installed the runtime/description locally with hash verification. In-game layout remains pending; no publication was performed.

### 正文说明 batch 4
- Added 164 shared gameplay entries: environmental effects, equipment and potion restrictions, crafting/resources, recruitment/upgrades, traits, team morale and related effect text.
- Main content coverage is now 2,390/4,215 (56.7% by entries), with 2,396 main runtime entries including metadata, 2,410 total runtime entries and 1,825 English fallback keys.
- Reused existing terminology and UI labels; documented affinity, prestige and source-text ambiguities. Updated the Chinese Workshop progress description while retaining all campaign names.
- Build, placeholder/HTML and Java font checks passed for 2,410 runtime entries and 1,825 English fallback entries. Preserved all prior main values and campaign samples; backed up and installed the runtime/description locally, verifying hashes and unchanged remaining mod files. In-game layout remains pending; no publication was performed for this batch.

### Workshop description upload fix
- Latest wording: removed English explanatory text while preserving all 32 bilingual campaign/expansion names and setup labels. “Main text” is now “正文”; the current description is 4,134 UTF-8 bytes.
- The user's upload returned `InvalidParam`; the local description was 8,341 UTF-8 bytes, exceeding Steam's 8,000-byte limit although the character-count check passed.
- Compacted repeated campaign-status rows to lists, retaining every campaign name and progress heading. Description is now 7,062 UTF-8 bytes.
- Packaging and the local description helper now check UTF-8 bytes before changing files, with a conservative 7,999-byte maximum. Both reject the original description and boundary overflow cases; normal packaging passes.
- Backed up and updated local installed/package metadata. A successful Workshop retry remains unconfirmed; no upload was performed by the assistant.

### Terminology batch 3
- Added 1,027 main entries: 449 item/resource names and templates plus 578 skills, attributes, conditions, crafting professions, set names and short display fragments.
- Completed the 937-key main label block (399 item names/templates and 538 other labels), the 51 crafting-material labels, nine crafting-profession labels and 30 item-set labels. The 450 item/resource-name total replaces the earlier 455 suffix-based estimate, which accidentally included five UI prompts.
- Consolidated 1,528 glossary keys. Documented context-sensitive meanings, provisional proper names, and misleading internal identifiers; preserved all previously deployed main translations.
- Current coverage: 2,226/4,215 content entries (52.8% by entries, not words), 2,232 main runtime entries including metadata, 2,246 runtime entries including campaign samples, and 1,989 missing main keys.
- Expanded build coverage checks for the terminology blocks; long descriptions and in-game layout remain incomplete.
- Batch 3 passed text/build checks, Java decoding of 2,246 runtime entries, four-style font coverage including engine symbols and 1,989 English fallback entries, and a 1,528-row glossary comparison. Installed locally after backup and verified by SHA-256; no Steam upload or GitHub push.

### Terminology batch 2
- Added 396 main entries: 298 remaining object names, 70 remaining race/group labels, and 28 battlefield/stat fragments. All 326 object names and the 73-label source race/group section are covered. Descriptions remain at 28 of 326.
- Consolidated 501 keyed glossary entries. Preserved displayed-name distinctions such as GHOST=Incorporeal versus INCORPOREAL=Phasing; standardized Vase to 花瓶.
- Current totals: 1,205 main entries including metadata, 1,219 runtime entries including retained campaign samples, and 3,016 main keys remaining (28.4% text-entry coverage).
- Replaced SimHei in all four settings with local static regular Noto Sans SC, fixing missing NBSP/bullet glyph coverage. Added reproducible variable-to-static font preparation and configured-font packaging checks.
- Expanded Java validation to engine tooltip symbols, four font styles and remaining English main text. The old font fails this regression check; the replacement passes all 1,219 runtime entries and 3,016 English fallback entries. Headless Swing preview inspected; in-game confirmation remains pending.

### Added
- 320 main-text translations: 129 gameplay/statistics/inventory/skill entries, 54 bestiary entries covering 27 units, and 137 combat-log entries.
- Main-text scope and glossary notes. The initial campaign deferral was superseded by the user's restored order: terminology, gameplay descriptions, shared events, then campaigns starting with Undead.
- Consolidated terminology baseline and localization plan, with explicit remaining terminology work.

### Changed
- Register three new main-text batches in the build and report their counts separately from the original 481 Phase 1 entries.
- Record source coverage: 809 of 4,221 main-text entries supplied (including metadata); 3,412 remain untranslated. The full runtime has 823 entries including retained campaign samples.
- Generate UI properties and the validation report with LF line endings for reproducible Windows builds.

### Validation
- Source keys, duplicate keys, placeholder counts, balanced HTML and original button/settings coverage passed.
- The game's bundled Java decoded all 823 runtime entries and the local test font covered every character. All 489 previous main entries were retained; campaign runtime files were unchanged.
- Installed the main runtime file and updated description into the local test item after backing it up; installed files matched the staged package by SHA-256. No Steam upload was performed.
- New batch requires in-game review, particularly compact stat columns, long tooltips and bestiary descriptions. The earlier conversation validation warning remains unresolved.
- Later screenshot investigation confirmed SimHei lacks U+00A0/U+2022 used in engine-generated tooltip prefixes. Batch 2 addresses these with a replacement font and broader checks; game layout confirmation remains pending.

## [0.1.0] - 2026-11-15

### Added
- Initial collaborative repository for Age of Fear: Total Simplified Chinese localization.
- 481 Phase 1 translations covering menus, settings, tooltips, battle controls, difficulty and multiplayer dialogs.
- Chinese language/font metadata and small Undead campaign and conversation samples: 489 UI entries, 503 runtime entries in total.
- Validation of duplicate keys, source keys, placeholders, HTML, selected source-block coverage and ASCII Java-properties encoding.
- Project handoff, milestone notes, contributor workflow, dependency list and local-resource setup script.
- Explicit Workshop item and expected-owner arguments for packaging and description updates.

### Known limitations
- Most campaign text and gameplay descriptions remain untranslated and fall back to English.
- Full in-game layout review is pending; a conversation validation warning remains unresolved.
- Campaign edits are not rebuilt by the UI build script; extend validation/build support before substantial campaign work.
- Font files and original game resources are not distributed. A redistributable font is needed for a public playable release.
- Original pilot bootstrap retains machine-specific paths; use setup_local.py for a fresh checkout.
