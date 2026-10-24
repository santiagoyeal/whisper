
import whisper

model = whisper.load_model("base")

videos = ["1.mp4", "2.mp4", "3.mp4"]

for video in videos:
    print(f"Transcribiendo {video}...")

    result = model.transcribe(video, language="es")

    nombre_txt = video.replace(".mp4", ".txt")

    with open(nombre_txt, "w", encoding="utf-8") as archivo:
        archivo.write(result["text"].strip())

    print(f"Transcripción guardada en {nombre_txt}")

print("¡Transcripción de los tres videos completada!")
