# 术语表 / Terminology baseline

当前阶段：先统一术语，再推进玩法说明、通用事件及战役剧情；剧情从亡灵战役开始。

这份表收录当前已采用的 **1630 个文本键**，包括同一术语的不同界面用法。它是项目工作基线，不代表用户逐项审定，也不代表全部术语已经完成。这里的英文短名称用于定位术语；完整英文资源仍保留在 Git 忽略的 `source/` 中。

当前主文本包含 **326 个单位与场景对象名称键**、**450 个物品／材料名称及名称模板键**；技能、特性及状态另行整理。本批已覆盖全部 326 个单位／场景对象名称，以及基础种族分组段的 73 个标签；全部326条对象说明现已译完。本批还覆盖主名称段中的 538 个技能／属性／条件标签、450 个物品与材料名称／模板、9 个制作职业和30个套装标签。原来的455统计按 `_ITEM` 后缀计数，误包含5条界面提示，已修正。主消息文件中的效果说明现已全部补译，仍需游戏内校对。

## 使用规则

- 地名采用“中文名 (English)”格式，保留原文拼写和大小写，使用半角括号，例如用户给出的“斯托斯 (Storrs)”。该示例仅用于说明格式，不据此新增游戏条目。后续地点标签、叙述和对话中的地名均采用此格式。
- 用户偏好自然、贴近原意的表达，避免刻意添加方言或过度口语化。例如已确认“这个乞丐在浪费我们的时间，我们走吧。”；角色特色仍应依据原文保留。

- 单位、物品和技能的显示名称以本表为基线；将来的描述、战斗日志、通用事件及剧情复用同一译名。
- 原有通用术语继续沿用：Campaign＝战役、Battle＝战斗、Turn＝回合、Unit＝单位、Team＝队伍、Faction＝阵营、Skill＝技能、Trait＝特性、Evolve＝进阶、Items Cache＝物品仓库。
- 先按英文显示名称和玩法上下文确定含义，再翻译；不要仅依据文本键或内部类名猜测。保留原键名、占位符及功能性 HTML。
- 普通标签与窄栏简称分别记录，例如“生命值／生命”“远程攻击／远攻”；简称不替代正文中的完整名称。
- 修订术语时同步更新名称、相关说明和日志，再更新本表及变更记录。已有译文需一并检索，不能只修改新批次。
- 未确定的词保留为待定项，结合单位说明、技能效果或游戏画面核对，不把英文回退计作已翻译。

## 容易混淆的含义

- **Affinity / alignment＝阵营倾向**：指邪恶、神圣或中立，区别于队伍所属的 Faction／阵营。
- **Prestige＝资历**：对应正规／老兵／精英；Evolve＝进阶，指兵种进阶。界面按钮沿用“进阶”“解散”“技能”。
- **Minor hero＝次要英雄；serious wound＝重伤**。重伤需要战外治疗；不要与普通生命值损失混为一谈。

- **unblockable＝不受牵制限制**：相邻敌军使多数法术与远程攻击无法使用时，此行动仍可使用；它不是“无法格挡”。
- **Raise Dead＝唤起亡者，Resurrection＝复活术**：保留两种不同技能的区别。
- **Ensnared＝网缚，Entangled＝缠绕**：不同状态使用不同名称。
- **Lifedrain＝生命汲取，Soul Capture＝灵魂捕获**：生命与灵魂不是同一效果。
- **Wight＝尸妖，Lich＝巫妖，Ghoul＝食尸鬼**：不同单位不得混译。
- **Relic＝圣物，Artefact＝宝物，Treasure＝财宝**：分别对应当前物品品质／类别；涉及新物品时仍需核对实际背景。
- 源文键含 `OVERLOADED` 的几条战斗日志实际显示的是泛指的 “affected”；当前按显示文本译为“受到影响”，不擅自增加过载效果。

## 单位与对象 / Units and objects

| English | 中文 | 文本键 |
| --- | --- | --- |
| Abomination | 憎恶 | `game.object.abomination.name` |
| Alchemist | 炼金术士 | `game.object.alchemist.name` |
| Animated Armour | 活化铠甲 | `game.object.animatedarmor.name` |
| Battle Animated Armour | 战斗活化铠甲 | `game.object.animatedarmorupgraded.name` |
| Animated Bed | 活化床 | `game.object.animatedbeddouble.name` |
| Animated Chair | 活化椅子 | `game.object.animatedchairwooden.name` |
| Halloween Pumpkin | 万圣节南瓜 | `game.object.animatedpumpkin.name` |
| Animated Table | 活化桌子 | `game.object.animatedtablefancy.name` |
| Training Dummy | 训练假人 | `game.object.animatedtrainingdummy.name` |
| Animated Vase | 活化花瓶 | `game.object.animatedvasebig.name` |
| Anvil | 铁砧 | `game.object.anvil.name` |
| Archmage | 大法师 | `game.object.archmage.name` |
| Artificer | 炼金工匠 | `game.object.artificer.name` |
| Ballista | 弩炮 | `game.object.ballista.name` |
| Banshee | 报丧女妖 | `game.object.banshee.name` |
| Greater Banshee | 高等报丧女妖 | `game.object.bansheeancient.name` |
| Barbarian | 野蛮人 | `game.object.barbarian.name` |
| Bard | 吟游诗人 | `game.object.bard.name` |
| Barrel | 木桶 | `game.object.barrel.name` |
| Barrel | 木桶 | `game.object.barrelempty.name` |
| Barrel | 木桶 | `game.object.barrelgrain.name` |
| Barrel | 木桶 | `game.object.barrelwater.name` |
| Barricade | 路障 | `game.object.barricade.name` |
| Barricade Gate | 路障门 | `game.object.barricadegate.name` |
| Snares | 捕兽夹 | `game.object.beartrap.name` |
| Beastmaster | 驯兽师 | `game.object.beastmaster.name` |
| Bed | 床 | `game.object.beddouble.name` |
| Berserker | 狂战士 | `game.object.berserker.name` |
| Black Dragon | 黑龙 | `game.object.blackdragon.name` |
| Juggernaut Golem | 毁灭魔像 | `game.object.blackirongolem.name` |
| Black Knight | 黑骑士 | `game.object.blackknight.name` |
| Black Knight | 黑骑士 | `game.object.blackknightindulf.name` |
| Black Orc | 黑兽人 | `game.object.blackorc.name` |
| Blademaster | 剑术大师 | `game.object.blademaster.name` |
| Bone Dragon | 骨龙 | `game.object.bonedragon.name` |
| Bone Golem | 骸骨魔像 | `game.object.bonegolem.name` |
| Bone Trap | 骸骨陷阱 | `game.object.bonetrap.name` |
| Bowman | 弓箭手 | `game.object.bowman.name` |
| Bull | 公牛 | `game.object.bull.name` |
| Cactus | 仙人掌 | `game.object.cactus.name` |
| Cactus | 仙人掌 | `game.object.cactustall.name` |
| Cannon | 加农炮 | `game.object.cannon.name` |
| Swamp Ivy | 沼泽藤蔓 | `game.object.carnivorousivy.name` |
| Mutated Swamp Ivy | 变异沼泽藤蔓 | `game.object.carnivorousivymutated.name` |
| Cauldron | 大锅 | `game.object.cauldron.name` |
| Cave Bear | 洞熊 | `game.object.cavebear.name` |
| Cerberus | 地狱三头犬 | `game.object.cerberus.name` |
| Chair | 椅子 | `game.object.chairwooden.name` |
| Channeler | 引魔者 | `game.object.channeler.name` |
| Fire Hydra | 烈焰多头蛇 | `game.object.chaoshydra.name` |
| Chaos Mage | 混沌法师 | `game.object.chaosmage.name` |
| Horror | 恐魔 | `game.object.chaosspawn.name` |
| Greater Horror | 高等恐魔 | `game.object.chaosspawngreater.name` |
| Chicken | 鸡 | `game.object.chicken.name` |
| Chieftain | 酋长 | `game.object.chieftain.name` |
| Chimera | 奇美拉 | `game.object.chimera.name` |
| Clay Golem | 黏土魔像 | `game.object.claygolem.name` |
| Corrupted Ent | 腐化树人 | `game.object.corruptedent.name` |
| Corrupted Spider | 腐化蜘蛛 | `game.object.corruptedgiantspider.name` |
| Couch | 沙发 | `game.object.couch.name` |
| Couch | 沙发 | `game.object.couchcorner.name` |
| Cow | 奶牛 | `game.object.cow.name` |
| Crabman | 蟹人 | `game.object.crabman.name` |
| Crate | 木箱 | `game.object.crate.name` |
| Crystal Ball | 水晶球 | `game.object.crystalball.name` |
| Cyclops | 独眼巨人 | `game.object.cyclops.name` |
| Warrior Cyclops | 独眼巨人战士 | `game.object.cyclopswar.name` |
| Dancer | 舞者 | `game.object.dancerfemale.name` |
| Dark Acolyte | 黑暗侍僧 | `game.object.darkacolyte.name` |
| Demon Mistress | 恶魔女主人 | `game.object.demonmistress.name` |
| Demonologist | 恶魔术士 | `game.object.demonologist.name` |
| Dire Bear | 恐熊 | `game.object.direbear.name` |
| Djinn | 灯神 | `game.object.djin.name` |
| Ifrit | 伊弗利特 | `game.object.djinifrit.name` |
| Drider | 蛛人 | `game.object.drider.name` |
| Drider Blood Mage | 蛛人血法师 | `game.object.driderbloodmage.name` |
| Drider Warrior | 蛛人战士 | `game.object.driderwarrior.name` |
| Dryad | 林妖 | `game.object.dryad.name` |
| Blade Dancer | 剑舞者 | `game.object.dryadbladedancer.name` |
| Huntress | 女猎手 | `game.object.dryadhuntress.name` |
| Nature Sorceress | 自然女巫 | `game.object.dryadsorceress.name` |
| Dungeon Door | 地牢门 | `game.object.dungeondoor.name` |
| Death Seeker | 寻死者 | `game.object.dwarfdeathseeker.name` |
| Dwarven Engineer | 矮人工程师 | `game.object.dwarfflamethrower.name` |
| Forgemaster | 锻造大师 | `game.object.dwarfforgemaster.name` |
| Dwarven Ghost | 矮人幽灵 | `game.object.dwarfghost.name` |
| Gunner | 火枪手 | `game.object.dwarfgunner.name` |
| Dwarven Lord | 矮人领主 | `game.object.dwarflord.name` |
| Dwarven Mine | 矮人地雷 | `game.object.dwarfmine.name` |
| Mutated Dwarf | 变异矮人 | `game.object.dwarfmutant.name` |
| Dwarven Rogue | 矮人游荡者 | `game.object.dwarfrouge.name` |
| Runesmith | 符文锻造师 | `game.object.dwarfrunemaster.name` |
| Sentry Gun | 哨戒炮 | `game.object.dwarfsentrygun.name` |
| Tesla Gunner | 特斯拉炮手 | `game.object.dwarfteslagunner.name` |
| Dwarven Warrior | 矮人战士 | `game.object.dwarfwarrior.name` |
| Air Elemental | 风元素 | `game.object.elementalair.name` |
| Earth Elemental | 土元素 | `game.object.elementalearth.name` |
| Fire Elemental | 火元素 | `game.object.elementalfire.name` |
| Water Elemental | 水元素 | `game.object.elementalwater.name` |
| Ent | 树人 | `game.object.ent.name` |
| Saproling | 幼树人 | `game.object.entsaproling.name` |
| Evil Eyes | 邪眼 | `game.object.evileyes.name` |
| Elder | 邪眼长老 | `game.object.evileyeselder.name` |
| Executioner | 刽子手 | `game.object.executioner.name` |
| Gunpowder Barrel | 火药桶 | `game.object.explosivebarrel.name` |
| Fairy | 妖精 | `game.object.fairy.name` |
| Fiend | 凶魔 | `game.object.fiend.name` |
| Fire Archer | 烈焰弓箭手 | `game.object.firearcher.name` |
| Brazier | 火盆 | `game.object.firestand.name` |
| Footman | 步兵 | `game.object.footman.name` |
| Fungusoid | 菌人 | `game.object.fungusoid.name` |
| Elder Fungusoid | 菌人长老 | `game.object.fungusoidelder.name` |
| Parasitic Fungusoid | 寄生菌人 | `game.object.fungusoidvampiric.name` |
| Gargoyle | 石像鬼 | `game.object.gargoyle.name` |
| Elder Gargoyle | 石像鬼长老 | `game.object.gargoyleelder.name` |
| Clockwork Gargoyle | 发条石像鬼 | `game.object.gargoylemechanical.name` |
| Dracolich | 龙巫妖 | `game.object.ghostdragon.name` |
| Ghoul | 食尸鬼 | `game.object.ghoul.name` |
| Sea Snake | 海蛇 | `game.object.gianteel.name` |
| Venomous Sea Snake | 剧毒海蛇 | `game.object.gianteelpoisonous.name` |
| Ice Giant | 冰霜巨人 | `game.object.giantice.name` |
| Giant Warrior | 巨人战士 | `game.object.giantmauler.name` |
| Giant Rat | 巨鼠 | `game.object.giantrat.name` |
| Crab God | 蟹神 | `game.object.giantredcrab.name` |
| Desert Scorpion | 沙漠蝎 | `game.object.giantscorpion.name` |
| Giant Spider | 巨型蜘蛛 | `game.object.giantspider.name` |
| Black Spider | 黑蜘蛛 | `game.object.giantspiderblack.name` |
| Stone Giant | 岩石巨人 | `game.object.giantstone.name` |
| Wasp | 胡蜂 | `game.object.giantwasp.name` |
| Killer Wasp | 杀人蜂 | `game.object.giantwaspkiller.name` |
| Goblin | 地精 | `game.object.goblin.name` |
| Goblin Archer | 地精弓箭手 | `game.object.goblinarcher.name` |
| Goblin Assassin | 地精刺客 | `game.object.goblinassassin.name` |
| Goblin Catcher | 地精捕手 | `game.object.goblincatcher.name` |
| Goblin Wolf Rider | 地精狼骑兵 | `game.object.goblinrider.name` |
| Goblin Sapper | 地精工兵 | `game.object.goblinsapper.name` |
| Grain Bag | 粮袋 | `game.object.grainbag.name` |
| Grain Bags | 粮袋 | `game.object.grainbags.name` |
| Harpy | 鹰身女妖 | `game.object.harpy.name` |
| Harpy Fury | 狂怒鹰身女妖 | `game.object.harpyfury.name` |
| Storm Witch | 风暴女巫 | `game.object.harpywitch.name` |
| Heater | 暖炉 | `game.object.heater.name` |
| Hellbat | 地狱蝠 | `game.object.hellbat.name` |
| Hellblazer | 地狱雷炮 | `game.object.hellblazer.name` |
| High Priest | 大祭司 | `game.object.highpriest.name` |
| Hydra | 多头蛇 | `game.object.hydra.name` |
| Clockwork Hydra | 发条多头蛇 | `game.object.hydramechanical.name` |
| Ice Golem | 寒冰魔像 | `game.object.icegolem.name` |
| Imp | 小恶魔 | `game.object.imp.name` |
| Impaled Skeleton | 穿刺骸骨 | `game.object.impaledskeleton.name` |
| Inquisitor | 审判官 | `game.object.inquisitor.name` |
| Insectoid | 虫人 | `game.object.insectoid.name` |
| Insectoid Brute | 虫人蛮兵 | `game.object.insectoidbrute.name` |
| Insectoid Hunter | 虫人猎手 | `game.object.insectoidhunter.name` |
| Larva | 幼虫 | `game.object.insectoidlarva.name` |
| Iron Golem | 钢铁魔像 | `game.object.irongolem.name` |
| Jellyfish | 水母 | `game.object.jellyfish.name` |
| Ocean Jellyfish | 远洋水母 | `game.object.jellyfishdeep.name` |
| Jug | 水罐 | `game.object.jug.name` |
| King | 国王 | `game.object.king.name` |
| Knight | 骑士 | `game.object.knight.name` |
| Fallen Knight | 堕落骑士 | `game.object.knightevil.name` |
| Griffin Rider | 狮鹫骑士 | `game.object.knightgriffin.name` |
| Lady | 贵妇 | `game.object.lady.name` |
| Guardian | 守护者 | `game.object.laserbarrelrobot.name` |
| Armoured Guardian | 装甲守护者 | `game.object.laserbarrelrobotupgraded.name` |
| Lava Spike | 熔岩尖刺 | `game.object.lavaspire.name` |
| Lever | 拉杆 | `game.object.leverfloor.name` |
| Lich | 巫妖 | `game.object.lich.name` |
| Lightning Ball | 闪电球 | `game.object.lightningball.name` |
| Mage | 法师 | `game.object.mage.name` |
| Elementalist | 元素使 | `game.object.mageelementalist.name` |
| Magic Crystal | 魔法水晶 | `game.object.magiccrystal.name` |
| Magma Golem | 熔岩魔像 | `game.object.magmagolem.name` |
| Mancubus | 曼库魔 | `game.object.mancubus.name` |
| Mancubus Brute | 蛮力曼库魔 | `game.object.mancubusbrute.name` |
| Mandrake Root | 曼德拉草根 | `game.object.mandragora.name` |
| Marine | 海军陆战队员 | `game.object.marine.name` |
| S.W.A.T. | 特警 | `game.object.marineswat.name` |
| Mature Slime | 成熟史莱姆 | `game.object.matureslime.name` |
| Clockwork Dragon | 发条巨龙 | `game.object.mechanicaldragon.name` |
| Mimic | 拟态怪 | `game.object.mimic.name` |
| Minotaur | 牛头人 | `game.object.minotaur.name` |
| Monk | 僧侣 | `game.object.monk.name` |
| Mortar | 迫击炮 | `game.object.mortar.name` |
| Mummy | 木乃伊 | `game.object.mummy.name` |
| Naga | 娜迦 | `game.object.naga.name` |
| Naga Archer | 娜迦弓箭手 | `game.object.nagaarcher.name` |
| Naga Warrior | 娜迦战士 | `game.object.nagawarrior.name` |
| Necromancer | 死灵法师 | `game.object.necromancer.name` |
| Ninja | 忍者 | `game.object.ninja.name` |
| Noble | 贵族 | `game.object.nobleyoung.name` |
| Nuclear Goblin Sapper | 核爆地精工兵 | `game.object.nucleargoblinsapper.name` |
| Octopod | 章鱼 | `game.object.octopod.name` |
| Electrical Octopod | 电能章鱼 | `game.object.octopodelectric.name` |
| Kraken | 克拉肯 | `game.object.octopodkraken.name` |
| Ogre | 食人魔 | `game.object.ogre.name` |
| Oracle | 神谕者 | `game.object.oracle.name` |
| Fallen Angel | 堕落天使 | `game.object.oracleevil.name` |
| Orc | 兽人 | `game.object.orc.name` |
| Paladin | 圣骑士 | `game.object.paladin.name` |
| Peasant | 农民 | `game.object.peasant.name` |
| Pig | 猪 | `game.object.pig.name` |
| Pikeman | 长枪兵 | `game.object.pikeman.name` |
| Pirate | 海盗 | `game.object.pirate.name` |
| Swashbuckler | 劫掠海盗 | `game.object.pirateupgraded.name` |
| Plague Rat | 疫鼠 | `game.object.plaguerat.name` |
| Ranger | 游侠 | `game.object.ranger.name` |
| Rat Monstrosity | 畸变鼠怪 | `game.object.ratmanabomination.name` |
| Toxicologist | 毒药师 | `game.object.ratmanalchemist.name` |
| Rat Assassin | 鼠人刺客 | `game.object.ratmanassassin.name` |
| Rat Assassin | 鼠人刺客 | `game.object.ratmanassassinfemale.name` |
| Rat Master Assassin | 鼠人刺客大师 | `game.object.ratmanassassinmaster.name` |
| Rat Brawler | 鼠人格斗士 | `game.object.ratmanbrawler.name` |
| Rat Brute | 鼠人蛮兵 | `game.object.ratmanbrute.name` |
| Rat Enforcer | 鼠人执法者 | `game.object.ratmancrossbow.name` |
| Rat Grenadier | 鼠人掷弹兵 | `game.object.ratmangrenadier.name` |
| Rat Armoured Grenadier | 鼠人重甲掷弹兵 | `game.object.ratmangrenadierarmored.name` |
| Rat Guardian | 鼠人卫士 | `game.object.ratmanguardian.name` |
| Rat Headhunter | 鼠人猎头者 | `game.object.ratmanheadhunter.name` |
| Rat Hunter | 鼠人猎手 | `game.object.ratmanhunter.name` |
| Pack Master | 群鼠统领 | `game.object.ratmanpackmaster.name` |
| Acid Cannon | 酸液炮 | `game.object.ratmanplaguecannon.name` |
| Sage | 贤者 | `game.object.ratmansage.name` |
| Grand Sage | 大贤者 | `game.object.ratmansagegrand.name` |
| Rat Scout | 鼠人斥候 | `game.object.ratmanscout.name` |
| Rat Thrull | 鼠人奴仆 | `game.object.ratmanthrull.name` |
| Lava Crystal | 熔岩水晶 | `game.object.redcrystal.name` |
| Red Dragon | 红龙 | `game.object.reddragon.name` |
| Revenant | 复生亡灵 | `game.object.revenant.name` |
| Royal Guard | 皇家卫士 | `game.object.royalguard.name` |
| Fire Rune Trap | 火焰符文陷阱 | `game.object.runetrapfire.name` |
| Freezing Rune Trap | 冰冻符文陷阱 | `game.object.runetrapfreeze.name` |
| Lightning Rune Trap | 闪电符文陷阱 | `game.object.runetraplighting.name` |
| Ronin | 浪人 | `game.object.samurai.name` |
| Samurai | 武士 | `game.object.samuraiarmored.name` |
| Tengu | 天狗 | `game.object.samuraidemon.name` |
| Samurai Rifleman | 铁炮武士 | `game.object.samuraigunner.name` |
| Undead Samurai | 亡灵武士 | `game.object.samuraiundead.name` |
| Sandworm | 沙虫 | `game.object.sandworm.name` |
| Sarcophagus | 石棺 | `game.object.sarcophagusbroken.name` |
| Mummy Sarcophagus | 木乃伊石棺 | `game.object.sarcophagusmummy.name` |
| Sea Diver | 潜海者 | `game.object.seadiver.name` |
| Sea Diver Fisher | 潜海者渔夫 | `game.object.seadiverfisher.name` |
| Sea Diver Warrior | 潜海者战士 | `game.object.seadiverwarrior.name` |
| Shade | 暗影幽魂 | `game.object.shade.name` |
| Shaman | 萨满 | `game.object.shaman.name` |
| Waste Golem | 污秽魔像 | `game.object.shitgolem.name` |
| Mermaid | 美人鱼 | `game.object.siren.name` |
| Sea Witch | 海巫 | `game.object.sirenwitch.name` |
| Skeleton | 骷髅 | `game.object.skeleton.name` |
| Skeleton Archer | 骷髅弓箭手 | `game.object.skeletonarcher.name` |
| Skeletal Beast | 骸骨巨兽 | `game.object.skeletonbeast.name` |
| Skeleton Mage | 骷髅法师 | `game.object.skeletonmage.name` |
| Skeleton Rider | 骷髅骑兵 | `game.object.skeletonrider.name` |
| Skeleton Warrior | 骷髅战士 | `game.object.skeletonwarrior.name` |
| Bone Catapult | 骸骨投石车 | `game.object.skullcatapult.name` |
| Slime | 史莱姆 | `game.object.slime.name` |
| Sea Harpooner | 海洋鱼叉手 | `game.object.snailartillery.name` |
| Snake | 蛇 | `game.object.snake.name` |
| Snowman | 雪人 | `game.object.snowman.name` |
| Spores | 孢子 | `game.object.sporestrap.name` |
| Dragon Statue | 巨龙雕像 | `game.object.statuedragon.name` |
| Lampman Statue | 持灯人雕像 | `game.object.statuelampman.name` |
| Lizard Statue | 蜥蜴雕像 | `game.object.statuelizard.name` |
| Stone Golem | 岩石魔像 | `game.object.stonegolem.name` |
| Iron Stove | 铁炉 | `game.object.stoveiron.name` |
| Succubus | 魅魔 | `game.object.succubus.name` |
| Summoner | 召唤师 | `game.object.summoner.name` |
| Swamp Beast | 沼泽巨兽 | `game.object.swampbeast.name` |
| Swamp Flower | 沼泽花 | `game.object.swampflower.name` |
| Swamp Willow | 沼泽柳 | `game.object.swampwillow.name` |
| Table | 桌子 | `game.object.tablefancy.name` |
| Table | 桌子 | `game.object.tablewooden.name` |
| Table | 桌子 | `game.object.tablewoodenlong.name` |
| Tavernmaster | 酒馆老板 | `game.object.tavernkeeper.name` |
| Telescope | 望远镜 | `game.object.telescope.name` |
| Torch | 火把 | `game.object.torchlit.name` |
| Torch | 火把 | `game.object.torchlitblue.name` |
| Torch | 火把 | `game.object.torchunlit.name` |
| Battle Totem | 战斗图腾 | `game.object.totembattle.name` |
| Disease Totem | 疾病图腾 | `game.object.totemdisease.name` |
| Fear Totem | 恐惧图腾 | `game.object.totemfear.name` |
| Healing Totem | 治疗图腾 | `game.object.totemheal.name` |
| Toxic Spores | 剧毒孢子 | `game.object.toxicspores.name` |
| Training Dummy | 训练假人 | `game.object.trainingdummy.name` |
| Rubble | 碎石堆 | `game.object.trashsewer.name` |
| Treasure Chest | 宝箱 | `game.object.treasurechest.name` |
| Enhanced Treasure Chest | 强化宝箱 | `game.object.treasurechestmagic.name` |
| Troll | 巨魔 | `game.object.troll.name` |
| Troll Thrower | 巨魔投掷者 | `game.object.trollthrower.name` |
| Turtle | 乌龟 | `game.object.turtle.name` |
| Turtle Beast | 巨龟兽 | `game.object.turtlebeast.name` |
| Altar of Undead | 亡灵祭坛 | `game.object.undeadaltar.name` |
| Undead King | 亡灵之王 | `game.object.undeadking.name` |
| Unicorn | 独角兽 | `game.object.unicorn.name` |
| War Unicorn | 战争独角兽 | `game.object.unicornwar.name` |
| Valkyrie | 女武神 | `game.object.valkyrie.name` |
| Vampire | 吸血鬼 | `game.object.vampire.name` |
| Vampiric Bat | 吸血蝙蝠 | `game.object.vampirebat.name` |
| Vampiric Mist | 吸血迷雾 | `game.object.vampirefog.name` |
| Vampire Hunter | 吸血鬼猎人 | `game.object.vampirehunter.name` |
| Vampire Hydra | 吸血多头蛇 | `game.object.vampirehydra.name` |
| Vampiress | 女吸血鬼 | `game.object.vampirelady.name` |
| Vampire Lord | 吸血鬼领主 | `game.object.vampirelord.name` |
| Vase | 花瓶 | `game.object.vasebig.name` |
| Decorative Vase | 装饰花瓶 | `game.object.vasedecorative.name` |
| Vase | 花瓶 | `game.object.vaseempty.name` |
| Vase | 花瓶 | `game.object.vaseflowers.name` |
| Warg | 座狼 | `game.object.warg.name` |
| Warlock | 术士 | `game.object.warlock.name` |
| War Ogre | 战争食人魔 | `game.object.warogre.name` |
| Wasp Nest | 胡蜂巢 | `game.object.waspnest.name` |
| Weapon Rack | 武器架 | `game.object.weaponrack.name` |
| Werewolf | 狼人 | `game.object.werewolf.name` |
| Alpha Werewolf | 狼人首领 | `game.object.werewolfalpha.name` |
| Wight | 尸妖 | `game.object.wight.name` |
| Will-o'-Wisp | 鬼火 | `game.object.willowisp.name` |
| Witch | 女巫 | `game.object.witch.name` |
| Witch | 女巫 | `game.object.witchyoung.name` |
| Wolf | 狼 | `game.object.wolf.name` |
| Wyvern | 双足飞龙 | `game.object.wyvern.name` |
| Wyverns Nest | 双足飞龙巢 | `game.object.wyverneggs.name` |
| Zombie | 僵尸 | `game.object.zombie.name` |
| Plague Zombie | 瘟疫僵尸 | `game.object.zombieplague.name` |
| Super Zombie | 超级僵尸 | `game.object.zombiesuper.name` |


