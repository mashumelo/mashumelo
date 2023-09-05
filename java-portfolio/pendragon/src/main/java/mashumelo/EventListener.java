package mashumelo;

//imports
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.entities.channel.concrete.TextChannel;
import net.dv8tion.jda.api.entities.channel.middleman.AudioChannel;
import net.dv8tion.jda.api.events.guild.voice.GuildVoiceUpdateEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

public class EventListener extends ListenerAdapter {

    @Override
    public void onGuildVoiceUpdate(@NotNull GuildVoiceUpdateEvent event) {
        // Get the text channel where you want to send the update
        TextChannel channel = event.getGuild().getTextChannelById("1122394088189206550");
        User user = event.getEntity().getUser();
        String serverName = event.getGuild().getName();
        AudioChannel oldChannel = event.getChannelLeft();
        AudioChannel newChannel = event.getChannelJoined();

        if (oldChannel != null) {
            // User left a specific voice channel
            String message = user.getAsMention() + " left " + oldChannel.getAsMention();
            channel.sendMessage(message).complete();
            System.out.println(message);
        }

        if (newChannel != null) {
            // User joined a specific voice channel
            String message = user.getAsMention() + " joined " + newChannel.getAsMention();
            channel.sendMessage(message).complete();
            System.out.println(message);
        }

        // Check if the user joined or left the server
        if (event.getGuild().getMember(user) != null) {
         // User joined the server
            String message = user.getAsMention() + " has joined" + serverName + "!";
            channel.sendMessage(message).complete();
            System.out.println(message);
        } else {
            // User left the server
            String message = user.getAsMention() + " has left" + serverName + "!";
            channel.sendMessage(message).complete();
            System.out.println(message);
        }

    }
}