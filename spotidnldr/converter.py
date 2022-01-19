import ffmpeg
import pathlib


def convert_to_mp3(file_path, out_file_path, audiobitrate=192000, verbose=True):
    print("[*] converting to mp3")
    print("in :", file_path)
    print("out :", out_file_path)
    input_file = ffmpeg.input(file_path)
    audio = input_file.audio
    print("passed audio capture")
    out = ffmpeg.output(
        audio,
        str(pathlib.Path(out_file_path)),
        format="mp3",
        audio_bitrate=audiobitrate,
    )
    print(out)
    ffmpeg.run(out, quiet=(not verbose))
    print(f"[*] converted to mp3 with bitrate of {audiobitrate/1000}K")


if __name__ == "__main__":
    print("main")
