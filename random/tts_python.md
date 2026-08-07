### Text to Speech in terminal

`spd-say "hello avro"` speaks the argument aloud from terminal.

```zsh
spd-say "hello avro 
dquote>
```

That dquote> prompt means "double quote open".Your terminal noticed you opened an inverted comma (") but never closed it. It is paused and waiting for you to type the rest of your text before running the command. It displays dquote> as a helper prompt, telling you: "I am still collecting text for your double-quoted string."

This feature allows you to pass long, multi-line blocks of text into commands like `spd-say` or `echo` without cramming everything onto one single line.

If you want `spd-say` to read a poem or a list with natural pauses, you can intentionally use this multi-line feature:

```zsh
spd-say "Hello avro.
dquote> Welcome back to your Ubuntu terminal.
dquote> Today we are testing multi-line speech."
```
### install another tts software package : SVOX Pico

Step 1: Install it
`sudo apt install libttspico-utils speech-dispatcher-pico
`
Step 2: Un-comment the Pico Module Configuration

The `speech-dispatcher` process will ignore Pico if its module configuration line is commented out with a `#` inside the configuration profile. 

1. Open your system's global runtime configuration file:
```
    sudo nano /etc/speech-dispatcher/speechd.conf
    ```

2. Press `Ctrl + W` to trigger a search, type **`pico`**, and press `Enter`.
3. Look for a configuration line that matches this format:
```
    #AddModule "pico" "sd_pico" "pico.conf"
    ```
    
4. **Remove the `#` sign** from the front of that line so it looks exactly like this:
    
    ```
    AddModule "pico" "sd_pico" "pico.conf"
    ```
    
5. Scroll up or search for `DefaultModule` and make sure it is assigned directly to Pico: 

    DefaultModule pico

6. Save and exit (`Ctrl + O`, `Enter`, then `Ctrl + X`). 


Step 3: Hard-Restart the Background Speech Daemon

Kill the active running background processes completely so they are forced to reload your configuration file from scratch: 

	killall speech-dispatcher

	spd-say "Hello avro, this should sound completely different now."