## 种族与阵营 / Races and alignment

| English | 中文 | 文本键 |
| --- | --- | --- |
| Dragons | 龙族 | `DRAGONS` |
| Knights | 骑士 | `KNIGHTS` |
| Soldiers | 士兵 | `SOLDIERS` |
| Pirates | 海盗 | `PIRATES` |
| Samurais | 武士 | `SAMURAIS` |
| Mages | 法师 | `MAGES` |
| Chaos Mages | 混沌法师 | `CHAOS_MAGES` |
| Human Mages | 人类法师 | `HUMAN_MAGES` |
| Sages | 贤者 | `SAGES` |
| Priests | 祭司 | `PRIESTS` |
| Peasants | 农民 | `PEASANTS` |
| Nobles | 贵族 | `NOBLES` |
| Sandworms | 沙虫 | `SANDWORMS` |
| Goblins | 地精 | `GOBLINS` |
| Golems | 魔像 | `GOLEMS` |
| Grogan | 格罗甘 | `GROGAN` |
| Orcs | 兽人 | `ORCS` |
| Ogres | 食人魔 | `OGRES` |
| Trolls | 巨魔 | `TROLLS` |
| Shamans | 萨满 | `SHAMANS` |
| Wolves | 狼 | `WOLVES` |
| Wargs | 座狼 | `WARGS` |
| Ghosts | 幽灵 | `GHOSTS` |
| Zombies | 僵尸 | `ZOMBIES` |
| Necromancers | 死灵法师 | `NECROMANCERS` |
| Alchemists | 炼金术士 | `ALCHEMISTS` |
| Rat Grenadiers | 鼠人掷弹兵 | `RATMEN_GRENADIERS` |
| Ratmen | 鼠人 | `RATMEN` |
| Skeletons | 骷髅 | `SKELETONS` |
| Vampires | 吸血鬼 | `VAMPIRES` |
| Demons | 恶魔 | `DEMONS` |
| Desert Dwellers | 沙漠居民 | `DESERT_DWELLERS` |
| Constructs | 构装体 | `CONSTRUCTS` |
| Assassins | 刺客 | `ASSASSINS` |
| Hydras | 多头蛇 | `HYDRAS` |
| Beasts | 野兽 | `BEASTS` |
| Dwarves | 矮人 | `DWARVES` |
| Liches | 巫妖 | `LICHES` |
| Slimes | 史莱姆 | `SLIMES` |
| Slavers | 奴隶贩子 | `SLAVERS` |
| Ifrit | 伊弗利特 | `IFRIT` |
| Insectoids | 虫人 | `INSECTOIDS` |
| Ents | 树人 | `ENTS` |
| Fungusoids | 菌人 | `FUNGUSOIDS` |
| Executioners | 刽子手 | `EXECUTIONERS` |
| Mandragoras | 曼德拉草 | `MANDRAGORAS` |
| Ivies | 藤蔓 | `IVIES` |
| Dryads | 林妖 | `DRYADS` |
| Fairies | 妖精 | `FAIRIES` |
| Elementals | 元素生物 | `ELEMENTALS` |
| Furniture pieces | 家具 | `FURNITURES` |
| Driders | 蛛人 | `DRIDERS` |
| Pigs | 猪 | `PIGS` |
| Cows | 奶牛 | `COWS` |
| Turtles | 龟类 | `TURTLES` |
| Chickens | 鸡 | `CHICKENS` |
| Bears | 熊 | `BEARS` |
| Unicorns | 独角兽 | `UNICORNS` |
| Gargoyles | 石像鬼 | `GARGOYLES` |
| Octopods | 章鱼 | `OCTOPODS` |
| Nagas | 娜迦 | `NAGAS` |
| Eels | 海蛇 | `EELS` |
| Divers | 潜海者 | `DIVERS` |
| Plants | 植物 | `PLANTS` |
| Werewolves | 狼人 | `WEREWOLVES` |
| Minotaurs | 牛头人 | `MINOTAURS` |
| Harpies | 鹰身女妖 | `HARPIES` |
| Halloween | 万圣节 | `HALLOWEEN` |
| Cyclops | 独眼巨人 | `CYCLOPS` |
| Ninjas | 忍者 | `NINJAS` |
| Sirens | 海妖 | `SIRENS` |
| Jellyfishes | 水母 | `JELLYFISHES` |
| Giants | 巨人 | `GIANTS` |
| Undead | 亡灵 | `UNDEAD` |
| Humans | 人类 | `HUMANS` |
| Neutral | 中立 | `NEUTRAL` |
| Evil | 邪恶 | `EVIL` |
| Holy | 神圣 | `HOLY` |


## 属性与简称 / Statistics and compact labels

| English | 中文 | 文本键 |
| --- | --- | --- |
| Hit Points | 生命值 | `HIT_POINTS` |
| Magic Points | 魔法值 | `MAGIC_POINTS` |
| Morale | 士气 | `MORALE` |
| Attack | 攻击 | `ATTACK` |
| Defence | 防御 | `DEFENCE` |
| Speed | 速度 | `SPEED` |
| Ranged Attack | 远程攻击 | `RANGED_ATTACK` |
| Experience | 经验值 | `EXPERIENCE` |
| Kills | 击杀数 | `KILLS` |
| Race | 种族 | `RACE` |
| HP | 生命 | `HP_STATS` |
| MP | 魔法 | `MP_STATS` |
| MRL | 士气 | `MRL_STATS` |
| ATT | 攻击 | `ATT_STATS` |
| DEF | 防御 | `DEF_STATS` |
| SPD | 速度 | `SPD_STATS` |
| ATR | 远攻 | `ATR_STATS` |
| EXP | 经验 | `EXP_STATS` |
| KLS | 击杀 | `KLS_STATS` |
| Ingredient Resources | 制作材料 | `INGREDIENT_RESOURCES` |

## 物品类别与品质 / Item categories and rarity

| English | 中文 | 文本键 |
| --- | --- | --- |
| Common | 普通 | `ITEM_RARITY_COMMON` |
| Legendary | 传说 | `ITEM_RARITY_LEGENDARY` |
| Rare | 稀有 | `ITEM_RARITY_RARE` |
| \*Relic\* | \*圣物\* | `ITEM_RARITY_RELIC` |
| amulet | 护符 | `ITEM_TYPE_AMULET` |
| armour | 护甲 | `ITEM_TYPE_ARMOUR` |
| artefact | 宝物 | `ITEM_TYPE_ARTEFACT` |
| bow/crossbow | 弓／弩 | `ITEM_TYPE_BOW_WEAPON` |
| headgear | 头部装备 | `ITEM_TYPE_HEADGEAR` |
| potion | 药剂 | `ITEM_TYPE_POTION` |
| resource | 材料 | `ITEM_TYPE_RESOURCE` |
| ring | 戒指 | `ITEM_TYPE_RING` |
| shield | 盾牌 | `ITEM_TYPE_SHIELD` |
| shoes | 鞋靴 | `ITEM_TYPE_SHOES` |
| staff | 法杖 | `ITEM_TYPE_STAFF` |
| treasure | 财宝 | `ITEM_TYPE_TREASURE` |
| trophy | 战利品 | `ITEM_TYPE_TROPHY` |
| two-handed weapon | 双手武器 | `ITEM_TYPE_TWOHANDED_WEAPON` |
| weapon | 武器 | `ITEM_TYPE_WEAPON` |

## 技能与状态 / Skills and statuses

