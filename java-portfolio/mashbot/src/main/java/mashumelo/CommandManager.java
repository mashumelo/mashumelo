package mashumelo;

import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.entities.Role;
import net.dv8tion.jda.api.entities.channel.Channel;
import net.dv8tion.jda.api.entities.channel.middleman.MessageChannel;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.MessageEmbed;
import java.awt.Color;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.events.guild.GuildReadyEvent;
import net.dv8tion.jda.api.interactions.commands.OptionMapping;
import net.dv8tion.jda.api.interactions.commands.OptionType;
import net.dv8tion.jda.api.interactions.commands.build.CommandData;
import net.dv8tion.jda.api.interactions.commands.build.Commands;
import net.dv8tion.jda.api.interactions.commands.build.OptionData;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.JSONArray;
import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.List;

public class CommandManager extends ListenerAdapter {

    public String getRandomCatImageUrl() {
    String catImageUrl = "";

    try {

        HttpClient httpClient = HttpClientBuilder.create().build();

        HttpGet request = new HttpGet("https://api.thecatapi.com/v1/images/search");

        HttpResponse response = httpClient.execute(request);

        String responseBody = EntityUtils.toString(response.getEntity());

        JSONArray jsonArray = (JSONArray) JSONValue.parse(responseBody);
        JSONObject jsonObject = (JSONObject) jsonArray.get(0);

        catImageUrl = (String) jsonObject.get("url");
    } catch (Exception e) {
        e.printStackTrace();
    }

    return catImageUrl;
}

    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        String command = event.getName();
        String userTag = event.getUser().getAsMention();

        if (command.equals("help")) {
            event.deferReply().setEphemeral(true).queue();
    
            EmbedBuilder embedBuilder = new EmbedBuilder();
            embedBuilder.setTitle("List of commands");
            embedBuilder.setDescription("/roles - Lists all roles in the guild\n/say - Sends a message to a channel\n/d20 - Rolls a d20\n/diceroll - Rolls a dice\n/cat - Gets a random cat image");
            embedBuilder.setColor(Color.BLUE);
    
            MessageEmbed embed = embedBuilder.build();
            event.getHook().sendMessageEmbeds(embed).queue();
        }

        else if (command.equals("roles")) {
            event.deferReply().setEphemeral(true).queue();
            String response = "";
            for (Role role : event.getGuild().getRoles()) {
                response += role.getAsMention() + "\n";  //@Role Names
            }
            event.getHook().sendMessage(response).queue();
        }

        else if (command.equals("say")) {
            OptionMapping messageOption = event.getOption("message");
            String message = messageOption.getAsString();

            MessageChannel channel;
            OptionMapping channelOption = event.getOption("channel");
            if (channelOption != null) {
                Channel guildChannel = channelOption.getAsChannel();
                if (guildChannel instanceof MessageChannel) {
                    channel = (MessageChannel) guildChannel;
                } else {
                    channel = event.getChannel();
                }

            } else {
                channel = event.getChannel();
            }

            EmbedBuilder embedBuilder = new EmbedBuilder();
            embedBuilder.setDescription (message);
            embedBuilder.setColor (Color.GREEN);

            MessageEmbed embed = embedBuilder.build();
            channel.sendMessageEmbeds (embed).queue();
            
            event.reply(userTag + "Your message was sent!").setEphemeral(true).queue();
            }

        else if (command.equals("d20")) {
            event.deferReply().setEphemeral(false).queue();

            EmbedBuilder embed = new EmbedBuilder();
            embed.setColor(Color.GREEN);
            embed.setTitle("d20 roll");
            embed.setDescription(userTag + " rolled a " + (int)(Math.random() * 20 + 1));

            event.getHook().sendMessageEmbeds(embed.build()).queue();
        }

        else if (command.equals("diceroll")) {
            event.deferReply().setEphemeral(false).queue();

            EmbedBuilder embed = new EmbedBuilder();
            embed.setColor (Color.GREEN);
            embed.setTitle ("Dice Roll");
            embed.setDescription (userTag + " rolled a " + (int)(Math.random() * 6 + 1));

            event.getHook().sendMessageEmbeds(embed.build()).queue();

        }

        else if (command.equals ("cat")) {
            String catImageUrl = getRandomCatImageUrl();

            EmbedBuilder embed = new EmbedBuilder();
            embed.setColor (Color.GREEN);
            embed.setTitle ("Cat");
            embed.setImage (catImageUrl);

            MessageChannel channel = event.getChannel();

            channel.sendMessageEmbeds(embed.build()).queue();
        }
    }


    @Override
    public void onGuildReady(@NotNull GuildReadyEvent event) {
        
        List<CommandData> commandData = new ArrayList<>();
        commandData.add(Commands.slash("roles", "Display the roles available in the server."));

        OptionData option1 = new OptionData(OptionType.STRING, "message" , "The message to send.", true);
        OptionData option2 = new OptionData(OptionType.CHANNEL,"channel", "The channel to send the message to.", false);
        commandData.add(Commands.slash("say", "Says the text from input.").addOptions(option1, option2));

        commandData.add(Commands.slash("d20", "Rolls a d20."));
        commandData.add(Commands.slash("diceroll", "Rolls a dice."));
        commandData.add(Commands.slash("cat", "Sends a random cat image."));

        event.getGuild().updateCommands().addCommands(commandData).queue();
    }
    
}

