.. _examples:

Examples
========

Matches
#######

List pro matches details
------------------------
.. code-block:: none

	$ dotacli matches --league 'Major'

	-> The Chongqing Major
	ID: 4350358576, duration: 39:18
	Vici Gaming           24
	PSG.LGD               20 WON

	-> The Chongqing Major
	ID: 4350242887, duration: 20:24
	PSG.LGD               18 WON
	Vici Gaming            3

	-> The Chongqing Major
	ID: 4350011381, duration: 40:37
	Virtus.pro            27 WON
	Evil Geniuses         31

List public matches details
---------------------------
.. code-block:: none

	$ dotacli matches --id '4350105687'

	Antree                     2 /  9 / 11  networth:  7671
	  Pudge                  LVL 15   GPM 246   XPM 325
	SG                         4 /  8 /  8  networth:  6985
	  Undying                LVL 11   GPM 224   XPM 202
	Sokoban                    9 /  7 /  1  networth: 16090
	  Shadow Fiend           LVL 22   GPM 516   XPM 647
	Curban                     3 /  8 / 13  networth: 10321
	  Venomancer             LVL 15   GPM 331   XPM 362
	Unknown                    4 /  5 /  1  networth: 14157
	  Anti-Mage              LVL 19   GPM 454   XPM 502

	Radiant                          22
	Dire                             35   WON

	Element                    2 /  5 / 19  networth:  9822
	  Dazzle                 LVL 16   GPM 315   XPM 384
	goššky fanboy              4 /  3 / 11  networth: 20050
	  Terrorblade            LVL 23   GPM 643   XPM 716
	Unknown                   13 /  2 /  9  networth: 19302
	  Pangolier              LVL 21   GPM 619   XPM 601
	zouson                     3 /  7 / 14  networth:  9479
	  Lich                   LVL 17   GPM 304   XPM 422
	Unknown                   13 /  5 /  5  networth: 16246
	  Clinkz                 LVL 21   GPM 521   XPM 590


