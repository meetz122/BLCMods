#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2018, CJ Kucera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

try:
    from hotfixes import Hotfixes
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink hotfixes.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

###
### Constants
###

mod_name = 'Luneshine on Uniques'
mod_version = '1.0.0'
input_filename = 'mod-input-file.txt'
output_filename = 'Luneshine on Uniques'

###
### Hotfix object to store all our hotfixes
###

hfs = Hotfixes()

# Adds Luneshine to some unique weapons which didn't have them,
# previously.  This too is autogenerated by `gen_guaranteed_luneshine.py`
# from my own TPS Better Loot mod, though I've since edited it slightly
# to handle the one launcher properly.
hfs.add_level_hotfix('luneshine_override_0',
    'LuneshineOverride',
    """,GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList,Accessory2PartData,,
    (
        bEnabled=True,
        WeightedParts=(
            (
                bDisabled=True,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_None',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_FastLearner',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_HardenUp',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Boominator',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Safeguard',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Oxygenator',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_PiercingRounds',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            ),
            (
                bDisabled=False,
                Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Serenity',
                Manufacturers=(
                    (
                        Manufacturer=None,
                        DefaultWeightIndex=1
                    )
                ),
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=1
            )
        )
    )""")

for idx, partlist in enumerate([
        'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_ZX1:PartList',
        'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_CyberColt:PartList',
        'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Old_Hyperion_BlackSnake:WeaponPartListCollectionDefinition_163',
        'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn:PartList',
        'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_TooScoops:PartList',
        'GD_Cypressure_Weapons.A_Weapons_Unique.AR_Bandit_3_BossNova:PartList',
        'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:WeaponPartListCollectionDefinition_282',
        'GD_Petunia_Weapons.SMGs.SMG_Tediore_3_Boxxy:PartList',
        'GD_Petunia_Weapons.Shotguns.SG_Tediore_3_PartyLine:PartList',
        'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett:WeaponPartListCollectionDefinition_283',
        ]):
    hfs.add_level_hotfix('luneshine_override_{}'.format(idx+1),
        'LuneshineOverride',
        """,{},Accessory2PartData,,
        (
            bEnabled=True,
            WeightedParts=(
                (
                    bDisabled=True,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_None',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_FastLearner',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_HardenUp',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Boominator',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Safeguard',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Oxygenator',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_PiercingRounds',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Punisher',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Serenity',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                )
            )
        )
        """.format(partlist))

# Now read in our main input file
with open(input_filename, 'r') as df:
    loot_str = df.read()

with open(output_filename, 'w') as df:
    df.write(loot_str.format(
        mod_name=mod_name,
        mod_version=mod_version,
        hotfixes=hfs,
        ))
print('Wrote mod file to: {}'.format(output_filename))
