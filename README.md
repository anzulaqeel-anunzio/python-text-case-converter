# Text Case Converter

A handy CLI utility to convert strings between various naming conventions like snake_case, camelCase, kebab-case, and PascalCase.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Smart Detection**: Handles input in any format (snake, camel, spaces, mixed).
*   **Multiple Formats**: Supports:
    *   `snake`: `hello_world`
    *   `kebab`: `hello-world`
    *   `camel`: `helloWorld`
    *   `pascal`: `HelloWorld`
    *   `constant`: `HELLO_WORLD`
    *   `sentence`: `Hello world`
    *   `title`: `Hello World`

## Usage

```bash
python run_converter.py [text] --to [format]
```

### Examples

**1. Snake to Camel**
```bash
python run_converter.py "hello_world_example" --to camel
# Output: helloWorldExample
```

**2. Sentence to Constant (Screaming Snake)**
```bash
python run_converter.py "Server Config Error" --to constant
# Output: SERVER_CONFIG_ERROR
```

**3. Mixed to Kebab**
```bash
python run_converter.py "JSONParserFactory" --to kebab
# Output: json-parser-factory
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