| English | 中文 | 文本键 |
| --- | --- | --- |
| Defensive Stance | 防御姿态 | `DEFENSIVESTANCE_SPELL` |
| unblockable | 不受牵制限制 | `UNBLOCKABLE` |
| self | 自身 | `SELF` |
| Lifedrain Attack | 生命汲取攻击 | `LIFEDRAINATTACK` |
| Lifedrain | 生命汲取 | `LIFEDRAIN_SPELL` |
| Lifedrain | 生命汲取 | `LIFEDRAIN` |
| Raise Dead | 唤起亡者 | `RAISEDEAD_SPELL` |
| Resurrection | 复活术 | `RESURRECTION_SPELL` |
| Soul Capture | 灵魂捕获 | `SOULCAPTURE` |
| Blinded | 失明 | `BLINDED` |
| Burning | 燃烧 | `BURNING` |
| Confused | 混乱 | `CONFUSED` |
| Crippled | 残疾 | `CRIPPLED` |
| Deep Wound | 深度创伤 | `DEEPWOUND` |
| Disease | 疾病 | `DISEASE` |
| Frozen | 冻结 | `FROZEN` |
| Head Injury | 头部创伤 | `HEADINJURY` |
| Panic | 恐慌 | `PANIC` |
| Poisoned | 中毒 | `POISONED` |
| Corrosion | 腐蚀 | `CORROSION` |
| Stunned | 眩晕 | `STUNNED` |
| Ensnared | 网缚 | `ENSNARED` |
| Entangled | 缠绕 | `ENTANGLED` |
| High Morale | 高昂士气 | `HIGHMORALE` |
| Avatar | 化身 | `AVATAR` |
| Illusion | 幻象 | `ILLUSION` |
| Shadow Oil | 暗影油 | `INVISIBILITYPOTION_ITEM` |
| Hide in Shadow | 潜入暗影 | `INVISIBILITYSELF_SPELL` |
| Invisibility | 隐形术 | `INVISIBILITY_SPELL` |
| Identify | 鉴定 | `CRAFTINGIDENTIFY` |
| Alchemist | 炼金术士 | `CRAFTINGALCHEMIST` |
| Backstab | 背刺 | `BACKSTAB` |
| Greater Backstab | 强效背刺 | `IMPROVEDBACKSTAB` |
| Camouflage | 伪装 | `CAMOUFLAGE` |
| Floating | 漂浮 | `FLOATING` |
| Incorporeal | 无实体 | `GHOST` |
| Phasing | 相位化 | `INCORPOREAL` |


## 战斗结果 / Combat outcomes

| English | 中文 | 文本键 |
| --- | --- | --- |
| Miss | 未命中 | `MISS` |
| Hit | 命中 | `HIT` |
| Resist | 抵抗 | `RESIST` |
| Failed | 失败 | `FAILED` |
| Critical Hit | 暴击 | `CRITICAL_HIT` |
| Critical | 暴击 | `CRITICAL` |
| Critical Miss | 严重失误 | `CRITICAL_MISS` |
| Critical Miss (Evade) | 严重失误（闪避） | `CRITICAL_MISS_EVADE` |

## 战场与地形 / Terrain

| English | 中文 | 文本键 |
| --- | --- | --- |
| Swamp | 沼泽 | `SWAMP` |
| Swamp | 沼泽 | `SWAMPGLOBAL` |
| Winter | 冬季 | `WINTER` |
| Sewer | 下水道 | `SEWER` |
| Cave | 洞穴 | `CAVE` |
| Village | 村庄 | `VILLAGE` |
| Lava Fields | 熔岩地带 | `LAVA` |
| Sea | 海洋 | `SEA` |
| Forest | 森林 | `FOREST` |
| Desert | 沙漠 | `DESERT` |
| Plains | 平原 | `PLAINS` |
| Crystal Forest | 水晶森林 | `MAGIC_PLAINS` |
| Dungeon | 地牢 | `DUNGEON` |

## 物品与制作材料名称 / Item and material names

