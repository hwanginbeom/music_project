from django.shortcuts import render
from .models import *
# Create your views here.

def index(request) :
    song_meta = SongMeta.objects.all()
    # song = song_meta.filter(song_id = 0)

    idx = []
    for i, obj in enumerate(song_meta):
        idx.append(obj)
        if(i == 1) :
            break

    # id = 0
    # song_id_list = [song_meta[idx[0]].song_id, song_meta[idx[1]].song_id]
    # song_id = song_meta[id].song_id
    # album_id = song_meta[id].album_id
    # artist_id_basket = song_meta[id].artist_id_basket
    # artist_name_basket = song_meta[id].artist_name_basket
    # song_name = song_meta[id].song_name
    # song_gn_gnr_basket = song_meta[id].song_gn_gnr_basket
    # song_gn_dtl_gnr_basket = song_meta[id].song_gn_dtl_gnr_basket
    # issue_date = song_meta[id].issue_date
    # url_link = song_meta[id].url_link
    # album_image = song_meta[id].album_image
    #
    # print(">>>>>>>>>>>>>>>>>>>>" , song_id_list)
    print(">>>>>>>>>>>>>>>>>>>> idx ", len(idx))
    # context = {'song_id': song_id_list, 'album_id' : album_id, 'artist_id_basket' : artist_id_basket,
    #            'artist_name_basket' : artist_name_basket, 'song_name' : song_name, 'song_gn_gnr_basket' : song_gn_gnr_basket,
    #            'song_gn_dtl_gnr_basket' : song_gn_dtl_gnr_basket, 'issue_date' : issue_date, 'url_link' : url_link,
    #            'album_image' : album_image, 'song_meta' : song_meta, 'idx' : idx}
    context = { 'idx' : idx }
    return render(request, 'musicApp/index.html', context)

def elements(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'musicApp/elements.html')

def generic(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'musicApp/generic.html')