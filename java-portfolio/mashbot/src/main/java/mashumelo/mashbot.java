package mashumelo;

import javax.security.auth.login.LoginException;

import net.dv8tion.jda.api.JDABuilder;

public class mashbot
{
    public static void main( String[] args) throws LoginException
    {
        final String TOKEN = "";
        JDABuilder jdaBuilder = JDABuilder.createDefault(TOKEN);

        jdaBuilder.build();
    
    }
}
