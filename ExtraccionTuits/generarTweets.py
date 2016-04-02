import tweepy
import sys
import nltk
import time

auth = tweepy.OAuthHandler("YmRjJN7ZRRAxXMtugoMiZWuEy","gtrFB8Udsbzu1Hmg17zBd6U3XxsfTEemYHBP6RgZ5CrddCbud4")
auth.set_access_token("134903713-af69tmSatzWkBIssxeAAtjbB5Dm0yhs4twdrttHB", "Xr4zlnzG6zwdZeZwTnHEDamOuTmaDTL3uwcugi3agIJlB")

api = tweepy.API(auth)

# user = api.get_user('jemd93') # La variable user contiene la info del usuario jemd93. 
# user2 = api.get_user(user.id) # En user2 tambien esta la info de jemd93 pero usando el id para encontrarlo.
# print(user.id)				  # Muestra el id de jemd93
# print(user.screen_name)		  # Muestra el screen name (jemd93)
# print(user.followers_count)	  # Cantidad de followers
# for friend in user.friends(): # Imprime todos los "amigos" del usuario jemd93 aunque no ando claro que es esto. No son followers.
#    print(friend.screen_name)

# for user1 in tweepy.Cursor(api.followers, screen_name="jemd93").items() : #Imprime los followers de una persona. TODOS.
# 	print(user1.screen_name)

# hramosallup
# 
# c = tweepy.Cursor(api.followers, screen_name="dcabellor").items()
# f = open('dcabellor.dat','w+')
# i = 0
# while i < 5000 :
# 	try :
# 		follower = c.next()
# 		f.write(follower.screen_name+"\n")
# 		i = i+1
# 	except tweepy.TweepError :
# 		time.sleep(60*15)
# 		continue
# 	except StopIteration:
# 		break

# f.close()

finput = open('trainingSet.dat','r')
i = 1
for line in finput :
	user = line.split(' ')[0]
	filename = 'UserDocs/'+str(i)+'.txt'
	fout = open(filename,'w+')
	try : 
		tweets = api.user_timeline(screen_name=user,count=25)
	except tweepy.TweepError :
		time.sleep(60)
	except StopIteration:
		break
	fout.write('Tweets de '+user+"\n")
	for t in tweets :
		fout.write(t.text+"\n")
	fout.close()
	i=i+1
	# for tweet in api.search(q=user,count=25,show_user=False,rpp=25) : 
	# 	fout.write(tweet.text+"\n")
	# fout.close()
	# except tweepy.TweepError :
	# 	time.sleep(60*15)
	# 	continue
	# except StopIteration:
	# 	break

finput.close()

