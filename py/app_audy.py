from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import yt_dlp
import os
import sys

app = Flask(__name__)
CORS(app)

# Ruta para descargar video (la original)
@app.route('/download_audio', methods=['GET'])
def download_video():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'videos_descargados')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'video')
            ydl.download([video_url])
            
            download_url = f"/downloads/{video_title}.mp4"

        return jsonify({
            "success": True, 
            "message": "Download completed", 
            "title": video_title,
            "download_url": download_url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Nueva ruta para descargar solo el audio
@app.route('/download_audio', methods=['GET'])
def download_audio():
    audio_url = request.args.get('url')
    if not audio_url:
        return jsonify({"error": "No URL provided"}), 400

    # Define la ruta de salida para los archivos de audio
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audios_descargados')

    # Crea el directorio si no existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Opciones de yt-dlp para descargar solo audio
    ydl_opts = {
        'format': 'bestaudio/best',  # 'bestaudio' descarga el mejor formato de audio
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', # Calidad de audio en kbps
        }],
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(audio_url, download=False)
            audio_title = info_dict.get('title', 'audio')
            ydl.download([audio_url])

            download_url = f"/audios/{audio_title}.mp3"

        return jsonify({
            "success": True, 
            "message": "Download completed", 
            "title": audio_title,
            "download_url": download_url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para servir los archivos descargados
@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'videos_descargados'), filename)

@app.route('/audios/<path:filename>')
def serve_audio(filename):
    return send_from_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audios_descargados'), filename)

if __name__ == '__main__':
    app.run(port=5000, debug=True)