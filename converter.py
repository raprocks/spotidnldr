import ffmpeg

def convert_to_mp3(file_path, out_file_path):
    input=ffmpeg.input(file_path)
    audio=input.audio
    out = ffmpeg.output(audio, out_file_path, format="mp3", audio_bitrate=192000)
    ffmpeg.run(out, quiet=True)

if __name__=="__main__":
    print("main")
    convert_to_mp3("./hello.webm","./out.mp3")