| English | 中文 | 文本键 |
| --- | --- | --- |
| Acidious Bracelet | 酸蚀手镯 | `ACIDBRACELET_ITEM` |
| Acid Sword | 酸蚀之剑 | `ACIDSWORD_ITEM` |
| All-Seeing Eye | 全视之眼 | `ALLSEEINGEYE_ITEM` |
| Amulet of Chaos | 混沌护符 | `AMULETOFCHAOS_ITEM` |
| Amulet of Courage | 勇气护符 | `AMULETOFCOURAGE_ITEM` |
| Amulet of Raw Mana | 原始魔力护符 | `AMULETOFCRYSTALMAGIC_ITEM` |
| Night's Eye | 夜之眼 | `AMULETOFNIGHTEYE_ITEM` |
| Amulet of Destruction | 毁灭护符 | `AMULETOFDESTRUCTION_ITEM` |
| Amulet of False Life | 虚假生命护符 | `AMULETOFFALSELIFE_ITEM` |
| Amulet of Health | 健康护符 | `AMULETOFLIFE_ITEM` |
| Amulet of Night | 暗夜护符 | `AMULETOFNIGHT_ITEM` |
| Amulet of Scholar | 学者护符 | `AMULETOFSCHOLAR_ITEM` |
| Anti-Magic Shield | 抗魔盾 | `ANTIMAGICSHIELD_ITEM` |
| Antidote | 解毒剂 | `ANTIDOTEPOTION_ITEM` |
| Anatase | 锐钛矿 | `ANATASE_ITEM` |
| Advanced Antidote | 高效解毒剂 | `ADVANCEDANTIDOTEPOTION_ITEM` |
| Archmage Hood | 大法师兜帽 | `ARCHMAGEHOOD_ITEM` |
| Archmage Robe | 大法师长袍 | `ARCHMAGEROBE_ITEM` |
| Armour of Haste | 迅捷护甲 | `ARMOROFHASTE_ITEM` |
| Amulet of Haste | 迅捷护符 | `AMULETOFHASTE_ITEM` |
| Northman's Armour | 北地人护甲 | `NORTHARMOR_ITEM` |
| Northman's Hat | 北地人帽 | `NORTHHAT_ITEM` |
| Northman's Axe | 北地人战斧 | `NORTHAXE_ITEM` |
| Greaves | 护胫 | `ARMOREDBOOTS_ITEM` |
| Assassin's Armour | 刺客护甲 | `ASSASSINARMOR_ITEM` |
| Crossbow of Charm | 魅惑之弩 | `CHARMCROSSBOW_ITEM` |
| Multi-shot Crossbow | 连射弩 | `DOUBLECROSSBOW_ITEM` |
| Assassin's Crossbow | 刺客之弩 | `ASSASSINCROSSBOW_ITEM` |
| Assassin's Helmet | 刺客头盔 | `ASSASSINHELMET_ITEM` |
| Barbarian's Armour | 野蛮人护甲 | `BARBARIANARMOR_ITEM` |
| Barbarian King's Crown | 蛮王之冠 | `BARBARIANCROWN_ITEM` |
| Barbarian's Helmet | 野蛮人头盔 | `BARBARIANHELMET_ITEM` |
| Bard's Lute | 吟游诗人的鲁特琴 | `BARDLUTE_ITEM` |
| Squeeze Box | 手风琴 | `SQUEZEBOX_ITEM` |
| Battle Mask | 战斗面具 | `BATTLEMASK_ITEM` |
| Beating Stick | 殴打棍 | `BEATINGSTICK_ITEM` |
| Belt of Giant's Strength | 巨力腰带 | `BELTOFSTRENGTH_ITEM` |
| Berserker's Armour | 狂战士护甲 | `BERSERKERARMOR_ITEM` |
| Berserker's Helmet | 狂战士头盔 | `BERSERKERHELMET_ITEM` |
| Black Dragon's Head | 黑龙之首 | `BLACKDRAGONHEAD_ITEM` |
| Black Dragon Seal | 黑龙封印 | `BLACKDRAGONSEAL_ITEM` |
| Black Ice Mace | 黑冰钉锤 | `BLACKICEMACE_ITEM` |
| Black Pearl | 黑珍珠 | `BLACKPEARL_ITEM` |
| Black Tombstone | 黑色墓碑 | `BLACKTOMBSTONE_ITEM` |
| Blood Chalice | 鲜血圣杯 | `BLOODCHALICE_ITEM` |
| Bloody Axe | 染血战斧 | `BLOODYAXE_ITEM` |
| Bone Armour | 骸骨护甲 | `BONEARMOR_ITEM` |
| Bone Candle | 骨烛 | `BONECANDLE_ITEM` |
| Bone Helmet | 骸骨头盔 | `BONEHELMET_ITEM` |
| Bone Shield | 骸骨盾 | `BONESHIELD_ITEM` |
| Book of The Dead | 亡者之书 | `BOOKOFTHEDEAD_ITEM` |
| Dark Grimore | 黑暗魔典 | `DARKGRIMORE_ITEM` |
| Seal of Excellence | 卓越印章 | `BROOCHOFCHARISMA_ITEM` |
| Brooch of Luck | 幸运胸针 | `BROOCHOFLUCK_ITEM` |
| Carrot | 胡萝卜 | `CARROT_ITEM` |
| Witcher's Amulet | 猎魔人护符 | `CATAMULET_ITEM` |
| Cave Mushroom | 洞穴蘑菇 | `CAVEMUSHROOM_ITEM` |
| Legion Sergeant Helmet | 军团军士头盔 | `CHAOSWARRIORHELMET_ITEM` |
| Chimera's Blood | 奇美拉之血 | `CHIMERABLOOD_ITEM` |
| Anti-Magic Collar | 抗魔项圈 | `COLLAROFANTIMAGIC_ITEM` |
| Battle Collar | 战斗项圈 | `COLLAROFBATTLE_ITEM` |
| Collar of Command | 统御项圈 | `COLLAROFCOMMAND_ITEM` |
| Collar of Defence | 防御项圈 | `COLLAROFDEFENSE_ITEM` |
| Collar of Bird | 飞鸟项圈 | `COLLAROFFEATHERS_ITEM` |
| Icy Collar | 寒冰项圈 | `COLLAROFICE_ITEM` |
| Collar of Joy | 喜悦项圈 | `COLLAROFJOY_ITEM` |
| Collar of Power | 力量项圈 | `COLLAROFPOWER_ITEM` |
| Spiked Collar | 尖刺项圈 | `COLLAROFSPIKES_ITEM` |
| Conclave Amulet | 秘会护符 | `CONCLAVEAMULET_ITEM` |
| Conclave Armour | 秘会护甲 | `CONCLAVEARMOR_ITEM` |
| Conclave Helmet | 秘会头盔 | `CONCLAVEHELMET_ITEM` |
| Crest of Burning Sun | 烈日徽章 | `CRESTOFSUN_ITEM` |
| Crystal Armour | 水晶护甲 | `CRYSTALARMOR_ITEM` |
| Crystal Cap | 水晶头盔 | `CRYSTALHELMET_ITEM` |
| Crystal Shield | 水晶盾 | `CRYSTALSHIELD_ITEM` |
| Cursed Sword | 诅咒之剑 | `CURSEDSWORD_ITEM` |
| Spinning Wheel | 纺车 | `SPINNINGWHEEL_ITEM` |
| Darkstone Bracelet | 暗石手镯 | `IMMORTALITYBRACELET_ITEM` |
| Dagger of Lightning | 闪电匕首 | `DAGGEROFLIGHTING_ITEM` |
| Crossbow of Lightning | 闪电弩 | `LIGHTINGCROSSBOW_ITEM` |
| Dark Dagger | 黑暗匕首 | `DARKDAGGER_ITEM` |
| Pirate's Hat | 海盗帽 | `PIRATEHAT_ITEM` |
| Pirate's Hook | 海盗铁钩 | `PIRATEHOOK_ITEM` |
| Skull Amulet | 骷髅护符 | `SKULLAMULET_ITEM` |
| Skull Ring | 骷髅戒指 | `SKULLRING_ITEM` |
| Dark Elves Staff | 黑暗精灵法杖 | `DARKELVESSTAFF_ITEM` |
| Death's Warrior Armour | 死亡战士护甲 | `DEATHWARRIORARMOR_ITEM` |
| Death's Warrior Helmet | 死亡战士头盔 | `DEATHWARRIORHELMET_ITEM` |
| Demon's Blood | 恶魔之血 | `DEMONBLOODPOTION_ITEM` |
| Demonic Flower | 恶魔之花 | `DEMONFLOWER_ITEM` |
| Demon's Heart | 恶魔之心 | `DEMONHEART_ITEM` |
| Demon's Whip | 恶魔之鞭 | `DEMONSWHIP_ITEM` |
| Diamond | 钻石 | `DIAMOND_ITEM` |
| Divine Cross | 神圣十字架 | `DIVINECROSS_ITEM` |
| Djinn's Lamp | 灯神之灯 | `DJINLAMP_ITEM` |
| Djinn's Shoes | 灯神之鞋 | `DJINSHOES_ITEM` |
| Doombringer | 末日使者 | `DOOMBRINGER_ITEM` |
| Dolomite | 白云石 | `DOLOMITE_ITEM` |
| Dragon Boots | 龙之靴 | `DRAGONBOOTS_ITEM` |
| Dragon Scale's Armour | 龙鳞护甲 | `DRAGONSCALESARMOR_ITEM` |
| Dragon Scale's Helmet | 龙鳞头盔 | `DRAGONSCALESHELMET_ITEM` |
| Dragon Slayer | 屠龙者 | `DRAGONSLAYER_ITEM` |
| Seal Piece | 封印碎片 | `DRAGONSTATUESEALPIECE_ITEM` |
| Latern | 提灯 | `LATERN_ITEM` |
| Complete Seal | 完整封印 | `DRAGONSTATUESEALWHOLE_ITEM` |
| Dragon Teeth | 龙牙 | `DRAGONTEETH_ITEM` |
| Dwarven Shield | 矮人盾 | `DWARVENSHIELD_ITEM` |
| Dwarven Crossbow | 矮人弩 | `DWARVENCROSSBOW_ITEM` |
| Dwarven Sword | 矮人剑 | `DWARVENSWORD_ITEM` |
| Elven Crossbow | 精灵弩 | `ELVENCROSSBOW_ITEM` |
| Earrings of Viper | 毒蛇耳环 | `EARRINGSOFVIPER_ITEM` |
| Elementalist Staff | 元素使法杖 | `ELEMENTALISTSTAFF_ITEM` |
| Endless Purse | 无尽钱袋 | `ENDLESSPURSE_ITEM` |
| Enforcer's Armour | 执法者护甲 | `ENFORCERARMOR_ITEM` |
| Enforcer's Helmet | 执法者头盔 | `ENFORCERHELMET_ITEM` |
| Everfrozen Stone | 永冻石 | `EVERFROZENSTONE_ITEM` |
| Fire Rune Stone | 火焰符文石 | `FIRESTONE_ITEM` |
| Executioner Blade | 刽子手之刃 | `EXECUTIONERBLADE_ITEM` |
| Crab Pincers | 蟹钳 | `CRABPINCERS_ITEM` |
| Explorer's Boots | 探险家之靴 | `EXPLORERBOOTS_ITEM` |
| Eye Patch | 眼罩 | `EYEPATCH_ITEM` |
| Pirate's Bandana | 海盗头巾 | `PIRATEBANDANA_ITEM` |
| Luxury Witch Hat | 华贵女巫帽 | `FASHIONWITCHHAT_ITEM` |
| Feathers Shield | 羽毛盾 | `FEATHERSHIELD_ITEM` |
| Fire Walker's Shoes | 踏火者之鞋 | `FIREWALKERSHOES_ITEM` |
| Santa's Boots | 圣诞老人之靴 | `SANTABOOTS_ITEM` |
| Santa's Hat | 圣诞老人帽 | `SANTAHAT_ITEM` |
| Santa's Cape | 圣诞老人披风 | `SANTACAPE_ITEM` |
| Fire Wand | 火焰魔杖 | `FIREWAND_ITEM` |
| Burning Axe | 燃烧战斧 | `FLAMEAXE_ITEM` |
| Flame Sword | 烈焰之剑 | `FLAMESWORD_ITEM` |
| Spike Root Sword | 棘根之剑 | `SPIKEROOTSWORD_ITEM` |
| Dragon Sword | 巨龙之剑 | `DRAGONSWORD_ITEM` |
| Pyramid of Focus | 专注金字塔 | `FOCUSPYRAMID_ITEM` |
| Frost Brooch | 寒霜胸针 | `FROSTBROOCH_ITEM` |
| Ghost Katana | 幽灵太刀 | `GHOSTKATANA_ITEM` |
| Glass Crystal | 玻璃水晶 | `GLASSCRYSTAL_ITEM` |
| Gold Bar | 金锭 | `GOLDBAR_ITEM` |
| Ancessors Helmet | 先祖头盔 | `GOLDDWARFHELMET_ITEM` |
| Golden Apple | 金苹果 | `GOLDENAPPLE_ITEM` |
| Golden Axe | 黄金战斧 | `GOLDENAXE_ITEM` |
| Golden Sword | 黄金之剑 | `GOLDENSWORD_ITEM` |
| Golden Crown | 黄金王冠 | `GOLDENCROWN_ITEM` |
| Golden Sickle | 黄金镰刀 | `GOLDENSICKLE_ITEM` |
| Wand of Thunder | 雷霆魔杖 | `GOLDENWAND_ITEM` |
| Goldman's Amulet | 戈德曼护符 | `GOLDMANAMULET_ITEM` |
| Halloween Pumpkin | 万圣节南瓜 | `HALLOWEENPUMPKIN_ITEM` |
| Hammer of Lightning | 闪电战锤 | `HAMMEROFLIGHTING_ITEM` |
| Hammer of Strength | 力量战锤 | `HAMMEROFSTRENGTH_ITEM` |
| Heart Stone | 心石 | `HEARTSTONE_ITEM` |
| Heart Stone Mace | 心石钉锤 | `HEARTSTONEMACE_ITEM` |
| Meteor Iron Greaves | 陨铁护胫 | `HEAVYARMOREDBOOTS_ITEM` |
| Hellish Candle | 地狱蜡烛 | `HELLISHCANDLE_ITEM` |
| Hellish Shield | 地狱之盾 | `HELLISHSHIELD_ITEM` |
| Helmet of Haste | 迅捷头盔 | `HELMETOFHASTE_ITEM` |
| Hematite | 赤铁矿 | `HEMATITE_ITEM` |
| Potion of Heroism | 英勇药剂 | `HEROISMPOTION_ITEM` |
| High Priest's Hat | 大祭司帽 | `HIGHPRIESTHAT_ITEM` |
| Holy Chalice | 圣杯 | `HOLYCHALICE_ITEM` |
| Holy Pendant | 神圣吊坠 | `HOLYPENDANT_ITEM` |
| Hook Mace | 钩刺钉锤 | `HOOKMACE_ITEM` |
| Ice Sword | 寒冰之剑 | `ICESWORD_ITEM` |
| Ice Walker's Shoes | 踏冰者之鞋 | `ICEWALKERSHOES_ITEM` |
| Idol of Happiness | 幸福神像 | `IDOLOFHAPPINESS_ITEM` |
| Ambrosia | 神馔 | `IMMORTALITYPOTION_ITEM` |
| Mutagen | 诱变剂 | `MUTATINGPOTION_ITEM` |
| Imperial Opal | 帝王欧泊 | `IMPERIALOPAL_ITEM` |
| Essence of Life | 生命精华 | `IMPROVEDLIFEPOTION_ITEM` |
| Elixir of Youth | 青春灵药 | `FULLLIFEPOTION_ITEM` |
| Moonstone | 月光石 | `MOONSTONE_ITEM` |
| Invulnerability Formula | 无敌配剂 | `INVULNERABILITYPOTION_ITEM` |
| Jade Sword | 玉石之剑 | `JADESWORD_ITEM` |
| Jester's Hat | 弄臣帽 | `JESTERHAT_ITEM` |
| Dr Jones' Hat | 琼斯博士的帽子 | `JONESHAT_ITEM` |
| Kama | 手镰 | `KAMA_ITEM` |
| Katana | 太刀 | `KATANA_ITEM` |
| King's Armour | 国王护甲 | `KINGSARMOR_ITEM` |
| Knight's Mace | 骑士钉锤 | `KNIGHTSMACE_ITEM` |
| Knight's Warhammer | 骑士战锤 | `KNIGHTSWARHAMMER_ITEM` |
| Kunai | 苦无 | `KUNAI_ITEM` |
| Lamp of Blood | 鲜血之灯 | `LAMPOFBLOOD_ITEM` |
| Limestone | 石灰石 | `LIMESTONE_ITEM` |
| Legion Armour | 军团护甲 | `LEGIONARMOR_ITEM` |
| Legion's Banner | 军团战旗 | `LEGIONBANNER_ITEM` |
| Legion Helmet | 军团头盔 | `LEGIONHELMET_ITEM` |
| Legion Mage's Hood | 军团法师兜帽 | `LEGIONMAGEHOOD_ITEM` |
| Healing Brew | 治疗药液 | `LIFEPOTION_ITEM` |
| Pirate's Rum | 海盗朗姆酒 | `MORALEPOTION_ITEM` |
| Lizard Mask | 蜥蜴面具 | `LIZARDMASK_ITEM` |
| Love Potion | 爱情药剂 | `LOVEPOTION_ITEM` |
| Magical Bell | 魔法铃铛 | `LUCKYBELL_ITEM` |
| Golden Clover | 金色三叶草 | `GOLDENCLOVER_ITEM` |
| Lucky Horseshoe | 幸运马蹄铁 | `LUCKYHORSESHOE_ITEM` |
| Lucky Rabbit's Foot | 幸运兔脚 | `LUCKYRABBITFOOT_ITEM` |
| Bear Claw | 熊爪 | `BEARCLAW_ITEM` |
| Magic Crystal | 魔法水晶 | `MAGICCRYSTAL_ITEM` |
| Radagast's Isolator | 拉达加斯特的隔绝药剂 | `MAGICIMMUNITYPOTION_ITEM` |
| Magician Mirror | 魔术师之镜 | `MAGICMIRROR_ITEM` |
| Mana Restorative | 魔力恢复剂 | `MAGICPOTION_ITEM` |
| Purified Mana | 纯净魔力 | `IMPROVEDMAGICPOTION_ITEM` |
| Power Concentrate | 魔力浓缩液 | `MAGICREGENERATIONPOTION_ITEM` |
| Anti-Magic Drops | 抗魔滴剂 | `MAGICRESISTANCEPOTION_ITEM` |
| Magic Torc | 魔法颈环 | `MAGICTORC_ITEM` |
| Magical Hourglass | 魔法沙漏 | `MAGICALHOURGLASS_ITEM` |
| Magical Compass | 魔法罗盘 | `MAGICALCOMPASS_ITEM` |
| Pirate's Parrot | 海盗鹦鹉 | `PIRATEPARROT_ITEM` |
| Pirate's Leg | 海盗假腿 | `PIRATELEG_ITEM` |
| Magician Staff | 魔术师法杖 | `MAGICIANSTAFF_ITEM` |
| Mana Shard | 魔力碎片 | `MANASHARD_ITEM` |
| Assassin's Dagger | 刺客匕首 | `MASTERASSASSINDAGGER_ITEM` |
| Maul of Strength | 力量重锤 | `MAULOFSTRENGTH_ITEM` |
| Mechanical Heart | 机械之心 | `MECHANICHEART_ITEM` |
| Meteor Iron Armour | 陨铁护甲 | `METEORARMOR_ITEM` |
| Meteor Iron Helmet | 陨铁头盔 | `METEORHELMET_ITEM` |
| Mirror Cloak | 镜面斗篷 | `MIRRORCLOAK_ITEM` |
| Moon Key | 月之钥 | `MOONKEY_ITEM` |
| Singing Hat | 歌唱之帽 | `MUSICIANHAT_ITEM` |
| Nature Crown | 自然之冠 | `NATURECROWN_ITEM` |
| Necromancer's Rod | 死灵法师权杖 | `NECROMANCERROD_ITEM` |
| Stick of Ikeus | 伊凯乌斯之杖 | `IKEASTICK_ITEM` |
| Nesting Doll | 套娃 | `NESTINGDOLL_ITEM` |
| Night Robe | 暗夜长袍 | `NIGHTROBE_ITEM` |
| Night Slippers | 暗夜便鞋 | `NIGHTSLIPPERS_ITEM` |
| Scorpion Kusarigama | 蝎之锁镰 | `NINJAFLAILFIRE_ITEM` |
| Tremor Kusarigama | 震颤锁镰 | `NINJAFLAILHAND_ITEM` |
| Sub-zero Kusarigama | 零度锁镰 | `NINJAFLAILICE_ITEM` |
| Kusarigama | 锁镰 | `NINJAFLAIL_ITEM` |
| Shadow Kusarigama | 暗影锁镰 | `NINJAFLAILNIGHT_ITEM` |
| Pain Kusarigama | 痛苦锁镰 | `NINJAFLAILRAZOR_ITEM` |
| Ninja's Sandals | 忍者草鞋 | `NINJASANDALS_ITEM` |
| Patent of Nobility | 贵族敕书 | `NOBILITYPATENT_ITEM` |
| Noble's Cloak | 贵族斗篷 | `NOBLECLOAK_ITEM` |
| Noble Clothes | 贵族服饰 | `NOBLECLOTHES_ITEM` |
| Head Bag | 头颅袋 | `HEADBAG_ITEM` |
| Nunchaku | 双节棍 | `NUNCHAKU_ITEM` |
| Ogre's Head | 食人魔头颅 | `OGREHEAD_ITEM` |
| Ogre's Mace | 食人魔钉锤 | `OGREMACE_ITEM` |
| Ogre's Skin Shoes | 食人魔皮鞋 | `OGRESKINBOOTS_ITEM` |
| One-Of-Many Ring | 万中之一戒指 | `ONEOFMANYRING_ITEM` |
| Orc's Fang | 兽人獠牙 | `ORCFANG_ITEM` |
| Ornamental Buckler | 装饰圆盾 | `ORNAMENTALBUCKLER_ITEM` |
| Incrusted Sword | 镶嵌之剑 | `ORNAMENTALSWORD_ITEM` |
| Sabre | 军刀 | `PIRATESABRE_ITEM` |
| Falchion | 弯刃刀 | `FALCHIONSWORD_ITEM` |
| Owl's Head Helmet | 枭首头盔 | `OWLHELMET_ITEM` |
| Patron Cookie | 赞助者饼干 | `PATRONCOOKIE_ITEM` |
| Cheese | 奶酪 | `CHEESE_ITEM` |
| Pearl | 珍珠 | `PEARL_ITEM` |
| Phantom Shield | 幻影之盾 | `PHANTOMSHIELD_ITEM` |
| Phasing Cape | 相位披风 | `PHASINGCAPE_ITEM` |
| Phoenix Feather | 凤凰之羽 | `PHOENIXFEATHER_ITEM` |
| Soul Phylactery | 灵魂命匣 | `PHYLACTERY_ITEM` |
| Pirate's Knife | 海盗小刀 | `PIRATESKNIFE_ITEM` |
| Pitchfork | 干草叉 | `PITCHFORK_ITEM` |
| Poison Axe | 剧毒战斧 | `POISONAXE_ITEM` |
| Poisonous Extract | 剧毒提取液 | `POISONSKIN_ITEM` |
| Prayer Beads | 念珠 | `PRAYERBEADS_ITEM` |
| Protector Shield | 护卫之盾 | `PROTECTORSHIELD_ITEM` |
| Pyrope | 镁铝榴石 | `PYROPE_ITEM` |
| Pyromancer's Sceptre | 火焰术士权杖 | `PYROMANCERSPECTRE_ITEM` |
| Meteor Staff | 陨石法杖 | `METEORSTAFF_ITEM` |
| Quality Armour | 精制护甲 | `QUALITYARMOR_ITEM` |
| Quality Axe | 精制战斧 | `QUALITYAXE_ITEM` |
| Battle Rune Axe | 战斗符文斧 | `BATTLERUNEAXE_ITEM` |
| Quality Great Sword | 精制巨剑 | `QUALITYGREATSWORD_ITEM` |
| Quality Warhammer | 精制战锤 | `QUALITYWARHAMMER_ITEM` |
| Quality Helmet | 精制头盔 | `QUALITYHELMET_ITEM` |
| Quality Sandals | 精制凉鞋 | `QUALITYSANDALS_ITEM` |
| Quality Shield | 精制盾牌 | `QUALITYSHIELD_ITEM` |
| Quality Sword | 精制长剑 | `QUALITYSWORD_ITEM` |
| Quality Mace | 精制钉锤 | `QUALITYMACE_ITEM` |
| Quality Bow | 精制弓 | `QUALITYBOW_ITEM` |
| Quality Crossbow | 精制弩 | `QUALITYCROSSBOW_ITEM` |
| Bone Bow | 骸骨弓 | `BONEBOW_ITEM` |
| Bone Crossbow | 骸骨弩 | `BONECROSSBOW_ITEM` |
| Vampiric Crossbow | 吸血弩 | `VAMPIRECROSSBOW_ITEM` |
| Golden Bow | 黄金弓 | `GOLDENBOW_ITEM` |
| Demon's Bow | 恶魔之弓 | `DEMONBOW_ITEM` |
| Bow of Grasses | 芳草之弓 | `FORESTBOW_ITEM` |
| Sniper Pistol | 狙击手枪 | `SNIPERPISTOL_ITEM` |
| Repeater | 连发手枪 | `REPEATERPISTOL_ITEM` |
| Tesla Pistol | 特斯拉手枪 | `LIGHTINGPISTOL_ITEM` |
| Silver Pistol | 白银手枪 | `SILVERPISTOL_ITEM` |
| Quality Pistol | 精制手枪 | `QUALITYPISTOL_ITEM` |
| Hand Cannon | 手炮 | `HANDCANNON_ITEM` |
| Fire Pistol | 烈焰手枪 | `FIREPISTOL_ITEM` |
| Fire Opal | 火欧泊 | `FIREOPAL_ITEM` |
| Heavy Bow | 重弓 | `HEAVYBOW_ITEM` |
| Black Ice Bow | 黑冰弓 | `ICEBOW_ITEM` |
| Ice Crossbow | 寒冰弩 | `ICECROSSBOW_ITEM` |
| Bow of Legends | 传奇之弓 | `LEGENDBOW_ITEM` |
| Night Wing | 夜翼 | `NIGHTBOW_ITEM` |
| Spider Bow | 蜘蛛弓 | `SPIDERBOW_ITEM` |
| Radiating Stone | 辐光石 | `RADIATINGSTONE_ITEM` |
| Random Item | 随机物品 | `RANDOM_ITEM` |
| Ranger's Cloak | 游侠斗篷 | `RANGERCLOAK_ITEM` |
| Ranger Shoes | 游侠之鞋 | `RANGERSHOES_ITEM` |
| Razor Edge | 剃刀之锋 | `RAZOREDGE_ITEM` |
| Razor Shurikens | 剃刀手里剑 | `RAZORSHURIKEN_ITEM` |
| Red Skull Staff | 赤颅法杖 | `REDSKULLSTAFF_ITEM` |
| Elementals Protection | 元素防护药剂 | `RESISTANCEPOTION_ITEM` |
| Stoneskin Decoction | 石肤煎剂 | `STONESKINPOTION_ITEM` |
| Ring of Agility | 敏捷戒指 | `RINGOFAGILITY_ITEM` |
| Ring of Rogue | 游荡者戒指 | `RINGOFAMBUSH_ITEM` |
| Ring of Anti-Magic | 抗魔戒指 | `RINGOFANTIMAGIC_ITEM` |
| Ring of Anti-venom | 抗毒戒指 | `RINGOFPOISONRESISTANCE_ITEM` |
| Ring of Blessings | 祝福戒指 | `RINGOFBLESSINGS_ITEM` |
| Ring of Command | 统御戒指 | `RINGOFCOMMAND_ITEM` |
| Clockwork Ring | 发条戒指 | `RINGOFGOLEM_ITEM` |
| Stone of Slimes | 史莱姆之石 | `SLIMESTONE_ITEM` |
| Ring of Lightning | 闪电戒指 | `RINGOFLIGHTING_ITEM` |
| Ring of Magic | 魔法戒指 | `RINGOFMAGIC_ITEM` |
| Ring of Protection | 防护戒指 | `RINGOFPROTECTION_ITEM` |
| Ring of Scholar | 学者戒指 | `RINGOFSCHOLAR_ITEM` |
| Ring of Sleeper | 沉睡者戒指 | `RINGOFSLEEPER_ITEM` |
| Ring of Speed | 速度戒指 | `RINGOFSPEED_ITEM` |
| Ring of Strength | 力量戒指 | `RINGOFSTRENGTH_ITEM` |
| Ruby | 红宝石 | `RUBY_ITEM` |
| Sapphire | 蓝宝石 | `SAPPHIRE_ITEM` |
| Sea Shell | 贝壳 | `SEASHELL_ITEM` |
| Sacrificial Mask | 献祭面具 | `SACRIFICIALMASK_ITEM` |
| Sai | 铁尺 | `SAI_ITEM` |
| Sailor's Sandals | 水手凉鞋 | `SAILORSANDALS_ITEM` |
| Saint's Warhammer | 圣徒战锤 | `SAINTWARHAMMER_ITEM` |
| Samurai Armour | 武士甲 | `SAMURAIARMOR_ITEM` |
| General Samurai Armour | 武士大将甲 | `SAMURAIGENERALARMOR_ITEM` |
| Noble Samurai Armour | 贵族武士甲 | `SAMURAINOBLEARMOR_ITEM` |
| Scythe | 长柄镰刀 | `SCYTHE_ITEM` |
| Seaweed | 海藻 | `SEAWEED_ITEM` |
| Seedling | 幼苗 | `SEEDLING_ITEM` |
| Mackerel | 鲭鱼 | `FISHBLUE_ITEM` |
| Red Snapper | 红鲷鱼 | `FISHRED_ITEM` |
| King Tuna | 金枪鱼王 | `FISHGOLD_ITEM` |
| Seer's Hat | 先知帽 | `SEERHAT_ITEM` |
| Serpent Staff | 蛇之法杖 | `SERPENTSTAFF_ITEM` |
| Staff Of Hippocrates | 希波克拉底之杖 | `HIPPOCRATESSTAFF_ITEM` |
| Shadow Hand | 暗影之手 | `SHADOWHAND_ITEM` |
| Shadow Hood | 暗影兜帽 | `SHADOWHOOD_ITEM` |
| Shadow Mask | 暗影面具 | `SHADOWMASK_ITEM` |
| Shard Blade | 碎晶之刃 | `SHARDBLADE_ITEM` |
| Shield of Ages | 岁月之盾 | `SHIELDOFAGES_ITEM` |
| Guardian of Faith | 信仰守护者 | `SHIELDOFFAITH_ITEM` |
| Shimmer | 微光 | `SHIMMER_ITEM` |
| Shitanto | 希坦刀 | `SHITANTO_ITEM` |
| Shuko | 手甲钩 | `SHUKO_ITEM` |
| Silver Bar | 银锭 | `SILVERBAR_ITEM` |
| Silver Sword | 白银之剑 | `SILVERSWORD_ITEM` |
| Skull Belt | 骷髅腰带 | `SKULLBELT_ITEM` |
| Souls Collector | 灵魂收集器 | `SOULCOLLECTOR_ITEM` |
| Captured Soul | 被捕获的灵魂 | `SOUL_ITEM` |
| Souls Bell | 灵魂之铃 | `SOULSBELL_ITEM` |
| Elixir of Swiftness | 迅捷灵药 | `SPEEDPOTION_ITEM` |
| Time Substance | 时间物质 | `TIMEPOTION_ITEM` |
| Scroll of {0} | {0}卷轴 | `SPELLSCROLL_OF_S_ITEM` |
| Sphere of Magic | 魔法宝珠 | `SPHEREOFMAGIC_ITEM` |
| Sphinx's Stone | 斯芬克斯之石 | `SPHINXSTONE_ITEM` |
| Living Fire | 活火 | `LIVINGFIRE_ITEM` |
| Sprite Stones | 精灵石 | `SPRITESTONES_ITEM` |
| Staff of Striking | 打击之杖 | `STAFFOFSTRIKING_ITEM` |
| Brute's Brew | 蛮力药液 | `STRENGTHPOTION_ITEM` |
| Blurry Infuse | 朦胧浸剂 | `RANGEDDEFENCEPOTION_ITEM` |
| Standstill Liquid | 定息药液 | `PRECISIONPOTION_ITEM` |
| Study Book | 研习书 | `STUDYBOOK_ITEM` |
| Suppressing Chain | 压制锁链 | `SUPPRESSINGCHAIN_ITEM` |
| Swamp Berries | 沼泽浆果 | `SWAMPBERRIES_ITEM` |
| Swamp Mace | 沼泽钉锤 | `SWAMPMACE_ITEM` |
| Tear of God | 神之泪 | `TEAROFGOD_ITEM` |
| Krill's Teddy | 克里尔的泰迪熊 | `TEDDY_ITEM` |
| Teeth Mace | 獠牙钉锤 | `TEETHMACE_ITEM` |
| Templar Knight's Shield | 圣殿骑士之盾 | `TEMPLARKNIGHTSHIELD_ITEM` |
| Bracelet of Thorns | 荆棘手镯 | `THORNBRACELET_ITEM` |
| Three Pearls Shield | 三珠之盾 | `THREEPEARLSSHIELD_ITEM` |
| Armour of Toxicity | 剧毒护甲 | `TOXICARMOR_ITEM` |
| Helmet of Toxicity | 剧毒头盔 | `TOXICHELMET_ITEM` |
| Tribal Necklace | 部族项链 | `TRIBALNECKLACE_ITEM` |
| Troll's Skin Shoes | 巨魔皮鞋 | `TROLLSKINSHOES_ITEM` |
| Undead Bane | 亡灵克星 | `UNDEADBANE_ITEM` |
| Crown of The Undead | 亡灵之冠 | `UNDEADCROWN_ITEM` |
| Undertaker's Coat | 殡葬师外套 | `UNDERTAKERCOAT_ITEM` |
| Inferno Sceptre | 炼狱权杖 | `UNDERWORLDSCEPTRE_ITEM` |
| Valentine's Rose | 情人玫瑰 | `VALENTINEROSE_ITEM` |
| Vampire's Kiss | 吸血鬼之吻 | `VAMPIREKISS_ITEM` |
| Vengeance | 复仇 | `VENGEANCESHIELD_ITEM` |
| Vial of Blood | 瓶装鲜血 | `VIALOFBLOODPOTION_ITEM` |
| Nimbus Mushroom | 灵光菇 | `WANNI_ITEM` |
| Clan's War Drum | 氏族战鼓 | `WARDRUM_ITEM` |
| Warhorn | 战争号角 | `WARHORN_ITEM` |
| Wizard's Cloak | 巫师斗篷 | `WIZARDCLOAK_ITEM` |
| Wolf's Shield | 狼之盾 | `WOLFSHIELD_ITEM` |
| World Tree's Leaves | 世界树之叶 | `WORLDTREEBRANCH_ITEM` |
| Zombie's Brain | 僵尸之脑 | `ZOMBIEBRAIN_ITEM` |
| Zombie's Hand | 僵尸之手 | `ZOMBIEHAND_ITEM` |
| Zombie's Heart | 僵尸之心 | `ZOMBIEHEART_ITEM` |
| Zombie's Leg | 僵尸之腿 | `ZOMBIELEG_ITEM` |
| Zombie's Meat | 僵尸腐肉 | `ZOMBIEMEAT_ITEM` |
| Dragon's Skull | 龙之颅骨 | `DRAGONSKULL_ITEM` |
| Pure Iron | 纯铁 | `PUREIRON_ITEM` |
| Ancient Coal | 远古煤炭 | `ANCIENTCOAL_ITEM` |
| Liver-worm | 肝虫 | `LIVERWORM_ITEM` |
| Demon's Crystal | 恶魔水晶 | `BLOODCRYSTAL_ITEM` |
| Spider Fangs | 蜘蛛毒牙 | `SPIDERFANGS_ITEM` |
| Volcano Crystal | 火山水晶 | `VOLCANOCRYSTAL_ITEM` |
| Bone Powder | 骨粉 | `BONEPOWDER_ITEM` |
| Vampire Ash | 吸血鬼灰烬 | `VAMPIREASH_ITEM` |
| Deep Potatoe | 地底薯 | `DEEPPOTATO_ITEM` |
| Star Flower | 星花 | `STARFLOWER_ITEM` |
| Copper | 铜 | `COPPER_ITEM` |
| Pyradyne | 派拉丁 | `PYRADYNE_ITEM` |
| Black Yarrow | 黑蓍草 | `BLACKYARROW_ITEM` |
| Poison Basil | 毒罗勒 | `POISONBASIL_ITEM` |
| Black Ice | 黑冰 | `BLACKICE_ITEM` |
| Black Gold | 黑金 | `BLACKGOLD_ITEM` |
| Blackheart Stone | 黑心石 | `BLACKHEARTSTONE_ITEM` |
| Sulphur | 硫磺 | `SULPHUR_ITEM` |
| Devil's Onion | 恶魔洋葱 | `DEVILONION_ITEM` |
| Lead | 铅 | `LEAD_ITEM` |
| Amber | 琥珀 | `AMBER_ITEM` |
| Quartz | 石英 | `QUARTZ_ITEM` |
| Silk Twine | 丝线 | `SILKTWINE_ITEM` |
| Toadstool | 毒蘑菇 | `TOADSTOOL_ITEM` |
| Butter-worms | 黄油虫 | `BUTTERWORMS_ITEM` |
| Night Gem | 夜之宝石 | `NIGHTGEM_ITEM` |
| Blood Berries | 血浆果 | `BLOODBERRIES_ITEM` |
| Jade Stone | 玉石 | `JADE_ITEM` |
| Salamander's Egg | 火蜥蜴卵 | `SALAMANDEREGG_ITEM` |
| Elowan Roots | 埃洛万根 | `ELOWANROOTS_ITEM` |
| Lich's Skull | 巫妖颅骨 | `LICHSKULL_ITEM` |
| King's Foil | 王叶草 | `KINGSFOIL_ITEM` |
| Fairy Sage | 妖精鼠尾草 | `FAIRYSAGE_ITEM` |
| Witch Orchid | 女巫兰 | `WITCHORCHID_ITEM` |
| Slik-spider Web | 丝蛛网 | `SILKSPIDERWEB_ITEM` |
| Tube-shrooms | 管状蘑菇 | `TUBESHROOMS_ITEM` |
| Tropical Frog | 热带蛙 | `TROPICALFROG_ITEM` |
| Slime Goo | 史莱姆黏液 | `SLIMEGOO_ITEM` |
| Pointy Peppers | 尖椒 | `POINTYPEPPERS_ITEM` |
| Dragon Fruit | 火龙果 | `DRAGONFRUIT_ITEM` |
| Cuckoo Egg | 杜鹃卵 | `CUCKOOEGG_ITEM` |
| Circle Mushrooms | 环生蘑菇 | `CIRLEMUSHROOMS_ITEM` |
| Golden Grapes | 金葡萄 | `GOLDENGRAPES_ITEM` |
| Moonlight Grass | 月光草 | `MOONLIGHTGRASS_ITEM` |
| Ent Leaves | 树人之叶 | `ENTLEAVES_ITEM` |
| Silver Lettuce | 银叶莴苣 | `SILVERLETTUCE_ITEM` |
| Dragon Scales | 龙鳞 | `DRAGONSCALES_ITEM` |
| Magnesium | 镁 | `MAGNESIUM_ITEM` |
| Mithril | 秘银 | `MITHRIL_ITEM` |
| Thick Leather | 厚皮革 | `THICKLEATHER_ITEM` |
| Meteor Metal | 陨铁 | `METEORMETAL_ITEM` |
| Mistletoe | 槲寄生 | `MISTLETOE_ITEM` |
| White Yarrow | 白蓍草 | `WHITEYARROW_ITEM` |

