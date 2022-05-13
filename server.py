# Dependencies: Flask, pydub, ffmpeg-python
# (pip install Flask)

from flask import Flask, jsonify, request, make_response
from pydub import AudioSegment
from io import BytesIO

app = Flask(__name__)

@app.route('/convert/alac-to-flac/', methods=['POST'])
def convertAlacToFlac():
    # ファイルが含まれていない場合、エラーとして返す
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"})
    alacFile = request.files['file']

    # AudioSegmentを用いてファイルを開く
    segment = AudioSegment.from_file(BytesIO(alacFile.stream.read()), "m4a")

    # メモリーにファイルをエクスポートする
    flacFile = segment.export(format="flac")

    # レスポンスを生成する
    response = make_response()
    response.data = flacFile.read()
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = 'attachment; filename=output.flac'
    return response

app.run(port=8000)
