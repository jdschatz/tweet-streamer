#!/usr/bin/env python3
#jdschatz

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import vlc    # To access audio files and speakers
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import wolframalpha

import SecretKeys

#CHECKPOINT1
print('[Checkpoint 01] Listening for tweets from Twitter API' + '\n')

#keys and secrets
tConsumerKey = SecretKeys.TWITTER_CKEY
tConsumerSecret = SecretKeys.TWITTER_CSECRET
tApiToken = SecretKeys.TWITTER_ATOKEN
tApiSecret = SecretKeys.TWITTER_ASECRET
ibmKey = SecretKeys.IBM_KEY
wolframKey = SecretKeys.WOLFRAM_KEY

#initialization of WolframAlpha client
wolframClient = wolframalpha.Client(wolframKey)

class listener(StreamListener):

    def on_status(self, status):
        
        #retrieve question from twitter
        question = status.text.replace('#jdschatz', '')
        
        #CHECKPOINT2
        print('[Checkpoint 02] New Question: ' + question + '\n')
        
        
        #CHECKPOINT3
        print('[Checkpoint 03] Preparing to speak question' + '\n')
        listener.sayThePhrase(question)

        #CHECKPOINT4
        print('[Checkpoint 04] Sending question to WolframAlpha' + '\n')
        res = wolframClient.query(question)
        output = next(res.results).text
        
        #CHECKPOINT5
        print('[Checkpoint 05] Received answer from WolframAlpha: ' + output + '\n')
        
        #CHECKPOINT6
        print('[Checkpoint 06] Preparing to speak answer')
        listener.sayThePhrase(output)
        
        #CHECKPOINT7
        print('[Checkpoint 07] Waiting for next tweet or termination of the program' + '\n')
        
    def on_error(self, status):
        print(status.text)
        
    def sayThePhrase(phrase):
        authenticator = IAMAuthenticator(ibmKey)
        text_to_speech = TextToSpeechV1(
            authenticator=authenticator
        )
        
        text_to_speech.set_service_url('https://api.us-east.text-to-speech.watson.cloud.ibm.com')
        fileName = 'phrase' + '.wav'

        with open(fileName, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    phrase,
                    voice='en-GB_KateV3Voice',
                    accept='audio/wav'
                ).get_result().content)

        player = vlc.MediaPlayer(fileName)
        player.play()

auth = OAuthHandler(tConsumerKey, tConsumerSecret)
auth.set_access_token(tApiToken, tApiSecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#jdschatz"])