#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


import time

from objects.base_object import BaseObject
from objects.client_object_mixin import ClientObjectMixin
from objects.object_enums import ResetReason
from mystify.modinfo import ModInfo

from mystify.timer_store import TimerStore
from mystify.translucency_store import TranslucencyStore
from sims.sim import Sim

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, 'TranslucencyManager')
log.enable()


class TranslucencyManager:
    def __init__(self):
        pass

    @staticmethod
    def fade_to(obj, opacity):
        if isinstance(obj, Sim):
            TranslucencyStore.sims.update({obj: opacity})
            TimerStore.sims.update({obj: time.time()})
            obj.fade_out()
            if opacity == 1:
                del TranslucencyStore.sims[obj]
        else:
            TranslucencyStore.objects.update({obj: opacity})
            TimerStore.objects.update({obj: time.time()})
            obj.fade_out()
            if opacity == 1:
                del TranslucencyStore.objects[obj]

    @staticmethod
    def get_opacity(obj):
        opacity = 1
        if isinstance(obj, Sim):
            opacity = TranslucencyStore.sims.get(obj, 1)
        else:
            opacity = TranslucencyStore.objects.get(obj, 1)
        return opacity

    @staticmethod
    def reset_sim(sim):
        try:
            TranslucencyStore.sims.update({sim: 1})
            sim.fade_out()
            del TranslucencyStore.sims[sim]
            del TimerStore.sims[sim]
        except:
            try:
                del TranslucencyStore.sims[sim]
                del TimerStore.sims[sim]
            except:
                pass

    @staticmethod
    def reset_all_sims():
        sims = set(TranslucencyStore.sims.keys())
        for sim in sims:
            try:
                TranslucencyStore.sims.update({sim: 1})
                sim.fade_out()
                del TranslucencyStore.sims[sim]
                del TimerStore.sims[sim]
            except:
                try:
                    del TranslucencyStore.sims[sim]
                    del TimerStore.sims[sim]
                except:
                    pass

    @staticmethod
    def reset_all_objects():
        objects = set(TranslucencyStore.objects.keys())
        for obj in objects:
            try:
                TranslucencyStore.objects.update({obj: 1})
                # obj.opacity = self.opacity
                obj.fade_out()
                del TranslucencyStore.objects[obj]
                del TimerStore.objects[obj]
            except:
                try:
                    del TranslucencyStore.sims[object]
                    del TimerStore.objects[obj]
                except:
                    pass


# def fade_opacity(self, opacity:float, duration:float, immediate=False, additional_channels=None):
@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), ClientObjectMixin, ClientObjectMixin.fade_opacity.__name__)
def o19_fade_opacity(original, self, opacity: float, duration: float, *args, **kwargs):
    if self in TranslucencyStore.sims:
        opacity = TranslucencyStore.sims.get(self, opacity)
        log.debug(f"Fading '{self}' to {opacity}")
        duration = 2
    elif self in TranslucencyStore.objects:
        opacity = TranslucencyStore.objects.get(self, opacity)
        log.debug(f"Fading '{self}' to {opacity}")
        duration = 3
    original(self, opacity, duration, *args, **kwargs)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), BaseObject, BaseObject.reset.__name__)
def o19_opacity_hard_reset(original, self, reset_reason: ResetReason = ResetReason.RESET_EXPECTED, source=None, cause=None, *args, **kwargs):
    log.debug(f'o19_opacity_hard_reset({self}, {reset_reason}, {source}, {cause})')
    rv = original(self, reset_reason, source, cause, *args, **kwargs)
    try:
        sim: Sim = CommonSimUtils.get_sim_instance(self)
        if sim:
            sim.fade_in()
    except Exception as e:
        log.debug(f"Oops: '{e}'")
    return rv
