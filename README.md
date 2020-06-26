# tweet-streamer
tweet-streamer is a program that helps the user receive the answer to any computational knowledge question, sent
via Twitter!

## How it works:

tweet-streamer works by streaming all the tweets from Twitter that use the hashtag "#jdschatz". It then
parses the text of that tweet and prints it the console. After which, it then sends the tweet
(which should be in the form of a question, examples will be provided below) to the Wolfram Alpha
Computational Knowledge engine. Once tweet-streamer receives the answer back from
WolframAlpha, it will print the answer to the console.

The Wolfram Alpha Computational Knowledge engine is a powerful tool that can answer nearly any factual
question you have. As for what types of questions it can handle, think of what you could ask Siri, Cortana,
or any of the other personal assistant softwares. Some example include, but are not limited to:
    
What is the population of France?

What is the weather in Washington DC?

How many people does a 20 pound turkey feed?

81 divided by 9

Both the question and the answer will be read out-loud through the IBM Watson Text-To-Speech API.
In addition, an audio file called phrase.wav will be created in the same directory as the program,
and will contain the text-to-speech audio.

After finishing answering the question, tweet-streamer is ready to listen to the next tweet should the
user wish to send another question. If not, the program can be safely terminated at this point.

## How to use:

Unfortunately, tweet-streamer requires secret api keys from Twitter, WolframAlpha, and IBM in order 
to run correctly. Such keys can be obtained by creating developer accounts at each of these organization's
websites. Once obtained, place them like I did in the sample_SecretKeys.py file.

I created and ran this program in Ubuntu on my RaspberryPi, so the instructions are tailed towards
linux users. For Windows, you would need to install the same software with different commands.

There are several commands that need to be executed before operation that are listed below. Please
execute them in the path of your python project folder. (The path of the repository if cloned).

pip3 install --user tweepy

pip3 install --user --upgrade "ibm-watson>=4.2.1"

pip3 install --user python-vlc

pip3 install --user wolframalpha api

This program requires that the user has VLC Media Player installed, because that is what the 
text-to-speech uses for its audio.

To run the file, make sure you are in the directory holding the file and type:

python3 tweet-streamer.py

## Screenshots

These are two screenshots of the output while running the program. Obviously, it's impossible to
demonstrate the text-to-speech through a screenshot, however every step of the program is printed
to the console, so it should give you a good idea of the entire process.

![Alt text](https://github.com/jdschatz/tweet-streamer/blob/master/sample_output1.jpg?raw=true "Sample output 1")

![Alt text](https://github.com/jdschatz/tweet-streamer/blob/master/sample_output2.jpg?raw=true "Sample output 2")
                                                                                               