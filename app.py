# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/YouTube-Search-API/blob/main/LICENSE

from flask import Flask, redirect, render_template, request, jsonify, json
from youtubesearchpython import *


app = Flask(__name__, template_folder="public")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search/", methods=['GET'])
def search():
    query = request.args.get('query')
    limit = int(request.args.get('limit')) if request.args.get('limit') else 100
    language = request.args.get('language') if request.args.get('language') else None
    region = request.args.get('region') if request.args.get('region') else None
    all = Search(query, limit=limit, language=language, region=region)
    return jsonify(all.result())


@app.route("/videos/", methods=['GET'])
def videos():
    query = request.args.get('query')
    limit = int(request.args.get('limit')) if request.args.get('limit') else 100
    language = request.args.get('language') if request.args.get('language') else None
    region = request.args.get('region') if request.args.get('region') else None
    videos = VideosSearch(query, limit=limit, language=language, region=region)
    return jsonify(videos.result())


@app.route("/playlists/", methods=['GET'])
def playlists():
    query = request.args.get('query')
    limit = int(request.args.get('limit')) if request.args.get('limit') else 100
    language = request.args.get('language') if request.args.get('language') else None
    region = request.args.get('region') if request.args.get('region') else None
    playlists = PlaylistsSearch(query, limit=limit, language=language, region=region)
    return jsonify(playlists.result())


@app.route("/channels/", methods=['GET'])
def channels():
    query = request.args.get('query')
    limit = int(request.args.get('limit')) if request.args.get('limit') else 100
    language = request.args.get('language') if request.args.get('language') else None
    region = request.args.get('region') if request.args.get('region') else None
    channels = ChannelsSearch(query, limit=limit, language=language, region=region)
    return jsonify(channels.result())


@app.route("/video/get/", methods=['GET'])
def getvideo():
    query = request.args.get('query')
    video = Video.get(query, mode=ResultMode.json)
    return jsonify(video)


@app.route("/video/getinfo/", methods=['GET'])
def getvideoinfo():
    query = request.args.get('query')
    videoinfo = Video.getInfo(query, mode=ResultMode.json)
    return jsonify(videoinfo)


@app.route("/video/getformats/", methods=['GET'])
def getvideoformats():
    query = request.args.get('query')
    videoformat = Video.getFormats(query, mode=ResultMode.json)
    return jsonify(videoformat)


@app.route("/playlist/get/", methods=['GET'])
def getplaylist():
    query = request.args.get('query')
    playlist = Playlist.get(query, mode=ResultMode.json)
    return jsonify(playlist)


@app.route("/playlist/getvideos/", methods=['GET'])
def getplaylistvideos():
    query = request.args.get('query')
    playlistvideos = Playlist.getFormat(query, mode=ResultMode.json)
    return jsonify(playlistvideos)


@app.route("/hashtag/", methods=['GET'])
def hashtag():
    query = request.args.get('query')
    limit = int(request.args.get('limit')) if request.args.get('limit') else 100
    hashtag = Hashtag(query, limit=limit)
    return jsonify(hashtag.result())


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
