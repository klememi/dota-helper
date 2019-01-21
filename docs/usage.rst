.. _usage:

Usage
=====

	dotacli [OPTIONS] COMMAND [ARGS]


Options
^^^^^^^
-c, --config PATH	Path for the configuration file. Default: **~/.dotacli**
-i, --id TEXT		Your personal account ID.
--help				Prints help informations.
--version			Prints version information.


Commands
^^^^^^^^
favourite
~~~~~~~~~
Manage favourite players.

Options
#######
-a, --add TEXT		Add player ID to favourites.
-r, --remove TEXT	Remove player ID from favourites.


heroes
~~~~~~
Show information about heroes.

Options
#######
-n, --name TEXT		Specifies hero by name.
-b, --best			Show best player with specified hero.
-m, --meta			Show heroes currently in meta.
-c, --counter		Show heroes which counters specified hero.

Heroes names
############
To specify hero by name use one of these names (or substring): Anti-Mage, Axe, Bane, Bloodseeker, Crystal Maiden, Drow Ranger, Earthshaker, Juggernaut, Mirana, Morphling, Shadow Fiend, Phantom Lancer, Puck, Pudge, Razor, Sand King, Storm Spirit, Sven, Tiny, Vengeful Spirit, Windranger, Zeus, Kunkka, Lina, Lion, Shadow Shaman, Slardar, Tidehunter, Witch Doctor, Lich, Riki, Enigma, Tinker, Sniper, Necrophos, Warlock, Beastmaster, Queen of Pain, Venomancer, Faceless Void, Wraith King, Death Prophet, Phantom Assassin, Pugna, Templar Assassin, Viper, Luna, Dragon Knight, Dazzle, Clockwerk, Leshrac, Natures Prophet, Lifestealer, Dark Seer, Clinkz, Omniknight, Enchantress, Huskar, Night Stalker, Broodmother, Bounty Hunter, Weaver, Jakiro, Batrider, Chen, Spectre, Ancient Apparition, Doom, Ursa, Spirit Breaker, Gyrocopter, Alchemist, Invoker, Silencer, Outworld Devourer, Lycan, Brewmaster, Shadow Demon, Lone Druid, Chaos Knight, Meepo, Treant Protector, Ogre Magi, Undying, Rubick, Disruptor, Nyx Assassin, Naga Siren, Keeper of the Light, Io, Visage, Slark, Medusa, Troll Warlord, Centaur Warrunner, Magnus, Timbersaw, Bristleback, Tusk, Skywrath Mage, Abaddon, Elder Titan, Legion Commander, Techies, Ember Spirit, Earth Spirit, Underlord, Terrorblade, Phoenix, Oracle, Winter Wyvern, Arc Warden, Monkey King, Dark Willow, Pangolier, Grimstroke


matches
~~~~~~~
Show information about matches.

Options
#######
-t, --team TEXT		Filter matches by team. You can specify up to 2 teams.
-l, --league TEXT	Filter matches by league.
-i, --id TEXT		Show exact match details.
-l, --live          Show live matches information.


mmr
~~~
Show information about MMR distribution.

Options
#######
-r, --ranks			Show players distribution by ranks.
-c, --country TEXT	Show average MMR of specified country. For countries use standard 2-letters
					abbreviations.


players
~~~~~~~
Show player's information.

Options
#######
-f, --favourite 	Show favourite players informations.
-c, --country TEXT	Show players from specified country.
-t, --team TEXT		Show players filtered by team name.
-n, --name TEXT		Show players filtered by name.
-i, --id TEXT		Show specific player informations.
-m, --me 			Show your personal information.
