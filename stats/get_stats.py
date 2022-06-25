import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from numpy import NaN
import pandas as pd


# Current Season Rating
def selection_ratings(data):
    cs = data['currentSeasonPlaces']
    cs_runs = data['currentSeasonRuns']
    if cs_runs > 0:
        cs_rating_points = 100/cs_runs
        cs_rating = 0
        cs_rating_adjustment = 1
    
        for i in cs:
            cs_rating = cs_rating + (cs_rating_points * i)/cs_rating_adjustment 
            cs_rating_adjustment += 1 
    else:
        cs_rating = NaN



    fav = data['favPlaces']
    fav_runs = data['favRuns']
    if fav_runs > 0:
        fav_rating_points = 100/fav_runs
        fav_rating = 0
        fav_rating_adjustment = 1
    
        for i in fav:
            fav_rating = fav_rating + (fav_rating_points * i)/fav_rating_adjustment 
            fav_rating_adjustment += 1
    else:
        fav_rating = NaN


    good = data['goodPlaces']
    good_runs = data['goodRuns']
    if good_runs > 0:
        good_rating_points = 100/good_runs
        good_rating = 0
        good_rating_adjustment = 1
    
        for i in good:
            good_rating = good_rating + (good_rating_points * i)/good_rating_adjustment 
            good_rating_adjustment += 1
    else:
        good_rating = NaN



    soft = data['softPlaces']
    soft_runs = data['softRuns']
    if soft_runs > 0:
        soft_rating_points = 100/soft_runs
        soft_rating = 0
        soft_rating_adjustment = 1
    
        for i in soft:
            soft_rating = soft_rating + (soft_rating_points * i)/soft_rating_adjustment 
            soft_rating_adjustment += 1
    else:
        soft_rating = NaN


    heavy = data['heavyPlaces']
    heavy_runs = data['heavyRuns']
    if heavy_runs > 0:
        heavy_rating_points = 100/heavy_runs
        heavy_rating = 0
        heavy_rating_adjustment = 1
    
        for i in heavy:
            heavy_rating = heavy_rating + (heavy_rating_points * i)/heavy_rating_adjustment 
            heavy_rating_adjustment += 1
    else:
        heavy_rating = NaN



    last10 = data['lastTenPlaces']
    last10_runs = data['lastTenRuns']
    if last10_runs > 0:
        last10_rating_points = 20
        last10_rating = 0
        last10_rating_adjustment = 1
    
        for i in last10:
            last10_rating = last10_rating + (last10_rating_points * i)/last10_rating_adjustment 
            last10_rating_adjustment += 1
    else:
        last10_rating = NaN


    
    jockey_trainer = data['placesByTrainerJockey']
    jockey_trainer_runs = data['runsByTrainerJockey']
    if jockey_trainer_runs > 0:
        jockey_trainer_rating_points = 100/jockey_trainer_runs
        jockey_trainer_rating = 0
        jockey_trainer_rating_adjustment = 1
    
        for i in jockey_trainer:
            jockey_trainer_rating = jockey_trainer_rating + (jockey_trainer_rating_points * i)/jockey_trainer_rating_adjustment 
            jockey_trainer_rating_adjustment += 1
    else:
        jockey_trainer_rating = NaN

    
    
    
    distance = data['placesByDistance']
    distance_runs = data['runsByDistance']
    if distance_runs > 0:
        distance_rating_points = 100/distance_runs
        distance_rating = 0
        distance_rating_adjustment = 1
    
        for i in distance:
            distance_rating = distance_rating + (distance_rating_points * i)/distance_rating_adjustment 
            distance_rating_adjustment += 1
    else:
        distance_rating = NaN



    track_distance = data['placesByDistTrack']
    track_distance_runs = data['runsByDistTrack']
    if track_distance_runs > 0:
        track_distance_rating_points = 100/track_distance_runs
        track_distance_rating = 0
        track_distance_rating_adjustment = 1
    
        for i in track_distance:
            track_distance_rating = track_distance_rating + (track_distance_rating_points * i)/track_distance_rating_adjustment 
            track_distance_rating_adjustment += 1
    else:
        track_distance_rating = NaN



    first_up = data['firstUpPlaces']
    first_up_runs = data['firstUpRuns']
    if first_up_runs > 0:
        first_up_rating_points = 100/first_up_runs
        first_up_rating = 0
        first_up_rating_adjustment = 1
    
        for i in first_up:
            first_up_rating = first_up_rating + (first_up_rating_points * i)/first_up_rating_adjustment 
            first_up_rating_adjustment += 1
    else:
        first_up_rating = NaN


    second_up = data['secondUpPlaces']
    second_up_runs = data['secondUpStarts']
    if second_up_runs > 0:
        second_up_rating_points = 100/second_up_runs
        second_up_rating = 0
        second_up_rating_adjustment = 1
    
        for i in second_up:
            second_up_rating = second_up_rating + (second_up_rating_points * i)/second_up_rating_adjustment 
            second_up_rating_adjustment += 1
    else:
        second_up_rating = NaN



    third_up = data['thirdUpPlaces']
    third_up_runs = data['thirdUpStarts']
    if third_up_runs > 0:
        third_up_rating_points = 100/third_up_runs
        third_up_rating = 0
        third_up_rating_adjustment = 1
    
        for i in third_up:
            third_up_rating = third_up_rating + (third_up_rating_points * i)/third_up_rating_adjustment 
            third_up_rating_adjustment += 1
    else:
        third_up_rating = NaN

    

    total = data['totalPlaces']
    total_runs = data['totalRuns']
    if total_runs > 0:
        total_rating_points = 100/total_runs
        total_rating = 0
        total_rating_adjustment = 1
    
        for i in total:
            total_rating = total_rating + (total_rating_points * i)/total_rating_adjustment 
            total_rating_adjustment += 1
    else:
        total_rating = NaN

    
    try:
        last_three = data['lastTenFigure'][-3:]
        if last_three[-1] == 'x':
            next = 'First Up'
        elif last_three[-2] == 'x':
            next = 'Second Up'
        elif last_three[-3] == 'x':
            next = 'Third Up'
        else:
            next = 'No'

    except Exception:
        next = 'No'


    return_data = {
        "currentSeason": cs_rating,
        "fav": fav_rating,
        "good": good_rating,
        "soft": soft_rating,
        "heavy": heavy_rating,
        "lastTen": last10_rating,
        "trainerJockey": jockey_trainer_rating,
        "distance": distance_rating,
        "trackDistance": track_distance_rating,
        "firstUp": first_up_rating,
        "secondUp": second_up_rating,
        "thirdUp": third_up_rating,
        "total": total_rating,
        "up": next,

    }

    

    return return_data