List top currently ongoing live games
-------------------------------------
.. code-block:: none

	$ dotacli matches --live

	-> 4351189332, Time: 35:11 (avg: 6831 MMR) Radiant 23 - 42 Dire
	    Liquid.Miracle- (Juggernaut)
	    Espada.633 (Tidehunter)
	-> 4351108530, Time: 32:02 (avg:    0 MMR) Radiant 21 - 26 Dire
	    BOOM.Fervian (Medusa)
	    BOOM.Khezcute (Crystal Maiden)
	    ThePrime.Varizh (Grimstroke)
	    BOOM.Fbz (Timbersaw)
	    ThePrime.KelThuzard (Luna)
	    ThePrime.Nafari (Doom)
	    ThePrime.Panda (Sven)
	    Tigers.k`wonderkid (Shadow Fiend)
	    BOOM.Jhocam (Tusk)
	    BOOM._Mikoto (Queen of Pain)

Players
#######

List pro players details
------------------------
.. code-block:: none

	$ dotacli players --id '26771994'

	JerAx, FI
	Unknown (8147 MMR)
	Win: 1670  Loss: 979
	Prefers: Radiant
	Avg KDA: 3.4
	Courier kills: 52
	# RECENT MATCHES
	4329424310  Very High Skill  Captains Mode           Chen                   1/ 5/ 7  LOST
	4329276408  Very High Skill  Captains Mode           Oracle                 2/ 3/ 2  LOST
	4329131044  Very High Skill  Captains Mode           Earth Spirit           8/ 2/13  LOST
	4326910684  Very High Skill  Captains Mode           Earth Spirit           0/ 9/ 3  LOST
	4326819878  Very High Skill  Captains Mode           Grimstroke             0/ 4/ 3  LOST
	# BEST HEROES
	Elder Titan           Games:   47  Won:  80.9 %
	Earth Spirit          Games:  352  Won:  75.9 %
	Io                    Games:   34  Won:  73.5 %
	# SCARIEST HEROES
	Earth Spirit          Against:  103  Lost:  48.5 %
	Lycan                 Against:   70  Lost:  47.1 %
	Io                    Against:  136  Lost:  47.1 %
	# BEST FRIENDS
	You can't buy culture          (18180970)  Games:   38  Win:  84.2 %
	3&D vetmin role player         (75750590)  Games:   38  Win:  78.9 %
	MMMMMMMMMMMMMM                 (98172857)  Games:   42  Win:  78.6 %

Watch your favourite players stats
----------------------------------
.. code-block:: none

	$ dotacli players --favourite

	Ceb, UNKNOWN
	Immortals (6747 MMR)
	Win: 7061  Loss: 6381
	Prefers: Radiant
	Avg KDA: 3.7
	Courier kills: 395
	# RECENT MATCHES
	4350346356  Very High Skill  All Draft               Lycan                  4/ 1/ 7  WON
	4350253660  Very High Skill  All Draft               Pugna                 11/ 8/15  LOST
	4349260888  Very High Skill  All Draft               Enigma                 5/ 8/15  LOST
	4348843344  Very High Skill  All Draft               Phoenix                9/ 7/20  LOST
	4348771379  Very High Skill  All Draft               Doom                   6/ 4/ 9  WON
	# BEST HEROES
	Chaos Knight          Games:   65  Won:  67.7 %
	Wraith King           Games:   38  Won:  65.8 %
	Night Stalker         Games:  103  Won:  65.0 %
	# SCARIEST HEROES
	Lycan                 Against:  249  Lost:  59.8 %
	Io                    Against:  647  Lost:  55.3 %
	Omniknight            Against:  543  Lost:  54.5 %
	# BEST FRIENDS
	eN                             (110194593)  Games:   69  Win:  65.2 %
	Ace                            (97590558)  Games:   73  Win:  63.0 %
	Maden                          (93473848)  Games:  116  Win:  62.1 %
	--------------------------------------------------------------------------------
	N0tail, DK
	Unknown (8155 MMR)
	Win: 1139  Loss: 697
	Prefers: Radiant
	Avg KDA: 3.4
	Courier kills: 51
	# RECENT MATCHES
	4329424310  Very High Skill  Captains Mode           Lich                   0/ 5/ 7  LOST
	4329276408  Very High Skill  Captains Mode           Io                     2/ 6/ 5  LOST
	4329131044  Very High Skill  Captains Mode           Undying                3/ 7/13  LOST
	4326910684  Very High Skill  Captains Mode           Witch Doctor           0/11/ 3  LOST
	4326819878  Very High Skill  Captains Mode           Dazzle                 1/ 8/ 2  LOST
	# BEST HEROES
	Elder Titan           Games:   33  Won:  81.8 %
	Terrorblade           Games:   35  Won:  77.1 %
	Beastmaster           Games:   32  Won:  75.0 %
	# SCARIEST HEROES
	Chen                  Against:  104  Lost:  54.8 %
	Centaur Warrunner     Against:   52  Lost:  51.9 %
	Io                    Against:   92  Lost:  51.1 %
	# BEST FRIENDS
	MMMMMMMMMMMMMM                 (98172857)  Games:   35  Win:  88.6 %
	qwerty                         (169181898)  Games:   46  Win:  82.6 %
	11                             (89550641)  Games:   38  Win:  81.6 %
	--------------------------------------------------------------------------------

MMR
###

Show distribution of MMR data by bracket
----------------------------------------
.. code-block:: none

	$ dotacli mmr --ranks

	Current Dota 2 players distribution by ranks
	###############################################################################
	                                                              145  Herald I
	                                                              927  Herald II
	█                                                            3313  Herald III
	███                                                         10074  Herald IV
	██████                                                      20193  Herald V
	█████████                                                   30766  Guardian I
	████████████                                                39528  Guardian II
	██████████████                                              47959  Guardian III
	█████████████████                                           56779  Guardian IV
	████████████████████                                        66406  Guardian V
	████████████████████████                                    78816  Crusader I
	███████████████████████████                                 90930  Crusader II
	███████████████████████████████                            103010  Crusader III
	███████████████████████████████████                        114487  Crusader IV
	██████████████████████████████████████                     126098  Crusader V
	███████████████████████████████████████████                143170  Archon I
	██████████████████████████████████████████████             153390  Archon II
	█████████████████████████████████████████████████          163167  Archon III
	████████████████████████████████████████████████████       170338  Archon IV
	█████████████████████████████████████████████████████      173273  Archon V
	█████████████████████████████████████████████████████████  186291  Legend I
	███████████████████████████████████████████████████████    182988  Legend II
	██████████████████████████████████████████████████████     177140  Legend III
	██████████████████████████████████████████████████         166001  Legend IV
	████████████████████████████████████████████               145606  Legend V
	█████████████████████████████████████████                  136735  Ancient I
	██████████████████████████████████                         113232  Ancient II
	███████████████████████████                                 89326  Ancient III
	█████████████████████                                       70591  Ancient IV
	█████████████████████████████                               94954  Ancient V
	███████████                                                 36156  Divine I
	████████                                                    26179  Divine II
	██████                                                      20914  Divine III
	████                                                        14861  Divine IV
	███                                                         10755  Divine V
	█████████                                                   31944  Immortals

Show distribution of MMR data by country
----------------------------------------
.. code-block:: none

	$ dotacli mmr --country 'CZ'

	Czechia                                            -> avg MMR: 3107, players:   4750

Heroes
######

Show top players by hero
------------------------
.. code-block:: none

	$ dotacli heroes --name 'Rubick' --best

	 1 S.g.b                          ID: 149071227  (Immortals)
	 2 y`                             ID: 111114687  (Immortals)
	 3 Fade                           ID: 182331313  (Immortals)
	 4 lucky guy                      ID: 76104605   (Immortals)
	 5 iNSaNia                        ID: 54580962   (Immortals)
	 6 C.C                            ID: 156120474  (Immortals)
	 7 SeeL                           ID: 207983361  (Immortals)
	 8 想念Wings的第683天               ID: 254489464  (Immortals)
	 9 D1330XD                        ID: 149969795  (Immortals)
	10 Проклятый бабкой               ID: 394335293  (Immortals)