## 技能、特性与物品套装 / Skills, traits and item sets

| English | 中文 | 文本键 |
| --- | --- | --- |
| Corrosive Blood | 腐蚀之血 | `ACIDBLOOD` |
| Death Fog | 死亡迷雾 | `ACIDCLOUD_SPELL` |
| Acid Grenade | 酸液手雷 | `ACIDGRENADE_SPELL` |
| Acid Spit | 喷吐酸液 | `ACIDSPITRANGEDATTACK` |
| Acid Splash | 酸液飞溅 | `ACIDSPLASH_SPELL` |
| Acid Wave | 酸液波 | `ACIDWAVE_SPELL` |
| Adrenaline | 肾上腺素 | `ADRENALINE` |
| Alchemy | 炼金术 | `ALCHEMY` |
| Bad Luck | 厄运 | `BADLUCK` |
| Horrific Scream | 恐怖尖啸 | `BANSHEESCREAMWAVE_SPELL` |
| Roar | 咆哮 | `ROAR_SPELL` |
| Barkskin | 树皮术 | `BARKSKIN_SPELL` |
| Battle Forged | 久经战阵 | `BATTLEFORGED` |
| Demonborn | 魔裔 | `CHAOSCHOSEN` |
| Alpha Rat | 首领鼠 | `RATALPHA` |
| Beta Rat | 从属鼠 | `RATBETA` |
| Gambler | 赌徒 | `GAMBLER` |
| Focused | 专注 | `FOCUSED` |
| Battle Frenzy | 战斗狂乱 | `BATTLEFRENZY` |
| Battle Frenzy Aura | 战斗狂乱光环 | `BATTLEFRENZYAURA` |
| Beast | 野兽 | `BEAST` |
| Bees Swarm | 蜂群 | `BEESSWARM_SPELL` |
| Berserker | 狂战士 | `BERSERKER` |
| Big Target | 大型目标 | `BIGTARGET` |
| Tasty | 美味 | `TASTY` |
| Swiftly | 敏捷迅速 | `SWIFT` |
| Black Dragon Form | 黑龙形态 | `BLACKDRAGONSELFPOLYMORPH_SPELL` |
| Bless | 祝福术 | `BLESS_SPELL` |
| Silence | 沉默术 | `SILENCE_SPELL` |
| Blessed | 祝福 | `BLESSED` |
| Vitalized | 生命充盈 | `BLOODMAGIC` |
| Berserker's Rage | 狂战士之怒 | `BERSERKERRAGE` |
| Blood Moon | 血月 | `BLOODMOON_SPELL` |
| Battle Rage | 战斗狂怒 | `BLOODLUST` |
| Bloodlust | 嗜血 | `BLOODTHIRST` |
| Brave | 勇敢 | `BRAVE` |
| Arachnophobia | 蜘蛛恐惧症 | `ARACHNOPHOBIA` |
| Burning Skulls | 燃烧颅骨 | `BURNINGSKULLS` |
| Bear Form | 熊形态 | `CAVEBEARSELFPOLYMORPH_SPELL` |
| Chain Lightning | 连锁闪电 | `CHAINLIGHTING_SPELL` |
| Champion | 勇士 | `CHAMPIONGLOBAL` |
| Nature's Luck | 自然眷顾 | `NATURELUCKGLOBAL` |
| Motivated | 斗志昂扬 | `CHAMPION` |
| Chaos Storm | 混沌风暴 | `CHAOSSTORM` |
| Charisma | 魅力 | `CHARISMA` |
| Charm | 魅惑 | `CHARM` |
| Chill Touch | 寒冷之触 | `CHILLTOUCH_SPELL` |
| Force Push | 念力推击 | `FORCEPUSH_SPELL` |
| Cleanse | 净化术 | `CLEANSE_SPELL` |
| Cleave | 顺劈 | `CLEAVE` |
| Tenacity | 坚韧 | `TENACITY` |
| Cluster Bomb | 集束炸弹 | `CLUSTERBOMB` |
| Freezing Cold | 严寒 | `COLDGLOBAL` |
| Cold Resistance | 寒冷抗性 | `COLDRESISTANCE` |
| Cold Vulnerability | 寒冷易伤 | `COLDVULNERABILITY` |
| Collector | 收藏家 | `COLLECTOR` |
| Construct | 构装体 | `CONSTRUCT` |
| Consume Corpse | 吞食尸体 | `CONSUMECORPSE_SPELL` |
| Command Construct | 控制构装体 | `CONTROLCONSTRUCT_SPELL` |
| Command Elemental | 控制元素生物 | `CONTROLELEMENTAL_SPELL` |
| Command Plant | 控制植物 | `CONTROLPLANT_SPELL` |
| Command Undead | 控制亡灵 | `CONTROLUNDEAD_SPELL` |
| Coward | 怯懦 | `COWARD` |
| Mercenary | 雇佣兵 | `MERCENARY` |
| Crippling Shot | 致残射击 | `CRIPPLINGSHOT` |
| Precision | 精准 | `CRITICALHIT` |
| Crusader | 十字军 | `CRUSADER` |
| Crusher | 粉碎者 | `CRUSHER` |
| Curse | 诅咒术 | `CURSE_SPELL` |
| Dark Awakening | 黑暗觉醒 | `DARKBLESSING` |
| Sharp Claws | 利爪 | `SHARPCLAWS` |
| Hard Shell | 硬壳 | `HARDSHELL` |
| Darkness | 黑暗 | `DARKNESSGLOBAL` |
| Death Ray | 死亡射线 | `DEATHRAYRANGEDATTACK` |
| Death Beam | 死亡光束 | `DEATHRAYSPELL` |
| Acid Beam | 酸液光束 | `PLAGUEACIDRAYSPELL` |
| Freezing Beam | 冰冻光束 | `FREEZINGRAYSPELL` |
| Decay | 腐朽 | `DECAY` |
| Silenced | 沉默 | `SILENCED` |
| Decay | 腐朽 | `DECAY_SPELL` |
| Hold | 定身术 | `HOLDPERSON_SPELL` |
| Taunt | 嘲讽 | `TAUNT_SPELL` |
| Demon | 恶魔 | `DEMON` |
| Demons Pact | 恶魔契约 | `DEMONPACT` |
| Broken Heart | 心碎 | `BROKENHEART` |
| Crystal Battery | 水晶电池 | `DEMONICBATTERY` |
| Demons Realm | 恶魔领域 | `DEMONSREALMGLOBAL` |
| Mana Field | 魔力场 | `MANAFIELDGLOBAL` |
| Fear Attack | 恐惧攻击 | `DESPAIRATTACK` |
| Detonate | 引爆 | `DETONATE_SPELL` |
| War Bear Form | 战熊形态 | `DIREBEARSELFPOLYMORPH_SPELL` |
| Disease Spreading | 疾病传播 | `DISEASE_SPREAD` |
| Paralyze | 麻痹 | `PARALYZE` |
| Fear | 恐惧 | `FEAR` |
| Entangle | 缠绕 | `ENTANGLE` |
| Ensnare | 网缚 | `ENSNARE` |
| Push | 推开 | `PUSH` |
| Stun | 击晕 | `STUN` |
| Disease Aura | 疾病光环 | `DISEASEAURA` |
| Fear Aura | 恐惧光环 | `FEARAURA` |
| Disease Carrier | 疾病携带者 | `DISEASECARRIER` |
| Disintegration | 解离术 | `DISINTEGRATION_SPELL` |
| Dispel Magic | 驱散魔法 | `DISPELMAGIC_SPELL` |
| Magic Burn | 魔力灼伤 | `DISTURBEDMAGIC` |
| Magic Burn Attack | 魔力灼伤攻击 | `DISTURBINGMAGICATTACK` |
| Divine Shield | 神圣护盾 | `DIVINESHIELD_SPELL` |
| Double Attack | 双重攻击 | `DOUBLEATTACK` |
| Double Damage | 双倍伤害 | `DOUBLEDAMAGE` |
| Pushing Attack | 推击 | `PUSHINGATTACK` |
| Drunkard | 酒鬼 | `DRUNKARD` |
| Dual Wield | 双持 | `DUALWIELD` |
| Archer | 弓箭手 | `BOWEQUIP` |
| Dwarven Ale | 矮人麦酒 | `DWARVENALE_SPELL` |
| Earth Quake | 地震 | `EARTHQUAKEGLOBAL` |
| Elemental | 元素生物 | `ELEMENTAL` |
| Elementals Resistance | 元素抗性 | `ELEMENTALSRESISTANCE` |
| Elite | 精英 | `ELITE` |
| Enhanced Armour | 强化护甲 | `ENHANCEDARMOR` |
| Enhanced Weapon | 强化武器 | `ENHANCEDWEAPON` |
| Enslave | 奴役 | `ENSLAVE_SPELL` |
| Tame Beast | 驯服野兽 | `TAMEBEAST_SPELL` |
| Seduce | 诱惑 | `SEDUCTION_SPELL` |
| Seduced | 受诱惑 | `SEDUCED` |
| Enslaved | 被奴役 | `ENSLAVED` |
| Tamed | 已驯服 | `TAMED` |
| Ensnare | 网缚 | `ENSNARERANGEDATTACK` |
| Entangling Roots | 根须缠绕 | `ENTANGLINGATTACK` |
| Exhausted | 疲惫 | `EXHAUSTED` |
| Exorcism | 驱魔术 | `EXORCISM_SPELL` |
| Advanced Summoning | 高等召唤术 | `EXTENDEDSUMMONS` |
| Finger of Death | 死亡一指 | `FINGEROFDEATH_SPELL` |
| Fire Aura | 火焰光环 | `FIREAURA` |
| Raise Furniture | 活化家具 | `SUMMONFURNITURESSPELL` |
| Fire Strike | 烈焰打击 | `FIREDAMAGE` |
| Fire Grenade | 燃烧手雷 | `FIREGRENADE_SPELL` |
| Fire Gun | 火枪射击 | `FIREGUNRANGEDATTACK` |
| Sniper Shot | 狙击 | `LONGFIREGUNRANGEDATTACK` |
| Fire Resistance | 火焰抗性 | `FIRERESISTANCE` |
| Flammable | 易燃 | `FIREVULNERABILITY` |
| Fireball | 火球术 | `FIREBALL_SPELL` |
| Hellish Assault | 地狱突袭 | `DEMONTELEPORTATIONSELF_SPELL` |
| Tunnel | 地底穿行 | `BURROWTELEPORTATIONSELF_SPELL` |
| Blink | 闪现 | `TELEPORTATIONSELF_SPELL` |
| Dark Vision | 黑暗视觉 | `DARKVISION_SPELL` |
| Firebolt | 火焰箭 | `FIREBOLT_SPELL` |
| Sleeping Dart | 催眠飞镖 | `SLEEPDART_SPELL` |
| Flame Wave | 烈焰波 | `FLAMEWAVE_SPELL` |
| Four Arms | 四臂 | `FOURARMS` |
| Freezing Attack | 冰冻攻击 | `FREEZINGATTACK` |
| Freezing Aura | 冰冻光环 | `FREEZINGAURA` |
| Freezing Flask | 冰冻药瓶 | `FREEZINGFLASK_SPELL` |
| Freezing Tornado | 冰冻龙卷风 | `FREEZINGTORNADO_SPELL` |
| Black Vortex | 黑色漩涡 | `BLACKVORTEX_SPELL` |
| Overloaded | 过载 | `BLACKVORTEX` |
| Freezing Wave | 冰冻波 | `FREEZINGWAVE_SPELL` |
| Gate | 传送门 | `GATE` |
| Giant's Strength | 巨人之力 | `GIANTSTRENGTH` |
| Hatch Eggs | 孵卵 | `HATCHEGGSONDEATH` |
| Executioner | 刽子手 | `HEADHUNTER` |
| Heal | 治疗术 | `HEAL_SPELL` |
| Heal Undead | 治疗亡灵 | `UNDEADHEAL_SPELL` |
| Healing Aura | 治疗光环 | `HEALINGAURA` |
| Health Potion | 生命药剂 | `HEALTHPOTION_SPELL` |
| Blood Transfusion | 输血术 | `BLOODTRANSFUSION_SPELL` |
| Magic Dust | 魔法粉尘 | `MAGICDUST_SPELL` |
| Healthy | 健康 | `HEALTHY` |
| Hero | 英雄 | `HERO` |
| Hero (non-minor) | 英雄（非次要） | `HERO_NON_MINOR` |
| Church Donation | 教会捐赠 | `HOLYCHURCHOFFERING` |
| Holy Grenade | 神圣手雷 | `HOLYGRENADE` |
| Holy Ground | 圣地 | `HOLYGROUNDGLOBAL` |
| Holy Light | 圣光 | `HOLYLIGHT` |
| Holy Strike | 神圣打击 | `HOLYSTRIKE` |
| Greater Holy Strike | 强效神圣打击 | `IMPROVEDHOLYSTRIKE` |
| Drunken Master | 醉拳大师 | `DRUNKENMASTER` |
| Holy Water | 圣水 | `HOLYWATER_SPELL` |
| Howl | 嚎叫 | `HOWL_SPELL` |
| Hypnotize | 催眠术 | `HYPNOTIZE_SPELL` |
| Greater Hypnotize | 强效催眠术 | `IMPROVEDHYPNOTIZE_SPELL` |
| Hypnotized | 被催眠 | `HYPNOTIZED` |
| Ice Shard | 冰刺 | `ICEBOLT_SPELL` |
| Phoenix | 凤凰 | `PHOENIX` |
| Non-Blocking | 不造成牵制 | `NONBLOCKING` |
| Impale | 穿刺 | `IMPALE_SPELL` |
| Nullify Magic | 魔法无效化 | `IMPROVEDDISPELMAGIC_SPELL` |
| Firestorm | 火焰风暴 | `IMPROVEDFIREBALL_SPELL` |
| Meteor Fall | 陨石天降 | `METEOR_SPELL` |
| Greater Heal | 强效治疗术 | `IMPROVEDHEAL_SPELL` |
| Greater Magic Resistance | 强效魔法抗性 | `IMPROVEDMAGICRESISTANCE` |
| Beyond the Grave | 墓外归来 | `IMPROVEDRAISEDEAD_SPELL` |
| Greater Regeneration | 强效再生 | `IMPROVEDREGENERATION` |
| Complete Regeneration | 完全再生 | `COMPLETEREGENERATION` |
| Greater Soul Capture | 强效灵魂捕获 | `IMPROVEDSOULCAPTURE` |
| Greater War Runes | 强效战争符文 | `IMPROVEDWARRUNES` |
| Warriors Clan | 战士氏族 | `RATRUNES` |
| Nobles Clan | 贵族氏族 | `IMPROVEDRATRUNES` |
| Intelligent | 聪慧 | `INTELLIGENT` |
| Corpseless | 不留尸体 | `DESTROYAFTERDEATH` |
| Creature of Night | 夜行生物 | `CREATUREOFNIGHT` |
| Snares | 捕兽夹 | `BEARTRAP` |
| Bone Trap | 骸骨陷阱 | `BONETRAP` |
| Fire Rune Trap | 火焰符文陷阱 | `RUNETRAPFIRE` |
| Freezing Rune Trap | 冰冻符文陷阱 | `RUNETRAPFREEZE` |
| Lightning Rune Trap | 闪电符文陷阱 | `RUNETRAPLIGHTING` |
| Spores | 孢子 | `SPORESTRAP` |
| Immortality | 不朽 | `ANCIENT` |
| Heretic | 异端 | `CHAOSCORRUPTED` |
| Saint | 圣徒 | `SAINT` |
| Greed | 贪婪 | `GREEDY` |
| Poison Eater | 食毒者 | `SNAKEEATER` |
| Madness | 疯狂 | `MADNESS` |
| Duelist | 决斗家 | `DUELIST` |
| Iron Lungs | 钢铁之肺 | `IRONLUNGS` |
| Cold-blooded | 冷血 | `COLDBLOOD` |
| Puppet Master | 傀儡师 | `PUPPETMASTER` |
| Sharpshooter | 神射手 | `SCOUT` |
| Savage | 野蛮 | `SAVAGE` |
| Brawler | 格斗士 | `BRAWLER` |
| Memories | 回忆 | `MEMORIES` |
| Crystal Skin | 水晶皮肤 | `CRYSTAL_SKIN` |
| Moon Mage | 月之法师 | `MOONMAGE` |
| Dance of Swords | 剑舞 | `SWORD_DANCE` |
| Intoxicated | 醉酒 | `INTOXICATED` |
| Invisible | 隐形 | `INVISIBILITY` |
| Burrow | 潜地 | `BURROW_SPELL` |
| Unburrow | 钻出地面 | `UNBURROW_SPELL` |
| Rain | 降雨 | `RAIN_SPELL` |
| Earthquake | 地震 | `EARTHQUAKE_SPELL` |
| Strong Wind | 强风 | `STRONGWIND_SPELL` |
| Invulnerability Armour | 无敌护甲 | `INVULNERABILITYARMOR_SPELL` |
| Fire Shield | 火焰护盾 | `FIREAURA_SPELL` |
| Freezing Shield | 冰冻护盾 | `FREEZINGAURA_SPELL` |
| Iron Golem Form | 钢铁魔像形态 | `IRONGOLEMSELFPOLYMORPH_SPELL` |
| Black Spider Form | 黑蜘蛛形态 | `GIANTSPIDERBLACKSELFPOLYMORPH_SPELL` |
| Bat Form | 蝙蝠形态 | `VAMPIREBATSELFPOLYMORPH_SPELL` |
| Mist Form | 迷雾形态 | `VAMPIREFOGSELFPOLYMORPH_SPELL` |
| Charge | 冲锋 | `JOUSTING` |
| Greater Charge | 强效冲锋 | `IMPROVEDJOUSTING` |
| Hit and Run | 打带跑 | `HITANDRUNATTACK` |
| Sixth Sense | 第六感 | `KIEVADE` |
| KI Master | 气功大师 | `KIMASTER` |
| Evade | 闪避 | `RATMANEVADE` |
| Better Evade | 强化闪避 | `RATMANIMPROVEDEVADE` |
| Killing Blow | 致命一击 | `KILLINGBLOW` |
| Bushido | 武士道 | `BUSHIDOKILLING` |
| Midas Touch | 点石成金 | `MIDASTOUCH` |
| Knife Throw | 飞刀投掷 | `KNIFETHROWRANGEDATTACK` |
| Heat Ray | 热能射线 | `LASERRAYRANGEDATTACK` |
| Heat Beam | 热能光束 | `LASERRAYSPELL` |
| Lay on Hands | 圣疗术 | `LAYONHANDS_SPELL` |
| Leadership | 领导力 | `LEADERSHIP` |
| Grumpy | 暴躁 | `GRUMPY` |
| Lone Hero | 孤胆英雄 | `SINGLEUNIT` |
| Limited Supply | 补给有限 | `LIMITEDSUPPLY` |
| Pack Master | 群鼠统领 | `SLAVEMASTER` |
| Brainwash | 洗脑 | `DESERTIONBRAINWASH` |
| Intimidate | 威吓 | `DESERTIONINTIMIDATE` |
| Tranquility | 宁静 | `DESERTIONTRANQUILITY` |
| Drunkard | 酒鬼 | `DESERTIONDRUNKARD` |
| Seduction | 诱惑 | `DESERTIONSEDUCTION` |
| Pack Master | 群鼠统领 | `DESERTIONSLAVEMASTER` |
| Song of Bravery | 勇气之歌 | `DESERTIONSONGOFSIREN` |
| Hypnotize | 催眠术 | `DESERTIONHYPNOTIZE` |
| Prayer | 祈祷 | `DESERTIONPRAYER` |
| Drugs | 药物 | `DESERTIONDRUGS` |
| Warboss | 战争头目 | `WARBOSS` |
| Warchief | 战争酋长 | `IMPROVEDWARBOSS` |
| Vampiric Mist | 吸血迷雾 | `LIFEDRAINCLOUD_SPELL` |
| Holy Protection | 神圣庇护 | `HOLYPROTECTION` |
| Lightning Strike | 闪电打击 | `LIGHTINGATTACK` |
| Lightning Aura | 闪电光环 | `LIGHTINGAURA` |
| Lightning | 闪电 | `LIGHTINGRANGEDATTACK` |
| Lightning Resistance | 闪电抗性 | `LIGHTINGRESISTANCE` |
| Lightning Vulnerability | 闪电易伤 | `LIGHTINGVULNERABILITY` |
| Liquid Fire | 液态火焰 | `LIQUIDFIRE_SPELL` |
| Lightning Bottle | 闪电瓶 | `LIGHTINGBOTTLE_SPELL` |
| Shoot Arrow | 射箭 | `LONGRANGEDATTACK` |
| Multi-Shot Arrow | 多重射箭 | `MULTILONGRANGEDATTACK` |
| Gold | 金币 | `LOOT` |
| Luck | 幸运 | `LUCK` |
| Magic Channel | 魔力传导 | `MAGICCHANNEL_SPELL` |
| Magic Immunity | 魔法免疫 | `MAGICIMMUNITY` |
| Magic Missile | 魔法飞弹 | `MAGICMISSLERANGEDATTACK` |
| Magic Source | 魔力源泉 | `MAGICREGENERATIONAURA` |
| Magic Resistance | 魔法抗性 | `MAGICRESISTANCE` |
| Traps Resistance | 陷阱抗性 | `TRAPSRESISTANCE` |
| Magic Shield | 魔法护盾 | `MAGICSHIELD` |
| Magic Shield | 魔法护盾 | `MAGICSHIELD_SPELL` |
| Reflection Shield | 反射护盾 | `REFLECTIONMAGICSHIELD_SPELL` |
| Magic Vulnerability | 魔法易伤 | `MAGICVULNERABILITY` |
| Magical Armour | 魔法护甲 | `MAGICALARMOR` |
| Magical Weapon | 魔法武器 | `MAGICALWEAPON` |
| Mark of Pain | 痛苦印记 | `MARKOFDEATH_SPELL` |
| Mass Bless | 群体祝福术 | `MASSBLESS_SPELL` |
| Nightmares | 梦魇 | `MASSNIGHTMARES_SPELL` |
| Mass Slow | 群体迟缓术 | `MASSSLOW_SPELL` |
| Mass Confuse | 群体混乱术 | `MASSCONFUSE_SPELL` |
| Piercing Magic | 穿透魔法 | `MASSPIERCINGMAGIC_SPELL` |
| Mass Stoneskin | 群体石肤术 | `MASSSTONESKIN_SPELL` |
| Mass Black Widow Venom | 群体黑寡妇毒液 | `MASSWIDOWVENOM_SPELL` |
| Arcane Master | 奥术大师 | `MASTERMAGICIAN` |
| Raw Meat Diet | 生肉食性 | `MEATDIET` |
| Meditate | 冥想 | `MEDITATE_SPELL` |
| Blood Sacrifice | 血祭 | `BLOODSACRIFICE_SPELL` |
| Lightning | 闪电 | `MEDIUMLIGHTINGRANGEDATTACK` |
| Shoot Arrow | 射箭 | `MEDIUMRANGEDATTACK` |
| Multi-Shot Arrow | 多重射箭 | `MULTIMEDIUMRANGEDATTACK` |
| Merchant | 商人 | `MERCHANT` |
| Metal Net | 金属网 | `METALNET` |
| Knockout Gas | 昏迷毒气 | `KNOCKOUTGAS` |
| Mind Blast | 心灵冲击 | `MINDBLAST_SPELL` |
| Devour | 吞噬 | `SANDWORMCONSUME_SPELL` |
| Ironmind | 钢铁意志 | `MIND_SPELLSIMMUNITY` |
| Team Morale (Happy) | 队伍士气（愉快） | `MORALEHAPPY` |
| Team Morale (Neutral) | 队伍士气（平静） | `MORALENEUTRAL` |
| Team Morale (Regretful) | 队伍士气（懊悔） | `MORALEUNHAPPY` |
| Team Morale (Very Happy) | 队伍士气（非常愉快） | `MORALEVERYHAPPY` |
| Multi-Attack | 多重攻击 | `MULTIATTACK` |
| Multi Fire Gun | 多重火枪射击 | `MULTIFIREGUNRANGEDATTACK` |
| Multi Knife Throw | 多重飞刀投掷 | `MULTIKNIFETHROWRANGEDATTACK` |
| Multi Shuriken Throw | 多重手里剑投掷 | `MULTISHURIKENTHROWRANGEDATTACK` |
| Shuriken Throw | 手里剑投掷 | `SHURIKENTHROWRANGEDATTACK` |
| Multi Magic Missile | 多重魔法飞弹 | `MULTIMAGICMISSLERANGEDATTACK` |
| Magic Regeneration | 魔法再生 | `MULTIMAGICREGENERATION` |
| Friends of Forest | 森林之友 | `NATURECALL_SPELL` |
| Dance Macabre | 死亡之舞 | `DANCEMACABRECALL_SPELL` |
| Nature Wisdom | 自然智慧 | `NATUREWISDOM` |
| No Damage Attack | 无伤害攻击 | `NODAMAGEATTACK` |
| Static Magic | 魔法停滞 | `NOMAGICREGENERATION` |
| No Melee Attack | 无法近战 | `NOMELEEATTACK` |
| Noble | 贵族 | `NOBILITY` |
| Nuke | 核爆 | `NUKE_SPELL` |
| Paralyzed | 麻痹 | `PARALYZED` |
| Paralyzing Attack | 麻痹攻击 | `PARALYZINGATTACK` |
| Parry | 招架 | `PARRY` |
| Passive | 被动 | `PASSIVE` |
| Physical Resistance | 物理抗性 | `PHYSICALRESISTANCE` |
| Retribution | 惩戒 | `RETRIBUTION_SPELL` |
| Polymorph | 变形术 | `PIGPOLYMORPH_SPELL` |
| Plant | 植物 | `PLANT` |
| Poison Aura | 剧毒光环 | `POISONAURA` |
| Poison Cloud | 毒云 | `POISONCLOUD_SPELL` |
| Poison Flask | 毒药瓶 | `POISONFLASK_SPELL` |
| Poison Grenade | 毒气手雷 | `POISONGRENADE_SPELL` |
| Poison Immunity | 毒素免疫 | `POISONIMMUNITY` |
| Poison Resistance | 毒素抗性 | `POISONRESISTANCE` |
| Fine Senses | 敏锐感官 | `SHARPSENSES` |
| Light Source | 光源 | `LIGHTSOURCE` |
| Detector | 探测者 | `DETECTOR` |
| Poison Vulnerability | 毒素易伤 | `POISONVULNERABILITY` |
| Reloading | 装填中 | `RELOADING` |
| Poisonous Attack | 毒素攻击 | `POISONOUSATTACK` |
| Venomous Attack | 剧毒攻击 | `IMROVEDPOISONOUSATTACK` |
| Possession | 附身术 | `POSSESS_SPELL` |
| Possessed | 被附身 | `POSSESSED` |
| Power Strike | 强力打击 | `POWERSTRIKEATTACK` |
| Shield Bash | 盾击 | `SHIELDBASHATTACK` |
| Prayer | 祈祷 | `PRAYER_SPELL` |
| Clairvoyance | 灵视术 | `CLAIRVOYANCE_SPELL` |
| Sharp Eyes | 锐眼术 | `SHARPEYES_SPELL` |
| Scan | 扫描 | `SCANSENSOR_SPELL` |
| Projectiles Resistance | 投射物抗性 | `PROJECTILESRESISTANCE` |
| Projectiles Reflection | 投射物反弹 | `ARROWREFLECTION` |
| Purple Heart | 紫心勋章 | `PURPLEHEART` |
| Quadruple Attack | 四重攻击 | `QUADRUPLEATTACK` |
| Quickness | 迅捷 | `QUICKNESS` |
| Quicksilver Armour | 水银护甲 | `QUICKSILVER` |
| Warcry | 战吼 | `RALLY_SPELL` |
| Reaper | 收割者 | `REAPER` |
| Recovery | 恢复 | `RECOVERY` |
| Regeneration | 再生 | `REGENERATION` |
| Regrowth | 复生 | `REGROWTH` |
| Divine Intervention | 神圣干预 | `DIVINEINTERVENTION` |
| Regular | 正规 | `REGULAR` |
| Reinforced | 加固 | `REINFORCED` |
| Reinforced Ale | 烈性麦酒 | `REINFORCEDDWARVENALE_SPELL` |
| Call Reinforcements | 呼叫援军 | `REINFORCEMENTSCALL_SPELL` |
| Rats Swarm | 鼠群 | `RATSWARM_SPELL` |
| Repair | 修复 | `REPAIR_SPELL` |
| Rune of Fire | 火焰符文 | `RUNEOFFIRE_SPELL` |
| Rune of Immolation | 献祭之焰符文 | `RUNEOFIMMOLATION_SPELL` |
| Rune of Freeze | 冰冻符文 | `RUNEOFFREEZE_SPELL` |
| Rune of Heal | 治疗符文 | `RUNEOFHEAL_SPELL` |
| Rune of Stone | 岩石符文 | `RUNEOFSTONE_SPELL` |
| Rune of Frenzy | 狂乱符文 | `RUNEOFFRENZY_SPELL` |
| Rune of Lightning | 闪电符文 | `RUNEOFLIGHTING_SPELL` |
| Rune of Poison | 剧毒符文 | `RUNEOFPOISON_SPELL` |
| Sacrifice | 献祭 | `SACRIFICE_SPELL` |
| Run | 奔跑 | `RUN_SPELL` |
| Sea Dog | 老海狗 | `SEADOGS` |
| Sea Sickness | 晕船 | `SEASICKNESS` |
| Sea Battle | 海战 | `SEASICKNESSGLOBAL` |
| Segmented Move | 分段移动 | `SEGMENTEDMOVE` |
| Shield Breaker | 破盾者 | `SHIELDBREAKER` |
| Sleep | 睡眠 | `SLEEP` |
| Clumsy | 笨拙 | `SLOWATTACK` |
| Slow | 迟缓术 | `SLOW_SPELL` |
| Confuse | 混乱术 | `CONFUSE_SPELL` |
| Song of Fear | 恐惧之歌 | `SONGOFFEAR_SPELL` |
| Song of Bravery | 勇气之歌 | `SONGOFSIREN_SPELL` |
| Release Swarm | 释放蜂群 | `SPAWN_WASP_ON_DEATH` |
| Sacred Armour | 神圣护甲 | `SPECIALARMOR` |
| Sacred Weapon | 神圣武器 | `SPECIALWEAPON` |
| Spikes | 尖刺 | `SPIKES` |
| Riposte | 还击 | `RIPOSTE` |
| Stationary | 固定不动 | `STATIONARY` |
| Steal Experience | 窃取经验 | `STEALEXPERIENCE_SPELL` |
| Soul Stealer | 窃魂者 | `STEALSOULATTACK` |
| Steal Item | 偷取物品 | `STEALITEM_SPELL` |
| Shadow Hand | 暗影之手 | `SHADOWHAND_STEAL_ITEM_SPELL` |
| Infravision | 红外视觉 | `STEALTHATTACK` |
| Stinky | 恶臭 | `STINKY` |
| Stone Form | 岩石形态 | `STONEFORM` |
| Burrowed | 潜地中 | `BURROWED` |
| Petrification | 石化 | `STONEFORMAFTERDEATH` |
| Stone Throw | 投石 | `STONETHROWRANGEDATTACK` |
| Stoneskin | 石肤术 | `STONESKIN_SPELL` |
| Strong Roots | 强韧根须 | `STRONGROOTS` |
| Stunning Attack | 击晕攻击 | `STUNNINGATTACK` |
| Stupidity | 愚笨 | `STUPIDITY` |
| Summon Avatar | 召唤化身 | `SUMMONAVATARS_SPELL` |
| Summon Illusions | 召唤幻象 | `SUMMONILLUSIONS_SPELL` |
| Place Mines | 布设地雷 | `SUMMONDWARFMINES_SPELL` |
| Place Sentry Gun | 架设哨戒炮 | `SUMMONDWARFSENTRYGUNS_SPELL` |
| Place Snares | 布设捕兽夹 | `SUMMONBEARTRAPS_SPELL` |
| Place Bone Trap | 布设骸骨陷阱 | `SUMMONBONETRAPS_SPELL` |
| Place Fire Rune | 布设火焰符文 | `SUMMONRUNETRAPSFIRE_SPELL` |
| Place Freezing Rune | 布设冰冻符文 | `SUMMONRUNETRAPSFREEZE_SPELL` |
| Place Lightning Rune | 布设闪电符文 | `SUMMONRUNETRAPSLIGHTING_SPELL` |
| Place Gunpowder Barrel | 放置火药桶 | `SUMMONEXPLOSIVEBARREL_SPELL` |
| Place Spores | 布设孢子 | `SUMMONSPORESTRAPS_SPELL` |
| Summon {0} | 召唤{0} | `SUMMON_S_SPELL` |
| Summoned | 召唤物 | `SUMMONED` |
| Survivor | 幸存者 | `SURVIVOR` |
| Wanted | 被通缉 | `WANTED` |
| Strong | 强壮 | `STRONG` |
| Feral | 野性 | `FERAL` |
| Fire Starter | 纵火者 | `FIRESTARTER` |
| (trait) | （特性） | `EMPTYTRAIT` |
| Maimed | 伤残 | `MAIMED` |
| Guardian | 守护者 | `DEFENDER` |
| Wild Mage | 狂野法师 | `WILDMAGE` |
| Fatso | 胖子 | `FATSO` |
| Claustrophobia | 幽闭恐惧症 | `CLAUSTROPHOBIA` |
| Die Hard | 顽强不屈 | `DIEHARD` |
| Loyal | 忠诚 | `LOYAL` |
| Deep Snow | 深雪 | `SNOWGLOBAL` |
| Slippery | 湿滑 | `SLIPPERYGLOBAL` |
| Desert Sun | 沙漠烈日 | `DESERTSUNGLOBAL` |
| Strong Wind | 强风 | `STRONGWINDGLOBAL` |
| Fog | 迷雾 | `FOG_SPELL` |
| Rain | 降雨 | `RAINGLOBAL` |
| Storm | 风暴 | `STORMGLOBAL` |
| Incendiary Cloud | 焚烧云 | `INCENDIARYCLOUDGLOBAL` |
| Acid Rain | 酸雨 | `ACIDRAINGLOBAL` |
| Blizzard | 暴风雪 | `BLIZZARDGLOBAL` |
| Teleportation | 传送术 | `TELEPORTATION_SPELL` |
| Advanced Teleportation | 高等传送术 | `IMPROVEDTELEPORTATION_SPELL` |
| Tentacle Whip | 触手鞭击 | `TENTACLEWHIPRANGEDATTACK` |
| Terror | 恐怖 | `TERRORGLOBAL` |
| Terror | 恐怖 | `TERROR` |
| Thick Hide | 厚皮 | `THICKHIDE` |
| Screaming Skull | 尖啸颅骨 | `THROWSCREAMINGSKULL_SPELL` |
| Time Shift | 时间偏移 | `TIMESHIFT_SPELL` |
| Dominate | 支配 | `DOMINATE_SPELL` |
| Whip-crack | 鞭笞 | `WHIPCRACK_SPELL` |
| Tough | 坚毅 | `TOUGH` |
| Transmutation | 转化术 | `TRANSMUTATION` |
| Scavenger | 拾荒者 | `GRAVEDIGGER` |
| Triple Damage | 三倍伤害 | `TRIPLEDAMAGE` |
| Quadruple Damage | 四倍伤害 | `QUADRUPLEDAMAGE` |
| Quintuple Damage | 五倍伤害 | `QUINTUPLEDAMAGE` |
| True Neutral | 绝对中立 | `TRUENEUTRAL` |
| Tutor | 导师 | `TUTOR` |
| Elder Tutor | 资深导师 | `IMPROVEDTUTOR` |
| Bard's Ballad | 吟游诗人的歌谣 | `BARDBALLAD` |
| Stubborn | 固执 | `STUBBORN` |
| Fire-based spells | 火焰系法术 | `FIREBASED_SPELLS` |
| (any other) | （其他任意） | `ANY_OTHER` |
| Unholy Endurance | 邪恶耐力 | `UNHOLYENDURANCE` |
| Assassin Drugs | 刺客秘药 | `ASSASSINDRUG` |
| Assassin Drugs | 刺客秘药 | `ASSASSINDRUG_SPELL` |
| Unholy Strength | 邪恶力量 | `UNHOLYSTRENGTH_SPELL` |
| False Life | 虚假生命 | `FALSELIFE_SPELL` |
| Unmorph | 恢复原形 | `UNPOLYMORPH_SPELL` |
| Chaos Magic | 混沌魔法 | `UNSTABLEMAGIC` |
| Unstable Summon | 不稳定召唤物 | `UNSTABLESUMMON` |
| Veteran | 老兵 | `VETERAN` |
| Volcano | 火山 | `VOLCANOGLOBAL` |
| Stealth Mission | 潜行任务 | `STEALTHMISSIONGLOBAL` |
| Ambush Disabled | 无法伏击 | `NOAMBUSHGLOBAL` |
| Battle Tasks | 战斗任务 | `BATTLETASKSGLOBAL` |
| Vorpal Blades | 斩首利刃 | `VORPALBLADES` |
| War Runes | 战争符文 | `WARRUNES` |
| Strong Tentacles | 强韧触手 | `STRONGTENTACLES1` |
| Stronger Tentacles | 更强韧触手 | `STRONGTENTACLES2` |
| Strongest Tentacles | 至强触手 | `STRONGTENTACLES3` |
| Advanced Design | 先进设计 | `ADVANCEDDESIGN` |
| Wasp's Sting | 胡蜂蜇刺 | `WASPSTING` |
| Barbed Blades | 倒刺利刃 | `BARBEDBLADE` |
| Bone-tip Arrows | 骨镞箭 | `BONEARROWS` |
| Jellyfish Tentacles | 水母触须 | `JELLYFISHTENTACLES` |
| Weak Melee Attack | 弱效近战攻击 | `WEAKMELEEATTACK` |
| Weakness | 虚弱术 | `WEAKNESS_SPELL` |
| Deathmark | 死亡印记 | `MARKOFHUNTED_SPELL` |
| Combat Shield Proficiency | 战盾精通 | `WEAPONANDSHIELDPROFICIENCY` |
| Armour Proficiency | 护甲精通 | `ARMORPROFICIENCY` |
| Black Widow Venom | 黑寡妇毒液 | `WIDOWVENOM_SPELL` |
| Blacksmith | 铁匠 | `CRAFTINGBLACKSMITH` |
| Runemaster | 符文大师 | `CRAFTINGRUNEMASTER` |
| Herbalist | 草药师 | `CRAFTINGHERBALIST` |
| Blesser | 赐福者 | `CRAFTINGBLESSER` |
| Evil Crafter | 邪恶工匠 | `CRAFTINGEVILCRAFTER` |
| Enhancer | 强化师 | `CRAFTINGENHANCER` |
| Jeweler | 珠宝匠 | `CRAFTINGJEWELER` |
| Potions | 药剂 | `GROUP_SET_ALCHEMY` |
| Potions | 药剂 | `GROUP_SET_HERBALIST` |
| Shadow | 暗影 | `GROUP_SET_ASSASSIN` |
| Shadow | 暗影 | `GROUP_SET_SHADOW` |
| Dark Art | 黑暗技艺 | `GROUP_SET_POISON` |
| Dark Art | 黑暗技艺 | `GROUP_SET_DARKNESS` |
| Necromancy | 死灵术 | `GROUP_SET_BONE_ART` |
| Necromancy | 死灵术 | `GROUP_SET_NECROMANCY` |
| Divine | 神圣 | `GROUP_SET_DIVINE` |
| Divine | 神圣 | `GROUP_SET_SAINT` |
| Might | 力量 | `GROUP_SET_STRENGTH` |
| Might | 力量 | `GROUP_SET_BARBARIAN` |
| Chaos | 混沌 | `GROUP_SET_CHAOS` |
| Chaos | 混沌 | `GROUP_SET_BERSERKER` |
| Headhunter | 猎头者 | `GROUP_SET_LEGION` |
| Headhunter | 猎头者 | `GROUP_SET_ENFORCER` |
| Magician | 魔术师 | `GROUP_SET_MAGICIAN` |
| Magician | 魔术师 | `GROUP_SET_ARCHMAGE` |
| Tribal | 部族 | `GROUP_SET_TRIBAL` |
| Tribal | 部族 | `GROUP_SET_FOREST` |
| Nobility | 贵族 | `GROUP_SET_KNIGHT` |
| Nobility | 贵族 | `GROUP_SET_MASTERY` |
| Runecraft | 符文工艺 | `GROUP_SET_CRYSTAL` |
| Runecraft | 符文工艺 | `GROUP_SET_RUNECRAFT` |
| Elemental | 元素 | `GROUP_SET_ICE` |
| Elemental | 元素 | `GROUP_SET_FLAME` |
| Elemental | 元素 | `GROUP_SET_LIGHTING` |
| Shinobi | 忍者 | `GROUP_SET_NINJA` |
| Shinobi | 忍者 | `GROUP_SET_SAMURAI` |
| Pirate | 海盗 | `GROUP_SET_PIRATE` |
| cursed item | 诅咒物品 | `CURSED_ITEM` |
| Quest Item | 任务物品 | `ITEM_RARITY_QUEST_ITEM` |
| duel | 决斗 | `DUEL` |
| {0} gp | {0}金币 | `S_GP` |
| {0}/{1} gp | {0}/{1}金币 | `S_S_GP` |
| serious wound | 重伤 | `PERMANENT_WOUND` |
| permanent | 永久 | `PERMANENT` |
| global | 全局 | `GLOBAL` |
| invocation | 咒术 | `INVOCATION` |
| aura | 光环 | `AURA` |
| chain | 连锁 | `CHAIN` |
| wave | 波动 | `WAVE` |
| line | 直线 | `LINE` |
| beam | 光束 | `BEAM` |
| blast | 爆发 | `BLAST` |
| delayed blast | 延迟爆发 | `DELAYED_BLAST` |
| continuous blast | 持续爆发 | `CONTINUOUS_BLAST` |
| team skill | 队伍技能 | `TEAM_SKILL` |
| activeable | 可主动使用 | `ACTIVEABLE` |
| ranged | 远程 | `RANGED` |
| {0}MP | {0}魔法值 | `S_MP` |
| {0} (+1 per level) turn(s) | {0}回合（每级增加1回合） | `S_PULS_ONE_PER_LEVEL_TURNSS` |
| {0}{1} turns | {0}{1}回合 | `SS_TURNS` |
| {0}{1} turn | {0}{1}回合 | `SS_TURN` |
| {0}{1} turn(s) | {0}{1}回合 | `SS_TURNSS` |
| {0} turns | {0}回合 | `S_TURNS` |
| {0} turn(s) | {0}回合 | `S_TURNSS` |
| {0} turn | {0}回合 | `S_TURN` |
| {0} uses | {0}次使用 | `S_USES` |
| {0} use | {0}次使用 | `S_USE` |
| Attack ({0}) | 攻击（{0}） | `ATTACK_S` |
| turns left: {0} | 剩余回合：{0} | `TURNS_LEFT_S` |
| {0} targets | {0}个目标 | `S_TARGETS` |
| {0} Slayer | {0}杀手 | `S_SLAYER` |

