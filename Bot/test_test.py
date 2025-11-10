import discord.ext.test as dpytest
import pytest
import pytest_asyncio


@pytest_asyncio.fixture
async def bot():
    from main import bot

    await bot._async_setup_hook()
    dpytest.configure(bot)

    yield bot

    await dpytest.empty_queue()


@pytest.mark.asyncio
async def test_basic(bot):
    message = await dpytest.message("Hello World!")
    assert message.content == "Hello World!"