Show heroes details
-------------------
.. code-block:: none

	$ dotacli heroes --name 'Shadow'

	Shadow Fiend        Ranged Agility        roles: Carry, Nuker
	Shadow Shaman       Ranged Intelligence   roles: Support, Pusher, Disabler, Nuker, Initiator
	Shadow Demon        Ranged Intelligence   roles: Support, Disabler, Initiator, Nuker

Show heroes in meta
-------------------
.. code-block:: none

	$ dotacli heroes --meta

	Tusk                picked: 268  banned: 335  winrate: 46.6 %
	Beastmaster         picked: 151  banned: 434  winrate: 58.9 %
	Dazzle              picked: 215  banned: 367  winrate: 49.8 %
	Grimstroke          picked: 264  banned: 315  winrate: 46.6 %
	Lich                picked: 332  banned: 241  winrate: 52.4 %
	Outworld Devourer   picked: 164  banned: 328  winrate: 52.4 %
	Magnus              picked: 124  banned: 360  winrate: 55.6 %
	Tiny                picked: 252  banned: 231  winrate: 56.3 %
	Anti-Mage           picked: 144  banned: 320  winrate: 53.5 %
	Juggernaut          picked: 216  banned: 234  winrate: 52.8 %
	Undying             picked: 146  banned: 273  winrate: 53.4 %
	Kunkka              picked: 194  banned: 211  winrate: 51.5 %

Find counter heroes
-------------------
.. code-block:: none

	$ dotacli heroes --name 'Anti-Mage' --counter

	Lifestealer         winrate: 25.0 %
	Beastmaster         winrate: 26.3 %
	Oracle              winrate: 28.6 %
	Lycan               winrate: 28.6 %
	Magnus              winrate: 35.3 %
	Bane                winrate: 37.5 %
	Disruptor           winrate: 40.9 %
	Slardar             winrate: 41.0 %
	Weaver              winrate: 41.2 %
	Razor               winrate: 41.7 %
	Chen                winrate: 41.7 %
	Clockwerk           winrate: 41.7 %

Personal
########

Show your personal stats
------------------------
.. code-block:: none

	$ dotacli players --me

	Element, CZ
	Ancient III (3843 MMR)
	Win: 1906  Loss: 1683
	Prefers: Radiant
	Avg KDA: 2.8
	Courier kills: 62
	# RECENT MATCHES
	4351250923  Very High Skill  All Draft               Lich                   6/ 8/20  LOST
	4351140237  High Skill       All Draft               Huskar                 3/12/ 4  LOST
	4350749013  High Skill       All Draft               Drow Ranger            0/11/ 3  LOST
	4350196013  Very High Skill  All Draft               Jakiro                 4/10/11  WON
	4350105687  Very High Skill  All Draft               Dazzle                 2/ 5/19  LOST
	# BEST HEROES
	Chaos Knight          Games:   41  Won:  75.6 %
	Dazzle                Games:   34  Won:  73.5 %
	Sniper                Games:   50  Won:  72.0 %
	# SCARIEST HEROES
	Chaos Knight          Against:  126  Lost:  62.7 %
	Zeus                  Against:  197  Lost:  60.9 %
	Riki                  Against:  239  Lost:  55.6 %
	# BEST FRIENDS
	VYHLASENA_KALAMITA666(forget)  (488180047)  Games:  151  Win:  60.3 %
	Mr.Sunstrike                   (372183905)  Games:  211  Win:  59.2 %
	MAČKOPES                       (381341959)  Games:  129  Win:  58.1 %

Show your best heroes
---------------------
.. code-block:: none

	$ dotacli heroes --best

	Chaos Knight          Games:   41  Won:  75.6 %
	Dazzle                Games:   34  Won:  73.5 %
	Sniper                Games:   50  Won:  72.0 %

Find counter heroes based on your stats
---------------------------------------
.. code-block:: none

	$ dotacli heroes --name 'Anti-Mage' --counter

	Lifestealer         winrate: 25.0 %
	Magnus              winrate: 35.3 %
	Bane                winrate: 37.5 %
	Slardar             winrate: 41.0 %
	Weaver              winrate: 41.2 %
	Razor               winrate: 41.7 %
	Clockwerk           winrate: 41.7 %
	Timbersaw           winrate: 44.4 %
	Drow Ranger         winrate: 44.4 %
	Juggernaut          winrate: 45.1 %
	Vengeful Spirit     winrate: 45.5 %
	Dark Seer           winrate: 45.8 %
