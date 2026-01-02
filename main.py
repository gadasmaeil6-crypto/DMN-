import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# --- ضع البيانات الخاصة بك هنا ---
ROLE_ID = 1454150613372899461  # ID الرتبة التي سيأخذها العضو
VERIFY_CHANNEL_ID = 1456612643719745596 # ID روم التوثيق

@bot.event
async def on_ready():
    print(f'✅ بوت التوثيق {bot.user} متصل وجاهز!')

# إنشاء شكل الزر وتفاعله
class VerifyView(View):
    def __init__(self):
        super().__init__(timeout=None) # الزر لا يتوقف عن العمل أبداً

    @discord.ui.button(label="توثيق الحساب ✅", style=discord.ButtonStyle.green, custom_id="verify_btn")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(ROLE_ID)
        
        if role in interaction.user.roles:
            await interaction.response.send_message("أنت موثق بالفعل! 😎", ephemeral=True)
        else:
            try:
                await interaction.user.add_roles(role)
                await interaction.response.send_message("تم توثيقك بنجاح! 🎉 استمتع بالسيرفر.", ephemeral=True)
            except:
                await interaction.response.send_message("❌ خطأ: تأكد أن رتبة البوت أعلى من رتبة العضو!", ephemeral=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    if ctx.channel.id != VERIFY_CHANNEL_ID:
        return await ctx.send("⚠️ هذا الأمر يُستخدم في روم التوثيق فقط!")
    
    embed = discord.Embed(
        title="🛡️ نظام حماية السيرفر",
        description="للوصول إلى كامل السيرفر، يرجى الضغط على الزر أدناه.",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed, view=VerifyView())

bot.run('MTQ1NjQyOTAxNzA5ODg3OTA1OQ.GttWTL.Zg_hiVc3-Ez617IzRWwKpevYUHA_Zg_QJP3S34')
