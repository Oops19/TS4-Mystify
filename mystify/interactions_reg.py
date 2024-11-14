#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


from typing import Tuple

from objects.script_object import ScriptObject
from sims4communitylib.enums.affordance_list_ids import CommonAffordanceListId
from sims4communitylib.enums.enumtypes.common_int import CommonInt
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.services.resources.common_instance_manager_modification_registry import CommonInstanceManagerModificationRegistry
from sims4communitylib.services.resources.modification_handlers.common_add_interactions_to_affordance_lists_handler import CommonAddInteractionsToAffordanceListsModificationHandler


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _RegisterInteractionsMystify_Mystify_0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0xDB8D07E4C8EDC9B7,  # 'Show' - fnv('o19_Mystify_PMC__Mystify_PMA_Show_debug')
            0xF01D0FF253D0DE9E,  # '80 %' - fnv('o19_Mystify_PMC__Mystify_PMA_80_x25_debug')
            0x89438988756AD03C,  # '60 %' - fnv('o19_Mystify_PMC__Mystify_PMA_60_x25_debug')
            0x4F4850F1DA029C4A,  # '40 %' - fnv('o19_Mystify_PMC__Mystify_PMA_40_x25_debug')
            0xA489761B8F4A48E6,  # '90 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_90_x25_debug')
            0xDE59428862E53F54,  # '70 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_70_x25_debug')
            0x9BC634B2C9F2A4E2,  # '50 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_50_x25_debug')
            0x87A944FF2B81D040,  # '30 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_30_x25_debug')
            0xE0BA3125DD31F194,  # '20 %' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_20_x25_debug')
            0x6DADD9CDC87A5F3D,  # '10 %' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_10_x25_debug')
            0x38942BE2CBE4155C,  # 'Hide' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_Hide_debug')
            0x2FA5029D50304F66,  # 'All' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_All_debug')
            0x49FE58161BCD359B,  # 'Self' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Self_debug')
            0xBF86BD79750AB811,  # 'Sims' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Sims_debug')
            0x8A13B5E860B7F83F,  # 'Objects' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Objects_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True


@CommonInstanceManagerModificationRegistry.register_modification_handler()
class _RegisterInteractionsMystify_Mystify_0_Debug(CommonAddInteractionsToAffordanceListsModificationHandler):
    @property
    def interaction_ids(self) -> Tuple[CommonInt, ...]:
        interactions: Tuple = (
            0xDB8D07E4C8EDC9B7,  # 'Show' - fnv('o19_Mystify_PMC__Mystify_PMA_Show_debug')
            0xF01D0FF253D0DE9E,  # '80 %' - fnv('o19_Mystify_PMC__Mystify_PMA_80_x25_debug')
            0x89438988756AD03C,  # '60 %' - fnv('o19_Mystify_PMC__Mystify_PMA_60_x25_debug')
            0x4F4850F1DA029C4A,  # '40 %' - fnv('o19_Mystify_PMC__Mystify_PMA_40_x25_debug')
            0xA489761B8F4A48E6,  # '90 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_90_x25_debug')
            0xDE59428862E53F54,  # '70 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_70_x25_debug')
            0x9BC634B2C9F2A4E2,  # '50 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_50_x25_debug')
            0x87A944FF2B81D040,  # '30 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_30_x25_debug')
            0xE0BA3125DD31F194,  # '20 %' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_20_x25_debug')
            0x6DADD9CDC87A5F3D,  # '10 %' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_10_x25_debug')
            0x38942BE2CBE4155C,  # 'Hide' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_Hide_debug')
            0x2FA5029D50304F66,  # 'All' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_All_debug')
            0x49FE58161BCD359B,  # 'Self' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Self_debug')
            0xBF86BD79750AB811,  # 'Sims' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Sims_debug')
            0x8A13B5E860B7F83F,  # 'Objects' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Objects_debug')
        )
        return interactions

    @property
    def affordance_list_ids(self) -> Tuple[int, ...]:
        result: Tuple[int, ...] = (
            CommonAffordanceListId.DEBUG_AFFORDANCES,
        )
        return result


class _RegisterInteractionsMystify_Mystify_0_DD:
    def __init__(self):
        try:
            import deviousdesires
            from deviousdesires.sex._injects._block_interactions_during_animation import DDInteractionBlocker
            ids = list(self.interaction_ids)
            deviousdesires.sex._injects._block_interactions_during_animation.DDInteractionBlocker().add_allowed_interaction_ids(ids)
        except Exception as e:
            pass

    @property
    def interaction_ids(self) -> Tuple[int, ...]:
        interactions: Tuple = (
            0xDB8D07E4C8EDC9B7,  # 'Show' - fnv('o19_Mystify_PMC__Mystify_PMA_Show_debug')
            0xF01D0FF253D0DE9E,  # '80 %' - fnv('o19_Mystify_PMC__Mystify_PMA_80_x25_debug')
            0x89438988756AD03C,  # '60 %' - fnv('o19_Mystify_PMC__Mystify_PMA_60_x25_debug')
            0x4F4850F1DA029C4A,  # '40 %' - fnv('o19_Mystify_PMC__Mystify_PMA_40_x25_debug')
            0xA489761B8F4A48E6,  # '90 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_90_x25_debug')
            0xDE59428862E53F54,  # '70 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_70_x25_debug')
            0x9BC634B2C9F2A4E2,  # '50 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_50_x25_debug')
            0x87A944FF2B81D040,  # '30 %' - fnv('o19_Mystify_PMC__Mystify__More_PMA_30_x25_debug')
            0xE0BA3125DD31F194,  # '20 %' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_20_x25_debug')
            0x6DADD9CDC87A5F3D,  # '10 %' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_10_x25_debug')
            0x38942BE2CBE4155C,  # 'Hide' - fnv('o19_Mystify_PMC__Mystify__Risky_PMA_Hide_debug')
            0x2FA5029D50304F66,  # 'All' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_All_debug')
            0x49FE58161BCD359B,  # 'Self' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Self_debug')
            0xBF86BD79750AB811,  # 'Sims' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Sims_debug')
            0x8A13B5E860B7F83F,  # 'Objects' - fnv('o19_Mystify_PMC__Mystify__Reset_PMA_Objects_debug')
        )
        return interactions


_RegisterInteractionsMystify_Mystify_0_DD()
