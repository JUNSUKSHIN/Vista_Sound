forfiles /s /m *.mp4 /c "cmd /c ffmpeg -i "@FILE" -r 1 output_%04d.png
