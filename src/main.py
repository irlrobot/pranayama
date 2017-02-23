#!/usr/bin/env
"""
Pranayama Skill
v1.0.0
github.com/irlrobot
"""
from __future__ import print_function
import json

APP_ID = 'amzn1.ask.skill.9dc6bb54-42b9-41a4-a5da-000663756fef'
STREAM = 'https://aws.userdel.com/bensound-relaxing.mp3'

def play_audio(behavior):
    '''
    Send AudioPlayer.Play Directive
    '''
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": behavior,
                    "audioItem": {
                        "stream": {
                            "token": "doesntreallymatter",
                            "url": STREAM,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }

def stop_audio():
    '''
    Send AudioPlayer.Stop Directive
    '''
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Stop",
                }
            ],
            "shouldEndSession": True
        }
    }

def handler(event, context):
    '''
    main function for Lambda
    '''
    print('==============lambda_handler started...')
    print(json.dumps(event))

    try:
        request_type = event['request']['type']
    except KeyError:
        request_type = ''

    try:
        intent_name = event['request']['intent']['name']
    except KeyError:
        intent_name = ''

    if request_type == 'LaunchRequest':
        print ('==============LaunchRequest fired...')
        return play_audio('REPLACE_ALL')
    if request_type == 'AudioPlayer.PlaybackNearlyFinished':
        print ('==============AudioPlayer.PlaybackNearlyFinished fired...')
        return play_audio('REPLACE_ENQUEUED')
    if intent_name == 'PlayAudio':
        print ('==============PlayAudio fired...')
        return play_audio('REPLACE_ALL')
    if intent_name == 'AMAZON.ResumeIntent':
        print ('==============AMAZON.ResumeIntent fired...')
        return play_audio('REPLACE_ALL')

    if intent_name == 'AMAZON.StopIntent':
        print ('==============AMAZON.StopIntent fired...')
        return stop_audio()
    if intent_name == 'AMAZON.CancelIntent':
        print ('==============AMAZON.CancelIntent fired...')
        return stop_audio()
    if intent_name == 'AMAZON.PauseIntent':
        print ('==============AMAZON.PauseIntent fired...')
        return stop_audio()
