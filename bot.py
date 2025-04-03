import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Lade die Umgebungsvariablen
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Funktion zur vollständigen Bereinigung und Synchronisierung der Befehle
async def sync_commands():
    try:
        # Globale Synchronisierung, um alle Befehle auf Discord zurückzusetzen
        await bot.tree.sync()
        print("Globale Synchronisierung durchgeführt. Alle Befehle wurden aktualisiert.")
    except Exception as e:
        print(f"Fehler bei der globalen Synchronisierung der Befehle: {e}")


# Lade alle Cogs (Befehle) im "commands" Ordner und gebe Feedback in der Konsole
@bot.event
async def on_ready():
    print("Lade alle Befehle...")
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")
                print(f"Befehl aus '{filename}' erfolgreich geladen.")
            except Exception as e:
                print(f"Fehler beim Laden von '{filename}': {e}")

    await sync_commands()
    print(f"Bot ist bereit und eingeloggt als {bot.user}.")

bot.run(TOKEN)


# Lade das Unban-Modul
from commands import unban
