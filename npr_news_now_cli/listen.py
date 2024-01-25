import time
import feedparser
import vlc
import warnings

def format_time(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def main():
    warnings.filterwarnings("ignore", category=UserWarning)

    feed_url = "https://feeds.npr.org/500005/podcast.xml"
    feed = feedparser.parse(feed_url)
    latest_entry = feed.entries[0]
    mp3_url = latest_entry.enclosures[0]['href']

    print(f"Title: {latest_entry.title}")
    print(f"MP3 URL: {mp3_url}")

    player = vlc.MediaPlayer(mp3_url)
    player.play()

    try:
        while player.get_state() not in [vlc.State.Ended, vlc.State.Stopped, vlc.State.Error]:
            loop_start_time = time.time()
            current_time = player.get_time()
            total_time = player.get_length()
            print(f"Time: {format_time(current_time)} / {format_time(total_time)}", end='\r')

            # Calculate the elapsed time and sleep for the remainder of 1 second
            elapsed_time = time.time() - loop_start_time
            time.sleep(max(1 - elapsed_time, 0))
    except KeyboardInterrupt:
        print("\nPlayback interrupted by user.")

    player.stop()
    print("\nPlayback finished or stopped.")

if __name__ == "__main__":
    main()
