from typing import Any


def download_progress_bar(stream, chunk: Any, bytes_remaining: int):
    total_size = stream.filesize
    width = 32
    phases = (" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█")
    empty_fill = " "
    nphases = len(phases)
    progress = min(1, (total_size - bytes_remaining) / total_size)
    filled_len = width * progress
    nfull = int(filled_len)  # Number of full chars
    phase = int((filled_len - nfull) * nphases)  # Phase of last char
    nempty = width - nfull  # Number of empty chars
    prog_bar = phases[-1] * nfull
    current = phases[phase] if phase > 0 else ""
    empty = empty_fill * max(0, nempty - len(current))
    line = "".join([prog_bar, current, empty])

    to_fill = ((total_size - bytes_remaining) / 1024) / 1024
    print(
        "\rDownloading.. |", line, f"| {to_fill:.2f}/{total_size/1024/1024:.2f}", end=""
    )
