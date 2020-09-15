import ffmpeg


def convert_to_mp3(file_path, out_file_path, audiobitrate=192000, verbose=False):
    print("[*] converting to mp3")
    input_file = ffmpeg.input(file_path)
    audio = input_file.audio
    out = ffmpeg.output(
        audio,
        out_file_path,
        format="mp3",
        audio_bitrate=audiobitrate)
    ffmpeg.run(out, quiet=(not verbose))
    print("[*] converted to mp3 with bitrate of {audiobitrate/1000}K")


if __name__ == "__main__":
    print("main")
