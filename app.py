# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/YouTube-Search-API/blob/main/LICENSE

from flask import Flask, redirect, request, jsonify, json
from youtubesearchpython import *


app = Flask(__name__)


@app.route("/")
def home():
    return "Documentation:- <a href='https://github.com/FayasNoushad/YouTube-Search-API'>YouTube-Search-API</a>"


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


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
