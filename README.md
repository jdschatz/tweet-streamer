# tweet-streamer
tweet-streamer is a program that helps the user receive the answer to any computational knowledge question, sent
via Twitter!

How it works:

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

Both the question and the answer will also be read out-loud through the IBM Watson Text-To-Speech API.
In addition, an audio file called phrase.wav will be created in the same directory as the program,
and will contain the text-to-speech audio.

After finishing answering the question, tweet-streamer is ready to listen to the next tweet should the
user wish to send another question. If not, the program can be safely terminated at this point.

                                                                                               