## 第7批补充：控制类型与作用对象

| English | 中文 | 文本键 |
| --- | --- | --- |
| Command | 统御 | `COMMAND` |
| Greenskins | 绿皮 | `GREENSKINS` |
| Heroes | 英雄 | `HEROES` |
| Paladins | 圣骑士 | `PALADINS` |
| Black Knights | 黑骑士 | `BLACK_KNIGHTS` |
| Black Guards | 黑卫士 | `BLACK_GUARDS` |
| Witches | 女巫 | `WITCHES` |
| Rat Brute | 鼠人蛮兵 | `RATMAN_BRUTE` |
| Succubi | 魅魔 | `SUCCUBI` |
| Mancubi | 曼库魔 | `MANCUBI` |
| spellcasters | 施法者 | `SPELLCASTERS` |
| archers | 弓箭手 | `ARCHERS` |
| Vampire Hunters | 吸血鬼猎人 | `VAMPIRE_HUNTERS` |
| Skeleton Mages | 骷髅法师 | `SKELETON_MAGES` |

## 第8批补充：人物与阵营

专名为当前暂定译法，剧情翻译时结合上下文复核；共享界面及战役名称沿用现有译名。

| English | 中文 | 文本键 |
| --- | --- | --- |
| Adventurers | 冒险者 | `ADVENTURERS` |
| Animals | 动物 | `ANIMALS` |
| Announcer | 播报员 | `ANNOUNCER` |
| Aurora | 奥萝拉 | `AURORA` |
| Bandits | 强盗 | `BANDITS` |
| Balbus | 巴尔布斯 | `BALBUS` |
| Barbarians | 野蛮人 | `BARBARIANS` |
| Blademaster | 剑术大师 | `BLADEMASTER` |
| Barbarian King | 蛮王 | `BARBARIAN_KING` |
| Cave Dwellers | 洞穴居民 | `CAVE_DWELLERS` |
| Chaos | 混沌 | `CHAOS` |
| Chaos Demons | 混沌恶魔 | `CHAOS_DEMONS` |
| Cheese | 奶酪 | `CHEESE` |
| Chimeras | 奇美拉 | `CHIMERAS` |
| City Guards | 城市卫兵 | `CITY_GUARDS` |
| Casino Guards | 赌场卫兵 | `CASINO_GUARDS` |
| Conclave | 秘会 | `CONCLAVE` |
| Corrupted Forest | 腐化森林 | `CORRUPTED_FOREST` |
| Crusaders | 十字军 | `CRUSADERS` |
| Crab God | 蟹神 | `CRAB_GOD` |
| Cultists | 邪教徒 | `CULTISTS` |
| Cursed | 受诅咒者 | `CURSED` |
| Defenders | 防守者 | `DEFENDERS` |
| Dummies | 训练假人 | `DUMMIES` |
| Dwarven Miners | 矮人矿工 | `DWARVEN_MINERS` |
| Dwarven Mutants | 变异矮人 | `DWARVEN_MUTANTS` |
| Earth Defence Force | 地球防卫军 | `EARTH_DEFENCE_FORCE` |
| Forest Dwellers | 森林居民 | `FOREST_DWELLERS` |
| Forest Creatures | 森林生物 | `FOREST_CREATURES` |
| Night Creatures | 暗夜生物 | `NIGHT_CREATURES` |
| Father Jonat | 乔纳特神父 | `FATHER_JONAT` |
| Forest Folk | 森林族群 | `FOREST_FOLK` |
| Greenskins Horde | 绿皮部落 | `GREENSKINS_HORDE` |
| Ghost Dragon | 幽灵龙 | `GHOST_DRAGON` |
| Graverobbers | 盗墓贼 | `GRAVEROBBERS` |
| Guardians | 守护者 | `GUARDIANS` |
| Guards | 卫兵 | `GUARDS` |
| Helna | 赫尔娜 | `HELNA` |
| Hive Defenders | 虫巢守卫 | `HIVE_DEFENDERS` |
| Holy Church | 圣教会 | `HOLY_CHURCH` |
| Human Defenders | 人类守军 | `HUMAN_DEFENDERS` |
| Human Kingdom | 人类王国 | `HUMAN_KINGDOM` |
| Hunters | 猎人 | `HUNTERS` |
| Hydra | 多头蛇 | `HYDRA` |
| Invaders | 入侵者 | `INVADERS` |
| Indulf | 因杜尔夫 | `INDULF` |
| Ikeus | 伊凯乌斯 | `IKEUS` |
| Iron Killer | 钢铁杀手 | `IRON_KILLER` |
| Kingdom Patrol | 王国巡逻队 | `KINGDOM_PATROL` |
| King William | 威廉国王 | `KING_WILLIAM` |
| Knight | 骑士 | `KNIGHT` |
| Mad Mage | 疯狂法师 | `MAD_MAGE` |
| Mages Guild | 法师公会 | `MAGES_GUILD` |
| Shinobi | 忍者 | `SHINOBI` |
| Marines | 海军陆战队 | `MARINES` |
| Moonshine Gang | 私酒帮 | `MOONSHINE_GANG` |
| Monstrosities | 怪物 | `MONSTROSITIES` |
| Mercs | 雇佣兵 | `MERCS` |
| Necromancer | 死灵法师 | `NECROMANCER` |
| Neutrals | 中立者 | `NEUTRALS` |
| Ninja | 忍者 | `NINJA` |
| Ogre | 食人魔 | `OGRE` |
| Portal Guardians | 传送门守卫 | `PORTAL_GUARDIANS` |
| Prisoners | 囚犯 | `PRISONERS` |
| Rats | 老鼠 | `RATS` |
| Rurora | 露萝拉 | `RURORA` |
| Sewer Dwellers | 下水道居民 | `SEWER_DWELLERS` |
| Sandworm | 沙虫 | `SANDWORM` |
| Sea People | 海族 | `SEA_PEOPLE` |
| Sea Creatures | 海洋生物 | `SEA_CREATURES` |
| Shades | 暗影幽魂 | `SHADES` |
| Sidra | 希德拉 | `SIDRA` |
| Sir Galad | 加拉德爵士 | `SIR_GALAD` |
| Souls Collector | 灵魂收集器 | `SOULS_COLLECTOR` |
| Spiders | 蜘蛛 | `SPIDERS` |
| Swamp Beasts | 沼泽野兽 | `SWAMP_BEASTS` |
| Swamp Dwellers | 沼泽居民 | `SWAMP_DWELLERS` |
| Swamp Witch | 沼泽女巫 | `SWAMP_WITCH` |
| Tavern Keeper | 酒馆老板 | `TAVERN_KEEPER` |
| Tunnel Dwellers | 地道居民 | `TUNNEL_DWELLERS` |
| Yazgut | 亚兹古特 | `YAZGUT` |
| Undead Altar | 亡灵祭坛 | `UNDEAD_ALTAR` |
| Undead King | 亡灵之王 | `UNDEAD_KING` |
| Undead Legion | 亡灵军团 | `UNDEAD_LEGION` |
| Villagers | 村民 | `VILLAGERS` |
| Waste Golems | 废料魔像 | `WASTE_GOLEMS` |
| Brutes | 蛮兵 | `BRUTES` |

