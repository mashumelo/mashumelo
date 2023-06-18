	#include <dpp/dpp.h>
    #include "discordtoken.h"
	 
	int main() {
	    dpp::cluster bot(DISCORD_TOKEN);

        bot.on_log(dpp::utility::cout_logger());

        bot.on_slashcommand([&bot](const dpp::slashcommand_t& event) {
            if (event.command.get_command_name() == "help") {
                event.reply("help: Prints this message\n");
            }
        });

        bot.on_ready([&bot](const dpp::ready_t& event) {
	        if (dpp::run_once<struct register_bot_commands>()) {
	            bot.global_command_create(dpp::slashcommand("help", "Prints commands and descriptions", bot.me.id));
	        }
	    });

        bot.start(dpp::st_wait);
	}