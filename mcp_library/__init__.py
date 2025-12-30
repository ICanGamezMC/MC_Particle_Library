__version__ = "0.0.1"


from beet import Context
from beet.contrib.load import load


def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/mcp_library/modules": "@mcp_library/modules",
            },
        ),
    )
