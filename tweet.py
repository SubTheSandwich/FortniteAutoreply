import tweepy
import random

auth = tweepy.OAuthHandler("#####, #####")
auth.set_access_token("######, ######")
api = tweepy.API(auth)

toReply = "FortniteGame"

tweets = api.user_timeline(screen_name = toReply, count=1)
tweet = api.user_timeline(screen_name = toReply, count=1)[0]

newValue = tweet.id
a = tweet.id
f = open('last-tweet.txt', 'r+')
b = f.read()
f.close()

def main():
    if (a == b):
        print(toReply + " has not done a new tweet yet.")
        exit()
    elif (int(a) != int(b)):
        print (a == b)
        print(a)
        print(b)
        print("New value!")
        with open("last-tweet.txt", 'r') as e:
            lines = e.readlines()
        with open("last-tweet.txt", 'w') as e:
            for line in lines:
                if line.strip("\n") != "never will be this so clear":
                  e.write(line)
        e = open('last-tweet.txt', 'w')
        e.write(str(a))

        rt = open('last-reply.txt', 'r+')
        lines = open('ratio-text.txt').read().splitlines()
        stweet = random.choice(lines)
        check = open('last-reply.txt', 'r')
        Checked = check.read()
        if (stweet == Checked):
            newS = random.choice(lines)
            
            with open("last-reply.txt", 'r') as h:
                lines = h.readlines()
            with open("last-reply.txt", 'w') as h:
                for line in lines:
                    if line.strip("\n") != "never will be this so clear":
                      h.write(line)
            h = open('last-reply.txt', 'w')
            h.write(newS)

            
            for pee in tweets:
                api.update_status("@" + toReply + " " + newS, in_reply_to_status_id = pee.id)
        elif (stweet != Checked):
            
            clear = rt.readlines()

            with open("last-reply.txt", 'r') as h:
                lines = h.readlines()
            with open("last-reply.txt", 'w') as h:
                for line in lines:
                    if line.strip("\n") != "never will be this so clear":
                      h.write(line)
            h = open('last-reply.txt', 'w')
            h.write(stweet)
            
            for pee in tweets:
                api.update_status("@" + toReply + " " + stweet, in_reply_to_status_id = pee.id)
       

if __name__ == "__main__":
    main()




        
    



    

    