## 新增机制用语

- 数字词按数值翻译：million＝百万、billion＝十亿。引擎仍以空格及千进位分组拼接，例如10,000显示“十 千”；不将million误译成“万”。属性加成中的“for {2}”已核实为持续时间时，统一用“持续{2}”。
- 控制效果类型 Command＝统御，替换第5批的“指挥”；心灵控制与统御并列时统一使用该译名。
- Mark of Death 的效果说明沿用游戏实际名称“痛苦印记”；Mark of Hunted 沿用“死亡印记”。已核对对应属性类的显示名称来源，避免按旧说明名称误配技能。

- Slayer＝杀手：击杀特定类型敌人后可能获得对应的攻击加成；与刺客兵种区别。
- 招架／还击说明中的 “Backstab attacks are ignored” 表示效果不适用于背刺攻击，不是免疫背刺。

- Regeneration＝再生；Regrowth＝复生（单位阵亡后在战斗结束时恢复）；Resurrection＝复活术。
- Battle Frenzy＝战斗狂乱；Battle Rage＝战斗狂怒；Bloodlust＝嗜血。
- Resistance＝抗性；Immunity＝免疫；Vulnerability＝易伤。无敌配剂保留原名称意象，其实际防护仅适用于物理攻击，后续说明不得宣称全伤害免疫。
- 内部键 HEADHUNTER 实际显示 Executioner（刽子手）；CRITICALHIT 实际显示 Precision（精准）；STEALTHATTACK 实际显示 Infravision（红外视觉）。
- Shitanto 已核对为双手武器，暂译希坦刀，不称短刀；装备效果与类型以游戏资料为准。

