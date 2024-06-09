![Teletify](./logo.png)

# TELETIFY

TELETIFY is a command-line tool for sending messages and documents via Telegram. It uses the Telegram Bot API to send text messages and documents to a specified chat ID.

## Features

- Send text messages to a specified chat ID
- Send documents with an optional caption to a specified chat ID
- Load configuration from a configuration file for ease of use

## Installation

> :warning: The `setup.py` using `--break-system-packages` in order to install the depedencies on the system.

   ```bash
   git clone https://github.com/yourusername/teletify.git
   cd teletify
   sudo python setup.py
   ```

## Usage



### Sending a Text Message

To send a text message, use the following command:

```bash
teletify text --message "Hello, World!"
```
Via Stdin :
```bash
echo "Hello World" | teletify text
```

### Sending a Document

To send a document with an optional caption, use the following command:

```bash
teletify document -f /path/to/your/file.pdf --message "Here is your document."
```

### Configuration

The configuration file is located at `~/.config/teletify/config.ini`. It contains the bot API key and the default chat ID:

```ini
[telegram]
bot_api_key = YOUR_BOT_API_KEY
default_chat_id = YOUR_DEFAULT_CHAT_ID
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
