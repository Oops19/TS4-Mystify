from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    """ Mod info for the S4.CL Sample Mod. """
    # To create a Mod Identity for this mod, simply do ModInfo.get_identity(). Please refrain from using the ModInfo of The Sims 4 Community Library in your own mod and instead use yours!
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        # This is the name that'll be used whenever a Messages.txt or Exceptions.txt file is created <_name>_Messages.txt and <_name>_Exceptions.txt.
        return 'Mystify'

    @property
    def _author(self) -> str:
        # This is your name.
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        # This is the name of the root package
        return 'mystify'

    @property
    def _file_path(self) -> str:
        # This is simply a file path that you do not need to change.
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '1.2.3'

'''
v1.2.3
    Updated README for new TS4 version
v1.2.2
    Updated README for new TS4 version
v1.2.1
    Updated compile script and docs for current TS4 version
v1.2.0
    Inject into TS4 instead of S4.CL reset method.
'''