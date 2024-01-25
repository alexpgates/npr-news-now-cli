# NPR News Now CLI

`npr-news-now-cli` is a command-line tool that plays the most recent NPR News Now hourly update. It's designed to provide a simple and immediate way to stay updated with the latest news from NPR.

## Why?

NPR publishes hourly news briefs called [NPR News Now](https://www.npr.org/podcasts/500005/npr-news-now) _The latest news in five minutes. Updated hourly._ This tool makes it easy for me to catch up on the news during a pomodoro break right from a terminal.

## Disclaimer

This tool is not officially affiliated with, authorized, maintained, sponsored, or endorsed by NPR (National Public Radio) or any of its affiliates or subsidiaries. This is an independent and unofficial project. Use at your own risk. The content accessed by this tool is subject to NPR's own terms of use.

## Prerequisites

Before you install and use `npr-news-now-cli`, you need to have VLC media player installed on your system as it relies on the VLC bindings for audio playback. Please follow the installation instructions on the [VLC official website](https://www.videolan.org/vlc/index.html).

## Installation

To install `npr-news-now-cli`, make sure you have Python and `pip` installed on your system, then run the following command:

```bash
pip install npr-news-now-cli
```

## Usage

After installation, you can run the tool using the following command:

```bash
npr-news-now
```

To stop listening, use `ctrl+c` in your terminal. Otherwise it will quit when the clip is finished.

## To do

- The playback time is sometimes jumpy and inconsistent.
- There's no way to pause / resume, but maybe that's okay.
- This has only been tested on MacOS 14.2.1, so, yeah.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.

## Get in touch

Find me at [alexpgates.com](https://www.alexpgates.com). PR's are welcome and appreciated!
