package mashumelo;

//Imports
import java.io.File;
import java.io.FileReader;

import javax.security.auth.login.LoginException;

import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.sharding.DefaultShardManagerBuilder;
import net.dv8tion.jda.api.sharding.ShardManager;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


public class mashbot
{

    private final ShardManager shardManager;

    public mashbot(String apiToken) throws LoginException
    {
        DefaultShardManagerBuilder builder = DefaultShardManagerBuilder.createDefault(apiToken);
        builder.setStatus(OnlineStatus.ONLINE);
        builder.setActivity(Activity.watching("Mash's Server"));
        shardManager = builder.build();

        //Register Event Listener
        shardManager.addEventListener(new EventListener());
    
    }

    public ShardManager getShardManager() {
        return shardManager;
    }

    public static void main(String[] args) {
        String apiToken = null; // Declare and initialize apiToken outside of the try block
    
        try {
            JSONParser parser = new JSONParser();
            Object obj = parser.parse(new FileReader("java-portfolio/mashbot/src/main/java/mashumelo/config.json"));
            JSONObject config = (JSONObject) obj;
            apiToken = (String) config.get("token"); // Initialize apiToken inside the try block
        } catch (Exception e) {
            System.out.println("ERROR: Bot Token provided is invalid!");
        }
    
        try {
            System.out.println(apiToken);
            mashbot bot = new mashbot(apiToken); // Pass apiToken as a parameter to the constructor
        } catch (LoginException e) {
            System.out.println("ERROR: Bot Token provided is invalid!");
        }
    }
}
