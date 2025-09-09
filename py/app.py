from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os
import sys

app = Flask(__name__)
# Enable CORS to allow requests from your HTML file
CORS(app)

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    # Define the output path
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'videos_descargados')
    
    # Create the directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # yt-dlp options
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info without downloading
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'video')
            # Download the video
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

if __name__ == '__main__':
    app.run(port=5000, debug=True)
