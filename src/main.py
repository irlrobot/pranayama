#!/usr/bin/env
"""
Pranayama Skill
v1.0.0
github.com/irlrobot
"""
from __future__ import print_function

APP_ID = 'amzn1.ask.skill.9dc6bb54-42b9-41a4-a5da-000663756fef'
STREAM = 'https://d38ybm4flaorq4.cloudfront.net/bensound-relaxing.mp3'

def play_audio():
    '''
    Build a response to play the audio stream
    '''
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
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

def handler(event, context):
    '''
    main function for Lambda
    '''
    print('lambda_handler started...')
    print(event)
    if event['session']['application']['applicationId'] != APP_ID:
        raise ValueError("Invalid Application ID")

    if event['request']['type'] == "LaunchRequest":
        print ('LaunchRequest fired...')
        return play_audio()
    if event['request']['type'] == "IntentRequest":
        print ('IntentRequest fired...')
        return play_audio()