## 共享地点与玩法用语（50%里程碑）

- 阵营据点：混沌之门 (Chaos Portal)、兽人村落 (Orcs Village)、矮人堡垒 (Dwarven Fortress)、巨石阵 (Stonehenge)、海滨村落 (Coast Village)、地下巢穴 (Underground Nest)、骑士领地 (Knight's Estate)、废墟 (Ruins)。地点和具名设施均保留原英文；建筑名的大小写与原文一致。
- 银色森林 (Silver Forest)、索罗顿 (Sorodon)、人类王国 (Human Kingdom)、冥界 (Underworld) 沿用中文加英文的格式。
- Fin＝芬、Taz＝塔兹，暂定音译；Darius 沿用达里乌斯。
- Regular／Veteran／Elite 为单位资历：正规／老兵／精英。Sea Diver 沿用潜海者；Rat Grenadier＝鼠人掷弹兵；Master Assassin＝鼠人刺客大师。
- 据点英文旧称 Plague Cannon 对应实际显示 Acid Cannon，沿用酸液炮。Lamp of Blood＝鲜血之灯；Ancestors Helmet＝先祖头盔；Endless Purse＝无尽钱袋。
- Pirate Rum＝海盗朗姆酒；Idol of Happiness＝幸福神像；Regretful＝懊悔；Shade＝暗影幽魂；Mermaid＝美人鱼；Siren＝海妖。
- 小游戏中的奖金／奖池与净收益区分；按实际脚本说明牌型及钓鱼机制。脚本直接赋值的英文动态片段不冒充已汉化；杯子结果附顺序对照，换牌结果用中性标签承接。
- `Dis artis, dan oute. Grotta, de feruam infera!` 为虚构咒语，保留原文，不杜撰字面含义。

## 通用事件人物与叙事用语

- 第17批：Haunted Mine＝闹鬼矿场 (Haunted Mine)，Crystal Mine＝水晶矿场 (Crystal Mine)；原文为 Crystal Mines 时保留复数形式。Cursed Wights＝受诅咒的尸妖 (Cursed Wights)，Wight 沿用尸妖，不能混作巫妖。
- 矿场的 duty 在此译为“上缴收益”，金额按当前队伍有无矮人决定；原文雇用矿工的说法保留为叙事，不额外添加不存在的雇佣选项。

- 第16批：Pearl Mermaid＝珍珠美人鱼 (Pearl Mermaid)，Shaman's Hut＝萨满小屋 (Shaman's Hut)。Crab God 沿用蟹神，Black Pearl 沿用黑珍珠。
- 萨满的 cleanse ritual 译为“净化仪式”，实际服务说明用“卸下诅咒物品”，不表示将物品变为无诅咒装备，也不表示销毁物品；任务物品除外。普通珍珠交易每日一次，黑珍珠事件是独立的一次性事件。

- 第15批：Tranquil Grove＝宁静林地 (Tranquil Grove)，Well of Souls＝灵魂之井 (Well of Souls)；原文写作 Souls Well 时保留该英文形式。Dream Forest 暂译梦境森林 (Dream Forest)。
- Seedling＝幼苗，是培育材料；Saproling＝幼树人，是单位。Mandrake Root、Fungusoid、Swamp Ivy 沿用曼德拉草根、菌人、沼泽藤蔓。
- 灵魂之井的 Offer 译为“献祭”，与月亮井献上物品供奉区分。Priest 使用种族分组“祭司”，不窄化为具体的僧侣单位；九类献祭分别限一次。Death Warrior Armor／Helmet 沿用实际物品显示名“死亡战士护甲／头盔”。

- 第14批：地点 Magic Source＝魔力源泉 (Magic Source)，World Tree＝世界树 (World Tree)。Golden Apple 沿用“金苹果”；世界树叙述中的 spirits 译为“树灵”，区别于精灵族单位。三处魔力源泉分别每日刷新；世界树的金苹果不按每日刷新机制描述。

- 第13批：Temple of The Moon＝月之神殿 (Temple of The Moon)，Moon Well＝月亮井 (Moon Well)，Four Obelisks＝四座方尖碑 (Four Obelisks)；“魔力方尖碑”作为事件统称，不改写原始地图标签。
- Moon Key 沿用“月之钥”，Mana Shard 沿用“魔力碎片”，Sapphire 沿用“蓝宝石”。月亮井的 offering 译为“供品／献上”，避免把物品供奉说成献祭单位。
- 方尖碑结果对话中的 crystal amulet 是外观叙述，译为“水晶护符”；实际奖励 `AmuletOfCrystalMagicItem` 的物品显示名仍为“原始魔力护符”。


- 第12批：Runesmith's Foundry＝符文锻造坊 (Runesmith's Foundry)；Transmuter's Laboratory＝转化实验室 (Transmuter's Laboratory)，原文缩写为 Transmuter's Lab 时保留该拼写。Transmuter＝转化师；符文锻造师沿用既有单位译名。
- Talnes 暂译“塔尔尼斯”，Lord Azil 暂译“阿齐尔领主”；Sir Edward 沿用爱德华爵士。后续战役出现时复核并保持一致。
- 本批材料沿用物品表中的金锭、银锭、龙鳞、贝壳、红宝石、钻石与珍珠。品质装备使用“精制”，升级产物严格对应脚本物品，不将头盔误写成护甲。
- 转化实验室的“每日一次”是所有转化共用的次数，不是每种各一次。让塔尔尼斯留下的选项明确写“该英雄将永久离队”，不暗示可以随时召回。


- 第11批：Mephistopheles 暂译“梅菲斯托费勒”；Fiend 沿用“凶魔”，Demon Heart 沿用物品名“恶魔之心”，Demon Pact 沿用“恶魔契约”。
- Demon City＝恶魔城 (Demon City)，用于地图标签、地点叙述和招募提示。Underworld Conclave＝冥界秘会，是组织名称，沿用 Conclave＝秘会；区别于地名 Underworld＝冥界 (Underworld)。
- 契约选项原文“lose -1 base HP”按扣减含义译为“基础生命值永久减少1点”，不把双重负号解释成增加，也不改成一次性受伤。


- 第10批：Vladamir＝弗拉达米尔，Lady Willsama＝威尔萨玛夫人，Igor＝伊戈尔，均为本批暂定人名；后续战役出现时沿用并复核原文拼写，不将 Vladamir 自动改为 Vladimir。
- Dark Castle＝黑暗城堡 (Dark Castle)，用于地图标签及具名地点叙述。委托中的 Goblin／Dwarf／Knight 沿用地精／矮人／骑士；脚本按种族分组选择，不能将“矮人”窄化为“矮人战士”。
- 保留威尔萨玛夫人礼貌措辞中的黑色幽默；伊戈尔用短句和停顿表现迟缓语气，地精惊慌、矮人愤怒，不额外添加方言。


- 第9批：Darius' Love 作为地图地点标签译为“达里乌斯的爱情 (Darius' Love)”；Black Dragon 的地图标签为“黑龙 (Black Dragon)”，对话中的单位名称仍为“黑龙”。
- Ballad of the Swords 暂译《剑之歌》，为达里乌斯拟写的作品；Maiden 是角色标签，译为“姑娘”，不将图像资源文件名中的外貌描述加进姓名。保留达里乌斯夸张、抒情的语气以及救援结局的反讽。


- 第8批沿用 Djinn＝灯神、Beastmaster＝驯兽师、Tayah＝泰娅；indestructible 在灯神愿望与石化结局中均译为“坚不可摧”，保留字面实现愿望的反讽，不改成“无敌”。
- 灯神的 meta-wishing 指用愿望要求更多愿望，说明中译作“用愿望换取愿望”，手册暂译《灯神法则与追加许愿规则》。“神意与命运变更委员会”是虚构机构，不是地点。


- IKEUS FURNITURE＝伊凯乌斯家具 (IKEUS FURNITURE)：仓库招牌按地点／店铺名保留原文大写；店主姓名仍为伊凯乌斯。
- Blood Sisters＝鲜血姐妹；Windmill＝风车磨坊 (Windmill)（与共享地点的地图标签一致）；Oracle＝神谕者。
- 兵种沿用骸骨投石车、骸骨魔像、复生亡灵、特斯拉炮手、骷髅骑兵、瘟疫僵尸；名为 Warlock 的单位沿用“术士”，叙事中泛称 shaman 时译作“萨满”。

- Holy Council＝神圣议会；Elsa＝艾尔莎；Isabelle＝伊莎贝尔。第4批暂定译名，后续剧情沿用并复核。
- Three Devils＝三魔峰 (Three Devils)；Iceland＝冰原 (Iceland)，原文为 Icelands 时写作冰原 (Icelands)。依据本机森林、绿皮战役文本，前者是南方火山区域，后者是北方积雪地区；不是现实国家名称。
- Count Passionfruit＝多情的百香果伯爵：狼人取笑吸血鬼的绰号，兼顾水果名称与 passion 的感情双关；不是正式爵号。“bird”在同段指姑娘。
- 僧侣的拉丁文祷词按含义译为“我信全能的天父，天地的创造者……”。

- Prime Source＝原初之源：第3批中的不稳定魔法源头，暂定译名；区别于技能 Magic Source＝魔力源泉。
- Bartolome＝巴托洛梅：蛇杖传说中的圣者，暂定音译；Gnomish＝侏儒的，区别于矮人。
- Warg＝座狼；Will-o’-Wisp＝鬼火；Dryad＝林妖；Mana Shard＝魔力碎片；永久创伤沿用界面术语。

- Lexa＝莱克莎：爱情药剂事件中的女巫，暂定音译；后续剧情需继续沿用并复核。
- 矮人符文事件的 Runemaster 指单位 `dwarfrunemaster`，沿用“符文锻造师”；制作职业 Runemaster 仍为“符文大师”。
- 迷失幽灵选项原文称 Ancient Banshee，实际奖励为 `bansheeancient`，沿用单位显示名“高等报丧女妖”。
- Brute’s Brew＝蛮力药液；Bone Candle＝骨烛；Love Potion＝爱情药剂；Die Hard＝顽强不屈。事件叙述与正文名称保持一致。

- Darius＝达里乌斯；Tayah＝泰娅。用于吟游诗人与驯兽师互动，暂定音译，后续对话继续沿用。
- Lord of the Ales＝麦酒之王：喝酒比赛中的荣誉称号，不擅自解释为新增属性。
- Note＝提示：系统叙述的说话者标签，不把标签混入人物台词。
- 兽人的口吻粗豪直接，吟游诗人的表白夸张抒情，泰娅的回应简短强硬。

## 亡灵战役人物与地点

- Noea＝诺娅；Sir Gareth＝加雷思爵士。教堂批次暂定音译，后续沿用并复核。诺娅对克里尔用敬称“主人”，同时保留她对往事的调侃口吻。
- Haunted Church＝闹鬼教堂 (Haunted Church)；Ruins＝废墟 (Ruins)，沿用既有据点名。泛指普通废墟时不附英文地名。
- Holy Church 沿用圣教会；Banshee＝报丧女妖，Bone Dragon＝骨龙，Plague Zombie＝瘟疫僵尸；两项教堂奖励沿用混沌护符和寒霜胸针。
- 骨龙对话中的 brother 译作“兄弟”，不凭空指定长幼关系。
- Kingdom Patrol＝王国巡逻队 (Kingdom Patrol)，作为地图节点时保留英文；Orcs' Hills＝兽人丘陵 (Orcs' Hills)，保留原文所有格拼写。Shadowmarshes沿用暗影沼泽 (Shadowmarshes)，Mistmill沿用雾磨镇 (Mistmill)。
- Kingdom Patrol的奖励沿用灵魂之铃；Soldiers沿用士兵。Monk标签译作僧侣，克里尔台词中泛称Priest时用祭司；Wight沿用尸妖。
- “Over my dead body”保留“从我的尸体上踏过去”的说法，以承接幽灵没有身体的笑话；脚踝对话保留原文对往日礼俗的夸张羞耻感，不添加恋情细节。

## 后续术语整理

1. 回查已覆盖的单位、种族和场景名称，重点审核暂定译名和游戏中的显示长度；保持同族群、升级单位的命名一致。
2. 核对已整理的属性、抗性、免疫、技能、法术与临时状态；在后续效果说明中统一叠加、持续时间和触发条件的用语。
3. 复核物品、套装与制作材料命名；Shitanto／希坦刀、Pyradyne／派拉丁、Elowan／埃洛万及物品中的人物专名仍是暂定译法。
4. 回查既有译文；完成上述基线后，按 `docs/LOCALIZATION-PLAN.md` 推进说明与剧情文本。

同一含义的英文短标签保持相同中文译法；Slow 在速度选项中是“慢”，作为法术是“迟缓术”；Elemental 在种族／特性中是“元素生物”，在物品套装中是“元素”。这些是有上下文依据的区分。花瓶的旧标签“空花瓶”统一为“花瓶”。文本键 GHOST 显示 Incorporeal，译为“无实体”；文本键 INCORPOREAL 实际显示 Phasing，译为“相位化”，两者不可按内部标识混译。Grogan／格罗甘和 Mancubus／曼库魔采用暂定音译；该工作基线不代表逐项人工批准，也不证明界面排版正常。
