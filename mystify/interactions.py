#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


from typing import Any

from mystify.modinfo import ModInfo
# from mystify.nothingness import TheVoid
from mystify.translucency_flags import TranslucencyFlags
from mystify.translucency_manager import TranslucencyManager

from sims.sim import Sim
from sims4.tuning.tunable import Tunable
from event_testing.results import TestResult
from interactions.context import InteractionContext

from sims4communitylib.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, 'main')
log.enable()


class InteractionsMystify(CommonImmediateSuperInteraction):
    INSTANCE_TUNABLES = {
        'opacity': Tunable(tunable_type=int, default=100),
        'reset': Tunable(tunable_type=int, default=0),
    }

    __slots__ = {'opacity', 'reset', }

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> TestResult:
        return TestResult.TRUE

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        log.debug(f"on_started({interaction_sim}, {type(interaction_target)}: {interaction_target} {interaction_target.id})")
        log.debug(f"opacity({self.opacity})")
        log.debug(f"reset({self.reset})")

        opacity = self.opacity / 100

        if self.reset == 0:
            TranslucencyManager.fade_to(interaction_target, opacity)
            if opacity < 1:
                pass
                # TheVoid.infect_object(interaction_target.id, CommonLocationUtils.get_current_zone_id(), CommonLocationUtils.get_current_lot())
        elif self.reset == TranslucencyFlags.reset_self:
            TranslucencyManager.reset_sim(interaction_sim)
        elif self.reset == TranslucencyFlags.reset_sims:
            TranslucencyManager.reset_all_sims()
        elif self.reset == TranslucencyFlags.reset_objects:
            TranslucencyManager.reset_all_objects()
        elif self.reset == TranslucencyFlags.reset_all:  # reset everything
            TranslucencyManager.reset_all_sims()
            TranslucencyManager.reset_all_objects()
        else:
            log.debug("no-match")
        return True
