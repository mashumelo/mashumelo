package mashumelo;

import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.entities.Role;
import net.dv8tion.jda.api.entities.channel.Channel;
import net.dv8tion.jda.api.entities.channel.middleman.MessageChannel;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.events.guild.GuildReadyEvent;
import net.dv8tion.jda.api.interactions.commands.OptionMapping;
import net.dv8tion.jda.api.interactions.commands.OptionType;
import net.dv8tion.jda.api.interactions.commands.build.CommandData;
import net.dv8tion.jda.api.interactions.commands.build.Commands;
import net.dv8tion.jda.api.interactions.commands.build.OptionData;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.List;

public class CommandManager extends ListenerAdapter {

    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        String command = event.getName();
        String userTag = event.getUser().getAsMention();

        if (command.equals("roles")) {
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
            channel.sendMessage(message).queue();
            event.reply(userTag + "Your message was sent!").setEphemeral(true).queue();
            }
    }


    @Override
    public void onGuildReady(@NotNull GuildReadyEvent event) {
        
        List<CommandData> commandData = new ArrayList<>();
        commandData.add(Commands.slash("roles", "Display the roles available in the server."));

        OptionData option1 = new OptionData(OptionType.STRING, "message" , "The message to send.", true);
        OptionData option2 = new OptionData(OptionType.CHANNEL,"channel", "The channel to send the message to.", false);
        commandData.add(Commands.slash("say", "Says the text from input.").addOptions(option1, option2));

        event.getGuild().updateCommands().addCommands(commandData).queue();
    }
    
}

